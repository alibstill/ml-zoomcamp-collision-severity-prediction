# Environment Setup

I am using [conda](https://docs.conda.io/projects/conda/en/latest/index.html) for package and environment management.

There are two environments:
- `collision_severity`: this contains all the packages needed to run the notebooks and scripts in this repo
- `collision_severity_prediction_service`: this contains all the packages needed to run the fastapi service without docker

## Setting up the environments

1. Install conda - see [instructions](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

2. Create environment

The conda environment for the notebooks is documented in the `environment.yml` file. It contains all the packages I have used for the project.

Run the following command in the root folder of this project to create this environment:

```bash
conda env create -f environment.yml 
```

The conda environment for the fastapi app is documented in `environment_fastapi.yaml`. It contains packages relevant to running this service.

Run the following command in the root folder of this project to create this environment:

```bash
conda env create -f environment_fastapi.yml 
```

**Troubleshooting: Struggling to run the environment.yml?**

If there are any issues with installing the environment from file, you can simply create a new environment yourself and install the packages manually:

```bash
# collision_severity
conda create --name collision_severity
conda install pandas==2.2.3 scikit-learn=1.5.2 matplotlib==3.9.2 seaborn==0.13.2 py-xgboost==2.1.2 jupyter python==3.13.0 ipykernel openpyxl==3.1.5 tqdm==4.67.1

# collision_severity_prediction_service (fastapi service environment)
conda create --name collision_severity_prediction_service
conda install fastapi==0.115.5 scikit-learn=1.5.2 pandas==2.2.3 py-xgboost==2.1.2 python==3.13.0 pydantic-settings==2.6.1 uvicorn==0.32.1
```

3. Activate environment

The environment is called `collision_severity`.

```bash
conda activate collision_severity
```


## Jupyter notebooks with the collision_severity environment
I use Jupyter notebooks throughout this project.   

### Running a notebook

Assuming that you have created the basic environment above do the following before running your **first** notebook. 

1. Activate environment

The environment is called `collision_severity`.

```bash
conda activate collision_severity
```

2. Register the `ipykernel` with Jupyter

This step only needs to be done once in the `collision_severity` environment which is used to run the notebooks. Thereafter, when running notebooks, you can skip this.

In your active environment

```bash
conda activate collision_severity
python -m ipykernel install --user --name=collision_severity --display-name "collision_severity"
```

3. Start Jupyter

Running this command in the root of this project will give you access to all the files and jupyter notebooks. This command will open a jupyter notebook in your browser.

```bash
jupyter notebook
```

If you are asked to pick a kernel, you should be able to find `collision_severity` available for selection.