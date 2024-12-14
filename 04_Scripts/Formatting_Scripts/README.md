## Overview

- scripts in this folder were used to convert the provided data by the CMI-PB team to a suitable format for the ENT predictor
- we highly recommend using the generic versions over the monocyte specific files, as they include PBMC, IgG and cytokine information in a single table, making it easier to use in the models, and include bug fixes not included in the other files

## Scripts

#### format_monocyte_data.py (deprecated)

- takes data from a table in wide format in code
- uses specimen ID to connect it to a subject ID from challenge_subject_specimen.tsv
- gets day from challenge_subject_specimen.tsv
- uses day to split assay data from D0 (features) and D1 (classes)
- extracts only monocyte total from D1
- merge demographic, D1 and D0 data into single file

#### format_monocyte_data_batchCorrected.py (deprecated)

- as format_monocyte_data.py, except it uses batch corrected data instead of harmonized data as an input
- as the batch corrected data has a slightly different format, some additional steps have been taken to convert it to the same format as the harmonized data

#### format_generic.py

- more generic version of the aforementioned formatting scripts, combines several tables in one
- works only on batchCorrected data (due to the different format)

#### format_generic_challenge_features.py

- same as the aforementioned generic formatting script, however this only works on challenge data (which does NOT include prediction targets as columns)

## Data format

- Wide format
- includes demographic data, monocyte data at day 1, IgG_PT at day 14, and other assay data
- Features: Every column, except "Monocytes_D1", "IgG_PT_D14"
- Classes/Prediction Target: Monocyte_D1 / IgG_PT_D14

## TODO / Future Possible Improvements

- CLI interface to allow more easier use of these scripts for different data sets of a similar format
