import pandas as pd
import numpy as np


# Load DATASET
df = pd.read_csv(r"C:\Users\youss\OneDrive\Documents\Bureau\Python_Worksplace\AI-Enhanced IDS Classifier\Data\cic_ids2017_combined_addBL.csv")


# DATA inspection

print(f"Number of duplicate rows: {df.duplicated().sum()}")

empty_columns = df.columns[df.isna().all()].tolist()
print("Completely empty columns:", empty_columns)

nan_columns = df.columns[df.isna().any()].tolist()
print("Columns with NaN:", nan_columns)


# Drop NaN 

df = df.dropna(subset=['Flow Bytes/s'])

print("NaN in Flow Bytes/s:", df['Flow Bytes/s'].isna().sum())
print("Empty strings in Flow Bytes/s:", (df['Flow Bytes/s'] == '').sum())


# Remove label column 

df = df.drop(' Label', axis=1)

df.to_csv(
    r"C:\Users\youss\OneDrive\Documents\Bureau\Python_Worksplace\AI-Enhanced IDS Classifier\Data\cic_ids2017_withoutLabel.csv",
    index=False
)


# Check for empty and  inf values

print("Any NaN left:", df.isna().any().any())
print("NaN count per column:\n", df.isna().sum())

print("Empty strings count:", (df == "").sum().sum())
print("Whitespace strings count:", (df == " ").sum().sum())

print("Total inf values:", np.isinf(df).sum().sum())
print("Columns with inf values:\n", np.isinf(df).sum()[np.isinf(df).sum() > 0])


# Reload data without label for final cleaning 

df2 = pd.read_csv(
    r"C:\Users\youss\OneDrive\Documents\Bureau\Python_Worksplace\AI-Enhanced IDS Classifier\Data\cic_ids2017_withoutLabel.csv"
)

# Replace empty strings with NaN
df2 = df2.replace(r'^\s*$', np.nan, regex=True)

print("NaN columns BEFORE cleaning:",
      df2.columns[df2.isna().any()].tolist())

print("Inf columns BEFORE cleaning:",
      df2.columns[np.isinf(df2).any()].tolist())

# Convert inf → NaN and drop all NaN rows
df2.replace([np.inf, -np.inf], np.nan, inplace=True)
df2.dropna(inplace=True)

print("NaN columns AFTER cleaning:",
      df2.columns[df2.isna().any()].tolist())

print("Inf columns AFTER cleaning:",
      df2.columns[np.isinf(df2).any()].tolist())


# Remove generated index columns

df2.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'], inplace=True)

df2.to_csv(
    r"C:\Users\youss\OneDrive\Documents\Bureau\Python_Worksplace\AI-Enhanced IDS Classifier\Data\cic_ids2017_theclean_version.csv",
    index=False
)


# final cleanup

df3 = pd.read_csv(
    r"C:\Users\youss\OneDrive\Documents\Bureau\Python_Worksplace\AI-Enhanced IDS Classifier\Data\cic_ids2017_theclean_version.csv"
)

print(df3.columns)
print(df3.shape)

df3.drop(columns=[' Fwd Header Length.1'], inplace=True)

df3.to_csv(r"C:\Users\youss\OneDrive\Documents\Bureau\Python_Worksplace\AI-Enhanced IDS Classifier\Data\cic_ids2017_clean_version.csv",
    index=False)

print("Final columns:", df3.columns)
