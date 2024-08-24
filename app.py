from flask import Flask, request, render_template_string, send_from_directory
from werkzeug.utils import secure_filename
import pdfplumber
import io
import logging
import os
from redact import redact_pdf  # Import the redact_pdf function from redact.py

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to process the PDF file using pdfplumber
def process_file(file_content):
    with pdfplumber.open(io.BytesIO(file_content)) as pdf:
        extracted_text = []
        for page in pdf.pages:
            # Extract text with layout preservation
            text = page.extract_text(layout=True)
            if text:
                extracted_text.append(text)
        full_text = "\n\n".join(extracted_text)
    return f"Extracted PDF content:\n{full_text}"

@app.route('/', methods=['GET'])
def index():
    with open('templates/test.html', 'r') as f:
        return render_template_string(f.read())

# Route for downloading PDFs
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    # Serve the file from the 'pdfs' directory
    return send_from_directory('pdfs', filename)

# Route for uploading a file and processing it
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        logger.warning("No file part in the request")
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        logger.warning("No selected file")
        return 'No selected file', 400
    if file:
        filename = secure_filename(file.filename)
        logger.info(f"Received file: {filename}")
        file_content = file.read()
        # Process the file content
        result = process_file(file_content)
        logger.info("File processed successfully")
        return result

# Route to handle redaction of PDFs
@app.route('/redact/<filename>', methods=['GET'])
def redact(filename):
    # Example redactions, adjust coordinates and page numbers as needed
    redactions = [
        {"page": 0, "coordinates": (100, 100, 200, 50)},  # Example coordinates for redaction
    ]
    input_pdf = os.path.join('pdfs', f"{filename}.pdf")
    output_pdf = os.path.join('pdfs', f"{filename}_redacted.pdf")
    
    # Perform the redaction
    redact_pdf(input_pdf, output_pdf, redactions)
    
    return f"Redaction completed for {filename}.pdf. Download the redacted file <a href='/download/{filename}_redacted.pdf'>here</a>."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
