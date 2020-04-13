# COVID_AIDrug10.20944
Tasly GeneNet COVID-19 DRUG REPURPOSING DATA SHARING


Tasly GeneNet COVID-19 DRUG REPURPOSING DATA SHARING

2019-nCoV-Network：
The network data was calculated automatically by AutoNet program. The 2019-nCoV-networkTable.txt contains two columns of genes in total of 938 interactions and 1344 genes. 2019-nCoV-networkList.txt contains the specific subnetworks named by hub-genes. Data sources for this network includes a local meta-pathway database for pathway enrichment analysis and a meta-PPI database to grow the network. The meta-pathway database is made of human pathways in KEGG40 and Reactome (v70)44 databases, after removing small pathways (less than five genes) and pathways which enrich too easily, such as hsa05200: Pathways in cancer. The meta-PPI database is composed of protein-protein interaction databases HPRD45, BioGrid46 (excluding genetic interactions), and STRING47 (excluding PPIs with confidence score < 0.7). 

2019-nCoV-Candidate Drug
2019nCOV-potential-drug.csv : a list of 78 repurposable drugs identified from more than 8200 potential drugs based on proximity-based network analysis. 

2019-nCoV-Core Biomarker
2019nCOV_autoseed_biomarkers-SYMBOL.csv file : a list of COVID-19 related genes and detailed descriptions from genecards. 
2019nCoV_target_New Chemical Entity-NCE.csv : New Chemical Entity information of the COVID-19 related genes.
gene.Rdata : a list of COVID-19 related genes stored in R format

2019-nCoV-Core Pathway
2019ncov_autoseed_core_pathways.csv: 24 enriched pathways associated with CODID-19 

2019-nCoV-VirusNGS
The seq.fasta file contains the complete genome sequences as representative to build a phylogenetic tree: Bat coronavirus BM48-31/BGR/2008 (NC_014470.1), Bat coronavirus CDPHE15/USA/2006 (NC_022103.1), NL63-related bat coronavirus strain BtKYNL63-9a (NC_032107.1), Bat coronavirus HKU8 (NC_010438.1), Bat coronavirus HKU5-1 (NC_009020.1), SARS-CoV (NC_004718.3), MERS-CoV (KX034094.1), Bat coronavirus 1A (NC_010437.1), Human coronavirus OC43 (KX344031.1), Human coronavirus NL63 (JX504050.1), Human coronavirus HKU1 (KF686340.1), Human coronavirus 229E (KY996417.1), Bat coronavirus HKU4-1 (NC_009019.1), Scotophilus bat coronavirus 512 (NC_009657.1), Rousettus bat coronavirus HKU9 (MG762674.1), Rousettus bat coronavirus HKU10 (NC_018871.1), Bat coronavirus HKU2 (NC_009988.1) and Porcine coronavirus HKU15 (NC_039208.1). the aln-fasta.fasta file contains the Multiple sequence alignment results which calculated by EMBL-EBI’s MSA tool.









