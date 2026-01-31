import pandas as pd 
import matplotlib.pyplot as plt

df= pd.read_csv(r"Path_to\cic_ids2017_combined_addBL.csv")


# Display the number of samples for each class
print(df['binary_label'].value_counts())

# Percentage distribution
print(df['binary_label'].value_counts(normalize=True) * 100)

# Visualization

df['binary_label'].value_counts().plot(kind='bar')
plt.title('Class Distribution')
plt.xlabel('Class')
plt.ylabel('Count')

# Display the plot
plt.show()
