# 🔐 AI-Based Cryptographic Side-Channel Attack Detection and Defense

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-CNN-orange)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Side%20Channel%20Analysis-red)
![Research Project](https://img.shields.io/badge/Status-Research%20Project-success)

---

## 📌 Overview

This project presents an AI-driven framework for detecting and analyzing cryptographic side-channel leakages using Machine Learning and Deep Learning techniques.

The system leverages the ASCAD (ANSSI Side-Channel Analysis Database) dataset to identify information leakage patterns from power consumption traces and provides automated defense recommendations to enhance cryptographic security.

The framework combines:

- Statistical Leakage Analysis
- Feature Engineering
- Random Forest Classification
- CNN-Based Leakage Detection
- Leakage Severity Scoring
- Explainable AI Techniques
- Automated Defense Recommendation Engine

---

## 🎯 Objectives

- Detect cryptographic side-channel vulnerabilities from power traces.
- Classify leakage patterns using Machine Learning and Deep Learning models.
- Analyze leakage severity levels.
- Generate automated defense recommendations.
- Improve security assessment of cryptographic implementations.

---

## 🏗️ System Architecture

```text
ASCAD Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Feature Extraction
      │
      ├──► Random Forest Classifier
      │
      └──► CNN-Based Leakage Detection
                   │
                   ▼
         Leakage Severity Analysis
                   │
                   ▼
      Defense Recommendation Engine
```

---

## 🚀 Key Features

### 🤖 AI-Powered Leakage Detection
Automatically detects vulnerable cryptographic traces.

### 📍 Leakage Localization
Identifies leakage-prone regions in power traces using statistical variance analysis.

### 🧠 Hybrid ML + Deep Learning Pipeline
Combines:
- Random Forest (Interpretable Baseline)
- CNN (Deep Learning Detection)

### ⚠ Leakage Severity Scoring
Assigns risk levels:
- Low
- Medium
- High

### 🔎 Explainable AI
Uses CNN saliency maps to highlight:
- Sensitive execution regions
- Important time samples
- Leakage-driving signal patterns

### 🛡️ Defense Recommendation Engine
Maps leakage severity to practical cryptographic countermeasures.

---

## 📊 Dataset

### ASCAD (AES Side-Channel Analysis Database)

Dataset Characteristics:

- 50,000 AES Power Traces
- Real Hardware Leakage Measurements
- AES Encryption Operations
- Side-Channel Leakage Labels
- Benchmark Dataset for Security Research

> Dataset files are not included in this repository due to size and licensing constraints.

---

## 🔬 Methodology

### 1. Leakage Localization
Variance-based statistical analysis is performed across aligned traces to identify leakage-prone regions.

### 2. Feature Extraction
Statistical descriptors are extracted, including:
- Energy
- Variance
- Signal Statistics
- Leakage Indicators

### 3. Random Forest Classifier
Provides:
- Fast Detection
- Feature Importance Analysis
- Interpretable Baseline Performance

### 4. CNN-Based Leakage Detection
A 1D Convolutional Neural Network learns:
- Leakage Signatures
- Sensitive Execution Patterns
- Complex Non-Linear Leakage Behavior

### 5. Leakage Severity Scoring

| Severity | Recommended Action |
|----------|-------------------|
| Low | Continue Monitoring |
| Medium | Noise Injection / Hiding |
| High | Masking / Randomization |

### 6. Explainable AI
Saliency maps visualize:
- Important Trace Segments
- Leakage-Prone Regions
- Model Decision Factors

---

## 📈 Results

| Model | Accuracy | Precision | Recall | F1 Score |
|---------|----------|----------|--------|---------|
| Logistic Regression | 84.2% | 83.7% | 84.0% | 83.8% |
| CNN (Raw Traces) | **96.6%** | **96.4%** | **96.7%** | **96.5%** |

---

## 📂 Project Structure

```text
AI-based-Cryptographic-Side-Channel-Attack-Detection-and-Defense/
│
├── scripts/
│   ├── preprocess_traces.py
│   ├── train_rf_baseline.py
│   ├── train_cnn_pytorch.py
│   ├── leakage_severity.py
│   ├── explain_cnn_leakage.py
│   └── defense_recommendation.py
│
├── data/
│
├── README.md
└── requirements.txt
```

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-Learn
- Random Forest
- Logistic Regression

### Deep Learning
- PyTorch
- Convolutional Neural Networks (CNN)

### Data Processing
- NumPy
- Pandas
- H5Py

### Visualization
- Matplotlib

---

## ⚙️ Installation

```bash
git clone https://github.com/shreyaaa26-codes/AI-based-Cryptographic-Side-Channel-Attack-Detection-and-Defense.git

cd AI-based-Cryptographic-Side-Channel-Attack-Detection-and-Defense

pip install -r requirements.txt
```

---

## ▶️ Usage

Train Random Forest:

```bash
python scripts/train_rf_baseline.py
```

Train CNN:

```bash
python scripts/train_cnn_pytorch.py
```

Run Leakage Severity Analysis:

```bash
python scripts/leakage_severity.py
```

Generate Defense Recommendations:

```bash
python scripts/defense_recommendation.py
```

---

## 🔮 Future Enhancements

- Real-Time Leakage Monitoring
- Streamlit-Based Dashboard
- Live Risk Visualization
- RSA/ECC Side-Channel Support
- Transformer-Based Leakage Detection
- Hardware Security Validation Integration

---

## 🏅 Research Presentation

Presented at:

**ISCADS 2026 – Indian Symposium on Cybersecurity and Data Science**  
Manipal Institute of Technology Bengaluru  
Manipal Academy of Higher Education

---

## 👩‍💻 Authors

- Shreya L
- Dhruti Aravind
- Nishanth Shet
- MK Koushik Iyer

---

## ⭐ Project Highlights

- AI-Powered Side-Channel Attack Detection
- Cryptographic Security Assessment
- Explainable AI Integration
- Automated Defense Recommendation System
- Research-Oriented Cybersecurity Project
