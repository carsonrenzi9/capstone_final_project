# capstone_final_project
Final Project for Statistics Capstone (STA 4945). 

# Evaluating Downside Volatility and Pricing Risk in Major League Baseball Starting Pitcher Contracts

## 📌 Project Overview
This project evaluates the financial and performance risks associated with multi-year free-agent contracts for Major League Baseball (MLB) starting pitchers. Using a **Cox Proportional Hazards Model**, this research identifies key pre-signing risk factors—such as pitcher age, workload, and performance metrics—that predict contract failure.

### Key Objectives
1. **Survival Modeling:** Quantify the instantaneous hazard (risk) of a pitcher contract failing over time.
2. **Risk Factor Identification:** Measure the effect of covariates like Age, Platform FIP, Fastball Velocity, and Tommy John surgery history on contract longevity.
3. **Model Discrimination:** Evaluate predictive power using the Concordance Index (C-index) and Kaplan-Meier risk separation curves.

---

## 📊 Dataset & Variables
The dataset consists of multi-year MLB starting pitcher free-agent contracts. 

* **Primary Response Variables:**
  * `Observed Length` (Quantitative): Contract duration or duration observed to date (in years).
  * `Failure` (Binary): `1` if the contract failed (met breakdown criteria like <50% expected starts or WAR threshold); `0` if censored/successful.

* **Explanatory Covariates:**
  * **Performance & Workload:** Platform Fastball Velocity (`Velo`), Platform Spin Rate (`Spin`), Platform Innings Pitched (`IP`), Platform FIP (`FIP`), Career FIP- (`FIP-`), Career Strikeout-to-Walk Ratio (`K/BB`).
  * **Demographics & Injury:** Age at contract start (`Age`), UCL Reconstruction History (`Tommy John`).

---

## 🛠️ Methodology & Diagnostics

1. **Cox Proportional Hazards Model:**
   $$h(t \mid X) = h_0(t) \exp(\boldsymbol{\beta X})$$
   * Model coefficients are exponentiated ($\exp(\beta)$) to yield **Hazard Ratios**.

2. **Diagnostics & Validation:**
   * **Multicollinearity:** Evaluated via Variance Inflation Factors (VIF < 3.1).
   * **Proportional Hazards Assumption:** Verified using **Schoenfeld residuals**.
   * **Predictive Discrimination:** Achieved a **Concordance Index (C-index) of 0.80**, indicating strong ability to rank risk between player pairs.

---

## 📁 Repository Structure
