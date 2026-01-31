import pandas as pd 

# Read the CSV file into a pandas DataFrame

df = pd.read_csv(r"Path_to\cic_ids2017_combined.csv")

# Print information about the DataFrame
print(df.info)

# Print the column names of the DataFrame
print(df.columns)

# Define a function to generate a binary label based on the input Label
def generate_label(Label) : 
   if Label == 'BENIGN':
        return 0 
   else :
       return 1 

# Apply the generate_label function to the ' Label' column 
df['binary_label'] = df[' Label'].apply(generate_label)

# Save the updated DataFrame to a new CSV file
df.to_csv(r"Path_to\cic_ids2017_combined_addBL.csv")

# Print the shape of the DataFrame for verification
print(df.shape)
