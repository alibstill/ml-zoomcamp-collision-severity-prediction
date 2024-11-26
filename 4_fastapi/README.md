# Collision Severity Prediction Service

The Collision Severity Prediction Service is a fastapi app that predicts whether a collision is severe (and by implication, likely to require further emergency services).


## Run the app locally (without docker)

Make sure that you have set up the `collision_severity_prediction_service` environment. See [enviroment_setup instruction](../environment_setup.md) This contains all the dependencies required to run the app.

To run the app **from this folder**:

```bash
conda activate 
uvicorn collision_severity_prediction_service.api:app --host 0.0.0.0 --port 8060
```


## Making a request
After getting the app running, navigate to `http://localhost:8060/docs` to view the API documentation and experiment with the API directly.

You will find an example request ready to for experimentation. The endpoint has validation and will tell you if you enter anything invalid. In these validation errors, you are also given example valid values.



