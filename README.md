# Pedestrian Volume Prediction using Nested MERF-XGB

This repository contains the official implementation of the modeling framework presented in the paper **"Improving Network Level Pedestrian Activity Prediction by Accounting for Spatial and Longitudinal Clustering in Crowdsourced Data"**.

The repository provides the complete pipeline for:
1. Comparing different modeling strategies (Local, Global, Global + Cluster Features, and Mixed-Effects models).
2. Performing hyperparameter tuning for the **Mixed-Effects Regression Forest with XGBoost Fixed Effects (MERF-XGB)** model using cluster-aware Group-K-Fold cross-validation.
3. Training the final predictive model with random intercepts per spatial-temporal cluster.
4. Conducting SHAP-based feature importance and location-specific attribution analyses.

---

## Methodological Overview

The core contribution of this work is the implementation of a semiparametric mixed-effects model for panel data. Standard machine learning models assume independence of observations, which is violated in travel volume datasets that exhibit spatial (site-specific) and temporal (longitudinal) dependencies. 

Our model, **MERF-XGB**, addresses this by:
- Modeling the complex, high-dimensional, and non-linear relationships of fixed-effects features using **XGBoost**.
- Modeling the hierarchical grouping of observations (nested site-year clustering) through a **random intercepts** structure estimated via the **Expectation-Maximization (EM)** algorithm.

---

## Repository Structure

```text
├── README.md                           # Project documentation
├── requirements.txt                     # Required Python packages
├── generate_dummy_data.py               # Script to generate a realistic synthetic dataset
├── MDOT_Synthetic_Data.xlsx            # Generated synthetic dataset (for demonstration)
└── Pedestrian_Prediction_MERF_XGB.ipynb # Jupyter Notebook containing the full modeling pipeline
```

---

## Data Availability Statement

Due to licensing and privacy agreements with **Strava Metro**, the raw pedestrian activity counts and matched spatial dataset cannot be shared publicly. 

To ensure complete reproducibility and allow others to build upon our methods, we provide a synthetic data generator (`generate_dummy_data.py`) which generates a dataset (`MDOT_Synthetic_Data.xlsx`) matching the exact structure, feature ranges, and statistical properties of our original modeling dataset. The Jupyter Notebook is configured to automatically detect and load the synthetic dataset if the original data is unavailable.

---

## Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/Pedestrian-MERF-XGB.git
   cd Pedestrian-MERF-XGB
   ```

2. **Install Dependencies:**
   It is recommended to use a virtual environment (e.g., conda or venv) with Python 3.9+.
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate Synthetic Data (Optional):**
   If the synthetic Excel file is not present, you can generate it by running:
   ```bash
   python generate_dummy_data.py
   ```

---

## Running the Modeling Pipeline

Open the Jupyter Notebook:
```bash
jupyter notebook Pedestrian_Prediction_MERF_XGB.ipynb
```

The notebook contains sections that walk you through:
1. **Data Preprocessing & Clustering:** Establishing the nested $(i, t)$ site-year identifiers to capture spatial and longitudinal dependencies.
2. **Strategy Comparison:** Evaluating the four modeling strategies on the same footing:
   - *Local Models* (independent XGBoost models per cluster)
   - *Global Model* (standard XGBoost)
   - *Global Model + Cluster Features* (XGBoost with one-hot encoded cluster dummies)
   - *MERF-XGB* (our mixed-effects formulation)
3. **Hyperparameter Optimization:** Optimizing the model using `GroupKFold` cross-validation based on the nested clusters.
4. **Final Model Performance:** Training and evaluating the final optimized model.
5. **SHAP Interpretation:** Generating beeswarm plots and location-specific feature importances.

---

## Citation

If you use this code or methodology in your research, please cite our paper:

```text
Farahani, P. S, et al. (2026). "Improving Network Level Pedestrian Activity Prediction by Accounting for Spatial and Longitudinal Clustering in Crowdsourced Data". https://doi.org/10.21203/rs.3.rs-8715658/v1
```
