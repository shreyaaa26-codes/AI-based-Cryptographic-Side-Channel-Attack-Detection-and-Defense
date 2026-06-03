import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load data
X = np.load("data/ascad/traces_window.npy")
features = np.load("data/ascad/features_rf.npy")

# Recreate binary labels (same as RF stage)
energy = features[:, -1]
threshold = np.median(energy)
y = (energy > threshold).astype(np.int64)

print("X shape:", X.shape)
print("y shape:", y.shape)

# Convert to PyTorch tensors
X = torch.tensor(X, dtype=torch.float32).unsqueeze(1)
y = torch.tensor(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

train_dataset = TensorDataset(X_train, y_train)
test_dataset = TensorDataset(X_test, y_test)

train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=128, shuffle=False)

print("CNN input shape:", X_train.shape)

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

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = CNN_SCA().to(device)

criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

train_acc, val_acc = [], []

epochs = 10

for epoch in range(epochs):
    model.train()
    correct, total = 0, 0

    for xb, yb in train_loader:
        xb, yb = xb.to(device), yb.to(device).float().unsqueeze(1)

        optimizer.zero_grad()
        outputs = model(xb)
        loss = criterion(outputs, yb)
        loss.backward()
        optimizer.step()

        preds = (outputs > 0.5).int()
        correct += (preds == yb.int()).sum().item()
        total += yb.size(0)

    acc = correct / total
    train_acc.append(acc)

    print(f"Epoch {epoch+1}/{epochs} — Train Accuracy: {acc:.4f}")

model.eval()
y_true, y_pred = [], []

with torch.no_grad():
    for xb, yb in test_loader:
        xb = xb.to(device)
        outputs = model(xb)
        preds = (outputs > 0.5).int().cpu().numpy()
        y_pred.extend(preds.flatten())
        y_true.extend(yb.numpy())

acc = accuracy_score(y_true, y_pred)
print("CNN Test Accuracy:", acc)

plt.plot(train_acc)
plt.title("CNN Training Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.show()

def forward(self, x):
    x = torch.relu(self.pool1(self.conv1(x)))
    x = torch.relu(self.pool2(self.conv2(x)))
    print("Flatten shape:", x.shape)  # 👈 TEMP
    x = x.view(x.size(0), -1)
    x = torch.relu(self.fc1(x))
    x = self.dropout(x)
    x = torch.sigmoid(self.fc2(x))
    return x

torch.save(model.state_dict(), "data/ascad/cnn_model.pth")
print("CNN model saved.")
