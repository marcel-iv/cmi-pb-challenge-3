## format_monocyte_data.py
- takes data from a table in wide format in code
- uses specimen ID to connect it to a subject ID from challenge_subject_specimen.tsv
- gets day from challenge_subject_specimen.tsv
- uses day to split assay data from D0 (features) and D1 (classes)
- extracts only monocyte total from D1
- merge demographic, D1 and D0 data into single file

## format_monocyte_data_batchCorrected.py
- as format_monocyte_data.py, except it uses batch corrected data instead of harmonized data as an input
- as the batch corrected data has a slightly different format, some additional steps have been taken to convert it to the same format as the harmonized data

## logistic_regression.py
- Implementatation of a logistic regression in sklearn
- deprecated, uses only binary classes

## svr.py
- Implementation of Support Vector Regression in sklearn
- Produces inferior results to Random Forests -> use random forests instead

## Data format
- Wide format 
- includes demographic data, monocyte data at day 1, and other assay data
- Features: Every column, except "Monocytes_D1" 
- Classes/Prediction Target: Monocyte_D1