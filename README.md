# Constructing Phylogenetic Tree from Viral Betacoronavirus Spike Protein Sequences

### Team Members
- Sara S. Ali
- Anya Mohanad
- Rand Saad

### Affiliation
Biologists of Baghdad (BOB) Science Club Summer Program 2024

### Project Overview
This project constructs a phylogenetic tree to understand the evolutionary relationships among viral betacoronavirus spike protein sequences. The main objective was educational, as part of the BOB Science Club Summer Program.

### Objectives
- Collect spike protein sequences from ENA.
- Clean and preprocess data using BioPython.
- Perform multiple sequence alignment (MSA) using MEGA 11.
- Construct a phylogenetic tree using ETE3 with 500 bootstrap replicates.
- Customize the phylogenetic tree for clear visualization.

### Tools and Software
- **BioPython**
- **MEGA 11**
- **ETE3**
- **Google Colab**

### Methods
1. **Sequence Alignment**: MSA with MEGA 11 (ClustalW).
2. **Tree Construction**: Using BioPython, Maximum Likelihood method, 500 bootstraps.
3. **Customization**: Tree customized with ETE3.

### Results
- Distinct clades for different betacoronavirus lineages.
- High bootstrap values indicate strong support.
- Highlights clades with unique spike protein mutations.

### Conclusion
Successfully constructed a phylogenetic tree, providing insights into betacoronavirus evolution. Demonstrated the educational value of bioinformatics projects.

### Files Included
- **README.md**: This file.
- **Cleaned_Data.fas**: Cleaned raw data file.
- **Cleaned_MSA.fas**: Cleaned MSA file.
- **Tree_construct.py**: Tree construction python script.
- **Visualization.py**: Tree visualization python script.
- **Tree.png**: Constructed tree visualization.

### References
- ENA: https://www.ebi.ac.uk/ena
- BioPython: https://biopython.org/
- MEGA 11: https://www.megasoftware.net/
- ETE3: http://etetoolkit.org/
