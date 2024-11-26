import argparse
import pickle
import logging
import json
import pandas as pd
from pathlib import Path
import xgboost as xgb

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def get_model_dv(model_filepath):
    with open(model_filepath, "rb") as f_in:
        dv_new, model_new = pickle.load(f_in)
        return dv_new, model_new


def get_input(input_filepath):
    with open(input_filepath, "r") as f_in:
        input = json.load(f_in)
        return input


def predict(model_filepath, input_filepath):
    input = get_input(input_filepath=input_filepath)
    logging.info("Collision Input: %s", input)
    dv_new, model_new = get_model_dv(model_filepath=model_filepath)
    X_new = dv_new.transform([input])
    dtest = xgb.DMatrix(X_new, feature_names=list(dv_new.get_feature_names_out()))

    y_pred = model_new.predict(dtest)
    logging.info("Prediction: %.3f", y_pred)
    is_severe_collision = "Yes" if y_pred >= 0.5 else "No"
    logging.info("Is this a severe collision?: %s", is_severe_collision)


if __name__ == "__main__":
    # Default Parameters
    base_path = Path(__file__).parent
    model_file_default = (
        base_path / "data/collision_severity_model_eta=0.3_md=4_mcw=5_nboost=43.bin"
    )
    input_file_default = base_path / "data/collision_example_request.json"

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model_filepath",
        help="Path to the bin file containing the model (and DictVectorizer)",
        default=model_file_default,
        type=str,
    )

    parser.add_argument(
        "--input_filepath",
        help="Path to the file containing input (json) ",
        default=input_file_default,
        type=str,
    )

    args = parser.parse_args()

    predict(model_filepath=args.model_filepath, input_filepath=args.input_filepath)
