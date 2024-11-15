## Log:
- implemented forest, SVR
- feature selection: variance threshold, k-best
- spearman as scoring function
- simple cross validation scoring
- parameter optimazation with grid

## Results:
- SVR: Spearman of 0.55 (feature selection increases score)
- Random Forest: Spearman of 0.83 (no features selection -> feature selection reduces score)

## Tasks:
- Marci: table with all non-gene expression data as features
	- demographic data,Monocyte_D1,all other data
- Raffael: apply to random forest, extract p% best features, test if it works
	- run optimization on server if neccessary
- Marci: Script to format challenge data, so that application becomes possible
- Raffael: Function to compute log change from estimator + challenge features
- ???: Script/Function to write results to final submission file