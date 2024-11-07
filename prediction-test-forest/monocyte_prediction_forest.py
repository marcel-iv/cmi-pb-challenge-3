import numpy as np
import pandas as pd
import statistics

from scipy.stats import spearmanr
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Data preprocessing, copied from the server
demographic_data = pd.read_csv("~/challenge_environment/Prediction_Challenge_Data/training_subject_specimen.tsv", sep="\t")
monocyte_data = pd.read_csv("~/challenge_environment/Prediction_Challenge_Data/training_pbmc_cell_frequency_wide.tsv", sep="\t")

data = demographic_data[["specimen_id", "subject_id", "planned_day_relative_to_boost", "infancy_vac", "biological_sex", "year_of_birth"]]

data["year_of_birth"] = data["year_of_birth"].apply(lambda x: 2024 - int(x[0:4]))
data = data.rename(columns={"year_of_birth": "age"})

data["infancy_vac"] = data["infancy_vac"].apply(lambda x: 0 if x == "wP" else 1)

data["biological_sex"] = data["biological_sex"].apply(lambda x: 0 if x == "Female" else 1)

data_monocyte = monocyte_data[["specimen_id",
                                "Monocytes",
                                "Classical_Monocytes", 
                                "Non-Classical_Monocytes", 
                                "Intermediate_Monocytes", 
                                "Bcells", "CD3CD19neg", 
                                "CD3 Tcells", 
                                "CD4Tcells", 
                                "CD8Tcells", 
                                "TemraCD4", 
                                "NaiveCD4", 
                                "TemCD4", 
                                "TcmCD4", 
                                "TemraCD8", 
                                "NaiveCD8", 
                                "TemCD8", 
                                "TcmCD8", 
                                "NK", 
                                "Basophils", 
                                "pDC", 
                                "B cells (CD19+CD3-CD14-CD56-)", 
                                "B cells (CD19+CD20+CD3-CD14-CD56-)", 
                                "Memory B cells",	
                                "Naive B cells",	
                                "Proliferating B cells", 
                                "Activated B cells (ABCs)", 
                                "CD56+CD3+T cells", 
                                "CD4+CD8+ T cells", 
                                "CD4-CD8- T cells", 
                                "NK cells (CD3-CD19-CD56+)", 
                                "CD3-CD19-CD56- cells", 
                                "non-pDCs", 
                                "CD3-CD19-CD56-CD14-CD16-CD123-CD11c-HLA-DR+cells", 
                                "Conventional dendritic cells (cDCs)", 
                                "cDC1", 
                                "cDC2", 
                                "Activated granulocytes", 
                                "Lineage negative cells (CD3-CD19-CD56-HLA-DR-CD123-CD66b-)", 
                                "CD56high NK cells"]]
data = (data.merge(data_monocyte, left_on="specimen_id", right_on="specimen_id")
       .reindex(columns=["specimen_id", "subject_id", "planned_day_relative_to_boost", "infancy_vac", "biological_sex", "age", "Monocytes", "Classical_Monocytes", "Non-Classical_Monocytes", "Intermediate_Monocytes", "Bcells", "CD3CD19neg", "CD3 Tcells", "CD4Tcells", "CD8Tcells", "TemraCD4", "NaiveCD4", "TemCD4", "TcmCD4", "TemraCD8", "NaiveCD8", "TemCD8", "TcmCD8", "NK", "Basophils", "pDC", "B cells (CD19+CD3-CD14-CD56-)", "B cells (CD19+CD20+CD3-CD14-CD56-)", "Memory B cells	Naive B cells",	"Proliferating B cells", "Activated B cells (ABCs)", "CD56+CD3+T cells", "CD4+CD8+ T cells", "CD4-CD8- T cells", "NK cells (CD3-CD19-CD56+)", "CD3-CD19-CD56- cells", "non-pDCs", "CD3-CD19-CD56-CD14-CD16-CD123-CD11c-HLA-DR+cells", "Conventional dendritic cells (cDCs)", "cDC1", "cDC2", "Activated granulocytes", "Lineage negative cells (CD3-CD19-CD56-HLA-DR-CD123-CD66b-)", "CD56high NK cells"]))


# split into training and testing
Features = data[['specimen_id', 'subject_id', 'planned_day_relative_to_boost', 'infancy_vac', 'biological_sex', 'age', "Classical_Monocytes", "Non-Classical_Monocytes", "Intermediate_Monocytes", "Bcells", "CD3CD19neg", "CD3 Tcells", "CD4Tcells", "CD8Tcells", "TemraCD4", "NaiveCD4", "TemCD4", "TcmCD4", "TemraCD8", "NaiveCD8", "TemCD8", "TcmCD8", "NK", "Basophils", "pDC", "B cells (CD19+CD3-CD14-CD56-)", "B cells (CD19+CD20+CD3-CD14-CD56-)", "Memory B cells	Naive B cells",	"Proliferating B cells", "Activated B cells (ABCs)", "CD56+CD3+T cells", "CD4+CD8+ T cells", "CD4-CD8- T cells", "NK cells (CD3-CD19-CD56+)", "CD3-CD19-CD56- cells", "non-pDCs", "CD3-CD19-CD56-CD14-CD16-CD123-CD11c-HLA-DR+cells", "Conventional dendritic cells (cDCs)", "cDC1", "cDC2", "Activated granulocytes", "Lineage negative cells (CD3-CD19-CD56-HLA-DR-CD123-CD66b-)", "CD56high NK cells"]]
Response = data[["Monocytes"]]

features_train, features_test, response_train, response_test = train_test_split(Features, Response, test_size = 0.2, random_state=101)


# Train the forest
RandomForest = RandomForestRegressor(n_estimators=500, max_depth=10, max_features="log2", random_state=101)
RandomForest.fit(features_train, response_train)

predictions = RandomForest.predict(features_test)

result = features_test
result["Monocytes"] = response_test
result["Prediction"] = predictions


# Evaluation
r2 = r2_score(response_test.values.ravel(), predictions)
spearman_correlation, p_value = spearmanr(response_test, predictions)

print("R^2 Value:")
print(r2)
print("Spearman Correlation:")
print(spearman_correlation)
