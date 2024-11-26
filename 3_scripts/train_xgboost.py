import argparse
import pandas as pd
import numpy as np
from pathlib import Path

import pickle
import logging

from sklearn.model_selection import train_test_split, KFold
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score
import xgboost as xgb

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def train(
    df_training,
    y_training,
    eta=0.1,
    max_depth=6,
    min_child_weight=5,
    num_boost_round=41,
):
    """Train the dataset

    Parameters
    ---------
    df_training: training dataframe
    y_training: np.array of y training values
    eta: the learning rate
    max_depth: int, the depth of the decision tree i.e. the number of levels from the root node to furthest leaf node
    min_child_weight: int, the minimum “sum of weights” of observations. Higher values are associated with less overfitting.
    num_boost_round: number of boosting rounds
    """
    xgb_final_params = {
        "booster": "gbtree",  # default
        "verbosity": 1,  # default
        "nthread": 6,  # how many cores/ how much parallelization, depends on your system
        "eta": eta,  # default
        "max_depth": max_depth,
        "min_child_weight": min_child_weight,  # default
        "objective": "binary:logistic",
        "seed": 1,  # random number seed to make the results reproducible
        "eval_metric": "auc",
    }

    dicts = df_training.to_dict(orient="records")
    dv = DictVectorizer(sparse=False).fit(dicts)
    X_training = dv.transform(dicts)
    dxtrain = xgb.DMatrix(
        X_training, label=y_training, feature_names=list(dv.get_feature_names_out())
    )

    model = xgb.train(xgb_final_params, dxtrain, num_boost_round=num_boost_round)

    return dv, model


def predict(df_v, dv, model, y_test):
    """Calculate predictions for given dataset

    Parameters
    ---------
    df_v: the validation dataset to perform the prediction on
    dv: DictVectorizer to use to transform the validation dataset
    model: The trained XGBoost model to use to calculate the predictions
    y_test: the list of actual target values in the validation dataset
    """
    dicts = df_v.to_dict(orient="records")

    X_test = dv.transform(dicts)
    dtest = xgb.DMatrix(
        X_test, label=y_test, feature_names=list(dv.get_feature_names_out())
    )

    y_pred = model.predict(dtest)

    return y_pred


def perform_validation(
    df, kfold_n_splits=10, eta=0.3, max_depth=4, min_child_weight=5, num_boost_round=43
):
    """Evaluate the model across different datasets

    Parameters
    ---------
    df: The dataset to use to extract training and validation datasets and perform evaluation
    kfold_n_slits: the number of groups the df should be split into
    eta: the learning rate
    max_depth: int, the depth of the decision tree i.e. the number of levels from the root node to furthest leaf node
    min_child_weight: int, the minimum “sum of weights” of observations. Higher values are associated with less overfitting.
    num_boost_round: number of boosting rounds
    """
    kfold = KFold(n_splits=kfold_n_splits, shuffle=True, random_state=1)

    scores = []

    for fold_num, (train_idx, val_idx) in enumerate(kfold.split(df)):
        df_t = df.iloc[train_idx]
        df_v = df.iloc[val_idx]

        y_t = df_t["is_severe"].values
        y_v = df_v["is_severe"].values

        del df_t["is_severe"]
        del df_v["is_severe"]

        dv, model = train(
            df_t,
            y_t,
            eta=eta,
            max_depth=max_depth,
            min_child_weight=min_child_weight,
            num_boost_round=num_boost_round,
        )
        y_pred = predict(df_v, dv, model, y_v)
        auc = roc_auc_score(y_v, y_pred)
        scores.append(auc)
        print(f"Score on fold {fold_num}: {auc}")
    return scores


def train_model(eta=0.3, max_depth=4, min_child_weight=5, num_boost_round=43):
    """Train and validate model and save to file

    Parameters
    ---------
    eta: the learning rate
    max_depth: int, the depth of the decision tree i.e. the number of levels from the root node to furthest leaf node
    min_child_weight: int, the minimum “sum of weights” of observations. Higher values are associated with less overfitting.
    num_boost_round: number of boosting rounds
    """
    kfold_n_splits = 5
    
    base_path = Path(__file__).parent
    model_file_path = base_path / "data/collisions_final.csv"
    output_file_path = base_path / f"data/collision_severity_model_eta={eta}_md={max_depth}_mcw={min_child_weight}_nboost={num_boost_round}.bin"

    # Read in and prepare data
    logger.info("Reading collision file")
    df_collision = pd.read_csv(model_file_path)
    df_collision.head(2)

    df_full_train, df_test = train_test_split(
        df_collision, test_size=0.2, random_state=11
    )

    # Perform validation
    logger.info("Performing validation")
    totals = perform_validation(
        df_full_train,
        kfold_n_splits=kfold_n_splits,
        eta=eta,
        max_depth=max_depth,
        min_child_weight=min_child_weight,
        num_boost_round=num_boost_round,
    )

    logger.info(
        "Validation results: max_depth=%d, min_samples_leaf=%d, n_estimators=%d %.3f +- %.3f",
        max_depth,
        min_child_weight,
        num_boost_round,
        np.mean(totals),
        np.std(totals),
    )

    # Train the final model
    logger.info("Training the final model")
    df_full_train = df_full_train.reset_index(drop=True)
    df_test = df_test.reset_index(drop=True)

    y_full_train = df_full_train["is_severe"].values
    y_test = df_test["is_severe"].values

    del df_test["is_severe"]
    del df_full_train["is_severe"]

    dv, model_final = train(
        df_full_train,
        y_full_train,
        eta=eta,
        max_depth=max_depth,
        min_child_weight=min_child_weight,
        num_boost_round=num_boost_round,
    )
    y_pred = predict(df_test, dv, model_final, y_test)
    auc = roc_auc_score(y_test, y_pred)

    logger.info("Score on final model: %.3f", auc)

    # Saving the model
    logger.info("Saving file to: %s", output_file_path)
    with open(output_file_path, "wb") as f_out:
        pickle.dump((dv, model_final), f_out)


if __name__ == "__main__":
    # Default Parameters
    num_boost_round_final = 43
    eta_final = 0.3
    max_depth_final = 4
    min_child_weight_final = 5

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--max_depth",
        help="depth of the decision tree (int)",
        default=max_depth_final,
        type=int,
    )

    parser.add_argument(
        "--min_child_weight",
        help="The minimum “sum of weights” of observations at each leaf.",
        default=min_child_weight_final,
        type=int,
    )
    parser.add_argument(
        "--num_boost_round",
        help="The number of boosting rounds",
        default=num_boost_round_final,
        type=int,
    )

    parser.add_argument(
        "--eta",
        help="The learning rate",
        default=eta_final,
        type=float,
    )

    args = parser.parse_args()

    train_model(
        max_depth=args.max_depth,
        min_child_weight=args.min_child_weight,
        num_boost_round=args.num_boost_round,
        eta=args.eta,
    )
