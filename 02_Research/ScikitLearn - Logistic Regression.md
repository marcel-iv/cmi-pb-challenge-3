# Logistic Regression
https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.LogisticRegression.html

## Summary of Method
- mainly used for classification
- fit all features alongside sigmoid function
- supports multi-class case


## Considerations
- 

## Options
- multiclass schemes
    - one-vs-rest (ovr)
    - cross-entropy loss (multinomial)
- class weight: if using bins, might be interesting?
- type of penality (L1, L2)
- type of solver (only multinomial)
    - lbfgs
    - newton-cg: recommended for n(samples) >> n(features): interesting if only considering non-transcriptome data
    - sag: requires features with the same scale
    - saga: requires features with the same scale

# Functions
- usually sci-kit learn function
- *predict_proba*: predicts probabilities
- *score*: accuracy of the test/classes. Especially harsh for multi-classes 
