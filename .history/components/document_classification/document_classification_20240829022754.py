from io import BytesIO
import anthropic
import json
import re
from components.pdf_input import PdfInput



import os
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import pytesseract
from io import BytesIO


# class PdfInput:
#     def __init__(self, file_path=None):
#         self.file_path = file_path

#     def execute(self):
#         if self.file_path and os.path.exists(self.file_path):
#             return self._read_local_pdf(self.file_path)
#         else:
#             return self._read_uploaded_pdf()

#     def _read_local_pdf(self, file_path):
#         with open(file_path, 'rb') as f:
#             pdf_data = f.read()
#         print(f"Read PDF from local file: {file_path}")
#         return pdf_data

#     def _read_uploaded_pdf(self):
#         raise NotImplementedError("File upload handling should be implemented here.")

#     def extract_text_from_pdf(self, pdf_file):
#         reader = PdfReader(pdf_file)
#         text = ""
#         for page in reader.pages:
#             page_text = page.extract_text()
#             if page_text:
#                 text += page_text
#         if not text:
#             # Fallback to OCR if no text was extracted
#             print("No text extracted using PyPDF2, attempting OCR...")
#             text = self.extract_text_from_image_pdf(pdf_file)
#         return text

#     def extract_text_from_image_pdf(self, pdf_file_path):
#         images = convert_from_path(pdf_file_path)
#         text = ""
#         for image in images:
#             text += pytesseract.image_to_string(image)
#         return text



class DocumentClassification:
    def __init__(self, pdf_data):
        self.pdf_data = pdf_data

    def execute(self):
        pdf_file = BytesIO(self.pdf_data)
        pdf_input = PdfInput()

        # Use the extract_text_from_pdf method from PdfInput
        text = pdf_input.extract_text_from_pdf(pdf_file)
        #print("Extracted Text:", text)

        classification_data = self.process_pdf_with_claude(text)

        if classification_data:
            form_type = classification_data.get("classification_type", "other")
            broker_name = classification_data.get("entities", {}).get("Broker Name", "Policyworks")
            sub_form_type = broker_name if broker_name else "Policyworks"

            return form_type, sub_form_type
        else:
            return "other", "Policyworks"
        
    def call_claude_api(self, text, prompt, api_key):
        client = anthropic.Client(api_key=api_key)

        full_prompt = f"\n\nHuman: You are an expert document analyst.\n\nHuman: {prompt}\n\nHuman: {text}\n\nAssistant:"

        response = client.completions.create(
            model="claude-2.1",
            max_tokens_to_sample=1000,
            prompt=full_prompt
        )

        if response and hasattr(response, 'completion'):
            return response.completion
        else:
            print("No completion received from Claude API.")
            return None

    def process_pdf_with_claude(self, text):
        prompt_classification = """
        You are tasked with analyzing the attached text extracted from a document. Your goal is to determine whether the document is directly related to a commercial insurance quote, submission, or application form, or if it is another type of insurance-related document.

        Please classify the document into one of the following categories:
        1. 'quote_attachment': if the document appears to be a commercial insurance quote, submission, or application form, containing details such as brokers, insurers, business details, effective dates, coverages, limits, and deductibles requested.
        2. 'insurance_supporting_document': if the document is related to insurance but does not constitute a quote, submission, or application form. Examples include loss runs, experience records, letters of insurance, or other supporting documents.
        3. 'other': if the document is unrelated to insurance.

        Additionally, provide a detailed reasoning for your classification, explaining why the document was categorized as 'quote_attachment', 'insurance_supporting_document', or 'other'.

        Your response should be structured as a JSON object with the following format:
        {
            "classification_type": "quote_attachment" or "insurance_supporting_document" or "other",
            "classification_reasoning": "detailed explanation for the classification",
            "entities": {
                "Broker Name": "Extracted broker name if available"
            }
        }
        """

        response_content = self.call_claude_api(text, prompt_classification, CONFIG_API_KEY)

        if response_content:
            try:
                json_match = re.search(r'\{.*\}', response_content, re.DOTALL)
                if json_match:
                    json_content = json_match.group(0)
                    return json.loads(json_content)
                else:
                    print("No JSON content found in response.")
                    print("Response content:", response_content)
                    return None
            except json.JSONDecodeError:
                print("Failed to parse JSON content.")
                print("Response content:", response_content)
                return None
        else:
            print("No response received from Claude API.")
            return None
