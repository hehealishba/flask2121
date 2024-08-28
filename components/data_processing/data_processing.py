import time
import random

def simulate_microservices_call():
    print("-- Microservices call to fetch territorial data, flood zones, earthquake zones...")
    time.sleep(random.uniform(1, 2))

def simulate_occupancy_code_lookup():
    print('-- Lookup Occupancy Code, Hazard Code, Sub Product for Implemented Quotes API...')
    time.sleep(random.uniform(1, 2))

def generate_random_data():
    flood_zone = random.randint(1, 10)
    earthquake_zone = random.choice(['A', 'B', 'C', 'D', 'E', 'F'])
    territory = random.randint(1, 99)
    closest_distance_to_waterbody = round(random.uniform(0.1, 5.0), 2)  # Random distance in km

    return {
        "flood_zone": flood_zone,
        "earthquake_zone": earthquake_zone,
        "territory": territory,
        "closest_distance_to_waterbody": closest_distance_to_waterbody
    }

def process_data():
    simulate_microservices_call()
    simulate_occupancy_code_lookup()

    random_data = generate_random_data()

    print(f"Flood Zone: {random_data['flood_zone']}")
    print(f"Earthquake Zone: {random_data['earthquake_zone']}")
    print(f"Territory: {random_data['territory']}")
    print(f"Closest Distance to Waterbody: {random_data['closest_distance_to_waterbody']} km")

    return random_data


