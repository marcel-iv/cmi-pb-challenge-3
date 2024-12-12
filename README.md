# Overview
Script and research repository for the 3rd CMI-PB Prediction Challenge supervised by the Wimmers Lab at the University of Tübingen. The challenge website can be found [here.](https://www.cmi-pb.org/blog/prediction-challenge-overview/)

We used python to write our scripts and [scikit-learn](https://scikit-learn.org/stable/) for machine learning.

## Completed Challenge Tasks
We submitted results for tasks one and two of the prediction challenge, see [here.](https://www.cmi-pb.org/blog/prediction-challenge-overview/#Prediction%20challenge%20tasks) The submission can be found in the [submission](06_Submission) folder.

### Antibody Level Prediction
This task was about predicting the levels of IgG antibodies 14 days after vaccination and their fold change relative to day zero.

### Cell Frequency Prediction
This task was about predicting the frequency of monocytes in the patients one day after vaccination and the fold change relative to the day zero values.

# Data Processing
We used the specimen and subject IDs to merge the assay data, subject meta data, and monocyte data into a single wide format file to base our predictions on. More details in regards to the process can be found in the [README of the formatting scripts folder](04_Scripts/Formatting_Scripts).

# Approach
We decided to try three approaches for the prediction: 
- Random Forest ([Folder with Scripts](04_Scripts/Random_Forest))
- Support Vector Regression ([Folder with Scripts](04_Scripts/Support_Vector_Regression))
- Logistic Regression ([Folder with Scripts](04_Scripts/Logistic_Regression))

Of these, the random forest regressor produced the highest spearman coefficient in our preliminary testing, so we decided to focus on it. We used the random forest regressor from sci-kit learn and tuned it using a portion of the training data as validation data with the grid-search cross validation from sci-kit learn. From this we determined the optimal parameters based on the spearman coefficient of the results.

# Results
The results of the random forest predictions for the two tasks can be found in the [Results](05_Results) folder. They were generated with monocyte_prediction_forest.py for task I and IgG_prediction_forest.py for task II.


# Team Members
- Marcel Schoch
- Glenn Cockburn
- Raffael Rack

**Supervisor:** Florian Wimmers
