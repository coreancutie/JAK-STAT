## Overview
This is a repository for the JAK/STAT project at the University of Oregon Knight Campus Graduate Internship Program in collaboration with the Allen Institute for Immunology. Our team of three students from the 2025-2026 cohort worked on this project with the guidance and mentorship from Dr. Lucas Graybuck, Palak Genge, Yudong He, Mansi Singh, and other professionals and support teams at the Allen Institute. 

This project analyzes data from the larger [IL-6 + JAK/STAT Inhibitors](https://apps.allenimmunology.org/aifi/resources/10x-flex-il6/) project, *10x Flex v2 Enables High Throughput IL-6 Signaling Inhibitor Analysis in T cells*, where the effects of 88 different JAK/STAT inhibitors were studied using a prototype 10x Flex kit. 

This specific [formulation comparisons](https://apps.allenimmunology.org/aifi/resources/10x-flex-il6/formulations/) project focuses on the isolated T-cell responses between eight different JAK/STAT inhibitors with two formulations each (for a total of 16 inhibitors), as well as two controls (a positive, IL-6 treated control and a negative DMSO control).

The Allen Institute team preprocessed and annotated the single-cell RNA sequencing data initially, and these steps can be found in their [il6-jak-stat-screen GitHub Repository](https://github.com/aifimmunology/il6-jak-stat-screen/tree/development). 

## Project Biological Background
The Interleukin 6 (IL-6) Janus kinases/Signal Transducers and Activators of Transcription (JAK/STAT) pathway helps regulate the body’s inflammatory response through the differentiation of T-cells. When released by other immune cells, the IL-6 cytokine protein binds to T-cell surfaces and activates JAK/STAT proteins downstream inside the cell. The STAT proteins are phosphorylated when activated and turn transcription factors on and off inside the cell nucleus for functions related to immunity and cell growth.

**High levels of IL-6 can lead to an overactive immune response, causing overinflammation and contributing to cytokine storm responses in diseases such as COVID-19 and autoimmune diseases such as rheumatoid arthritis.** Common treatments of these diseases to reduce the inflammatory response are inhibitors along the JAK/STAT pathway.

## Project Goals
To learn more about known JAK/STAT inhibitors that either already serve as treatments or autoimmune diseases, or have the potential to be used as a treatment drug, this project aims to:
- investigate isolated T-cell response to the 16 JAK/STAT inhibitors
- identify differences between formulations
- explore off-target effects using singlecell RNA-sequencing data.

## Enviroment
Most of the single-cell analyses and visualizations were completed on the Allen Institute for Immunology's Human Immune System Explorer (HISE), using Jupyter Notebook instances. All notebooks are compatible with Python3.

## Repository Structure
Below is the tree structure of this repository. The directories that are not collapsed contain reproducible single-cell data exploration, differential gene expression, and gene set enrichment analyses, and the results of these sc-RNA seq analyses in the form of CSV files.

```
├── 2026_BGMP_JAKSTAT_poster.pdf
├── data_exploration
│   ├── data_exp_and_analysis_CC.ipynb
│   ├── data_exp_barplot_heatmap_CC.ipynb
│   ├── data_exp_filtering_PCA_UMAP_CC.ipynb
│   ├── data_exploration_1_JW.ipynb
│   ├── data_exploration_JW.ipynb
│   ├── exploring_data_CC.ipynb
│   ├── figures
│   └── Python_exploring_h5ad_files.ipynb
├── deg
│   ├── deg_CC.ipynb
│   ├── deg_final_files
│   │   ├── head-to-head_wilcoxon_deg_results.csv
│   │   ├── wilcoxon_deg_counts_logfc_0.1.csv
│   │   ├── wilcoxon_deg_counts_logfc_1.csv
│   │   └── wilcoxon_deg_results.csv
│   ├── deg_formulations.ipynb
│   ├── deg.ipynb
│   ├── figures
│   ├── intake_processing_upload.ipynb
│   └── interactive_drug_pairs_vis.py
├── gseapy
│   ├── gsea_tutorials
│   ├── gseapy_final_files
│   │   ├── il6_jak-stat_head_to_head_gseapy_hallmark.csv
│   │   ├── il6_jak-stat_head_to_head_gseapy_kegg.csv
│   │   ├── il6_jak-stat_head_to_head_gseapy_reactome.csv
│   │   ├── il6_jak-stat_paired-form_gseapy_hallmark.csv
│   │   ├── il6_jak-stat_paired-form_gseapy_kegg.csv
│   │   └── il6_jak-stat_paired-form_gseapy_reactome.csv
│   ├── gseapy_Hallmark_JW.ipynb
│   ├── gseapy_head_to_head_Hallmark_JW.ipynb
│   ├── gseapy_head_to_head_KEGG_JW.ipynb
│   ├── gseapy_head_to_head_Reactome_JW.ipynb
│   ├── gseapy_KEGG_JW.ipynb
│   ├── gseapy_Reactome_JW.ipynb
│   ├── gseapy_unused_visualization_code.ipynb
│   └── gseapy_poster_figures
│   │   ├── CD4Naive_Canertinib_scatterplot.svg
│   │   ├── CD4EffMem_RuxoComparison_scatterplot.svg
├── README.md
├── scanpy_tutorials
└── ssgsea
    ├── decoupler_DEG_results_CC.ipynb
    ├── decoupler_hall_and_prog_CC.ipynb
    ├── decoupler_hallmark_CC.ipynb
    ├── decoupler_progeny_CC.ipynb
    ├── decoupler_tuttorial_CC.ipynb
    ├── figures
    └── ssgsea_final_files
        ├── il6_jak-stat_paired-form_ssgsea_hallmark.csv
        └── il6_jak-stat_paired-form_ssgsea_progeny.csv
```

### Differentially Expressed Genes (deg):
Scanpy’s built in functions were utilized (Wolf, et al. 2018) to perform differential gene expression analysis. For each treatment and cell type, DGEs were determined with log1p-normalized counts using the negative (DMSO) control as the reference through Wilcoxon rank-sum tests. 

DGE was conducted between formulations for each drug pair using the same methodology. The CSV file for this head to head comparision between the formulations can be found in the `head-to-head_wilcoxon_deg_results.csv` file. For each comparison, gene-level statistics (test scores, log fold changes, p-values, and adjusted p-values) were extracted and compiled into individual results tables.

DGE was conducted between cell type + drug vs. control comparison using the same methodology. The results from these comparisons can be found in `wilcoxon_deg_counts_logfc_0.1.csv` and `wilcoxon_deg_counts_logfc_1.csv` where the long fold change was <0.1 and < 1 respectively. For each comparison, gene-level statistics (test scores, log fold changes, p-values, and adjusted p-values) were extracted and compiled into individual results tables.

CSV files for each cell type + drug vs. control comparison (preserving all genes in the limited panel) were used as input for downstream gene set enrichment analysis and single sample gene set enrichment analysis. 

### Gene Set Enrichment Analysis (gseapy):
Get set enrichment analysis (GSEA) was performed with the `GSEApy` package (Fang et al., 2023) using the MSigDB Hallmark, KEGG, and Reactome databases. First, genes were preranked based on the differential expression (log-fold change) for each drug treatment vs. DMSO control, or for each drug treatment pair's formulation comparisons, within each cell type. Pre-ranked GSEA was then conducted using the ranked gene lists to test for enrichment of predefined gene sets from the three databases.

Code for the pathway enrichment analyses and visualizations performed on the differential expression results for each cell type + drug treatment vs. DMSO control can be found in the following notebooks: `gseapy_<gene_set>_JW.ipynb`.
- The `il6_jak-stat_paired-form_gseapy_<gene_set>.csv` results include normalized enrichment scores, nominal p-values, and FDR q-values annotated with each cell type and drug treatment vs. control comparison.

For gene set enrichment analysis performed on the differential expression results between formulations for each drug pair, code can be found in these notebooks: `gseapy_head_to_head_<gene_set>_JW.pynb`.
- The `il6_jak-stat_head_to_head_gseapy_<gene_set>.csv` results include normalized enrichment scores, nominal p-values, and FDR q-values annotated with each cell type and formulation pair comparison.

For each database, certain pathways related to JAK/STAT, IL-6 signaling, immune responses, and innate immunity were selected for visualization purposes.

### Single Sample Gene Set Enrichment Analysis (ssgsea):
Single sample gene set enrichment analysis specifically for pathway enrichment analysis was using decoupler (Badia‑i‑Mompel et al., 2022) on the differential expression results for each cell type + drug treatment vs. DMSO control. We utilized decoupler's built-in function `dc.mt.ulm()` (Decoupler's Univariate Linear Model), to calculate enrichment scores from the PROGENy and MSigDB Hallmark databases. 

Code for the single sample pathway enrichment analyses and visualizations performed on the differential expression results for each cell type + drug treatment vs. DMSO control can be found in the following notebooks: `decoupler_hallmark_CC.ipynb`, `decoupler_progeny_CC.ipynb`, and `decoupler_hall_and_prog_CC.ipynb`. 

Enrichment result files `il6_jak-stat_paired-form_ssgsea_hallmark.csv` and `il6_jak-stat_paired-form_ssgsea_progeny.csv` include the mean change enrichment scores, p-values, and adjusted p-values annotated with each cell type, drug, and control for each database.

## Head-to-Head Formulation Comparisons Plotly App:
An interactive Plotly Dash web application exploring gene expression and pathway‑level results between formulations for each drug pair, and for each cell type, can be found linked to this project's [webpage](https://apps.allenimmunology.org/aifi/resources/10x-flex-il6/formulations/), or [here](https://allenimmunology.org/hydration/proxy/dash/1cc64dc0-acdf-4094-96be-d659960aaf5b//). The repository housing this app can be found within the [il6-jak-stat-screen GitHub Repository](https://github.com/aifimmunology/il6-jak-stat-screen/tree/development/uo-bgmp-dash/head-to-head-vis), under the `uo-bgmp-dash` directory.