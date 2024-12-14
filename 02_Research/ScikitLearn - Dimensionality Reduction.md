# Basic feature selection
https://scikit-learn.org/1.5/modules/feature_selection.html
- *Variance Threshold*: removes all features below certain threshold
- *SelectKBest*: extracts number of best features 
- *SelectPercentile*: extracts percentile of best features
    - Note: Useless for regression classification

# PCA
- unsupervised
- finds combination of features that accounts for highest variance across data

# Linear Discriminant Analysis (LDA)
- supervised 
- finds variance between classes

# Neighborhood Component Analysis (NCA)
https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_dim_reduction.html
- supervised
- finds features space that stochastic nearest neighbor algorithm will give the best accuracy
