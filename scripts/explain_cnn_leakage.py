import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# -------------------------------
# Load traces
# -------------------------------
traces = np.load("data/ascad/traces_window.npy")

# -------------------------------
# CNN model (same as before)
# -------------------------------
class CNN_SCA(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv1d(1, 32, kernel_size=5)
        self.pool1 = nn.MaxPool1d(2)
        self.conv2 = nn.Conv1d(32, 64, kernel_size=5)
        self.pool2 = nn.MaxPool1d(2)
        self.fc1 = nn.Linear(64 * 47, 128)
        self.fc2 = nn.Linear(128, 1)

    def forward(self, x):
        x = torch.relu(self.pool1(self.conv1(x)))
        x = torch.relu(self.pool2(self.conv2(x)))
        x = x.view(x.size(0), -1)
        x = torch.relu(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x

# -------------------------------
# Load trained model
# -------------------------------
device = torch.device("cpu")
model = CNN_SCA().to(device)
model.load_state_dict(torch.load("data/ascad/cnn_model.pth", map_location=device))
model.eval()

# -------------------------------
# Pick ONE trace to explain
# -------------------------------
idx = 0
trace = torch.tensor(traces[idx], dtype=torch.float32)
trace = trace.unsqueeze(0).unsqueeze(0)
trace.requires_grad = True        # 👈 IMPORTANT
trace.retain_grad()               # 👈 CRITICAL FIX

# -------------------------------
# Forward + backward
# -------------------------------
output = model(trace)
output.backward()

saliency = trace.grad.abs().squeeze().cpu().numpy()

# -------------------------------
# Plot explanation
# -------------------------------
plt.figure(figsize=(10,4))
plt.plot(traces[idx], label="Power Trace", alpha=0.6)
plt.plot(saliency, label="Saliency (Leakage Importance)", color="red")
plt.legend()
plt.title("CNN Saliency Map — Leakage Explanation")
plt.xlabel("Time Samples")
plt.ylabel("Amplitude")
plt.show()
