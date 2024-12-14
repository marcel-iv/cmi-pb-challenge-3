import pandas as pd

# constants
data_dir = "../00_data/master_allData_batchCorrected_TSV/"
demographic_data_dir = "../00_data/master_harmonized_data_TSV/"
crt_year = 2024

# import datasets
data_demographic = pd.read_csv(demographic_data_dir + "training_subject_specimen.tsv", sep="\t")
data_pbmc = pd.read_csv(data_dir + "pbmc_cell_frequency_batchCorrected_data.tsv", sep="\t")

data_pbmc = data_pbmc.transpose()

# list of columns without subject id -> list of PBMC types considered
cell_types = data_pbmc.columns.to_list()

# Subject ID is interpreted as an index -> use it as column instead
data_pbmc["specimen_id"] = data_pbmc.index
data_pbmc["specimen_id"] = data_pbmc["specimen_id"].apply(lambda x: int(x))

# format dataset
data = data_demographic[["subject_id", "specimen_id", "planned_day_relative_to_boost", "infancy_vac", "biological_sex", "year_of_birth"]]

# convert date of birth to age
data["year_of_birth"] = data["year_of_birth"].apply(lambda x: crt_year - int(x[0:4]))
data = data.rename(columns={"year_of_birth": "age"})

# convert type of vaccine to integer: 0 is wP, 1 is aP
data["infancy_vac"] = data["infancy_vac"].apply(lambda x: 0 if x == "wP" else 1)

# convert sex to integer: 0 is female, 1 is male
data["biological_sex"] = data["biological_sex"].apply(lambda x: 0 if x == "Female" else 1)

# get data from PBMC sheet, replace NA and merge into demographic table (which now acts as main table)
#monocyte_cols = data_pbmc.columns
data_pbmc = data_pbmc.fillna(0)

print(data.columns.to_list())
print(data_pbmc.columns.to_list())

## merge into demographic data, preserve all PBMC information, except for specimen_id of PBMC (to prevent duplicate)
data = (data.merge(data_pbmc, left_on="specimen_id", right_on="specimen_id", how="left")
       .reindex(columns=data.columns.to_list() + cell_types))


# split into pre/post vaccinated (or rather, D0 and D1)
pre_vax = data.loc[data["planned_day_relative_to_boost"] == 0]
# for post_vax, extract only D1 monocyte data, which is used as a prediction class/value + identifiers
post_vax = data.loc[data["planned_day_relative_to_boost"] == 1]

print(post_vax.columns)
post_vax = post_vax[["specimen_id", "subject_id", "Monocytes"]]

# rename columns to preserve day information in columns
pre_vax = pre_vax.rename(columns={"specimen_id": "specimen_id_D0"})
post_vax = post_vax.rename(columns={"specimen_id": "specimen_id_D1", "Monocytes": "Monocytes_D1"})

print("\n\n-------\n\n")
print(pre_vax.columns)
print(post_vax.columns)

final_cols = (["subject_id", "specimen_id_D0", "specimen_id_D1", "infancy_vac", "biological_sex", "age"] + cell_types + ["Monocytes_D1"])

# recombine both into single wide table
combined = (pre_vax.merge(post_vax, left_on="subject_id", right_on="subject_id")
            .reindex(columns=final_cols))

# write to tsv
combined.to_csv("./demographic_PBMCs_batchCorrected_wide.tsv", sep="\t", index=False)