import csv
import math
import pyBigWig

# Input and output files
input_file = "tis_positions.tsv"
bigwig_file = "phyloP.bw"
output_file = "conservation_scores.tsv"

# Calculate mean phyloP scores at positions -3 to +4 relative to the start codon
bw = pyBigWig.open(bigwig_file)

with open(input_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8", newline="") as fout:
    reader = csv.DictReader(fin, delimiter="\t")
    writer = csv.writer(fout, delimiter="\t")
    writer.writerow(["chrom", "pos", "conservation_score"])

    for row in reader:
        chrom, pos = row["chrom"], int(row["pos"])
        score = "NA"
        chrom_len = bw.chroms(chrom)

        if chrom_len is not None and 1 <= pos <= chrom_len:
            values = bw.values(chrom, max(0, pos - 4), min(chrom_len, pos + 3))
            valid = [v for v in values if v is not None and not math.isnan(v)]
            if valid:
                score = f"{sum(valid) / len(valid):.6f}"

        writer.writerow([chrom, pos, score])

bw.close()
print(f"Conservation scores saved to {output_file}")
