## Overview & Background of Project

This is a repository for the JAK/STAT project at the University of Oregon Knight Campus Graduate Internship Program in collaboration with the Allen Institute for Immunology. Three students from the 2025-2026 cohort worked on this project with the guidance and help from individuals at the Allen Institute. 

This project analyzes data from the [IL-6 + JAK/STAT Inhibitors](https://apps.allenimmunology.org/aifi/resources/10x-flex-il6/) project *10x Flex v2 Enables High Throughput IL-6 Signaling Inhibitor Analysis in T cells*. That project tested 88 different JAK/STAT inhibitors using a prototype 10x Flex kit. This specific project was a [formulation comparison](https://apps.allenimmunology.org/aifi/resources/10x-flex-il6/formulations/) between 8 different inhibitors with 2 formulations (16 inhibitors total) and 2 controls (posiitve IL-6 treated and negative DMSO). 

The Allen Institue team preprocessed, annotated, and handled the data and their work can be found in their [il6-jak-stat-screen GitHub Repository](https://github.com/aifimmunology/il6-jak-stat-screen/tree/development). 

## Project Biological Background

The Interleukin 6 (IL-6)  Janus kinases/  Signal Transducers and Activators of Transcription (JAK/STAT) pathway helps regulate the body’s inflammatory response through differentiation of T-Cells. The IL-6 cytokine protein binds to T-cell surfaces and activates JAK/STAT proteins downstream inside the cell. The STAT proteins get phosphorylated when activated and turns transcription factors on and off inside the cell nucleus. High levels of IL-6 are part of cytokine storm responses in diseases like COVID-19 and autoimmune diseases such as rheumatoid arthritis. Common treatments of these diseases to reduce the inflammatory response are treatments with inhibitors along the JAK/STAT pathway.

## Project Goals

This project aims to:
- investigate isolated T-cell response to 16 JAK/STAT inhibitors
- identify differences between formulations
- explore off-target effects using singlecell RNA-sequencing data
