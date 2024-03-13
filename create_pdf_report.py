from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_pdf_report():
    # Output PDF filename
    pdf_filename = "DS_INT_YOURNAME.pdf"

    # Create a PDF document
    pdf = canvas.Canvas(pdf_filename, pagesize=letter)

    # Add content to the PDF
    pdf.drawString(100, 800, "Data Science Internship Project Report")
    pdf.drawString(100, 780, "Abstract:")
    pdf.drawString(100, 760, "Objective:")
    pdf.drawString(100, 740, "Introduction:")
    pdf.drawString(100, 720, "Methodology:")
    pdf.drawString(100, 700, "Code:")
    pdf.drawString(100, 680, "Conclusion:")

    # Save the PDF document
    pdf.save()

if __name__ == "__main__":
    create_pdf_report()
