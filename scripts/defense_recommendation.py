import numpy as np

# Load severity labels (DATA file, not .py)
severity = np.load("data/ascad/leakage_severity.npy", allow_pickle=True)

label_map = {
    "L": "LOW",
    "M": "MEDIUM",
    "H": "HIGH"
}

recommendations = {
    "LOW": "No immediate action required. Continue monitoring.",
    "MEDIUM": "Apply masking or noise injection countermeasures.",
    "HIGH": "Enable constant-time execution and hardware masking."
}

print("\n Defense Recommendations:\n")

unique, counts = np.unique(severity, return_counts=True)

for lvl, count in zip(unique, counts):
    level = label_map[str(lvl)]
    print(f"{level}: {count} traces")
    print(f"→ Recommendation: {recommendations[level]}\n")
