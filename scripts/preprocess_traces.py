import h5py
import numpy as np
import matplotlib.pyplot as plt

file_path = "data/ascad/ASCAD_fixed_key.h5"

with h5py.File(file_path, "r") as f:
    traces = f["Profiling_traces/traces"][:]
    labels = f["Profiling_traces/labels"][:]

print("Original trace shape:", traces.shape)
mean = np.mean(traces, axis=0)
std = np.std(traces, axis=0) + 1e-9
traces_norm = (traces - mean) / std

start = 100
end = 300
traces_window = traces_norm[:, start:end]
print("Windowed trace shape:", traces_window.shape)

plt.figure(figsize=(10, 4))
plt.plot(traces_window[0])
plt.title("Normalized Leakage Window (Single Trace)")
plt.xlabel("Time Samples")
plt.ylabel("Normalized Power")
plt.tight_layout()
plt.show()

# -----------------------------
# STEP 3.5: Feature Extraction
# -----------------------------
# =========================
# STEP 3.5: Feature Extraction
# =========================

def extract_features(trace):
    return [
        np.mean(trace),
        np.var(trace),
        np.max(trace),
        np.min(trace),
        np.sum(trace ** 2)  # energy
    ]

features = np.array([extract_features(t) for t in traces_window])

print("Feature matrix shape:", features.shape)

# =========================
# STEP 3.6: Save processed data
# =========================

np.save("data/ascad/traces_window.npy", traces_window)
np.save("data/ascad/features_rf.npy", features)
np.save("data/ascad/labels.npy", labels)

print("Preprocessing complete. Files saved.")
