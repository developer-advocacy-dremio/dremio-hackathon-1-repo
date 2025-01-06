import pandas as pd

# Load the Parquet file
input_file = "players.parquet"
output_file = "players_updated.parquet"

# Read the Parquet file into a DataFrame
df = pd.read_parquet(input_file)

# Ensure the birthDate column is in the correct format (e.g., pandas datetime)
# Convert nanoseconds to milliseconds
df['birthDate'] = pd.to_datetime(df['birthDate']).dt.floor('ms')

# Save the updated DataFrame back to a new Parquet file
df.to_parquet(output_file, index=False)

print(f"Updated file saved as {output_file}")