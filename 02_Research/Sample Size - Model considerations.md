# Low Sample Size
- required sample size varies greatly by model choice: model choice first -> then choose if splitting models by vaccine status might be useful
- for regression models: Splitting seems fine (even N>=25 is sometimes enough for simple models) https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0229345#sec004
-> simply try both: vaccine status as a feature vs separate models

# Type of model
- data probably too limited for NN
- multi-task SVM works very well on proteasome data -> applicable to feature high data sets?
- logistic regression works well
- random forest
- classification models can also be used for a rather small dataset, by using it recursively

# Metric
- predict absolute values -> compute rank and fold change -> use spearman coefficent as optimization metric 

# Machine learning prediction of malaria vaccine efficacy based on antibody profiles
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012131
- multi-task SVM vs SVM vs random forest vs regression: multi-task SVM performs the best
- used proteome assay (high number of features)

# Machine Learning for Predicting Vaccine Immunogenicity
- https://pubsonline.informs.org/doi/full/10.1287/inte.2016.0862
- not many information due to being locked
- gene markers (EIF2AK4) can be extremly useful in predictions -> search for one might be useful if we have a ton of spare server time

# Methods for predicting vaccine immunogenicity and reactogenicity
- https://www.tandfonline.com/doi/full/10.1080/21645515.2019.1697110#abstract
- excellent introduction in the field
- details on automatic feature selection methods: wrapper, embedded
- DAMIP classifier is a strong method - but for classification only
- LogMiNeR - regression model
- SIMON - combines tons of methods to test for the best one for cohort
- k-fold cross validation (10-fold reported to work well)

# Predictive Markers of Immunogenicity and Efficacy for Human Vaccines
- https://www.mdpi.com/2076-393X/9/6/579
- highlights the important of biomarkers, especially cytokines
- sex can play a significant role
- IL-4/IL-6 