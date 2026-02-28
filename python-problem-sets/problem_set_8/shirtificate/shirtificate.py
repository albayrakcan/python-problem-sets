from fpdf import FPDF
from fpdf.enums import Align

name = input("name: ").title()

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=48)
pdf.cell(w=12, h=57, text="CS50 Shirtificate", align="C", center=True)
dim = 190
pdf.image(
    name="shirtificate.png", x=Align.C, y=70, w=dim, h=dim, keep_aspect_ratio=True
)
pdf.set_font("helvetica", size=28)
pdf.set_text_color(255, 255, 255)
pdf.cell(w=12, h=250, text=f"{name} took CS50", align="C", center=True)
pdf.output("shirtificate.pdf")
