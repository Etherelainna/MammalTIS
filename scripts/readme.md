\# TIS Characterization



This directory contains Python scripts used to calculate TIS characterization metrics in MammalTIS.



\## Kozak similarity score (KSS)



`calculate\_kss.py` calculates the Kozak similarity score based on the method described by Gleason et al. (2022). The score evaluates the similarity of sequences surrounding candidate TISs to the Kozak consensus sequence using position-specific nucleotide weights.



\## Conservation score



`calculate\_conservation.py` calculates the conservation score following the approach used in TISdb (Wan and Qian, 2014). The score is calculated as the mean phyloP value across seven nucleotides surrounding the start codon, using conservation tracks from the UCSC Genome Browser.



\## Cell TIS coverage and enrichment



`calculate\_cell\_metrics.py` calculates Cell TIS coverage and Cell TIS enrichment, two metrics defined in MammalTIS to characterize the distribution of candidate TISs across different cell types.



\## References



1\. Gleason AC, Ghadge G, Chen J, Sonobe Y, Roos RP. Machine learning predicts translation initiation sites in neurologic diseases with nucleotide repeat expansions. \*PLoS ONE\*. 2022;17:e0256411. https://doi.org/10.1371/journal.pone.0256411



2\. Wan J, Qian S-B. TISdb: A database for alternative translation initiation in mammalian cells. \*Nucleic Acids Research\*. 2014;42:D845–D850. https://doi.org/10.1093/nar/gkt1085



