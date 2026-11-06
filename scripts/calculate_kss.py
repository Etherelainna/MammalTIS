import csv

input_file = "tis_contexts.tsv"
output_file = "kss_scores.tsv"

# Position-specific weights (columns: A, T, G, C)
weights = [
    [0.04210526, 0, 0.03157895, 0.05263158],
    [0.04210526, 0.05263158, 0.10526316, 0.0625],
    [0.03157895, 0.04210526, 0.05263158, 0.07368421],
    [0.03157895, 0.01052632, 0.04210526, 0.05263158],
    [0.08421053, 0.07368421, 0.18947368, 0.10526316],
    [0.04210526, 0.05263158, 0.05263158, 0.08421053],
    [0.12631579, 0.0625, 0.12631579, 0.21052632],
    [0.83157895, 0.12631579, 0.65263158, 0.16842105],
    [0.15789474, 0.06315789, 0.11578947, 0.2],
    [0.21052632, 0.09473684, 0.31578947, 0.51578947],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0.24210526, 0.16666667, 0.53684211, 0.13684211],
    [0.15789474, 0.09473684, 0.09473684, 0.24210526],
    [0.05263158, 0.08421053, 0.14736842, 0.09473684],
    [0.07216495, 0.05263158, 0.10526316, 0.06315789],
    [0, 0, 0, 0.05263158],
    [0.05263158, 0.05263158, 0.10526316, 0.09473684],
    [0.04210526, 0.03157895, 0.05263158, 0.04210526],
    [0, 0, 0, 0],
    [0.04210526, 0.04210526, 0.08421053, 0.07368421],
    [0.0625, 0.04210526, 0.09473684, 0.05263158],
]

base_idx = {"A": 0, "T": 1, "G": 2, "C": 3}
max_score = sum(max(row) for row in weights)

def calculate_kss(context):
    context = context.strip().upper().replace("U", "T")
    if len(context) != 23: return "NA"
    score = sum(weights[i][base_idx[b]] for i, b in enumerate(context) if b in base_idx)
    return f"{score / max_score:.6f}"

with open(input_file, encoding="utf-8", newline="") as fin, open(output_file, "w", encoding="utf-8", newline="") as fout:
    reader = csv.DictReader(fin, delimiter="\t")
    writer = csv.writer(fout, delimiter="\t")
    writer.writerow(["context", "kss"])
    for row in reader:
        context = row["context"].strip()
        writer.writerow([context, calculate_kss(context)])

print(f"KSS results saved to {output_file}")
