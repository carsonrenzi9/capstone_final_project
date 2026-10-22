import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lifelines import CoxPHFitter
from statsmodels.api import add_constant
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Reading csv sheet into dataframe
df = pd.read_csv("Pitcher_Contracts_Updated.csv")

# Select model features and clean missing values
feature_cols = [
    "Platform_Velo",
    "Platform_Spin",
    "Platform_IP",
    "Platform_FIP",
    "Age",
    "Tommy_John",
    "Career_FIP-",
    "Career_K/BB",
]

model_data = df[
    ["Observed Length", "Failure"] + feature_cols
].dropna()

# Initialize and fit the Cox model
cph = CoxPHFitter()
cph.fit(
    model_data,
    duration_col="Observed Length",
    event_col="Failure",
)

# Print hazard ratios, p-values, and summary metrics
cph.print_summary()

# Test for Multicollinearity via VIF (Variance Inflation Factors)
X = add_constant(model_data[feature_cols])

vif_data = pd.DataFrame(
    {
        "Variable": feature_cols,
        "VIF": [
            variance_inflation_factor(X.values, i)
            for i in range(1, X.shape[1])
        ]
    }
)

print("\n--- Variance Inflation Factors (VIF) ---")
print(vif_data)

# Test Proportionality (Schoenfeld Residuals) & Plot
print("\n--- Checking Proportional Hazards Assumption ---")
cph.check_assumptions(model_data, p_value_threshold=0.05, show_plots=True)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt


fig, ax = plt.subplots(figsize=(8, 5))
cph.baseline_survival_.plot(ax=ax, color="#1f77b4", linewidth=2.5)

ax.set_title(
    "Baseline Survival Function: MLB Pitcher Contract Risk",
    fontsize=12,
    fontweight="bold",
)
ax.set_xlabel("Time (Seasons / Years)", fontsize=10)
ax.set_ylabel("Survival Probability (Contract Health)", fontsize=10)
ax.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
from lifelines import KaplanMeierFitter

# Updated with the exact space in your column name:
TIME_COL = "Observed Length"  # Matches your CSV column name
EVENT_COL = "Failure"  # Change to your actual binary event/failure column name

# 1. Get the partial hazard predictions for the dataset used in the model
predictions = cph.predict_partial_hazard(df)

# 2. Drop rows with NaNs in time/event columns so we have a clean evaluation set
eval_df = df.dropna(subset=[TIME_COL, EVENT_COL]).copy()
eval_preds = predictions.loc[eval_df.index]

# 3. Split into High and Low risk based on the median risk score
median_risk = eval_preds.median()
eval_df["Risk_Group"] = [
    "High Risk" if p > median_risk else "Low Risk" for p in eval_preds
]

# 4. Separate into high and low dataframes
high_df = eval_df[eval_df["Risk_Group"] == "High Risk"]
low_df = eval_df[eval_df["Risk_Group"] == "Low Risk"]

# 5. Fit Kaplan-Meier curves for the two groups
kmf_high = KaplanMeierFitter()
kmf_low = KaplanMeierFitter()

fig, ax = plt.subplots(figsize=(8, 5))

kmf_high.fit(high_df[TIME_COL], high_df[EVENT_COL], label="High Predicted Risk")
kmf_high.plot_survival_function(ax=ax, color="#d62728", linewidth=2)

kmf_low.fit(low_df[TIME_COL], low_df[EVENT_COL], label="Low Predicted Risk")
kmf_low.plot_survival_function(ax=ax, color="#2ca02c", linewidth=2)

ax.set_title(
    "Model Discrimination: High vs. Low Risk Pitcher Contracts (C-index = 0.80)",
    fontsize=12,
    fontweight="bold",
)
ax.set_xlabel("Time (Seasons / Years)", fontsize=10)
ax.set_ylabel(
    "Contract Survival Probability (Proportion Healthy)", fontsize=10
)
ax.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()