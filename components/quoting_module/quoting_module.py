# import json

# def process_implementable_coverage_models(entities):
#     """Processes implementable coverage models based on extracted entities and calculates total implementable premiums."""
#     coverage_results = {}
#     total_implementable_premium = 0.0
    
#     # Example data structure from extracted entities
#     coverages = entities.get("entities", {}).get("Coverage Information", {})
    
#     # Sample rates for the POC
#     building_implementable_rate = 0.0038
#     equipment_implementable_rate = 0.0050
#     liability_implementable_rate = 0.012
#     flood_implementable_rate = 0.0025
#     sbu_implementable_rate = 0.0035
#     earthquake_implementable_rate = 0.0060
    
#     # Process Property Building Coverage
#     if coverages.get("Property Building Coverage Present? (Y/N)") == "Y":
#         building_limit = float(coverages.get("Property Building Coverage Limit", "0").replace(",", ""))
#         implementable_building_premium = calculate_building_coverage(building_limit, building_implementable_rate)
#     else:
#         implementable_building_premium = 0.0
#     coverage_results["Implementable Property Building"] = implementable_building_premium
#     total_implementable_premium += implementable_building_premium

#     # Process Property Equipment Coverage
#     if coverages.get("Property Equipment Coverage Present? (Y/N)") == "Y":
#         equipment_limit = float(coverages.get("Property Equipment Coverage Limit", "0").replace(",", ""))
#         implementable_equipment_premium = calculate_contractors_equipment_coverage(equipment_limit, equipment_implementable_rate)
#     else:
#         implementable_equipment_premium = 0.0
#     coverage_results["Implementable Property Equipment"] = implementable_equipment_premium
#     total_implementable_premium += implementable_equipment_premium
    
#     # Process Liability Coverage
#     if coverages.get("Liability Coverage Present? (Y/N)") == "Y":
#         liability_limit = float(coverages.get("Liability Coverage Limit", "0").replace(",", ""))
#         implementable_liability_premium = calculate_cgl_coverage(liability_limit, liability_implementable_rate)
#     else:
#         implementable_liability_premium = 0.0
#     coverage_results["Implementable Liability"] = implementable_liability_premium
#     total_implementable_premium += implementable_liability_premium

#     # Process Flood Coverage
#     if coverages.get("Flood Coverage Present? (Y/N)") == "Y":
#         flood_premium = calculate_flood_coverage(flood_implementable_rate)
#     else:
#         flood_premium = 0.0
#     coverage_results["Implementable Flood"] = flood_premium
#     total_implementable_premium += flood_premium
    
#     # Process SBU Coverage
#     if coverages.get("SBU Coverage Present? (Y/N)") == "Y":
#         sbu_premium = calculate_sbu_coverage(sbu_implementable_rate)
#     else:
#         sbu_premium = 0.0
#     coverage_results["Implementable SBU"] = sbu_premium
#     total_implementable_premium += sbu_premium
    
#     # Process Earthquake Coverage
#     if coverages.get("Earthquake Coverage Present? (Y/N)") == "Y":
#         earthquake_premium = calculate_earthquake_coverage(earthquake_implementable_rate)
#     else:
#         earthquake_premium = 0.0
#     coverage_results["Implementable Earthquake"] = earthquake_premium
#     total_implementable_premium += earthquake_premium

#     return coverage_results, round(total_implementable_premium, 2)

# def calculate_building_coverage(ins_value, rate):
#     """Placeholder function to calculate Building coverage premium."""
#     return round(ins_value * rate, 2)

# def calculate_contractors_equipment_coverage(ins_value, rate):
#     """Placeholder function to calculate Contractors Equipment coverage premium."""
#     return round(ins_value * rate, 2)

# def calculate_cgl_coverage(rateable_base, rate):
#     """Placeholder function to calculate CGL coverage premium."""
#     return round(rateable_base * rate, 2)

# def calculate_flood_coverage(rate):
#     """Placeholder function to calculate Flood coverage premium."""
#     return round(25000 * rate, 2)  # Example calculation based on deductible

# def calculate_sbu_coverage(rate):
#     """Placeholder function to calculate Sewer Backup (SBU) coverage premium."""
#     return round(5000 * rate, 2)  # Example calculation based on deductible

# def calculate_earthquake_coverage(rate):
#     """Placeholder function to calculate Earthquake coverage premium."""
#     return round(100000 * rate, 2)  # Example calculation based on minimum deductible



import json

def process_implementable_coverage_models(entities):
    """Processes implementable coverage models based on extracted entities and calculates total implementable premiums."""
    coverage_results = {}
    total_implementable_premium = 0.0
    
    # Example data structure from extracted entities
    coverages = entities.get("entities", {}).get("Coverage Information", {})
    
    # Sample rates for the POC
    building_implementable_rate = 0.0038
    equipment_implementable_rate = 0.0050
    liability_implementable_rate = 0.012
    flood_implementable_rate = 0.0025
    sbu_implementable_rate = 0.0035
    earthquake_implementable_rate = 0.0060
    
    print("Building coverage ...")
    # Process Property Building Coverage
    if coverages.get("Property Building Coverage Present? (Y/N)") == "Y":
        building_limit = float(coverages.get("Property Building Coverage Limit", "0").replace(",", ""))
        implementable_building_premium = calculate_building_coverage(building_limit, building_implementable_rate)
    else:
        implementable_building_premium = 0.0
    coverage_results["Implementable Property Building"] = implementable_building_premium
    total_implementable_premium += implementable_building_premium

    print("Equipment coverage ...")
    # Process Property Equipment Coverage
    if coverages.get("Property Equipment Coverage Present? (Y/N)") == "Y":
        equipment_limit = float(coverages.get("Property Equipment Coverage Limit", "0").replace(",", ""))
        implementable_equipment_premium = calculate_contractors_equipment_coverage(equipment_limit, equipment_implementable_rate)
    else:
        implementable_equipment_premium = 0.0
    coverage_results["Implementable Property Equipment"] = implementable_equipment_premium
    total_implementable_premium += implementable_equipment_premium
    print("Commercial General Liability coverage ...")
    # Process Liability Coverage
    if coverages.get("Commercial General Liability Coverage Present? (Y/N)") == "Y":
        liability_limit = float(coverages.get("Commercial General Liability Coverage Limit", "0").replace(",", ""))
        implementable_liability_premium = calculate_cgl_coverage(liability_limit, liability_implementable_rate)
    else:
        implementable_liability_premium = 0.0
    coverage_results["Implementable Liability"] = implementable_liability_premium
    total_implementable_premium += implementable_liability_premium

    print("Flood coverage ...")
    # Process Flood Coverage
    if coverages.get("Flood Coverage Present? (Y/N)") == "Y":
        flood_premium = calculate_flood_coverage(flood_implementable_rate)
    else:
        flood_premium = 0.0
    coverage_results["Implementable Flood"] = flood_premium
    total_implementable_premium += flood_premium
    
    #print("Sewer Back-up coverage ...")
    # Process SBU Coverage
    if coverages.get("SBU Coverage Present? (Y/N)") == "Y":
        sbu_premium = calculate_sbu_coverage(sbu_implementable_rate)
    else:
        sbu_premium = 0.0
    coverage_results["Implementable SBU"] = sbu_premium
    total_implementable_premium += sbu_premium
    
    print("Earthquake coverage ...")
    # Process Earthquake Coverage
    if coverages.get("Earthquake Coverage Present? (Y/N)") == "Y":
        earthquake_premium = calculate_earthquake_coverage(earthquake_implementable_rate)
    else:
        earthquake_premium = 0.0
    coverage_results["Implementable Earthquake"] = earthquake_premium
    total_implementable_premium += earthquake_premium

    # Add the coverage results to the entities
    entities['implementable_coverage_results'] = coverage_results
    entities['total_implementable_premium'] = round(total_implementable_premium, 2)

    return entities

def calculate_building_coverage(ins_value, rate):
    """Placeholder function to calculate Building coverage premium."""
    return round(ins_value * rate, 2)

def calculate_contractors_equipment_coverage(ins_value, rate):
    """Placeholder function to calculate Contractors Equipment coverage premium."""
    return round(ins_value * rate, 2)

def calculate_cgl_coverage(rateable_base, rate):
    """Placeholder function to calculate CGL coverage premium."""
    return round(rateable_base * rate, 2)

def calculate_flood_coverage(rate):
    """Placeholder function to calculate Flood coverage premium."""
    return round(25000 * rate, 2)  # Example calculation based on deductible

def calculate_sbu_coverage(rate):
    """Placeholder function to calculate Sewer Backup (SBU) coverage premium."""
    return round(5000 * rate, 2)  # Example calculation based on deductible

def calculate_earthquake_coverage(rate):
    """Placeholder function to calculate Earthquake coverage premium."""
    return round(100000 * rate, 2)  # Example calculation based on minimum deductible
