---
semester: 7
note-type: research-notes
course: Prediction Challenge
date: 2024-10-18T13:00:00
default_file: "[[link]]"
summarised: true
tags: 
overview: "[[Orga - Prediction Challenge]]"
see also:
  - https://www.cmi-pb.org/blog/understand-data/
  - "[[2024-10-18 Prediction Meeting]]"
---

>[!todo]
>

---

## Vaccinations

>[!types of vaccines]
>- acellular pertussis (aP)
>	- born after 1995
>- whole-cellular pertussis (wP)
>	- born before 1995
>- booster: tetanus toxoid diphtheria toxoid (Td) + acellular pertussis antigens (ap, FHA, Fim2/3, PRN, pertussis toxin)

**Timeline**
![[Pasted image 20241017165951.png]]

>[!important] What does the data contain
>- <mark style="background: #BBFABBA6;">PBMC cell type frequencies</mark> for N=**122** subjects. Timepoints measured: Baseline, days 1,3,7,14
>- <mark style="background: #BBFABBA6;">Gene expression analysis on PBMCs</mark>. Samples that did not pass quality controls were removed and complete-time courses were obtained for N=**146** subjects. Timepoints measured: Baseline, days 1,3,7,14
>- <mark style="background: #BBFABBA6;">Plasma cytokine and chemokine concentrations</mark> of 45+ proteins of N=**107** subjects. Timepoints measured: Baseline, days 1,3,7,14
>- <mark style="background: #BBFABBA6;">Antigen-specific IgG, IgG subclasses (IgG1-4)</mark> for N=**166** subjects. Timepoints measured: Baseline, days 1,3,7,14
>- <mark style="background: #BBFABBA6;">_t_cell polarization_</mark> using FluoroSpot assay for N=**99** subjects. Timepoints measured: Baseline, day 28
>- <mark style="background: #BBFABBA6;">_t_cell activation_</mark> using AIM assay for N=**101** subjects. Timepoints measured: Baseline, day 28
>
>![[Pasted image 20241017170254.png]]

## Database

![[Pasted image 20241017170406.png]]

>[!info]- **A)** Information Tables
>- _subject_: Each row in the subject table represents an individual given a unique identification number (column name: subject_id). Other fields provide information about infancy vaccination status, TDaP (tetanus, diphtheria, and acellular-pertussis) vaccination booster date, and subject-specific information such as date of birth, biological sex, ethnicity, race, etc.
>- _specimen_: Each row in the subject table represents a clinical sample e.g., blood (specimen_id) for a subject (subject_id) at the particular visit. Additionally, information about the Nth visit, sample type, e.g., PBMC and days count relative to the boost is provided.

>[!info]- **B)** Experimental Data Tables
>These tables include data from mass cytometry, gene expression, antibody titer, and protein expression experiments. Each experimental data table has experiment-specific information.
>- _PBMC_cell_frequency:_ Each row in the _PBMC_cell_frequency_ table represents a specimen (specimen_id) along with the names and values for measured analytes, such as cell population name and percent live cell.
>- _plasma_gene_expression_: Each row in the _plasma_gene_expression_ table represents a specimen (specimen_id) along with the names and values for measured analytes such as gene (versioned_ensembl_gene_id) and tpm and raw count for each gene.
>- _plasma_ab_titer_: Each row in the _plasma_ab_titer_ table represents a specimen (specimen_id) along with the names and values for measured analytes such as antigen and IgG isotype with corresponding antibody titer. Antibody titer is represented by Mean Fluorescence Intensity (MFI) units.
>- _Plasma_cytokine_concentrations by Olink_: Each row in the _plasma_cytokine_concentrations_ table represents a specimen (specimen_id) along with the names and values for measured analytes such as the Olink protein identifier with corresponding protein expression values (_cytokine concentration_, pg/ml) and quality control values.
>- _Plasma_cytokine_concentrations by LEGENDplex_ table represents a specimen (specimen_id) along with the names and values for measured analytes, such as the protein identifier with corresponding protein expression values
>- _t_cell polarization_ table represents a specimen (specimen_id) along with the names and values for measured analytes (analyte concentration and unit).
>- _t_cell activation_ table represents a specimen (specimen_id) along with the names and values for measured analytes (analyte concentration and unit).

> [!info]- **C)** Metadata/ontology tables:
> This category includes metadata about genes, protein identifiers, and supplementary information to experimental data tables. For instance, cell populations are identified using the gating definition, and it is redundant to keep this information within the _PBMC_cell_frequency_ table. Therefore, a separate metadata table is created and linked.
> 
> - _gene_, _transcript_, and _protein_: These three metadata tables include gene and protein mapping information available in public databases such as Ensembl, Entrez, Uniprot, etc. Herein, gene, transcript, and protein ids are mapped to one another.
> 
> _cell_type_: It provides additional information about each cell population with their corresponding gating scheme used.

