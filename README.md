# IsoSeq_AS_de_novo

These scripts are writtern for doing de novo alternative splicing (AS) event detection using Iso-Seq data.

For AS detection, NCBI BLASTn results in .xml format should be used as the input for script 1step.py. Then, the output of 1step.py should be processed by other scripts in order, from 2.1 to 6.1. Finally, the 6.1step.py output should be processed by commands in the file 6.2step.txt. The final result is a list of read alignments which repersents AS event candidats. 

More details:
Liu, Xiaoxian, et al. "Detecting Alternatively Spliced Transcript Isoforms from Single‐Molecule Long‐Read Sequences without a Reference Genome." Molecular Ecology Resources (2017).
hppt://onlinelibrary.wiley.com/doi/10.1111/1755-0998.12670/full
