import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# -------------------------------
# Load saved data
# -------------------------------
features = np.load("data/ascad/features_rf.npy")
traces = np.load("data/ascad/traces_window.npy")

print("Features shape:", features.shape)
print("Traces shape:", traces.shape)

# -------------------------------
# Statistical leakage features
# -------------------------------
energy = features[:, -1]
variance = np.var(traces, axis=1)

def normalize(x):
    return (x - np.min(x)) / (np.max(x) - np.min(x) + 1e-9)

energy_n = normalize(energy)
variance_n = normalize(variance)

# -------------------------------
# CNN model definition
# -------------------------------
class CNN_SCA(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv1d(1, 32, kernel_size=5)
        self.pool1 = nn.MaxPool1d(2)
        self.conv2 = nn.Conv1d(32, 64, kernel_size=5)
        self.pool2 = nn.MaxPool1d(2)
        self.fc1 = nn.Linear(64 * 47, 128)
        self.dropout = nn.Dropout(0.4)
        self.fc2 = nn.Linear(128, 1)

    def forward(self, x):
        x = torch.relu(self.pool1(self.conv1(x)))
        x = torch.relu(self.pool2(self.conv2(x)))
        x = x.view(x.size(0), -1)
        x = torch.relu(self.fc1(x))
        x = self.dropout(x)
        x = torch.sigmoid(self.fc2(x))
        return x

# -------------------------------
# Load trained CNN
# -------------------------------
device = torch.device("cpu")
model = CNN_SCA().to(device)
model.load_state_dict(torch.load("data/ascad/cnn_model.pth", map_location=device))
model.eval()

# -------------------------------
# Compute CNN leakage scores
# -------------------------------
cnn_scores = []

with torch.no_grad():
    for i in range(len(traces)):
        x = torch.tensor(traces[i], dtype=torch.float32).unsqueeze(0).unsqueeze(0)
        score = model(x).item()
        cnn_scores.append(score)

cnn_scores = np.array(cnn_scores)
cnn_scores_n = normalize(cnn_scores)

# -------------------------------
# Final leakage risk score
# -------------------------------
risk_score = (
    0.4 * energy_n +
    0.4 * cnn_scores_n +
    0.2 * variance_n
)

# -------------------------------
# Severity classification
# -------------------------------
severity = np.zeros_like(risk_score, dtype=str)
severity[risk_score < 0.33] = "LOW"
severity[(risk_score >= 0.33) & (risk_score < 0.66)] = "MEDIUM"
severity[risk_score >= 0.66] = "HIGH"

unique, counts = np.unique(severity, return_counts=True)

plt.bar(unique, counts)
plt.title("Leakage Severity Distribution")
plt.xlabel("Severity Level")
plt.ylabel("Number of Traces")
plt.show()

np.save("data/ascad/leakage_severity.npy", severity)
print("Leakage severity saved.")
