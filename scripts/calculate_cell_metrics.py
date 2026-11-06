import csv
from collections import defaultdict

input_file = "tis_cell_data.tsv"
output_file = "cell_metrics.tsv"

# Store unique TISs at gene, cell-type, and species levels
gene_tis = defaultdict(set)
cell_gene_tis = defaultdict(set)
species_tis = defaultdict(set)
cell_tis = defaultdict(set)

with open(input_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        species = row["species"].strip().lower()
        gene = row["gene"].strip()
        cell = row["cell_type"].strip()
        chrom = row["chrom"].strip()
        strand = row["strand"].strip()
        pos = int(row["genomic_pos"])

        # Gene-level unique TIS: species + gene + genomic position
        gene_tis[(species, gene)].add(pos)

        # Species-level unique TIS: chromosome + strand + genomic position
        site = (chrom, strand, pos)
        species_tis[species].add(site)

        if cell:
            cell_gene_tis[(species, cell, gene)].add(pos)
            cell_tis[(species, cell)].add(site)

# Calculate Cell TIS coverage and Cell TIS enrichment
with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(["species", "gene", "cell_type", "cell_tis_count", "total_tis_count",
                     "cell_tis_coverage", "cell_tis_background", "cell_tis_enrichment"])

    for (species, cell, gene), sites in sorted(cell_gene_tis.items()):
        cell_count = len(sites)
        total_count = len(gene_tis[(species, gene)])
        coverage = cell_count / total_count
        background = len(cell_tis[(species, cell)]) / len(species_tis[species])
        enrichment = coverage / background

        writer.writerow([species, gene, cell, cell_count, total_count,
                         f"{coverage:.6f}", f"{background:.6f}", f"{enrichment:.6f}"])

print(f"Cell TIS metrics saved to {output_file}")
