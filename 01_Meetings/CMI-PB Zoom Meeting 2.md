# 1. Bonus Task
- Th1 vs Th2 response differs for a/wp vaccines -> impacts efficacy difference
- measured in IFN-gamme/IL-5 secretion
- cash prize separate to main challenge

# 2. Other Updates
- data requires processing / normalization (standardized pipeline exists, from 2nd challenge) - code on github
    - harmonization (standardized formats, feature matching)
    - data normalization, batch effect correction
- harmonized data also available for download

# 3. Submission Process
- Hand-in is simply a excel sheet with rank/fc data for the different tasks 
    - equal ranking: use average place
- template exists on the website
- instructions on how to transform data for submission on website

- basic model 1: use pre-vax levels of IgG to predict post-vax levels
- basic model 2: use age as sole predictor

# 4. Reminders
- Office Hours coming up (Zoom meeting, 08.10.2024, 18:00)
- general timeline
- solution centre for general questions

# 5. Q&A
- usage of external data/predictors allowed, but handing in existing predictors isn't recommended
- Ranking is **high to low** (Spearman Correlation Coefficient used as evaluation metric -> optimize for that in model)