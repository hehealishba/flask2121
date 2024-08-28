
# import os
# import numpy as np
# import pandas as pd
# import pickle
# from datetime import datetime
# from sklearn.preprocessing import StandardScaler
# import joblib
# # Path to the model
# MODEL_PATH  = '/Users/neerajnachnani/Library/Mobile Documents/com~apple~CloudDocs/Phantom Labs/DS/IDP_UW_Enrichment_Demo/idp_uw_enrichment_poc/Models/model_artifacts/ebm_quote_conversion_model.pkl'

# def calculate_days_from_effective_date(effective_date_str):
#     effective_date = datetime.strptime(effective_date_str, "%B %d, %Y")
#     current_date = datetime.now()
#     return (current_date - effective_date).days

# def generate_random_data(num_rows, days_max):
#     days_from_effective_date = np.random.randint(0, days_max, num_rows)
#     industry_code = np.random.choice(['A', 'B', 'C', 'D'], num_rows)
#     hazard_grade = np.random.choice([1, 2, 3, 4, 5], num_rows)
#     product_sub_type = np.random.choice(['Type1', 'Type2', 'Type3'], num_rows)
#     region = np.random.choice(['North', 'South', 'East', 'West'], num_rows)

#     # Create a DataFrame
#     data = pd.DataFrame({
#         'days_from_effective_date': days_from_effective_date,
#         'industry_code': industry_code,
#         'hazard_grade': hazard_grade,
#         'product_sub_type': product_sub_type,
#         'region': region
#     })

#     return data

# def load_model(model_path):
#     with open(model_path, 'rb') as file:
#         model = pickle.load(file)
#     return model

# def predict_prioritization(data, model):
#     # Assuming the model expects specific preprocessing
#     scaler = StandardScaler()
#     scaled_data = scaler.fit_transform(data[['days_from_effective_date', 'hazard_grade']])
    
#     # Prediction logic
#     predictions = model.predict(scaled_data)
    
#     return predictions
# def prioritize_quote(effective_date_str):
#     # Convert the effective date to a datetime object
#     effective_date = datetime.strptime(effective_date_str, "%B %d, %Y")
#     current_date = datetime.now()

#     # Calculate days from the effective date
#     days_from_effective_date = (current_date - effective_date).days

#     # Generate other required data points for the model
#     num_rows = 1  # Since this is a single quote prioritization, we generate data for one row
#     industry_code = np.random.choice(['A', 'B', 'C', 'D'], num_rows)
#     hazard_grade = np.random.choice([1, 2, 3, 4, 5], num_rows)
#     product_sub_type = np.random.choice(['Type1', 'Type2', 'Type3'], num_rows)
#     region = np.random.choice(['North', 'South', 'East', 'West'], num_rows)

#     # Create a DataFrame with the required inputs
#     input_df = pd.DataFrame({
#         'days_from_effective_date': days_from_effective_date,
#         'industry_code': industry_code,
#         'hazard_grade': hazard_grade,
#         'product_sub_type': product_sub_type,
#         'region': region
#     })

#     # Load the model - adjust the path to the model file
#     model_path ='/Users/neerajnachnani/Library/Mobile Documents/com~apple~CloudDocs/Phantom Labs/DS/IDP_UW_Enrichment_Demo/idp_uw_enrichment_poc/Models/model_artifacts/ebm_quote_conversion_model.pkl'
#     model = joblib.load(model_path)

#     # Predict the prioritization score
#     prioritization_score = model.predict(input_df)

#     # Create the output dictionary
#     prioritization_data = {
#         'quote_prioritization': {
#             'days_from_effective_date': days_from_effective_date,
#             'industry_code': industry_code[0],
#             'hazard_grade': hazard_grade[0],
#             'product_sub_type': product_sub_type[0],
#             'region': region[0],
#             'prioritization_score': prioritization_score[0]
#         }
#     }

#     return prioritization_data




# import os
# import numpy as np
# import pandas as pd
# from datetime import datetime
# import joblib
# from sklearn.preprocessing import StandardScaler

# # Path to the model
# MODEL_PATH = '/Users/neerajnachnani/Library/Mobile Documents/com~apple~CloudDocs/Phantom Labs/DS/IDP_UW_Enrichment_Demo/idp_uw_enrichment_poc/Models/model_artifacts/ebm_quote_conversion_model.pkl'

# def calculate_days_from_effective_date(effective_date_str):
#     effective_date = datetime.strptime(effective_date_str, "%B %d, %Y")
#     current_date = datetime.now()
#     return (current_date - effective_date).days

# def generate_random_data(num_rows, days_max):
#     days_from_effective_date = np.random.randint(0, days_max, num_rows)
#     industry_code = np.random.choice(['A', 'B', 'C', 'D'], num_rows)
#     hazard_grade = np.random.choice([1, 2, 3, 4, 5], num_rows)
#     product_sub_type = np.random.choice(['Type1', 'Type2', 'Type3'], num_rows)
#     region = np.random.choice(['North', 'South', 'East', 'West'], num_rows)

#     # Create a DataFrame
#     data = pd.DataFrame({
#         'days_from_effective_date': days_from_effective_date,
#         'industry_code': industry_code,
#         'hazard_grade': hazard_grade,
#         'product_sub_type': product_sub_type,
#         'region': region
#     })

#     return data

# def load_model(model_path):
#     with open(model_path, 'rb') as file:
#         model = joblib.load(file)
#     return model

# def prioritize_quote(effective_date_str):
#     # Convert the effective date to a datetime object
#     effective_date = datetime.strptime(effective_date_str, "%B %d, %Y")
#     current_date = datetime.now()

#     # Calculate days from the effective date
#     days_from_effective_date = (current_date - effective_date).days

#     # Generate other required data points for the model
#     num_rows = 1  # Since this is a single quote prioritization, we generate data for one row
#     industry_code = np.random.choice(['A', 'B', 'C', 'D'], num_rows)
#     hazard_grade = np.random.choice([1, 2, 3, 4, 5], num_rows)
#     product_sub_type = np.random.choice(['Type1', 'Type2', 'Type3'], num_rows)
#     region = np.random.choice(['North', 'South', 'East', 'West'], num_rows)

#     # Create a DataFrame with the required inputs
#     input_df = pd.DataFrame({
#         'days_from_effective_date': [days_from_effective_date],
#         'industry_code': industry_code,
#         'hazard_grade': hazard_grade,
#         'product_sub_type': product_sub_type,
#         'region': region
#     })

#     # One-hot encode categorical variables (same as in model training)
#     input_df = pd.get_dummies(input_df, columns=['industry_code', 'product_sub_type', 'region'], drop_first=True)

#     # Ensure the DataFrame has the same columns as the model was trained on
#     model = load_model(MODEL_PATH)
#     model_columns = model.preprocessor_.column_names_
#     input_df = input_df.reindex(columns=model_columns, fill_value=0)

#     # Predict the prioritization score
#     prioritization_score = model.predict(input_df)

#     # Create the output dictionary
#     prioritization_data = {
#         'quote_prioritization': {
#             'days_from_effective_date': days_from_effective_date,
#             'industry_code': industry_code[0],
#             'hazard_grade': hazard_grade[0],
#             'product_sub_type': product_sub_type[0],
#             'region': region[0],
#             'prioritization_score': prioritization_score[0]
#         }
#     }

#     return prioritization_data



## Third iteration

# import os
# import numpy as np
# import pandas as pd
# import joblib
# from datetime import datetime
# from sklearn.preprocessing import StandardScaler

# # Path to the model
# MODEL_PATH = '/Users/neerajnachnani/Library/Mobile Documents/com~apple~CloudDocs/Phantom Labs/DS/IDP_UW_Enrichment_Demo/idp_uw_enrichment_poc/Models/model_artifacts/ebm_quote_conversion_model.pkl'

# def calculate_days_from_effective_date(effective_date_str):
#     effective_date = datetime.strptime(effective_date_str, "%B %d, %Y")
#     current_date = datetime.now()
#     return (current_date - effective_date).days

# def generate_random_data(num_rows, days_max):
#     days_from_effective_date = np.random.randint(0, days_max, num_rows)
#     industry_code = np.random.choice(['A', 'B', 'C', 'D'], num_rows)
#     hazard_grade = np.random.choice([1, 2, 3, 4, 5], num_rows)
#     product_sub_type = np.random.choice(['Type1', 'Type2', 'Type3'], num_rows)
#     region = np.random.choice(['North', 'South', 'East', 'West'], num_rows)

#     # Create a DataFrame
#     data = pd.DataFrame({
#         'days_from_effective_date': days_from_effective_date,
#         'industry_code': industry_code,
#         'hazard_grade': hazard_grade,
#         'product_sub_type': product_sub_type,
#         'region': region
#     })

#     return data

# def load_model(model_path):
#     with open(model_path, 'rb') as file:
#         model = joblib.load(file)
#     return model

# def prepare_data_for_model(input_df):
#     # One-hot encode categorical variables
#     input_df_encoded = pd.get_dummies(input_df, columns=['industry_code', 'product_sub_type', 'region'], drop_first=True)

#     # Ensure that the encoded DataFrame matches the model's expected columns
#     expected_columns = [
#         'days_from_effective_date', 'hazard_grade', 
#         'industry_code_B', 'industry_code_C', 'industry_code_D',
#         'product_sub_type_Type2', 'product_sub_type_Type3',
#         'region_South', 'region_East', 'region_West'
#     ]

#     for col in expected_columns:
#         if col not in input_df_encoded.columns:
#             input_df_encoded[col] = 0

#     input_df_encoded = input_df_encoded[expected_columns]

#     # Standardize numerical features if needed (as per the model's training)
#     scaler = StandardScaler()
#     input_df_encoded[['days_from_effective_date', 'hazard_grade']] = scaler.fit_transform(
#         input_df_encoded[['days_from_effective_date', 'hazard_grade']]
#     )

#     return input_df_encoded

# def prioritize_quote(effective_date_str):
#     # Calculate days from the effective date
#     days_from_effective_date = calculate_days_from_effective_date(effective_date_str)

#     # Generate other required data points for the model
#     input_df = generate_random_data(num_rows=1, days_max=days_from_effective_date)

#     # Prepare the data for the model
#     input_df_prepared = prepare_data_for_model(input_df)

#     # Load the model
#     model = load_model(MODEL_PATH)

#     # Predict the prioritization score
#     prioritization_score = model.predict(input_df_prepared)

#     # Create the output dictionary
#     prioritization_data = {
#         'quote_prioritization': {
#             'days_from_effective_date': days_from_effective_date,
#             'industry_code': input_df['industry_code'][0],
#             'hazard_grade': input_df['hazard_grade'][0],
#             'product_sub_type': input_df['product_sub_type'][0],
#             'region': input_df['region'][0],
#             'prioritization_score': prioritization_score[0]
#         }
#     }

#     return prioritization_data

# import os
# import numpy as np
# import pandas as pd
# import pickle
# from datetime import datetime
# import joblib

# # Path to the model
# MODEL_PATH = '/Users/neerajnachnani/Library/Mobile Documents/com~apple~CloudDocs/Phantom Labs/DS/IDP_UW_Enrichment_Demo/idp_uw_enrichment_poc/Models/model_artifacts/ebm_quote_conversion_model.pkl'

# def calculate_days_to_effective_date(effective_date_str):
#     # List of common month abbreviations and their full names
#     month_abbreviations = {
#         "Jan": "January",
#         "Feb": "February",
#         "Mar": "March",
#         "Apr": "April",
#         "May": "May",
#         "Jun": "June",
#         "Jul": "July",
#         "Aug": "August",
#         "Sept": "September",  # Handle 'Sept' as 'September'
#         "Sep": "September",
#         "Oct": "October",
#         "Nov": "November",
#         "Dec": "December"
#     }

#     # Replace any abbreviated month in the effective_date_str with its full name
#     for abbrev, full in month_abbreviations.items():
#         if abbrev in effective_date_str:
#             effective_date_str = effective_date_str.replace(abbrev, full)
#             break

#     # Now parse the date string with the expected format
#     effective_date = datetime.strptime(effective_date_str, "%B %d, %Y")
#     current_date = datetime.now()
#     days_to_effective_date = (effective_date - current_date).days
#     return days_to_effective_date

# def generate_data(days_from_effective_date):
#     industry_code = np.random.choice(['A', 'B', 'C', 'D'], 1)
#     hazard_grade = np.random.choice([1, 2, 3, 4, 5], 1)
#     product_sub_type = np.random.choice(['Type1', 'Type2', 'Type3'], 1)
#     region = np.random.choice(['North', 'South', 'East', 'West'], 1)

#     # Create a DataFrame
#     data = pd.DataFrame({
#         'days_from_effective_date': [days_from_effective_date],
#         'industry_code': industry_code,
#         'hazard_grade': hazard_grade,
#         'product_sub_type': product_sub_type,
#         'region': region
#     })

#     return data

# def prioritize_quote(effective_date_str):
#     # Calculate days to the effective date
#     days_to_effective_date = calculate_days_to_effective_date(effective_date_str)

#     # Generate other required data points for the model, keeping the days_to_effective_date constant
#     input_df = generate_data(days_from_effective_date=days_to_effective_date)

#     # One-hot encode categorical variables
#     input_df = pd.get_dummies(input_df, columns=['industry_code', 'product_sub_type', 'region'], drop_first=True)

#     # Load the model
#     model = joblib.load(MODEL_PATH)

#     # Ensure the input data matches the model's expected features
#     model_columns = model.feature_names_in_  # Get the model's expected feature names
#     missing_cols = set(model_columns) - set(input_df.columns)
#     for col in missing_cols:
#         input_df[col] = 0
#     input_df = input_df[model_columns]  # Ensure the columns are in the correct order

#     # Predict the prioritization score
#     prioritization_score = model.predict(input_df)

#     # Create the output dictionary
#     prioritization_data = {
#         'quote_prioritization': {
#             'days_to_effective_date': days_to_effective_date,
#             'industry_code': input_df.columns[input_df.columns.str.contains('industry_code')][0],
#             'hazard_grade': input_df['hazard_grade'][0],
#             'product_sub_type': input_df.columns[input_df.columns.str.contains('product_sub_type')][0],
#             'region': input_df.columns[input_df.columns.str.contains('region')][0],
#             'prioritization_score': prioritization_score[0]
#         }
#     }

#     return prioritization_data




## Next Iteration


# import os
# import numpy as np
# import pandas as pd
# import joblib
# from datetime import datetime

# # Path to the model
# MODEL_PATH = '/Users/neerajnachnani/Library/Mobile Documents/com~apple~CloudDocs/Phantom Labs/DS/IDP_UW_Enrichment_Demo/idp_uw_enrichment_poc/Models/model_artifacts/ebm_quote_conversion_model.pkl'

# def calculate_days_to_effective_date(effective_date_str):
#     # List of common month abbreviations and their full names
#     month_abbreviations = {
#         "Jan": "January",
#         "Feb": "February",
#         "Mar": "March",
#         "Apr": "April",
#         "May": "May",
#         "Jun": "June",
#         "Jul": "July",
#         "Aug": "August",
#         "Sept": "September",  # Handle 'Sept' as 'September'
#         "Sep": "September",
#         "Oct": "October",
#         "Nov": "November",
#         "Dec": "December"
#     }

#     # Replace any abbreviated month in the effective_date_str with its full name
#     for abbrev, full in month_abbreviations.items():
#         if abbrev in effective_date_str:
#             effective_date_str = effective_date_str.replace(abbrev, full)
#             break

#     # Now parse the date string with the expected format
#     effective_date = datetime.strptime(effective_date_str, "%B %d, %Y")
#     current_date = datetime.now()
#     days_to_effective_date = (effective_date - current_date).days
#     return days_to_effective_date

# def generate_data(days_to_effective_date):
#     industry_code = np.random.choice(['A', 'B', 'C', 'D'], 1)
#     hazard_grade = np.random.choice([1, 2, 3, 4, 5], 1)
#     product_sub_type = np.random.choice(['Type1', 'Type2', 'Type3'], 1)
#     region = np.random.choice(['North', 'South', 'East', 'West'], 1)

#     # Create a DataFrame
#     data = pd.DataFrame({
#         'days_to_effective_date': [days_to_effective_date],
#         'industry_code': industry_code,
#         'hazard_grade': hazard_grade,
#         'product_sub_type': product_sub_type,
#         'region': region
#     })

#     return data

# def prioritize_quote(effective_date_str):
#     # Calculate days to the effective date
#     days_to_effective_date = calculate_days_to_effective_date(effective_date_str)

#     # Generate other required data points for the model, keeping the days_to_effective_date constant
#     input_df = generate_data(days_to_effective_date=days_to_effective_date)

#     # One-hot encode categorical variables
#     input_df = pd.get_dummies(input_df, columns=['industry_code', 'product_sub_type', 'region'], drop_first=True)

#     # Load the model
#     model = joblib.load(MODEL_PATH)

#     # Ensure the input data matches the model's expected features
#     model_columns = model.feature_names_in_  # Get the model's expected feature names
#     missing_cols = set(model_columns) - set(input_df.columns)
#     for col in missing_cols:
#         input_df[col] = 0
#     input_df = input_df[model_columns]  # Ensure the columns are in the correct order

#     # Predict the prioritization score, using predict_proba for probability
#     prioritization_score = model.predict_proba(input_df)[:, 1] * 100  # Scale to 1-100

#     # Create the output dictionary
#     prioritization_data = {
#         'quote_prioritization': {
#             'days_to_effective_date': days_to_effective_date,
#             'industry_code': input_df.columns[input_df.columns.str.contains('industry_code')][0],
#             'hazard_grade': input_df['hazard_grade'][0],
#             'product_sub_type': input_df.columns[input_df.columns.str.contains('product_sub_type')][0],
#             'region': input_df.columns[input_df.columns.str.contains('region')][0],
#             'prioritization_score': prioritization_score[0]
#         }
#     }

#     return prioritization_data



## Next StopIteration

import os
import numpy as np
import pandas as pd
import joblib
from datetime import datetime
import datefinder

# Path to the model
MODEL_PATH = '/Users/neerajnachnani/Library/Mobile Documents/com~apple~CloudDocs/Phantom Labs/DS/IDP_UW_Enrichment_Demo/idp_uw_enrichment_poc/Models/model_artifacts/ebm_quote_conversion_model.pkl'



def calculate_days_to_effective_date(effective_date_str):
    # Use datefinder to extract dates from the text
    matches = list(datefinder.find_dates(effective_date_str))

    if not matches:
        raise ValueError(f"No valid dates found in the string: {effective_date_str}")
    
    # Assuming the first match is the correct date
    effective_date = matches[0]
   # print(f"Effective Date: {effective_date}")

    current_date = datetime.now()
    days_to_effective_date = (effective_date - current_date).days

    return days_to_effective_date




def generate_data(days_to_effective_date):
    industry_code = np.random.choice(['A', 'B', 'C', 'D'], 1)
    hazard_grade = np.random.choice([1, 2, 3, 4, 5], 1)
    product_sub_type = np.random.choice(['Type1', 'Type2', 'Type3'], 1)
    region = np.random.choice(['North', 'South', 'East', 'West'], 1)

    # Create a DataFrame
    data = pd.DataFrame({
        'days_to_effective_date': [days_to_effective_date],
        'industry_code': industry_code,
        'hazard_grade': hazard_grade,
        'product_sub_type': product_sub_type,
        'region': region
    })

    return data

def prioritize_quote(effective_date_str):
    # Calculate days to the effective date
    days_to_effective_date = calculate_days_to_effective_date(effective_date_str)

    # Generate other required data points for the model, keeping the days_to_effective_date constant
    input_df = generate_data(days_to_effective_date=days_to_effective_date)

    # One-hot encode categorical variables
    input_df = pd.get_dummies(input_df, columns=['industry_code', 'product_sub_type', 'region'], drop_first=True)

    # Load the model
    model = joblib.load(MODEL_PATH)

    # Ensure the input data matches the model's expected features
    model_columns = model.feature_names_in_  # Get the model's expected feature names
    missing_cols = set(model_columns) - set(input_df.columns)
    for col in missing_cols:
        input_df[col] = 0
    input_df = input_df[model_columns]  # Ensure the columns are in the correct order

    # Predict the prioritization score, using predict_proba for probability
# Predict the prioritization score, using predict_proba for probability
    prioritization_score = np.round(model.predict_proba(input_df)[:, 1] * 100, 2)  # Scale to 1-100 and round to 2 decimal places

    # Create the output dictionary
    prioritization_data = {
        'quote_prioritization': {
            'days_to_effective_date': days_to_effective_date,
            'industry_code': input_df.columns[input_df.columns.str.contains('industry_code')][0],
            'hazard_grade': input_df['hazard_grade'][0],
            'product_sub_type': input_df.columns[input_df.columns.str.contains('product_sub_type')][0],
            'region': input_df.columns[input_df.columns.str.contains('region')][0],
            'prioritization_score': prioritization_score[0]
        }
    }

    return prioritization_data
