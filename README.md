# Collision Severity Prediction

## Scenario

Let's imagine we have a system that can detect when a collision involving casualties has happened on a road in Great Britain. Information about the location, the road, the number of vehicles, the environmental conditions and any particular hazards that exist on the road at the time are collected. 

We want to predict the severity of the collision: if the accident is severe, we want to ensure the relevant emergency services are notified immediately.

**Solution**

In this project, I build a model that predicts whether a collision is severe and make it available as an API. 

Note that this model is built to predict collision severity on roads in Great Britain only.

## Data used to build the model

The final dataset used to train the models in this project is based on a real Road Safety dataset for Great Britain. I have changed the original dataset quite substantially. For more information about the data and the preprocessing I carried out please see the [0_preprocessing](0_preprocessing/) folder.


## Navigating this project

This project documents the journey to creating the final prediction model and application.

- [0_preprocessing](0_preprocessing/): details how and why I transformed the original dataset
- [1_eda](1_eda/): exploratory data analysis
- [2_model_training](2_model_training/): I trained, tuned and evaluated 3 different models 
- [3_scripts](3_scripts/): contains scripts to train the final model and get predictions
- [4_fastapi](4_fastapi/): contains the fastapi app

Most of the sections contain Jupyter notebooks. To setup the local jupyter environment see [environment_setup.md](./environment_setup.md)


## The final app

### Running the final app

There are several ways to run the final app. 

Once running, navigate to `http://localhost:8060/docs` to view and test out the API.


1. Run docker-compose

```bash
docker-compose up -d
```

2. Build and run the docker container

```bash
# build the app
docker build -t collision_severity .
# Run the app
docker run -it --rm -p 8060:8060 collision_severity
```

3. Run locally without container

See [4_fastapi README.md](4_fastapi/README.md) for instructions.





