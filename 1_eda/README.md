# EDA

In this section I carry out some exploratory data analysis which led to further refinement.

1. **Stage 1**: Handle missing data, complex categories

There are quite a lot of missing data points. I have handled this problem through a mixture of imputation and removal. In the [first notebook](./01_handle_missing_and_unknown_values.ipynb), I perform the final refinement of the dataset.

**Collapsing categories**

In many cases, handling the missing data meant removing rows, but I have also collapsed some of the more complex categories into simple booleans e.g. most of the data had the `carriageway_hazard` field set to none. Within this field, there were 5 categories. To simplify the data for the algorithm, I decided to create a new boolean field that simply recorded if there were any carriageway hazards. 

I used a similar technique for `special_conditions_at_site`,`pedestrian_crossing_human_control`, `junction_detail` and `pedestrian_crossing_physical_facilities`. 

2. **Stage 2**: Examine the distributions of the final features

In this notebook, I look at some of the distributions of certain features.

See [second notebook](02_eda_distributions.ipynb)

3. **Stage 3**: EDA and Feature Importance and save final version of data

In [this notebook](./02_eda_feature_importance.ipynb) I provide a detailed description of the columns and evaluate feature importance.

I also save the final cleaned collisions dataset to several other locations for ease of use.