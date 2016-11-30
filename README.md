# IsoSeq_AS_de_novo

These scripts are writtern for doing de novo alternative splicing (AS) event detection using Iso-Seq data.

For AS detection, NCBI BLASTn results in .xml format should be used as the input for script 1step.py. Then, the output of 1step.py should be processed by other scripts in order, from 2.1 to 6.1. Finally, the 6.1step.py output should be processed by commands in the file 6.2step.txt. The final result is a list of read alignments which repersents AS event candidats. 


