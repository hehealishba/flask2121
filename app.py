from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
import pdfplumber
import io
import logging
import os
from redact import redact_pdf 

app = Flask(__name__, template_folder='templates')  

# Enable template auto-reloading
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_file(file_content):
    try:
        with pdfplumber.open(io.BytesIO(file_content)) as pdf:
            extracted_text = []
            for page in pdf.pages:
                text = page.extract_text(layout=True)
                if text:
                    extracted_text.append(text)
            full_text = "\n\n".join(extracted_text)
        return f"Extracted PDF content:\n{full_text}"
    except Exception as e:
        logger.error(f"Error processing file: {e}")
        return 'Error processing file', 500

@app.route('/')
def index():
    logger.info("Rendering test.html")  # Log rendering attempt
    try:
        return render_template('test.html')
    except Exception as e:
        logger.error(f"Error rendering template: {e}")
        return f"Error rendering template: {e}", 500  # Return error message to the user

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory('pdfs', filename)

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

        # Call Neeraj's model
        # Import pipeline_test.py
        # Call function with input = file_content
        # store result 

        result = call_neerajs_model(file_content)
        # result = process_file(file_content)

        logger.info("File processed successfully")
        return result

@app.route('/redact/<filename>', methods=['GET'])
def redact(filename):
    try:
        redactions = [
            {"page": 0, "coordinates": (100, 100, 200, 50)},  # Example coordinates for redaction
        ]
        input_pdf = os.path.join('pdfs', f"{filename}.pdf")
        output_pdf = os.path.join('pdfs', f"{filename}_redacted.pdf")
        
        redact_pdf(input_pdf, output_pdf, redactions)
        
        return f"Redaction completed for {filename}.pdf. Download the redacted file <a href='/download/{filename}_redacted.pdf'>here</a>."
    except Exception as e:
        logger.error(f"Error during redaction: {e}")
        return 'Error during redaction', 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3100))
    app.run(host="0.0.0.0", port=port, debug=True)
