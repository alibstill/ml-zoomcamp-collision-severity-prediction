# EDA

In this section I carry out some exploratory data analysis which lead to further refinement.

## Refinements: missing data, complex categories

There are quite a lot of missing data points in the dataset which I have handled through imputation or removed.

**Collapsing categories**

I have also collapsed some of the more complex categories into simple booleans e.g. most of the data had the `carriageway_hazard` field set to none. Within this field, there were 5 categories. To simplify the data for the algorithm, I decided to create a new boolean field that simplify recorded if there were any carriageway hazards. 

I used a similar technique for `special_conditions_at_site`,`pedestrian_crossing_human_control` and `pedestrian_crossing_physical_facilities`. 
