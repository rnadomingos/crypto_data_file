import pandas as pd
from hashlib import sha256

file_csv = "data/input/cliente_bmw.csv"

df = pd.read_csv(file_csv, sep=';')

df['Zip'] = df['Zip'].astype(str).str.zfill(5)

exclude_columns = ['Zip', 'Country']
# Iterate through each row and column
for index, row in df.iterrows():
    for column in df.columns:
        # Check if the column is in the exclusion list
        if column not in exclude_columns:
            # Get the value from the current cell
            value = str(row[column])

            # Hash the value using SHA-256
            hashed_value = sha256(value.encode(encoding='utf-8')).hexdigest()

            # Update the DataFrame with the hashed value
            df[column] = df[column].astype(str) 
            df.at[index, column] = hashed_value


# Path to save the hashed CSV file
hashed_file_path = "data/output/cliente_bmw_hashed.csv"

# Save the modified DataFrame to a new CSV file
df.to_csv(hashed_file_path, index=False)