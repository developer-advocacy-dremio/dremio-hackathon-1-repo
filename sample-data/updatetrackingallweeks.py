import pandas as pd

# Load the Parquet file
input_file = "tracking_all_weeks.parquet"
output_file = "tracking_all_weeks_updated.parquet"

# Read the Parquet file into a DataFrame
df = pd.read_parquet(input_file)

# Ensure the time column is in the correct format (e.g., pandas datetime)
# Convert nanoseconds to milliseconds
df['time'] = pd.to_datetime(df['time']).dt.floor('ms')

# Save the updated DataFrame back to a new Parquet file
df.to_parquet(output_file, index=False)

print(f"Updated file saved as {output_file}")