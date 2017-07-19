# Building RNA-seq Analysis Pipelines with Jupyter
## Overview
This repository contains a Jupyter notebook with a guided walkthrough to building a simple pipeline for analysis of an RNA-seq dataset, as well as supporting Python and R scripts.

The pipeline described in the notebook consists of the following steps:
1. **Download** an RNA-seq dataset (ARCHS4)
2. **Normalize expression** data (Variance Stabilizing Transformation)
3. Perform **Dimensionality Reduction** (PCA and t-SNE)
4. Visualize the dataset as a **clustered heatmap** (Clustergrammer)
5. Perform **Differential Gene Expression Analysis** (limma and CD)
6. Perform **Enrichment analysis** (Enrichr)
7. Perform a **small molecule query** (L1000CDS<sup>2</sup>)

## Requirements
To run the notebook, a stable installation of Python (>=2.7) and R (>=3.0) are required.  Some additional packages are required to run the pipeline, as shown in *requirements.txt*.

A Python 2.7 virtual environment with the required packages is included within the repository (*venv.zip*).