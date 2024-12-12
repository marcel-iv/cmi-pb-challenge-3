import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn import metrics
from sklearn.feature_selection import SelectKBest, r_regression
from sklearn.svm import SVR
from sys import exit
from scipy.stats import spearmanr


# constants
data_dir = "../00_data/master_harmonized_data_TSV/"
crt_year = 2024

# Helpers
def get_quals(estimator, x_test, y_test):
    y_predicted = estimator.predict(x_test)
    print(estimator.get_params())
    print("Spearman:", spearman(y_test, y_predicted))

# import dataset
combined = pd.read_csv("demographic_PBMCs_batchCorrected_wide.tsv", sep="\t")
demographic_columns = ['infancy_vac', 'biological_sex', 'age',]
cell_columns =  ['Monocytes', 'Classical_Monocytes',
       'Non-Classical_Monocytes', 'Intermediate_Monocytes', 'Bcells',
       'CD3CD19neg', 'CD3 Tcells', 'CD4Tcells', 'CD8Tcells', 'TemraCD4',
       'NaiveCD4', 'TemCD4', 'TcmCD4', 'TemraCD8', 'NaiveCD8', 'TemCD8',
       'TcmCD8', 'NK', 'Basophils', 'pDC', 'B cells (CD19+CD3-CD14-CD56-)',
       'B cells (CD19+CD20+CD3-CD14-CD56-)', 'Memory B cells', 'Naive B cells',
       'Proliferating B cells', 'Activated B cells (ABCs)', 'CD56+CD3+T cells',
       'CD4+CD8+ T cells', 'CD4-CD8- T cells', 'NK cells (CD3-CD19-CD56+)',
       'CD3-CD19-CD56- cells', 'non-pDCs',
       'CD3-CD19-CD56-CD14-CD16-CD123-CD11c-HLA-DR+cells',
       'Conventional dendritic cells (cDCs)', 'cDC1', 'cDC2',
       'Activated granulocytes',
       'Lineage negative cells (CD3-CD19-CD56-HLA-DR-CD123-CD66b-)',
       'CD56high NK cells']


# features
features = combined[demographic_columns + cell_columns].to_numpy()

# classes
classes = combined["Monocytes_D1"]

# Feature selection (pre-selection): select only the k best features
features =  SelectKBest(score_func=r_regression, k=10).fit_transform(features, classes)

# split into training, testing, validation
features_train, features_test, classes_train, classes_test = model_selection.train_test_split(features, classes, test_size=0.2, random_state=0)

# scorer method for spearman
def spearman(x,y):
    corr, pval = spearmanr(x,y)
    return(corr)

spearman_scorer = metrics.make_scorer(score_func=spearman, response_method='predict', greater_is_better=True)

# cross validation without optimization
cv = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
print(model_selection.cross_val_score(SVR(), features, classes, cv=cv, scoring=spearman_scorer))

# parameter grid
param_grid = [
    {'kernel': ['rbf', 'linear', 'poly'],
     'degree':[3,4,5],
     'C':[0.0001 ,0.001, 0.01, 0.1, 1, 5],
     'gamma':['scale', 'auto', 0.001, 0.01, 0.1, 0.2, 0.5, 1],
     'epsilon':[.1,.2,.3,.4]
     }]

# kernel: ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
# degree: poly only
# gamma: scale, auto, float
# episolon: >0
# C: >0

rgr_gridSearch = model_selection.GridSearchCV(SVR(), param_grid=param_grid, verbose=2, cv=cv, scoring=spearman_scorer)

rgr_gridSearch.fit(features_train, classes_train)

print(rgr_gridSearch.best_estimator_)
get_quals(rgr_gridSearch.best_estimator_, features_test, classes_test)



