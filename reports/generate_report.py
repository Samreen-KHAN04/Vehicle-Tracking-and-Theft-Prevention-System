import pandas as pd
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

csv_file = "data/vehicle_log.csv"
pdf_file = "outputs/vehicle_report.pdf"

# Read CSV
df = pd.read_csv(csv_file)

# Create PDF
from reportlab.lib.pagesizes import landscape, A4

pdf = SimpleDocTemplate(
    pdf_file,
    pagesize=landscape(A4)
)

styles = getSampleStyleSheet()

elements = []

title = Paragraph(
    "Vehicle Tracking & Theft Prevention Report",
    styles['Title']
)

elements.append(title)
elements.append(Spacer(1, 12))

# Convert dataframe to table
table_data = [list(df.columns)]

for row in df.values.tolist():
    table_data.append(row)

table = Table(
    table_data,
    colWidths=[90, 70, 70, 100, 100]
)

table.setStyle(
    TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),

        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),

        ('FONTSIZE', (0,0), (-1,-1), 7),   # smaller font
        ('LEADING', (0,0), (-1,-1), 8),

        ('GRID', (0,0), (-1,-1), 1, colors.black),

        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

        ('ALIGN', (1,1), (-1,-1), 'CENTER')
    ])
)

elements.append(table)

pdf.build(elements)

print("PDF Generated Successfully!")