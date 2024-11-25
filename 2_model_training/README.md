# Model Training and Evaluation

I trained and tuned three separate models:

- logistic regression
- random forest
- XGBoost

Be warned that some of these notebooks take a few minutes to run. I have used the `tqdm` package to show progress bars. I have set the algorithms to run with parallelisation where possible to speed things up.

## Results
All of the models had very similar ROC AUC scores after tuning. The results suggest that we should use the random forest model

| Model               | Final auc_score |
| ------------------- | --------------- |
| Logistic Regression | 0.614           |
| Random Forest       | 0.628           |
| XGBoost             | 0.628           |

## Evaluation and next steps
Our ROC AUC scores are disappointing but not necessarily 
surprising. I think the big problem here is the underlying dataset.

I wanted to work with a large real dataset with a decent amount of background information about the feature variables. The Road Safety dataset I am using is well documented but it was not built for predicting the severity of collisions: I have adapted the original for this purpose and taken some liberties with the meaning of the underlying features.

Since this project is purely to practice techniques, I don't consider my approach to be an issue. But if I really wanted to solve this problem I think I would learn more about this domain and collect slightly different data e.g. there is no data about the individuals involved in the collisions (perhaps this is important).

In addition to adding more appropriate data, I would also spend more time on feature engineering, dropping features with little value and possibly expressing the features in a slightly different way. Most of this data is categorical and many of these categories have lots of values. Perhaps a simpler categorisation would be useful initially.

