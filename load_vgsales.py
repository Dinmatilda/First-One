
import pandas as pd

# Load the CSV file
file_path = '/mnt/data/vgsales (1).csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print(data.head())

# Basic information about the dataframe
print("\nDataFrame Information:\n")
print(data.info())

# Summary statistics
print("\nSummary Statistics:\n")
print(data.describe())
