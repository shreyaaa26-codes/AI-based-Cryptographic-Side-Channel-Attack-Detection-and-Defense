import h5py
import numpy as np
import matplotlib.pyplot as plt

file_path = "data/ascad/ASCAD_fixed_key.h5"

with h5py.File(file_path, "r") as f:
    traces = f["Profiling_traces/traces"][:]

print("Total traces:", traces.shape)

# Plot first 20 traces
plt.figure(figsize=(12, 5))
for i in range(20):
    plt.plot(traces[i], alpha=0.3)

plt.title("Overlay of Multiple AES Power Traces")
plt.xlabel("Time Samples")
plt.ylabel("Power Consumption")
plt.tight_layout()
plt.show()

# Compute variance at each time sample
variance = np.var(traces[:2000], axis=0)

plt.figure(figsize=(12, 4))
plt.plot(variance)
plt.title("Variance Across Power Traces")
plt.xlabel("Time Samples")
plt.ylabel("Variance")
plt.tight_layout()
plt.show()

# Zoom into suspected leakage region
start = 100
end = 300

plt.figure(figsize=(50, 250))
for i in range(10):
    plt.plot(traces[i][start:end], alpha=0.5)

plt.title(f"Zoomed Leakage Window ({start}:{end})")
plt.xlabel("Time Samples")
plt.ylabel("Power")
plt.tight_layout()
plt.show()
