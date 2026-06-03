🔐 AI-Based Cryptographic Side-Channel Attack Detection and Defense
<p align="center"> <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python"> <img src="https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green?style=for-the-badge"> <img src="https://img.shields.io/badge/Deep%20Learning-CNN-orange?style=for-the-badge"> <img src="https://img.shields.io/badge/Cybersecurity-Side%20Channel%20Analysis-red?style=for-the-badge"> <img src="https://img.shields.io/badge/Research-ISCADS%202026-success?style=for-the-badge"> </p>
AI-Based Cryptographic Side-Channel Attack Detection and Defense
📌 Project Overview

Modern cryptographic algorithms such as AES and RSA are mathematically secure, but their hardware implementations often leak physical information through:

Power Consumption
Timing Variations
Electromagnetic Emissions

These unintended leakages can be exploited through Side-Channel Attacks (SCA) to recover secret cryptographic keys.

This project presents an AI-driven end-to-end framework for detecting, analyzing, scoring, explaining, and defending against side-channel leakage using:

Machine Learning
Deep Learning
Explainable AI (XAI)
Automated Defense Intelligence

Using the ASCAD (ANSSI Side-Channel Analysis Database) dataset, the framework automates leakage detection and provides security recommendations for cryptographic systems.

🎯 Objectives
Detect cryptographic side-channel vulnerabilities from hardware power traces.
Localize leakage-prone regions in cryptographic executions.
Classify leakage patterns using Machine Learning and Deep Learning.
Quantify leakage severity through risk scoring.
Explain model decisions using saliency visualization.
Generate automated defense recommendations.
🚀 Why This Project Matters

Traditional leakage assessment techniques:

Require significant domain expertise
Are time-consuming
Are difficult to scale across devices

This project introduces an AI-powered cybersecurity framework capable of:

✔ Automated leakage detection

✔ High-accuracy classification

✔ Explainable security intelligence

✔ Severity-aware risk assessment

✔ Practical defense recommendations

🏗️ System Architecture
Data Acquisition
      ↓
Trace Alignment & Normalization
      ↓
Leakage Localization
      ↓
Window Extraction & Feature Computation
      ↓
Random Forest Detection
      ↓
CNN-Based Leakage Detection
      ↓
Leakage Severity Scoring
      ↓
Saliency-Based Explainability
      ↓
Defense Recommendation Engine
🔍 Key Features
🤖 AI-Powered Leakage Detection

Automatically detects vulnerable cryptographic traces from side-channel measurements.

📍 Leakage Localization

Identifies leakage-prone regions using variance-based statistical analysis.

🧠 Hybrid ML + Deep Learning Pipeline

Combines:

Random Forest (Interpretable Baseline)
CNN-Based Raw Trace Learning
⚠ Leakage Severity Scoring

Assigns risk levels:

Low
Medium
High
🔎 Explainable AI

CNN saliency maps highlight:

Sensitive execution regions
Leakage-prone time samples
Prediction-driving signal patterns
🛡️ Automated Defense Recommendation Engine

Maps detected leakages to practical mitigation strategies.

📊 Dataset
ASCAD (ANSSI Side-Channel Analysis Database)

This project utilizes the ASCAD benchmark dataset for side-channel security research.

Dataset Characteristics
50,000 AES Power Traces
Real Hardware Leakage Measurements
~700 Time Samples Per Trace
AES Encryption Execution Data
Labeled Side-Channel Leakage Information
Applications
Leakage Localization
Feature Extraction
Model Training
Security Evaluation

Dataset files are not included in this repository due to size limitations and licensing considerations.

🔬 Methodology
1️⃣ Leakage Localization

Variance-based statistical analysis is applied across aligned traces.

High variance regions indicate potential cryptographic leakage points.

2️⃣ Feature Extraction

Extracted statistical descriptors include:

Energy
Variance
Signal Statistics
Leakage Indicators
3️⃣ Random Forest Classifier

Machine learning baseline for:

Fast detection
Feature importance analysis
Interpretability
4️⃣ CNN-Based Raw Trace Learning

A 1D CNN automatically learns:

Leakage signatures
Sensitive execution patterns
Non-linear leakage behavior

Benefits:

Minimal manual feature engineering
Better generalization
High classification performance
5️⃣ Leakage Severity Scoring

Risk scores are calculated using:

Statistical Leakage Features
Energy Scores
Variance Scores
CNN Confidence Scores
Severity	Recommended Action
Low	Continue Monitoring
Medium	Noise Injection / Hiding
High	Masking / Randomization
6️⃣ Explainable AI

Saliency maps visualize:

Critical trace regions
Leakage-driving samples
Model decision factors
📈 Model Performance
Model	Accuracy	Precision	Recall	F1 Score
Logistic Regression	84.2%	83.7%	84.0%	83.8%
CNN (Raw Traces)	96.6%	96.4%	96.7%	96.5%
🏆 Quantitative Highlights
🎯 96.6% Detection Accuracy
🔍 Automated Leakage Localization
🧠 CNN-Based Raw Trace Learning
📊 Explainable AI Integration
⚠ Severity-Aware Risk Assessment
🛡 Automated Defense Recommendation System
🛡 Defense Recommendation Logic
High Severity

Recommended Countermeasures:

Masking
Execution Randomization
Hiding Techniques
Medium Severity
Noise Injection
Hiding Strategies
Low Severity
Monitoring
Periodic Security Auditing
📂 Project Structure
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
│   └── Dataset files (excluded from GitHub)
│
├── README.md
├── requirements.txt
└── results/
🛠️ Tech Stack
Programming Languages
Python
Machine Learning
Scikit-Learn
Random Forest
Logistic Regression
Deep Learning
PyTorch
CNN
Data Processing
NumPy
Pandas
H5Py
Visualization
Matplotlib
Explainable AI
Saliency Maps
Feature Importance Analysis
⚙️ Installation
git clone https://github.com/shreyaaa26-codes/AI-based-Cryptographic-Side-Channel-Attack-Detection-and-Defense.git

cd AI-based-Cryptographic-Side-Channel-Attack-Detection-and-Defense

pip install -r requirements.txt
▶️ Usage

Train Random Forest:

python scripts/train_rf_baseline.py

Train CNN:

python scripts/train_cnn_pytorch.py

Perform Leakage Severity Analysis:

python scripts/leakage_severity.py

Generate Defense Recommendations:

python scripts/defense_recommendation.py
🔮 Future Enhancements
Real-Time Leakage Monitoring Dashboard
Streamlit-Based Deployment
Live Risk Visualization
Alert-Based Security Monitoring
RSA/ECC Side-Channel Support
Hardware Security Validation Integration
Transformer-Based Leakage Detection Models
📚 Research Contribution

This project demonstrates how Artificial Intelligence can be integrated with cybersecurity to automate cryptographic side-channel leakage detection, risk scoring, explainability, and defense planning.

It bridges the gap between:

Cryptographic Security
Machine Learning
Deep Learning
Explainable AI
Security Analytics
🏅 Conference Presentation

ISCADS 2026 – Indian Symposium on Cybersecurity and Data Science
Manipal Institute of Technology Bengaluru
Manipal Academy of Higher Education

👩‍💻 Authors
Shreya L
Dhruti Aravind
Nishanth Shet
MK Koushik Iyer
