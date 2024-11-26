# Scripts

In this section, you will find the final model exported as a couple of scripts.

## Environment setup

To run these scripts, make sure that you have set up and activated the conda environment `collision_severity`. See [environment_setup.md](../environment_setup.md) for a more detailed description.

```bash
conda activate collision_severity
```

## Train xgboost 
The `train_xgboost` script trains and validates an XGBoost model against our dataset and then saves it to the local folder directory i.e. [3_scripts/data](./data/).

To recreate my final model model i.e. use the parameters that I found produced the best predictive results, run the following **within this directory**

```bash
python train_xgboost.py
```
If you want to run this script from the root directory:

```bash
 python 3_scripts/train_xgboost.py
 ```

The **default parameters are the final tuned parameters**:

- num_boost_round_final = 43
- eta_final = 0.3
- max_depth_final = 4
- min_child_weight_final = 5


### Parameterization (optional)
If you want to train, validate and save a **new** model, the script allows you to do this.

The following parameters can be passed into the script if you want to create a new model.

- num_boost_round_final (depth of the decision tree (int))
- eta_final (The learning rate)
- max_depth (depth of the decision tree (int))
- min_child_weight (The minimum “sum of weights” of observations at each leaf.)

Note that arguments are not validated beyond some basic type checking: it is up to the user to pass in a sensible value. 

You can also see the configurable parameters by running help:

**help**

```bash
python train_xgboost.py -h 
```

**example script**

```bash
python train_xgboost.py --max_depth=4 --min_child_weight=5 --num_boost_round=43 --eta=0.3
```

## Predict
You can use the predict script to make a prediction with the model.

The script loads the model and DictVectorizer that we saved in the `train_xgboost.py` script.

Since the input is quite a long JSON, I have set up the script so it reads the input from a json file. 

The following command reads the `collision_severity_model_md=5_msf=5_nestimators=130.bin` model file (the file that contains our tuned model) and uses `08_collision_example_request.json` as the input file

```bash
python predict.py # from this directory
python 3_scripts/predict.py # from root folder
```

**validation**

Note that I have not done any indepth validation. In particular, I have not validated the input json. It is up to the user to choose suitable values.

**help**

```bash
python predict.py -h 
```

### Parameterization (optional)
It is possible to pass in the filepath to a new input file and new model file. 

It might be simpler however just to modify the example request manually.

```bash
python predict.py --input_filepath=./data/collision_example_request.json --model_filepath=./data/collision_severity_model_eta=0.3_md=4_mcw=5_nboost=43.bin
```

