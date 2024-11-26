# Environment Setup



## Jupyter notebooks
I use Jupyter notebooks throughout this project and the [conda](https://docs.conda.io/projects/conda/en/latest/index.html) tool for package and environment management. 

### Running a notebook

1. Install conda - see [instructions](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

2. Create environment

My conda environment is documented in the `environment.yml` file. It contains all the packages I have used for the project.

Run the following command in the root folder of this project to create this environment:

```bash
conda env create -f environment.yml
```

**Struggling to run the environment.yml?**

If there are any issues with installing the environment from file, you can simply create a new environment yourself and install the packages yourself manually:

```bash
conda create --name collision_severity
conda install pandas==2.2.3 scikit-learn=1.5.2 matplotlib==3.9.2 seaborn==0.13.2 py-xgboost==2.1.2 jupyter python==3.13.0 ipykernel openpyxl==3.1.5 tqdm==4.67.1
```


3. Activate environment

The environment is called `collision_severity`.

```bash
conda activate collision_severity
```

4. Register the `ipykernel` with Jupyter

In your active environment

```bash
conda activate collision_severity
python -m ipykernel install --user --name=collision_severity --display-name "collision_severity"

```

5. Start Jupyter

Running this command in the root of this project will give you access to all the files and jupyter notebooks. This command will open a jupyter notebook in your browser.

```bash
jupyter notebook
```

If you are asked to pick a kernel, you should be able to find `collision_severity` available for selection.