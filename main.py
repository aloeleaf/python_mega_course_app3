from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    # Set header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)

    # s Set content of page
    for i in range(20, 277, 10):
        pdf.line(x1=10, y1=i, x2=200, y2=i)

    # Set footer
    pdf.ln(269)
    pdf.set_text_color(180, 180, 180)
    pdf.set_font(family="Times", style="I", size=24)
    pdf.line(x1=10, y1=281, x2=200, y2=281)
    pdf.cell(w=0, txt=row["Topic"], align="R")

    for page in range(row["Pages"] - 1):
        pdf.add_page()

        # s Set content of page
        for i in range(10, 277, 10):
            pdf.line(x1=10, y1=i, x2=200, y2=i)
        # Set footer
        pdf.ln(281)
        pdf.line(x1=10, y1=281, x2=200, y2=281)
        pdf.set_font(family="Times", style="I", size=24)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, txt=row["Topic"], align="R")

pdf.output("output.pdf")