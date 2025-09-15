import pandas as pd
from fpdf import FPDF

INPUT_CSV = 'data/input.csv'
OUTPUT_EXCEL = 'data/output/cleaned_data.xlsx'
OUTPUT_PDF = 'data/output/report.pdf'

try:
    df = pd.read_csv(INPUT_CSV)
    print(f"Successfully loaded {len(df)} rows from {INPUT_CSV}.")
except FileNotFoundError:
    print(f"Error: The file {INPUT_CSV} was not found.")
    exit()

initial_rows = len(df)
df.drop_duplicates(inplace=True)
df.dropna(how='any', inplace=True)
final_rows = len(df)
removed_rows = initial_rows - final_rows

df.to_excel(OUTPUT_EXCEL, index=False)
print(f"Successfully exported {final_rows} cleaned rows to {OUTPUT_EXCEL}.")

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Data Cleaning Report", ln=True, align='C')
pdf.cell(200, 10, txt=f"Initial number of rows: {initial_rows}", ln=True)
pdf.cell(200, 10, txt=f"Rows removed: {removed_rows}", ln=True)
pdf.cell(200, 10, txt=f"Final number of rows: {final_rows}", ln=True)
pdf.output(OUTPUT_PDF)
print(f"Report saved to {OUTPUT_PDF}.")
