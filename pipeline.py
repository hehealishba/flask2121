import sys
from components.pdf_input import PdfInput
from components.document_classification import DocumentClassification
from components.entity_extraction import EntityExtraction
from components.data_processing import DataProcessing
from components.business_categorization import BusinessCategorization
from components.risk_review import RiskReview
from components.quote_prioritization import QuotePrioritization
from components.pricing_module import PricingModel
from components.gap_module import GapAnalysis
import config  # Import the config module
import pytesseract

# Use the API key from config
api_key = config.ANTHROPIC_API_KEY

# Example function using pytesseract
def example_function(image_path_or_data):
    text = pytesseract.image_to_string(image_path_or_data)
    return text

def main(pdf_file_path=None):
    try:
        # Step 1: PDF Input
        pdf_input = PdfInput(file_path=pdf_file_path)
        pdf_data = pdf_input.execute()

        # Step 2: Document Classification
        form_type, sub_form_type = DocumentClassification(pdf_data).execute()

        # Step 3: Entity Extraction
        entities = EntityExtraction(form_type, sub_form_type, pdf_data).execute()

        # Step 4: Data Processing
        processed_data = DataProcessing(entities).execute()

        # Step 5: Business Categorization
        business_code = BusinessCategorization(processed_data).execute()

        # Step 6: Risk Review & Underwriter Authority Suggestion
        risk_review = RiskReview(processed_data, business_code).execute()

        # Step 7: Quote Prioritization
        quote_priority = QuotePrioritization(risk_review).execute()

        # Step 8: Coverage & Pricing Model Execution
        pricing_output = PricingModel(processed_data).execute()

        # Step 9: Gap Analysis & Discount Suggestion
        final_output = GapAnalysis(pricing_output, quote_priority).execute()

        print("Pipeline execution completed. Final output:", final_output)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
