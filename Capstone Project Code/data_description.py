import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


df = pd.read_csv("Pitcher_Contracts_Updated.csv")

binary_cols = df[["Failure", "Tommy_John"]].dropna(axis=1, how="all")

for col in binary_cols.columns:
    print(f"The counts for {col} are: {binary_cols[col].value_counts().to_dict()}")
    print(f"The proportions for {col} are: {binary_cols[col].value_counts(normalize=True).to_dict()}")
    print(f"The mode is: {round(binary_cols[col].mode().iloc[0], 2)}")
    print(f"\n\n\nPlots showing the distribution of {col} are shown below:")
    if col == "Failure":
        counts = binary_cols[col].value_counts()
        counts.index = counts.index.map({0: "Success", 1: "Failure"})
        plt.figure(figsize=(6, 4))
        counts.plot(kind="bar", color=["skyblue", "salmon"])
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.show()

        plt.figure(figsize=(6, 4))
        counts.plot(kind="pie", autopct="%1.1f%%", colors=["skyblue", "salmon"], startangle=90)
        plt.title(f"Distribution of {col}")
        plt.ylabel("")
        plt.tight_layout()
        plt.show()

    elif col == "Tommy_John":
        counts = binary_cols[col].value_counts()
        counts.index = counts.index.map({0: "No Previous Tommy John Surgery", 1: "Previous Tommy John Surgery"})
        plt.figure(figsize=(6, 4))
        counts.plot(kind="bar", color=["lightgreen", "orange"])
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.show()

        plt.figure(figsize=(6, 4))
        counts.plot(kind="pie", autopct="%1.1f%%", colors=["lightgreen", "orange"], startangle=90)
        plt.title(f"Distribution of {col}")
        plt.ylabel("")
        plt.tight_layout()
        plt.show()

cont_cols = df[["Observed Length", "Platform_Velo", "Platform_Spin", "Platform_IP", "Platform_FIP", "Age", "Career_FIP-", "Career_K/BB"]].dropna(axis=1, how="all")

for col in cont_cols.columns:
    print(f"The measures of central tendency for {col} are:")
    print(f"Mean: {round(cont_cols[col].mean(), 2)}")
    print(f"Median: {round(cont_cols[col].median(), 2)}")
    print(f"Mode: {round(cont_cols[col].mode().iloc[0], 2)}")
    print(f"The measures of dispersion for {col} are:")
    print(f"Range: {round(cont_cols[col].max() - cont_cols[col].min(), 2)}")
    print(f"Min: {round(cont_cols[col].min(), 2)} and Max: {round(cont_cols[col].max(), 2)}")
    print(f"Standard Deviation: {round(cont_cols[col].std(), 2)}")
    print(f"\n\n\nPlots showing the distribution of {col} are given below:\n\n")
    plt.figure(figsize=(6, 4))
    cont_cols[col].plot(kind="hist", bins=30, color="lightblue", edgecolor="black")
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(6, 4))
    plt.boxplot(
        cont_cols[col].dropna(),
        vert=False,
        patch_artist=True,
        boxprops={"facecolor": "lightblue"},
    )
    plt.title(f"Boxplot of {col}")
    plt.xlabel(col)
    plt.tight_layout()
    plt.show()

