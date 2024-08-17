from flask import Flask, request, render_template_string
from werkzeug.utils import secure_filename
import io
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# This is a placeholder for Neeruj's script
def process_file(file_content):
    # Replace this with the actual processing logic
    logger.info(f"Processing file of size {len(file_content)} bytes")
    return f"Processed file content: {file_content[:100]}..."

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

if __name__ == '__main__':
    print("Server is starting...")
    logger.info("Server is running. Ready to handle requests.")
    app.run(port=8080,debug=True)