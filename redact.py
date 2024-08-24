import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def redact_pdf(input_pdf, output_pdf, redactions):
    reader = PyPDF2.PdfReader(input_pdf)
    writer = PyPDF2.PdfWriter()

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]

        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)

        # Apply redactions
        for redaction in redactions:
            if redaction['page'] == page_num:
                x, y, width, height = redaction['coordinates']
                can.setFillColorRGB(0, 0, 0)
                can.rect(x, y, width, height, fill=1)

        can.save()

        # Merge redaction with original page
        packet.seek(0)
        redaction_page = PyPDF2.PdfReader(packet).pages[0]
        page.merge_page(redaction_page)
        writer.add_page(page)

    with open(output_pdf, "wb") as output:
        writer.write(output)

# Example of redaction coordinates on a specific page (you will need to determine these manually)
redactions = [
    {"page": 0, "coordinates": (100, 100, 200, 50)},  # x, y, width, height
]

if __name__ == "__main__":
    redact_pdf("pdfs/sample1.pdf", "pdfs/sample1_redacted.pdf", redactions)
