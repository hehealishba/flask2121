from io import BytesIO
from components.pdf_input import PdfInput
from components.entity_extraction.llm_extraction.llm_extraction import process_with_prompts

class EntityExtraction:
    def __init__(self, form_type, sub_form_type, pdf_data):
        self.form_type = form_type
        self.sub_form_type = sub_form_type
        self.pdf_data = pdf_data

    def execute(self):
        if self.form_type == "quote_attachment":
            pdf_file = BytesIO(self.pdf_data)
            pdf_input = PdfInput()

            # Extract text once using PdfInput
            extracted_text = pdf_input.extract_text_from_pdf(pdf_file)

            classification_data = {
                "classification_type": self.form_type,
                "classification_reasoning": self.sub_form_type  # Using sub_form_type for reasoning
            }

            combined_results = process_with_prompts(extracted_text, classification_data)
            return combined_results
        else:
            return {
                "entities": {}
            }
