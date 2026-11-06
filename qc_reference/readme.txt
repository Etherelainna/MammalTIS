
# Ribo-TISH

MammalTIS used Ribo-TISH (v0.2.8) for data quality assessment and translation initiation site (TIS) identification. The `quality` module evaluates aligned ribosome-protected fragments (RPFs) by estimating P-site offsets for different RPF lengths and assessing read enrichment around annotated TISs.

## Quality control

For high-confidence TI-seq datasets, the mean TIS enrichment score of the three RPF lengths with the highest read counts was required to be at least 18.

To determine this threshold, three conventional Ribo-seq datasets were selected as background references. For each dataset, the mean TIS enrichment score of the three RPF lengths with the highest read counts was calculated. These three mean values were then averaged to obtain the Ribo-seq reference level, and three times this value was used as the minimum enrichment requirement for TI-seq datasets.

Quality assessment was performed using the following command:

```bash
ribotish quality \
  -b sample.bam \
  -g genome.gtf \
  -l 25,36 \
  -t \
  -p 8
```

## Data sources

The sequencing datasets were obtained from the NCBI [Sequence Read Archive (SRA)](https://www.ncbi.nlm.nih.gov/sra/).

Reference genome annotations (GTF) were obtained from NCBI RefSeq:

- **Human (GRCh38.p14, RS_2024_08):** [Download GTF](https://ftp.ncbi.nlm.nih.gov/genomes/all/annotation_releases/9606/GCF_000001405.40-RS_2024_08/)
- **Mouse (GRCm39, RS_2024_02):** [Download GTF](https://ftp.ncbi.nlm.nih.gov/genomes/all/annotation_releases/10090/GCF_000001635.27-RS_2024_02/)

## Reference

Zhang P, He D, Xu Y, et al. Genome-wide identification and differential analysis of translational initiation. *Nature Communications*. 2017;8:1749.

Ribo-TISH: https://github.com/zhpn1024/ribotish
