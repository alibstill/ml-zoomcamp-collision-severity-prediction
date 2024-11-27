FROM continuumio/miniconda3:24.9.2-0


# create and cd into app directory
WORKDIR /app

# copy conda dependencies file  into /app
COPY ["environment_fastapi.yml", "./"]

# create conda environment ensuring that start from scratch (no caching)
RUN conda env create -f environment_fastapi.yml && conda clean --all --yes

# Make sure that the collision_severity_prediction_service environment is available
# for any command without explicitly activating it
ENV PATH=/opt/conda/envs/collision_severity_prediction_service/bin:$PATH

# copy code into app
COPY ["./4_fastapi/collision_severity_prediction_service", "./prediction_service"]

# expose port 9696 to host machine
EXPOSE 8060

# execute this command when the dockerfile is run i.e run our predict service
ENTRYPOINT ["conda", "run", "-n", "collision_severity_prediction_service", "uvicorn", "--port", "8060", "--host","0.0.0.0", "prediction_service.api:app"]