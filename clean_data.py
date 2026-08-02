import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

print("========== ORIGINAL DATA ==========")
print(df)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Convert Age and Salary to numeric
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["City"] = df["City"].fillna("Unknown")
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Remove rows with invalid dates
df = df.dropna(subset=["Date"])

# Convert Age and Salary to integers
df["Age"] = df["Age"].astype(int)
df["Salary"] = df["Salary"].astype(int)

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\n========== CLEANED DATA ==========")
print(df)

print("\n✅ Project Completed Successfully!")