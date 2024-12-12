# Overview
Script and research repository for the 3rd CMI-PB Prediction Challenge (https://www.cmi-pb.org/blog/prediction-challenge-overview/), supervised by the Wimmers Lab at the University of Tübingen.

## Completed Challenge Tasks
We submitted results for tasks one and two of the prediction [challenge](https://www.cmi-pb.org/blog/prediction-challenge-overview/#Prediction%20challenge%20tasks). The submission can be found in the [Results](05_Results) folder.

# Data Processing
We used the specimen and subject IDs to merge the assay data, subject meta data, and monocyte data into a single wide format file to base our predictions on. More details in regards to the process can be found in the README of the formatting scripts folder.

# Approach
We decided to try three approaches for the prediction: a random forest, a support vector machine, and logistic regression. Of these, the random forest regressor produced the highest spearman coefficient in our preliminary testing, so we decided to focus on it.

# Team Members
- Marcel Schoch
- Glenn Cockburn
- Raffael Rack
- Florian Wimmers (Superviser)
