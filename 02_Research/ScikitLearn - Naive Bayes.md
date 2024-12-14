# Naive Bayes classifier
https://scikit-learn.org/1.5/modules/naive_bayes.html
https://scikit-learn.org/1.5/modules/generated/sklearn.naive_bayes.GaussianNB.html

## Summary
- mainly used for classification
- assume all variables are independant from each other

## Considerations
- independat assumption might be bad for assay data
- Good classifier, bad estimator

## Options
- Gaussian for continous data
- Multinomial for binned data (which is a loss of information, but kernel density estimation might improve this considerably https://scikit-learn.org/stable/modules/density.html)
