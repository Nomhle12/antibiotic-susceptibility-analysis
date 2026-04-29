import pandas as pd
import matplotlib.pyplot as plt
# Load the data
data = pd.read_csv("lab_antibiotic_data.csv")
print(data.head())

#clean data
data = data.dropna()
data =data.drop_duplicates()

print("\nAfter cleaning:")
print(data.head())

#Standerdise text
data["Bacteria"] = data["Bacteria"].str.lower()
data["Antibiotic"] = data["Antibiotic"].str.lower()

#Analysis 1: Best Antibiotic
result = data.groupby("Antibiotic")["Zone_mm"].mean()
print("\nAverage antibiotic effectiveness:")
print(result)

#Analysis 2: Most resistant bacteria
result2 = data.groupby("Bacteria")["Zone_mm"].mean()
print("\nBacterial resistance (average zones):")
print(result2)

#Graphical representation
result.plot(kind="bar")
plt.title("Average Antibiotic Effectiveness")
plt.ylabel("Zone of Inhibition (mm)")
plt.show()

