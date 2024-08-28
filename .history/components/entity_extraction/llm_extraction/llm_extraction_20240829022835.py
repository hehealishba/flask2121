import anthropic
import re
import json
from PyPDF2 import PdfReader


CONFIG_API_KEY = os.getenv("ANTHROPIC_API_KEY")


def call_claude_api(text, prompt, api_key):
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

def process_with_prompts(extracted_text, classification_data):
    classification_type = classification_data.get("classification_type", "other")
    classification_reasoning = classification_data.get("classification_reasoning", "N/A")

    combined_results = {
        "classification_type": classification_type,
        "classification_reasoning": classification_reasoning,
        "entities": {
            "Policy Information": {},
            "Claim Information": {},
            "Coverage Information": {}
        }
    }

    if classification_type == "quote_attachment":
        # Define more precise prompts for detailed extraction
        prompt_policy_info = """
        Based on the provided insurance document, please extract the following policy information and return it in the following JSON format:
        {
            "Broker Name": "",
            "Broker Address": "",
            "Insured Name": "",
            "Insured Mailing Address": "",
            "Insured Postal Code":"",
            "Operations IBC Code": "",
            "Operations IBC Description": "",
            "Description of Operations": "",
            "Gross Revenue": "",
            "Gross Revenue - CA%": "",
            "Gross Revenue - US%": "",
            "Gross Revenue - Foreign%": "",
            "Current Insurance Carrier": "",
            "Expiry Date of Current Policy": "",
            "Effective Date of Quote": "",
            "Years of Experience of Contractor": "",
            "Year Business was Established": "",
            "Year Built":"",
            "Building Construction":"",
            "Building Square Footage":""
        }
        """
        prompt_claim_info = """
        Please extract the following claim information from the insurance application and return it in the following JSON format:
        {
            "Claim 1 - Type of loss": "",
            "Claim 1 - Date of loss": "",
            "Claim 1 - Paid amount": "",
            "Claim 1 - Reserves amount": "",
            "Claim 1 - Status": "",
            "Claim 2 - Type of loss": "",
            "Claim 2 - Date of loss": "",
            "Claim 2 - Paid amount": "",
            "Claim 2 - Reserves amount": "",
            "Claim 2 - Status": "",
            "Claim 3 - Type of loss": "",
            "Claim 3 - Date of loss": "",
            "Claim 3 - Paid amount": "",
            "Claim 3 - Reserves amount": "",
            "Claim 3 - Status": ""
        }
        """
        prompt_coverage_info = """
        Please extract the following coverage information from the insurance application. Notes:
        1. Business Interruption is same as Actual Loss Sustained
        2. if you see Property of Every Description,  populate it in Property Equipment Coverage, and leave Property Stock Coverage "" 
        3. Non-Owned Automobile liability is SPF6        
        
        Return it in the following JSON format:
        {   "Property Building Coverage Present? (Y/N)":"",
            "Property Building Coverage Limit": "",
            "Property Building Coverage Deductible": "",
            "Flood Coverage Present? (Y/N)":"",
            "Flood Coverage Limit": "",
            "Flood Coverage Deductible": "",
            "Crime Coverage Limit": "",
            "Crime Coverage Deductible": "",
            "Non-Owned Auto Liability Limit": "",
            "Non-Owned Auto Liability Deductible": "",
            "Tenants Legal Liability Coverage Limit": "",
            "Tenants Legal Liability Coverage Deductible": "",
            "Cyber Liability Coverage Limit": "",
            "Cyber Liability Coverage Deductible": "",
            "Earthquake Coverage Present? (Y/N)":"",
            "Earthquake Coverage Deductible %": "",
            "Earthquake Coverage Min. Deductible %": "",
            "Business Interruption Coverage Limit": "Y",
            "Business Interruption Coverage Deductible": "",
            "Property Equipment Coverage Present? (Y/N)":"",
            "Property Equipment Coverage Limit": "",
            "Property Equipment Coverage Deductible": "",
            "Property Stock Coverage Limit": "",
            "Property Stock Coverage Deductible": "",
            "Tools Floater Coverage Limit": "",
            "Installation Floater": "",
            "Course of Construction":"",
            "Commercial General Liability Coverage Present? (Y/N)"
            "Commercial General Liability Coverage Limit": "",
            "Commercial General Liability Coverage Deductible": "",
            "Contractors Equipment Coverage Limit": "",
            "Contractors Equipment Coverage Deductible": "",
            "Wrap-up Liability Limit": "",
            "Profit Limit": "",
            "Gross Rent Limit": "",
            "SBU Coverage Present? (Y/N)":""

        }

        }
        """

        # Process the PDF with each prompt
        print("Extracting policy-level entities...")
        policy_info = call_claude_api(extracted_text, prompt_policy_info, CONFIG_API_KEY)
        print("Extracting claims-level entities...")
        claim_info = call_claude_api(extracted_text, prompt_claim_info, CONFIG_API_KEY)
        print("Extracting coverage-level entities...")
        coverage_info = call_claude_api(extracted_text, prompt_coverage_info, CONFIG_API_KEY)

        # Debugging: Print the raw LLM response
        # print("Policy Info Response:", policy_info)
        # print("Claim Info Response:", claim_info)
        # print("Coverage Info Response:", coverage_info)

        # Attempt to extract JSON content from the LLM response
        combined_results["entities"]["Policy Information"] = extract_json_from_response(policy_info)
        combined_results["entities"]["Claim Information"] = extract_json_from_response(claim_info)
        combined_results["entities"]["Coverage Information"] = extract_json_from_response(coverage_info)

    return combined_results

def extract_json_from_response(response):
    """
    Extracts and returns JSON content from a potentially messy LLM response.
    """
    if not response or not response.strip():
        print("No response or empty response received.")
        return {}

    # Use a regex to find the first JSON object in the response
    json_match = re.search(r'\{.*\}', response, re.DOTALL)
    if json_match:
        json_content = json_match.group(0)
        try:
            return json.loads(json_content)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON from LLM response: {e}")
            return {}
    else:
        print("No valid JSON found in response.")
        return {}

