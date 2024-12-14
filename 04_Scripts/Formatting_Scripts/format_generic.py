import pandas as pd
from datetime import datetime

# constants
data_dir = "../../03_Data/batchCorrected/"
demographic_data_dir = "../../03_Data/demographic/"
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
data_demographic = pd.read_csv(demographic_data_dir + "training_subject_specimen.tsv", sep="\t")

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
data = mergeAssay(data_demographic, toWide("plasma_ab_titer_batchCorrected_data.tsv"))
data = mergeAssay(data, toWide("pbmc_cell_frequency_batchCorrected_data.tsv"))
data = mergeAssay(data, toWide("plasma_cytokine_concentrations_by_olink_batchCorrected_data.tsv"))

# split into pre/post vaccinated (or rather, D0 and D1)
pre_vax = data.loc[data["planned_day_relative_to_boost"] == 0]
# for post_vax, extract only D1 monocyte data, which is used as a prediction class/value + identifiers
post_vax = data.loc[data["planned_day_relative_to_boost"] == 1]

post_vax = post_vax[["specimen_id", "subject_id", "Monocytes"]]

# get D14 data of IgG PT (target for task 1)
post_vax_D14 = data.loc[data["planned_day_relative_to_boost"] == 14]
post_vax_D14 = post_vax_D14[["specimen_id", "subject_id", "IgG_PT"]]

# rename columns to preserve day information in columns
pre_vax = pre_vax.rename(columns={"specimen_id": "specimen_id_D0"})
post_vax = post_vax.rename(columns={"specimen_id": "specimen_id_D1", "Monocytes": "Monocytes_D1"})
post_vax_D14 = post_vax_D14.rename(columns={"specimen_id": "specimen_id_D14", "IgG_PT": "IgG_PT_D14"})

post_vax = (post_vax.merge(post_vax_D14, left_on="subject_id", right_on="subject_id")
                          .reindex(columns=["subject_id", "specimen_id_D1", "specimen_id_D14", "Monocytes_D1", "IgG_PT_D14"]))

# subject_id specimen_id_D0 specimen_id_D planned_day_relative_to_boost infancy_vac biological_sex age Monocytes_D0
final_cols = ["subject_id", "specimen_id_D0", "specimen_id_D1", "specimen_id_D14", "infancy_vac", "biological_sex", "age", "Monocytes_D1", "IgG_PT_D14"] + pre_vax.columns.to_list()[6:]

# recombine both into single wide table
combined = (pre_vax.merge(post_vax, left_on="subject_id", right_on="subject_id")
            .reindex(columns=final_cols))

# write to tsv
combined.to_csv("../../03_Data/demographic_IgG_PBMC_cytokine_both.tsv", sep="\t", index=False)