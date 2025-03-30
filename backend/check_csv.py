import pandas as pd
import os

# Get absolute path to CSV file
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, 'dataset', 'operadoras_ativas.csv')

# Load the CSV file
df = pd.read_csv(csv_path, sep=';', encoding='latin1')

# Print column names and data types
print("Column names:")
print(df.columns.tolist())
print("\nColumn data types:")
print(df.dtypes)

# Print first few rows
print("\nFirst 2 rows:")
print(df.head(2))