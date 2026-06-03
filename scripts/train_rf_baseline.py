import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
features = np.load("data/ascad/features_rf.npy")
labels_raw = np.load("data/ascad/labels.npy")

print("Features shape:", features.shape)
print("Original labels shape:", labels_raw.shape)

# Compute leakage score (energy feature)
energy = features[:, -1]

# Threshold = median energy
threshold = np.median(energy)

# Binary labels
labels_binary = (energy > threshold).astype(int)

print("Attack samples:", np.sum(labels_binary == 1))
print("Safe samples:", np.sum(labels_binary == 0))

X_train, X_test, y_train, y_test = train_test_split(
    features,
    labels_binary,
    test_size=0.25,
    random_state=42,
    stratify=labels_binary
)

rf = RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Safe", "Attack"],
            yticklabels=["Safe", "Attack"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Attack Detection Confusion Matrix")
plt.tight_layout()
plt.show()

feature_names = ["Mean", "Variance", "Max", "Min", "Energy"]
importances = rf.feature_importances_

plt.figure(figsize=(6,4))
plt.bar(feature_names, importances)
plt.title("Feature Importance (Leakage Indicators)")
plt.ylabel("Importance")
plt.tight_layout()
plt.show()
