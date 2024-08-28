# import json
# import random

# def calculate_gap_amounts(technical_coverage_results, implementable_coverage_results):
#     """Calculate the gap amounts between technical and implementable coverage premiums."""
#     gap_results = {}
#     total_gap_amount = 0.0
    
#     for coverage in technical_coverage_results:
#         technical_premium = technical_coverage_results.get(coverage, 0.0)
#         implementable_premium = implementable_coverage_results.get(coverage.replace("Technical", "Implementable"), 0.0)
        
#         gap_amount = implementable_premium - technical_premium
#         gap_results[f"{coverage}_gap_amount"] = round(gap_amount, 2)
#         total_gap_amount += gap_amount
    
#     return gap_results, round(total_gap_amount, 2)

# def suggest_discount(technical_premium, implementable_premium, gap_results, extracted_text):
#     """Suggest a discount based on the gap amounts and extracted text."""
#     discount_percentage = 0
    
#     # Only suggest a discount if the technical premium is lower than the implementable premium
#     if technical_premium < implementable_premium:
#         # Randomly choose a discount between 5% and 15%
#         discount_percentage = random.uniform(5, 15)
        
#         # Analyze the extracted text to potentially modify the discount (Placeholder logic)
#         if "reduce risk" in extracted_text.lower() or "low exposure" in extracted_text.lower():
#             discount_percentage = max(discount_percentage, 10)
#         else:
#             discount_percentage = min(discount_percentage, 5)
    
#     # Calculate the actual discount amount
#     discount_amount = round((implementable_premium * discount_percentage) / 100, 2)
    
#     return discount_percentage, discount_amount

# def process_gap_and_discount(entities, technical_coverage_results, implementable_coverage_results, extracted_text):
#     """Process gap amounts and suggest a discount."""
#     gap_results, total_gap_amount = calculate_gap_amounts(technical_coverage_results, implementable_coverage_results)
    
#     technical_premium = entities['total_technical_premium']
#     implementable_premium = entities['total_implementable_premium']
    
#     discount_percentage, discount_amount = suggest_discount(technical_premium, implementable_premium, gap_results, extracted_text)
    
#     return gap_results, total_gap_amount, discount_percentage, discount_amount



import json
import random

def calculate_gap_amounts(technical_coverage_results, implementable_coverage_results):
    """Calculate the gap amounts between technical and implementable coverage premiums."""
    gap_results = {}
    total_gap_amount = 0.0
    
    for coverage in technical_coverage_results:
        technical_premium = technical_coverage_results.get(coverage, 0.0)
        implementable_premium = implementable_coverage_results.get(coverage.replace("Technical", "Implementable"), 0.0)
        
        gap_amount = implementable_premium - technical_premium
        gap_results[f"{coverage}_gap_amount"] = round(gap_amount, 2)
        total_gap_amount += gap_amount
    
    return gap_results, round(total_gap_amount, 2)

def suggest_discount(technical_premium, implementable_premium, gap_results, extracted_text):
    """Suggest a discount based on the gap amounts and extracted text."""
    discount_percentage = 0
    
    # Only suggest a discount if the technical premium is lower than the implementable premium
    if technical_premium < implementable_premium:
        # Randomly choose a discount between 5% and 15%
        discount_percentage = random.uniform(5, 15)
        
        # Analyze the extracted text to potentially modify the discount (Placeholder logic)
        if "reduce risk" in extracted_text.lower() or "low exposure" in extracted_text.lower():
            discount_percentage = max(discount_percentage, 10)
        else:
            discount_percentage = min(discount_percentage, 5)
    
    # Calculate the actual discount amount
    discount_amount = round((implementable_premium * discount_percentage) / 100, 2)
    
    return discount_percentage, discount_amount

def process_gap_and_discount(entities, technical_coverage_results, implementable_coverage_results, extracted_text):
    """Process gap amounts and suggest a discount."""
    gap_results, total_gap_amount = calculate_gap_amounts(technical_coverage_results, implementable_coverage_results)
    
    technical_premium = entities['total_technical_premium']
    implementable_premium = entities['total_implementable_premium']
    
    discount_percentage, discount_amount = suggest_discount(technical_premium, implementable_premium, gap_results, extracted_text)

    # Add the gap results and discount information to the entities
    entities['gap_results'] = gap_results
    entities['total_gap_amount'] = total_gap_amount
    entities['discount_percentage'] = discount_percentage
    entities['discount_amount'] = discount_amount
    
    return entities
