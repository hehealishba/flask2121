from flask import Flask, request, render_template_string
from werkzeug.utils import secure_filename
import pdfplumber
import io
import logging

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

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

