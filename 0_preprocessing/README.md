# Preprocessing

The final dataset I used to train the models for this project is based on a real Road Safety dataset. I have changed the original dataset quite substantially so that I can build a model to predict the severity of a road traffic collision.

In this section I outline this journey of refining the dataset. This achieved across three notebooks. 

I have used three notebooks instead of one to make the process more digestable. Each notebook produces an interim file `collisions{number}.csv` stored in the `data` folder. The interim file acts as the input to the next stage of processing.

1. Stage 1: Drop columns

In the [Drop Columns Notebook](./01_dropping_columns.ipynb), I remove columns I don't want to use and outline why I decided not to use them.

Produces: `collisions1.csv`

2. Stage 2: Interpret, filter and transform data

In the [Interpret and Transform Notebook](./02_interpret_transform.ipynb) notebook I carry out some additional refinement:
- transform the categorical variables into readable strings 
- filter the data to include only those datapoints that have been collected by police officers who attended the scene of the road accident
- create the target variable `is_severe` from the `accident_severity` column
- handle date and time information
- format the data for consistency

Produces: `collisions2.csv`

3. Stage 3: Make the data fit our imaginary problem

The casualty number refers to the number of casualties in the accident. This was a potential target variable. Rather than predict how many people were injured, I decided to predict how severe the collision was.

For the scenario I aim to solve, it is unlikely that we would have concrete information about the casualty number so I remove this from the data.

Produces: `collisions3.csv`

## Background on data

The UK Department of Transport publishes road accident/collision and safety statistics. This data is for Great Britain only (i.e. it includes data for England, Scotland and Wales but does not data for include Northern Ireland).

The road casualty data I am was collected by the police. Police record personal injury road traffic collisions using a form called [STATS19](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/995422/stats19.pdf).

### Issues with the dataset

The data only includes collisions where an injury occurred and it only includes collisions reported to the police. As such it does not provide a complete coverage of road collisions and casualties. 

The data I use is collected by police officers who attended the scene of the accident. There is an element of subjectivity to the data, especially in the assessment of `accident_severity`, which I use to predict whether an accident is severe or not: a police officer is not a healthcare professional and is perhaps not able to accurately judge the severity of an injury at the roadside.

All this is to say that the dataset is not ideal for the problem we want to solve and I have made some assumptions about the data e.g. that the police officer's evaluation of the `accident_severity` is correct. Since this is a practice project, I decided it was OK to proceed.

### Access
The Road Safety Data is available for [download](https://www.data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-safety-data). 

I used the 2023 collision dataset and have downloaded a copy [here](./data/dft-road-casualty-statistics-collision-2023.csv).


### Interpreting Data fields

My main reference was the accompanying 2023 data guide [downloaded here](./data/dft-road-casualty-statistics-road-safety-open-dataset-data-guide-2023.xlsx).

Where this interpretation was insufficient, I also used the following resources:
- [STATS19](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/995422/stats19.pdf)
- [STATS20 document](https://assets.publishing.service.gov.uk/media/60d0cc968fa8f57cf3f0b3ad/stats20-2011.pdf) contains guidance on how the data should be collected by the police
- [Reported road casualty statistics: Background Quality Report](https://www.gov.uk/government/publications/reported-road-casualty-statistics-background-quality-report/reported-road-casualty-statistics-background-quality-report)