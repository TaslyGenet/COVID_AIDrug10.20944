# COVID19 AI Drug
**Network Bioinformatics Analysis Provides Insight into Drug Repurposing for COVID-2019** (submitted) 
https://www.preprints.org/manuscript/202003.0286/v1 (preprint.org)


## 2019-nCoV-Network
The network data was calculated automatically by AutoNet program. The 2019-nCoV-networkTable.txt contains two columns of genes in total of 938 interactions and 1344 genes. 2019-nCoV-networkList.txt contains the specific subnetworks named by hub-genes. Data sources for this network includes a local meta-pathway database for pathway enrichment analysis and a meta-PPI database to grow the network. The meta-pathway database is made of human pathways in KEGG and Reactome (v70) databases, after removing small pathways (less than five genes) and pathways which enrich too easily, such as hsa05200: Pathways in cancer. The meta-PPI database is composed of protein-protein interaction databases HPRD, BioGrid (excluding genetic interactions), and STRING (excluding PPIs with confidence score < 0.7). 

## 2019-nCoV-Candidate Drug
`2019nCOV-potential-drug.csv`: a list of 78 repurposable drugs screened from more than 8200 potential drugs based on proximity-based network analysis.

## 2019-nCoV-Core Biomarker
Contains results and some code for Autoseed and literature text mining, including:  
 - `2019-nCoV-AutoSeed`folder:
   - `2019nCOV_autoseed_biomarkers-SYMBOL.csv`: a list of COVID-19 related genes and detailed descriptions from genecards. 
   - `2019nCoV_target_New Chemical Entity-NCE.csv`: New Chemical Entity information of the COVID-19 related genes.
   - `gene.Rdata`: a list of COVID-19 related genes stored in Rdata format
 - `2019-nCoV-Literature Mining` folder  

## 2019-nCoV-Core Pathway
`2019ncov_autoseed_core_pathways.csv`: 24 enriched pathways associated with COVID-19  

## 2019-nCoV-VirusNGS
`seq.fasta`: contains the complete genome sequences as representative to build a phylogenetic tree: Bat coronavirus BM48-31/BGR/2008 (NC_014470.1), Bat coronavirus CDPHE15/USA/2006 (NC_022103.1), NL63-related bat coronavirus strain BtKYNL63-9a (NC_032107.1), Bat coronavirus HKU8 (NC_010438.1), Bat coronavirus HKU5-1 (NC_009020.1), SARS-CoV (NC_004718.3), MERS-CoV (KX034094.1), Bat coronavirus 1A (NC_010437.1), Human coronavirus OC43 (KX344031.1), Human coronavirus NL63 (JX504050.1), Human coronavirus HKU1 (KF686340.1), Human coronavirus 229E (KY996417.1), Bat coronavirus HKU4-1 (NC_009019.1), Scotophilus bat coronavirus 512 (NC_009657.1), Rousettus bat coronavirus HKU9 (MG762674.1), Rousettus bat coronavirus HKU10 (NC_018871.1), Bat coronavirus HKU2 (NC_009988.1) and Porcine coronavirus HKU15 (NC_039208.1).  
`aln-fasta.fasta`: contains the Multiple sequence alignment results which calculated by EMBL-EBI’s MSA tool.  

## article_supplementary_info
Cotnains three tables mentioned in the publication:
`Supp_table_1_2019-nCoV_autoseed_34_seed_genes.xlsx`: lists 34 covid-19 related genes  
`Supp_table_2_2019-nCoV_enriched_pathways.xlsx`: lists enriched pathways  
`Supp_table_3_78_drugs.xlsx`: lists a full list of 78 predicted drugs for covid-19 repurposing  
 
