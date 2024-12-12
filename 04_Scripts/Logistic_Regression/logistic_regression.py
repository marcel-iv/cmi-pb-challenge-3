import pandas as pd
import numpy as np
import statistics
from sklearn import model_selection
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sys import exit


# constants
data_dir = "../00_data/master_harmonized_data_TSV/"
crt_year = 2024

# Helpers
def get_quals(estimator, x_test, y_test):
    y_predicted = estimator.predict(x_test)
    print(estimator.get_params())
    print("ACC: ", metrics.accuracy_score(y_test, y_predicted))
    print("Balanced ACC: ", metrics.balanced_accuracy_score(y_test, y_predicted))
    print("MCC: ", metrics.matthews_corrcoef(y_test, y_predicted))
    print("AUC: ", metrics.roc_auc_score(y_test, y_predicted))

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

# classes: continous does not work, requires discrete classes
classes = combined["Monocytes_D1"]

# workaround 1: above/below median as classes
print(statistics.median(classes))
igg_median = statistics.median(classes)
classes = np.array(list(map(lambda x: 1 if x >= igg_median else 0, combined["Monocytes_D1"])))

# split into training, testing, validation
features_train, features_test, classes_train, classes_test = model_selection.train_test_split(features, classes, test_size=0.2, random_state=0)

# cross validation without optimization
cv = model_selection.StratifiedShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
print(model_selection.cross_val_score(LogisticRegression(random_state=0, max_iter=1000), features, classes, cv=cv, scoring='roc_auc'))

# parameter grid
param_grid = [
    {'solver': [], 'C':[0.01, 0.1, 0.5, 1, 1.5, 2, 3, 4, 5], 'class_weight':[None, 'balanced'], 'solver':['lbfgs', 'libnear', 'newton-cg',  'newton-cholesky', 'sag', 'saga']}
]

grid = model_selection.GridSearchCV(LogisticRegression(), param_grid=param_grid, verbose=1, cv=cv, scoring='roc_auc')

# fit model with training set
#clf = LogisticRegression(random_state=0).fit(features_train, features_train)

exit()
grid.fit(features_train, features_train)
get_quals(grid.best_estimator_, features_test, classes_test)

# predict
#clf.predict()

# predict probability -> used for ranking
#clf.predict_proba()

# rank predictions according to probability (seperately by negative/positive)

# compute spearman ranking coefficient (scipy.stats.spearmanr)

