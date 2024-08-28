# import os
# import json
# import pandas as pd
# import anthropic
# import time
# import random
# import sys

# # Adjust the path to find config
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# from config import ANTHROPIC_API_KEY

# def load_industry_classifications(csv_file_path):
#     """Load industry classifications from CSV file."""
#     return pd.read_csv(csv_file_path)

# def call_claude_for_closest_match(concatenated_description, industry_names, api_key):
#     """Call Claude API to find the closest industry match."""
#     client = anthropic.Client(api_key=api_key)
    
#     industry_names_text = "\n".join(industry_names)
    
#     prompt = f"""
#     Here is a list of industry descriptions:
    
#     {industry_names_text}
    
#     The following is a description I need to match:
    
#     {concatenated_description}
    
#     Please return only the industry name from the list that most closely matches the provided description.
#     """
    
#     #print(f"Prompt sent to Claude:\n{prompt}\n")
    
#     response = client.completions.create(
#         model="claude-2.1",  # Replace with the correct model name
#         max_tokens_to_sample=500,
#         prompt=f"\n\nHuman: {prompt}\n\nAssistant:",
#         stop_sequences=["\n\nHuman:"]
#     )
    
#     # Extract the industry name from the response
#     if response and response.completion:
#         # Find the exact match from the industry names list in the response
#         response_text = response.completion.strip()
#        # print(f"Response from Claude:\n{response_text}\n")
        
#         for industry_name in industry_names:
#             if industry_name in response_text:
#                 #print(f"Identified Industry Name: {industry_name}")
#                 return industry_name
        
#         # If no match found, return the first line as a fallback
#         return response_text.split("\n")[0].strip()
#     else:
#         print("No valid response from Claude.")
#         return "Unknown Industry"


# def categorize_business(entities, industry_df, api_key, output_file_path):
#     """Categorize business based on extracted entities and save the updated JSON."""
#     policy_info = entities.get("entities", {}).get("Policy Information", {})
#     operations_ibc_desc = policy_info.get("Operations IBC Description", "")
#     description_of_operations = policy_info.get("Description of Operations", "")
    
#     #print(f"Operations IBC Description: {operations_ibc_desc}")
#     #print(f"Description of Operations: {description_of_operations}")
    
#     # Concatenate the descriptions
#     concatenated_description = f"{operations_ibc_desc} {description_of_operations}".strip()
#     #print(f"Concatenated Description: {concatenated_description}")

#     # Call Claude API to find the closest industry match
#     industry_names = industry_df['Industry Name'].tolist()
#     closest_industry = call_claude_for_closest_match(concatenated_description, industry_names, api_key)

#     #print(f"Closest Industry Match: {closest_industry}")

#     # Add only the industry name to the original JSON structure
#     entities["industry_name"] = closest_industry

#     # Save the updated JSON back to the output directory
#     with open(output_file_path, 'w') as file:
#         json.dump(entities, file, indent=4)

#     #print(f"Business categorization completed and saved to {output_file_path}")
#     print(f"Lookup Insurance Bureau of Canada (IBC) description ... ")
#     time.sleep(random.uniform(1, 2))
#     print(f"Extract Postal Code from Insured Address ... ")
#     time.sleep(random.uniform(1, 2))
#     print(f"Lookup rating territories, flood zone, sbu zone, earthquake zone ...")



# business_categorization.py

import os
import json
import pandas as pd
import anthropic
import time
import random

def load_industry_classifications(csv_file_path):
    """Load industry classifications from CSV file."""
    return pd.read_csv(csv_file_path)

def call_claude_for_closest_match(concatenated_description, industry_names, api_key):
    """Call Claude API to find the closest industry match."""
    client = anthropic.Client(api_key=api_key)
    
    industry_names_text = "\n".join(industry_names)
    
    prompt = f"""
    Here is a list of industry descriptions:
    
    {industry_names_text}
    
    The following is a description I need to match:
    
    {concatenated_description}
    
    Please return only the industry name from the list that most closely matches the provided description.
    """
    
    #print(f"Prompt sent to Claude:\n{prompt}\n")
    
    response = client.completions.create(
        model="claude-2.1",  # Replace with the correct model name
        max_tokens_to_sample=500,
        prompt=f"\n\nHuman: {prompt}\n\nAssistant:",
        stop_sequences=["\n\nHuman:"]
    )
    
    # Extract the industry name from the response
    if response and response.completion:
        # Find the exact match from the industry names list in the response
        response_text = response.completion.strip()
       # print(f"Response from Claude:\n{response_text}\n")
        
        for industry_name in industry_names:
            if industry_name in response_text:
                #print(f"Identified Industry Name: {industry_name}")
                return industry_name
        
        # If no match found, return the first line as a fallback
        return response_text.split("\n")[0].strip()
    else:
        print("No valid response from Claude.")
        return "Unknown Industry"

def categorize_business(entities, industry_df, api_key):
    """Categorize business based on extracted entities."""
    policy_info = entities.get("entities", {}).get("Policy Information", {})
    operations_ibc_desc = policy_info.get("Operations IBC Description", "")
    description_of_operations = policy_info.get("Description of Operations", "")

    # Concatenate the descriptions
    concatenated_description = f"{operations_ibc_desc} {description_of_operations}".strip()

    # Call Claude API to find the closest industry match
    industry_names = industry_df['Industry Name'].tolist()
    closest_industry = call_claude_for_closest_match(concatenated_description, industry_names, api_key)

    print(f"Closest Industry Match: {closest_industry}")

    # Add only the industry name to the original JSON structure
    entities["industry_name"] = closest_industry

    return entities
