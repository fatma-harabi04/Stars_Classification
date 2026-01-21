# 🌌 Astronomical Object Classification using SDSS Data

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://starsclassification.streamlit.app/)

An **end-to-end Machine Learning application** that classifies astronomical objects into **Galaxies**, **Quasars (QSO)**, or **Stars** using photometric observations from the **Sloan Digital Sky Survey (SDSS)**.  
The project covers the complete ML lifecycle: **data preprocessing, feature engineering, model comparison, and deployment**.

---

## ⭐ Project Highlights
- End-to-end ML pipeline from raw data to deployed web application  
- Physically motivated feature engineering using astronomical color indices  
- Comparative evaluation of multiple classification models  
- Real-time inference via an interactive Streamlit interface  

---

## 📊 Dataset Overview

The project uses photometric data from the **Sloan Digital Sky Survey (SDSS DR17)**, containing approximately **100,000 labeled astronomical observations**.

### Target Classes
- **GALAXY**
- **QSO (Quasar)**
- **STAR**

### Raw Input Features
- **u, g, r, i, z**: Apparent magnitudes measured across five optical wavelength bands

---

## 🔭 Scientific Context & Feature Interpretation

### Sloan Digital Sky Survey (SDSS)
The Sloan Digital Sky Survey is one of the most influential astronomical surveys, providing high-quality photometric and spectroscopic measurements for millions of celestial objects.  
This project relies on **photometric data**, which records how bright an object appears through different wavelength filters.

---

### Photometric Magnitudes (u, g, r, i, z)

Each magnitude represents the observed brightness of an object in a specific wavelength band:

| Band | Wavelength Region | Physical Interpretation |
|----|------------------|-------------------------|
| **u** | Ultraviolet | Sensitive to young, hot stars and accretion activity |
| **g** | Blue | Traces stellar populations and star formation |
| **r** | Red | Dominated by older stellar populations |
| **i** | Near-infrared | Less affected by dust extinction |
| **z** | Infrared | Sensitive to cool stars and distant galaxies |

Magnitudes follow a **logarithmic scale**, where smaller values indicate brighter objects.

---

### Astronomical Color Indices

Rather than relying on absolute magnitudes, the model uses **color indices**, defined as differences between magnitudes:

- **u − g**
- **g − r**
- **r − i**
- **i − z**

#### Physical Meaning
Color indices represent **relative flux differences** between wavelength bands and provide insight into:
- Surface temperature
- Stellar population age
- Chemical composition
- Redshift-related effects

Because magnitudes are logarithmic, each color index corresponds to the **logarithm of the flux ratio** between two bands.

---

### Why Color Indices Enable Classification

Different astronomical objects exhibit distinct spectral energy distributions:

- **Stars**  
  Emit approximately as black bodies; their colors correlate strongly with surface temperature.

- **Galaxies**  
  Produce composite spectra from billions of stars, gas, and dust, resulting in broader color distributions.

- **Quasars (QSO)**  
  Are dominated by accretion disks around supermassive black holes and often exhibit ultraviolet excess.

These physical differences cause natural separation in color-index feature space, making them highly effective for classification.

---

## 🧹 Data Preprocessing & Feature Engineering

- **Feature Selection**  
  Removed technical identifiers and observational metadata (e.g., object IDs, telescope configuration fields) that do not encode intrinsic physical properties.

- **Feature Engineering**  
  Constructed astrophysically meaningful color indices (`u−g`, `g−r`, `r−i`, `i−z`) to enhance class separability.

The final feature set focuses exclusively on **observable physical characteristics**, ensuring that predictions are driven by real astrophysical differences rather than dataset artifacts.

---

## 🤖 Modeling & Evaluation

Models were trained and evaluated using a **stratified train–test split** to preserve class balance.

| Model | Accuracy | Observations |
|------|----------|--------------|
| Logistic Regression | 76% | Baseline model; limited by linear decision boundaries |
| Decision Tree | 81–87% | Captured non-linear patterns but prone to overfitting |
| **XGBoost** | **88%** | Best overall performance and class-wise balance |

### Model Selection Rationale
**XGBoost** was selected due to:
1. Its ability to model complex non-linear relationships via gradient boosting  
2. Strong class-wise performance, achieving an **F1-score of 0.81 for the “STAR” class**  
3. Fast inference suitable for real-time web applications  

---

## 🚀 Interactive Web Application

The trained model is deployed using **Streamlit**, providing real-time predictions through an intuitive user interface.

**Application features:**
- Input validation using physically meaningful magnitude ranges (10.0–30.0)  
- Probabilistic confidence scores for each prediction  
- Instant classification from user-provided photometric values  

---

## ⚠️ Limitations & Future Work

- The model was trained on a single SDSS data release and may not generalize to other surveys  
- Future work could include uncertainty estimation, cross-survey validation, and temporal analysis  

---

## 🛠️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/fatma-harabi04/Stars_Classification.git

2. Create and activate a virtual environment:

python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.\.venv\Scripts\Activate.ps1     # Windows

3. Install dependencies:

pip install -r requirements.txt

4. Run the applicatio 

streamlit run app.py

## Technologies Used

Python

Pandas, NumPy

Scikit-learn

XGBoost

Streamlit

## Licence 
This project is intended for educational and portfolio purposes.