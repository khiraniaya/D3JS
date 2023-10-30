import pandas as pd

# Load the XLSX file
file_path = "base de données clean.xlsx"
df = pd.read_excel(file_path, header=[0, 1])

# Flatten the MultiIndex columns
df.columns = ['_'.join(col).strip() if col[1] else col[0] for col in df.columns]

# Save as CSV
output_csv = "base_de_donnees_clean.csv"
df.to_csv(output_csv)
