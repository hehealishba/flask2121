# import json

# def process_technical_coverage_models(entities):
#     """Processes technical coverage models based on extracted entities and calculates total technical premiums."""
#     coverage_results = {}
#     total_technical_premium = 0.0
    
#     # Example data structure from extracted entities
#     coverages = entities.get("entities", {}).get("Coverage Information", {})
    
#     # Sample rates for the POC
#     building_technical_rate = 0.0035
#     equipment_technical_rate = 0.0045
#     liability_technical_rate = 0.01
#     flood_technical_rate = 0.0020
#     sbu_technical_rate = 0.0030
#     earthquake_technical_rate = 0.0050
    
#     # Process Property Building Coverage
#     if coverages.get("Property Building Coverage Present? (Y/N)") == "Y":
#         building_limit = float(coverages.get("Property Building Coverage Limit", "0").replace(",", ""))
#         technical_building_premium = calculate_building_coverage(building_limit, building_technical_rate)
#     else:
#         technical_building_premium = 0.0
#     coverage_results["Technical Property Building"] = technical_building_premium
#     total_technical_premium += technical_building_premium

#     # Process Property Equipment Coverage
#     if coverages.get("Property Equipment Coverage Present? (Y/N)") == "Y":
#         equipment_limit = float(coverages.get("Property Equipment Coverage Limit", "0").replace(",", ""))
#         technical_equipment_premium = calculate_contractors_equipment_coverage(equipment_limit, equipment_technical_rate)
#     else:
#         technical_equipment_premium = 0.0
#     coverage_results["Technical Property Equipment"] = technical_equipment_premium
#     total_technical_premium += technical_equipment_premium
    
#     # Process Liability Coverage
#     if coverages.get("Liability Coverage Present? (Y/N)") == "Y":
#         liability_limit = float(coverages.get("Liability Coverage Limit", "0").replace(",", ""))
#         technical_liability_premium = calculate_cgl_coverage(liability_limit, liability_technical_rate)
#     else:
#         technical_liability_premium = 0.0
#     coverage_results["Technical Liability"] = technical_liability_premium
#     total_technical_premium += technical_liability_premium

#     # Process Flood Coverage
#     if coverages.get("Flood Coverage Present? (Y/N)") == "Y":
#         flood_premium = calculate_flood_coverage(flood_technical_rate)
#     else:
#         flood_premium = 0.0
#     coverage_results["Technical Flood"] = flood_premium
#     total_technical_premium += flood_premium
    
#     # Process SBU Coverage
#     if coverages.get("SBU Coverage Present? (Y/N)") == "Y":
#         sbu_premium = calculate_sbu_coverage(sbu_technical_rate)
#     else:
#         sbu_premium = 0.0
#     coverage_results["Technical SBU"] = sbu_premium
#     total_technical_premium += sbu_premium
    
#     # Process Earthquake Coverage
#     if coverages.get("Earthquake Coverage Present? (Y/N)") == "Y":
#         earthquake_premium = calculate_earthquake_coverage(earthquake_technical_rate)
#     else:
#         earthquake_premium = 0.0
#     coverage_results["Technical Earthquake"] = earthquake_premium
#     total_technical_premium += earthquake_premium

#     return coverage_results, round(total_technical_premium, 2)

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

def process_technical_coverage_models(entities):
    """Processes technical coverage models based on extracted entities and calculates total technical premiums."""
    coverage_results = {}
    total_technical_premium = 0.0
    
    # Example data structure from extracted entities
    coverages = entities.get("entities", {}).get("Coverage Information", {})
    
    # Sample rates for the POC
    # Building around 0.22-0.27 per $ million
    # Equipment around 0.5-0.6 per $100K
    # Stock around 0.5-0.6 per $200K?
    # CGL 1.75-2.15 per $50K
    # CTRE - Contractors Equipment around 0.9 to 1.15 per $100K

    building_technical_rate = 0.0035
    equipment_technical_rate = 0.0045
    liability_technical_rate = 0.01
    flood_technical_rate = 0.0020
    sbu_technical_rate = 0.0030
    earthquake_technical_rate = 0.0050
    
    # Process Property Building Coverage
    if coverages.get("Property Building Coverage Present? (Y/N)") == "Y":
        building_limit = float(coverages.get("Property Building Coverage Limit", "0").replace(",", ""))
        technical_building_premium = calculate_building_coverage(building_limit, building_technical_rate)
    else:
        technical_building_premium = 0.0
    coverage_results["Technical Property Building"] = technical_building_premium
    total_technical_premium += technical_building_premium

    # Process Property Equipment Coverage
    if coverages.get("Property Equipment Coverage Present? (Y/N)") == "Y":
        equipment_limit = float(coverages.get("Property Equipment Coverage Limit", "0").replace(",", ""))
        technical_equipment_premium = calculate_contractors_equipment_coverage(equipment_limit, equipment_technical_rate)
    else:
        technical_equipment_premium = 0.0
    coverage_results["Technical Property Equipment"] = technical_equipment_premium
    total_technical_premium += technical_equipment_premium
    
    # Process Liability Coverage
    if coverages.get("Commercial General Liability Coverage Present? (Y/N)") == "Y":
        liability_limit = float(coverages.get("Commercial General Liability Coverage Limit", "0").replace(",", ""))
        technical_liability_premium = calculate_cgl_coverage(liability_limit, liability_technical_rate)
    else:
        technical_liability_premium = 0.0
    coverage_results["Technical Liability"] = technical_liability_premium
    total_technical_premium += technical_liability_premium

    # Process Flood Coverage
    if coverages.get("Flood Coverage Present? (Y/N)") == "Y":
        flood_premium = calculate_flood_coverage(flood_technical_rate)
    else:
        flood_premium = 0.0
    coverage_results["Technical Flood"] = flood_premium
    total_technical_premium += flood_premium
    
    # Process SBU Coverage
    if coverages.get("SBU Coverage Present? (Y/N)") == "Y":
        sbu_premium = calculate_sbu_coverage(sbu_technical_rate)
    else:
        sbu_premium = 0.0
    coverage_results["Technical SBU"] = sbu_premium
    total_technical_premium += sbu_premium
    
    # Process Earthquake Coverage
    if coverages.get("Earthquake Coverage Present? (Y/N)") == "Y":
        earthquake_premium = calculate_earthquake_coverage(earthquake_technical_rate)
    else:
        earthquake_premium = 0.0
    coverage_results["Technical Earthquake"] = earthquake_premium
    total_technical_premium += earthquake_premium

    # Add the coverage results to the entities
    entities['technical_coverage_results'] = coverage_results
    entities['total_technical_premium'] = round(total_technical_premium, 2)

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
