import pandas as pd
from datetime import datetime

# constants
data_dir = "../../03_Data/harmonized/"
demographic_dir = "../../03_Data/demographic/"
crt_year = datetime.now().year

# read convert
def toWide(fn):
    df = pd.read_csv(data_dir + fn, sep="\t")
    df = df.fillna(0)
    df = df.transpose()
    df["specimen_id"] = df.index
    df["specimen_id"] = df["specimen_id"].apply(lambda x: int(x))
    return df

def mergeAssay(df1, df2):
    df2_assay_cols = df2.columns.to_list()
    df2_assay_cols.remove("specimen_id")
    df = (df1.merge(df2, left_on="specimen_id", right_on="specimen_id", how="left")
       .reindex(columns=df1.columns.to_list() + df2_assay_cols))
    df.fillna(0, inplace=True)
    return df

# import datasets
data_demographic = pd.read_csv(demographic_dir + "challenge_subject_specimen.tsv", sep="\t")

# format dataset
data_demographic = data_demographic[["subject_id", "specimen_id", "planned_day_relative_to_boost", "infancy_vac", "biological_sex", "year_of_birth"]]
# convert date of birth to age
data_demographic["year_of_birth"] = data_demographic["year_of_birth"].apply(lambda x: crt_year - int(x[0:4]))
data_demographic = data_demographic.rename(columns={"year_of_birth": "age"})
# convert type of vaccine to integer: 0 is wP, 1 is aP
data_demographic["infancy_vac"] = data_demographic["infancy_vac"].apply(lambda x: 0 if x == "wP" else 1)
# convert sex to integer: 0 is female, 1 is male
data_demographic["biological_sex"] = data_demographic["biological_sex"].apply(lambda x: 0 if x == "Female" else 1)

# combine all data sets of interest
df_pbmc = pd.read_csv(data_dir + "challenge_pbmc_cell_frequency_wide.tsv", sep="\t")
df_igg = pd.read_csv(data_dir + "challenge_plasma_antibody_levels_wide.tsv", sep="\t")
df_cytokine = pd.read_csv(data_dir + "challenge_plasma_cytokine_concentrations_by_olink_wide.tsv", sep="\t")

data = mergeAssay(data_demographic, df_igg)
data = mergeAssay(data, df_pbmc)
data = mergeAssay(data, df_cytokine)

# split into pre/post vaccinated (or rather, D0 and D1)
data = data.loc[data["planned_day_relative_to_boost"] == 0]

# write to tsv

data.to_csv("../../03_Data/challenge_IgG_PBMC_cytokine.tsv", sep="\t", index=False)