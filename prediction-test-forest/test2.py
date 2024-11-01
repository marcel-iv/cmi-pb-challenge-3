import numpy as np
import pandas as pd
import statistics

from scipy.stats import spearmanr
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Data preprocessing, copied from the server
demographic_data = pd.read_csv("~/challenge_environment/Prediction_Challenge_Data/training_subject_specimen.tsv", sep="\t")
antibody_data = pd.read_csv("~/challenge_environment/Prediction_Challenge_Data/training_plasma_antibody_levels_wide.tsv", sep="\t")

data = demographic_data[["specimen_id", "subject_id", "planned_day_relative_to_boost", "infancy_vac", "biological_sex", "year_of_birth"]]

data["year_of_birth"] = data["year_of_birth"].apply(lambda x: 2024 - int(x[0:4]))
data = data.rename(columns={"year_of_birth": "age"})

data["infancy_vac"] = data["infancy_vac"].apply(lambda x: 0 if x == "wP" else 1)

data["biological_sex"] = data["biological_sex"].apply(lambda x: 0 if x == "Female" else 1)

data_IgG_PT = antibody_data[["specimen_id", "IgG_PT", "IgG_PRN", "IgG_FHA", "IgG1_PT", "IgG1_PRN"]]
data = (data.merge(data_IgG_PT, left_on="specimen_id", right_on="specimen_id")
       .reindex(columns=["specimen_id", "subject_id", "planned_day_relative_to_boost", "infancy_vac", "biological_sex", "age", "IgG_PT", "IgG_PRN", "IgG_FHA", "IgG1_PT", "IgG1_PRN"]))

# split into training and testing

Features = data[['specimen_id', 'subject_id', 'planned_day_relative_to_boost', 'infancy_vac', 'biological_sex', 'age', "IgG_PRN", "IgG_FHA", "IgG1_PT", "IgG1_PRN"]]
Response = data[['IgG_PT']]

features_train, features_test, response_train, response_test = train_test_split(Features, Response, test_size = 0.2, random_state=101)

RandomForest = RandomForestRegressor(n_estimators=500, max_depth=10, max_features="log2", random_state=101)
RandomForest.fit(features_train, response_train)

predictions = RandomForest.predict(features_test)

result = features_test
result["IgG_PT"] = response_test
result["Prediction"] = predictions

r2 = r2_score(response_test.values.ravel(), predictions)
spearman_correlation, p_value = spearmanr(response_test, predictions)














print("R^2 Value:")
print(r2)
print("Spearman Correlation:")
print(spearman_correlation)
