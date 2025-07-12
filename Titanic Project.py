import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")
print(df.head())
print(df.shape)

print(df.columns)
print(df.dtypes)
print(df['age'].isnull().sum())

print(f"Mean of age is: {np.mean(df['age'])}.")
print(f"Standard Deviation of age is: {np.std(df['age'])}.")
print(f"The correlation between age and fare is: {np.corrcoef(df['age'], df['fare'])[0, 1]}.")

plt.hist(df["age"], bins=20, edgecolor='black')
plt.title("Distribution of Passenger Ages")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

grouped = df.groupby("pclass")["fare"].mean()
grouped.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Average Fare By Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Average Fare")
plt.grid(axis="y")
plt.show()

features = df[["age", "fare", "pclass", "survived"]]
correlation = features.corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

cleaned_df = df.dropna(subset=["age"])
print(cleaned_df.shape)

subset_df = df[(df["sex"] == "female") & (df["survived"] == 1) & (df["pclass"] == 1)]
print(subset_df.shape)

fares = df["fare"].values
std = np.std(fares)
mean = np.mean(fares)
z_scores = (fares - mean) / std

outliers = df[np.abs(z_scores) > 3]
print(len(outliers))

grouped = df.groupby("sex")["age"].mean().sort_values(ascending=False)
print(grouped)
