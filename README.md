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
│   ├── gseapy_app
│   │   └── app.py
│   ├── gseapy_final_files
│   │   ├── il6_jak-stat_head_to_head_gsea_hallmark.csv
│   │   ├── il6_jak-stat_head_to_head_gsea_kegg.csv
│   │   ├── il6_jak-stat_head_to_head_gsea_reactome.csv
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
│   └── poster_figures
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

### Differentially Expressed Genes (deg)

### Gene Set Enrichment Analysis (gseapy)

### Single Sample Gene Set Enrichment Analysis (ssgsea)