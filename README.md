# 🔬 Breast Cancer Detection System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-SVC-orange?style=for-the-badge&logo=scikit-learn)
![Accuracy](https://img.shields.io/badge/Accuracy-96%25-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**A machine learning web application that predicts whether a breast tumor is Malignant or Benign based on 20 clinical measurements.**

🚀 📓 [Notebook](notebook/breast_cancer.ipynb) &nbsp;|&nbsp; 📊 [Dataset](data/breast-cancer.csv)

</div>

---

## 📌 Overview

This project is a full end-to-end ML pipeline — from raw data preprocessing to a web application. It uses a **Support Vector Classifier (SVC)** trained on the Wisconsin Breast Cancer Dataset to classify tumors as **Malignant** or **Benign**.

> ⚠️ This tool is for **educational purposes only** and is not a substitute for clinical diagnosis.

---

## ✨ Features

- ✅ Full preprocessing pipeline — outlier detection, feature selection, scaling
- ✅ Trained SVC model with **96% test accuracy**
- ✅ Interactive web app built with Streamlit
- ✅ Real-time predictions from user input
- ✅ Clean, deployable project structure

---

## 🧠 ML Pipeline

```
Raw Data
   │
   ├── Check null values & duplicates
   ├── Drop ID column
   ├── Label encode target variable
   ├── Drop multicollinear features
   ├── Drop low correlation features
   ├── Detect & clip outliers
   │     ├── Normal features   → Z-score clipping
   │     └── Skewed features   → IQR clipping
   ├── Train / Test Split
   ├── Standard Scaling
   └── SVC Model (Polynomial Kernel, degree=3)
```

---

## 📊 Model Performance

| Metric | Malignant | Benign |
|--------|-----------|--------|
| Precision | 0.97 | 0.95 |
| Recall | 0.97 | 0.95 |
| F1-Score | 0.97 | 0.95 |
| **Overall Accuracy** | **96%** | |

### Model Configuration
```python
SVC(C=1, coef0=1, kernel='poly', degree=3, gamma='scale', max_iter=1000)
```

---

## 🗂️ Project Structure

```
breast-cancer-detection/
│
├── model/
│   ├── breast_cancer_model.pkl   ← trained SVC model
│   ├── scaler.pkl                ← fitted StandardScaler
│   └── features.pkl              ← selected feature names
│
├── notebook/
│   └── breast_cancer.ipynb       ← full pipeline notebook
│
├── data/
│   └── breast-cancer.csv         ← dataset
│
├── app.py                        ← Streamlit web app
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Scikit-learn | SVC model, preprocessing |
| Pandas & NumPy | Data manipulation |
| Streamlit | Web application |
| Joblib | Model serialization |
| Matplotlib | Visualization |

---

## ⚙️ How To Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/saim-ansari-tech/breast-cancer-detection.git
cd breast-cancer-detection
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

---

## 👨‍💻 Author

**Saim Ansari**
Robotics & AI Student | ML Engineer in Progress

[![GitHub](https://img.shields.io/badge/GitHub-saim--ansari--tech-black?style=flat&logo=github)](https://github.com/saim-ansari-tech)

---

<div align="center">
⭐ If you found this project helpful, please give it a star!
</div>