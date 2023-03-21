# CAR_T_clonal_kinetics
Profiling CAR-T Cell Transcriptomic and Clonal Kinetics During Treatment

How to re-run analysis:
1. Download [scRNA-seq expression data](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE125881&format=file&file=GSE125881%5Fraw%2EexpMatrix%2Ecsv%2Egz) and [TCR-seq data](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE125881&format=file) via the hyperlinks into directory of choice.
2. Run `python prep_geo_data.py` to process the downloaded data into usable forms
3. Run `python download_geo_metadata.py` to download and process metadata about the samples
4. `expr_preprocessing.ipynb` does initial QC and normalization on the scRNA-seq, adds in metadata, then saves a preprocessed version of the data to `expr_preprocessed.h5ad`, which is used in the other notebooks to reduce repeating computation
5. `expr_analysis.ipynb` runs the scRNA-seq clustering, DEG, and GSEA on the single cell data (before factoring in clonotype information)
6. `pair_tcr_and_expr_data.ipynb` pairs the sc and TCR data together, including QC plots, and saves the resulting information to barcode_clonotypes.csv
7. `expr_analysis_of_clones` does the analysis of clonotype kinetics: kinetic patterns of the different clonotypes and DEG/GSEA of between clones based on their kinetics