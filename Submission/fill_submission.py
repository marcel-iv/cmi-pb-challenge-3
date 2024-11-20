import pandas as pd

submission = pd.read_csv("3rdChallengeSubmissionTemplate_10032024.tsv", sep="\t")
igg_d14 = pd.read_csv("../02_results/IgG_D14_Predictions.tsv", sep="\t")
igg_fc = pd.read_csv("../02_results/IgG_Fold_Predictions.tsv", sep="\t")
pbmc_d1 = pd.read_csv("../02_results/Monocyte_D1_Predictions.tsv", sep="\t")
pbmc_fc = pd.read_csv("../02_results/Monocyte_Fold_Predictions.tsv", sep="\t")

# convert index to rank, then merge by subject_id
def fill_ranks(df1,df2, col_name):
    df2["rank"] = df2.index
    df2["rank"] = list(map(lambda x: int(x) + 1, df2["rank"]))

    cols = df1.columns.to_list()
    cols = list(map(lambda x: x.replace(col_name, "rank"), cols))
    
    df = df1.merge(df2, left_on="SubjectID", right_on="Subject_ID").reindex(columns=cols)
    df = df.rename(columns = {"rank": col_name})
    return df

submission = fill_ranks(submission, igg_d14, '1.1) IgG-PT-D14-titer-Rank')
submission = fill_ranks(submission, igg_fc, '1.2) IgG-PT-D14-FC-Rank')
submission = fill_ranks(submission, pbmc_d1, '2.1) Monocytes-D1-Rank')
submission = fill_ranks(submission, pbmc_fc, '2.2) Monocytes-D1-FC-Rank')

submission.to_csv("ChallengeSubmission_20112024_Schoch_Rack_Cockburn.tsv", sep="\t")
