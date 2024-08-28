from PyPDF2 import PdfReader
import os
import pytesseract
from pdf2image import convert_from_path


class PdfInput:
    def __init__(self, file_path=None):
        """
        Initializes the PdfInput component.
        
        :param file_path: Path to the local PDF file for testing purposes. If None, 
                          the file will be expected to be uploaded via the website.
        """
        self.file_path = file_path

    def execute(self):
        """
        Executes the PDF input process. If a file_path is provided, it reads from the local file system.
        Otherwise, it hooks into the file upload mechanism provided by the website (assumed to be 
        orchestrated by another service).
        
        :return: The raw PDF data.
        """
        if self.file_path and os.path.exists(self.file_path):
           # print(f"File path provided: {self.file_path}")
            return self._read_local_pdf(self.file_path)
        else:
           # print("No valid file path provided, expecting file upload.")
            return self._read_uploaded_pdf()


    def _read_local_pdf(self, file_path):
        """
        Reads a PDF file from the local file system.

        :param file_path: The path to the local PDF file.
        :return: The raw PDF data.
        """
        with open(file_path, 'rb') as f:
            pdf_data = f.read()
        #print(f"Read PDF from local file: {file_path}")
        return pdf_data

    def _read_uploaded_pdf(self):
        """
        Placeholder for reading a PDF file that has been uploaded through a website.
        This method would be integrated with the website's file handling system.

        :return: The raw PDF data.
        """
        # Placeholder code for the website's file upload mechanism
        # This will need to be integrated with the TS orchestration system
        raise NotImplementedError("File upload handling should be implemented here.")

    def extract_text_from_pdf(self, pdf_file):
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        
        # If text extraction is minimal, try OCR
        if len(text.strip()) < 50:  # Arbitrary threshold to decide if OCR is needed
            print("Text extraction is minimal, attempting OCR...")
            text += self.extract_text_from_image_pdf(self.file_path)
        
        return text


    def extract_text_from_image_pdf(pdf_file):
        images = convert_from_path(pdf_file)
        text = ""
        for image in images:
            text += pytesseract.image_to_string(image)
        return text
