import json

# Function to extract car overview
def car_overview_dict_creator(overview):
    # Correctly replace None and handle single quotes
    overview_dict = json.loads(overview.replace("'", '"').replace('None', 'null'))
    all_overviews = {}
    for dictionary in overview_dict.get('top', []):
        all_overviews[dictionary.get('key')] = dictionary.get('value')
    return all_overviews

# Function to extract car features
def car_feature_dict_creator(feature):
    all_features = {}
    # Correctly replace None and handle single quotes
    feature_dict = json.loads(feature.replace("'", '"').replace('None', 'null'))
    for dictionary in feature_dict.get('top', []):
        all_features[dictionary.get('value')] = True
    for section in feature_dict.get('data', []):
        for item in section.get('list', []):
            all_features[item.get('value')] = True
    return all_features

# Function to extract car specifications
def car_spec_dict_creator(spec):
    all_specs = {}
    # Correctly replace None and handle single quotes
    specs_dict = json.loads(spec.replace("'", '"').replace('None', 'null'))
    for dictionary in specs_dict.get('top', []):
        all_specs[dictionary.get('key')] = dictionary.get('value')
    # Extract nested specifications
    for dictionary in specs_dict.get('data', []):
        for item in dictionary.get('list', []):
            all_specs[item.get('key')] = item.get('value')
    return all_specs


import pandas as pd
import json

# Load data from Excel
df = pd.read_excel(r"C:\Users\Vishwa\Desktop\GUVI captone\CAR\bangalore_cars.xlsx")

# Function to extract car detail
def extract_car_detail(detail):
    return json.loads(detail.replace("'", '"').replace('None', 'null'))

# Apply car detail extraction
df['new_car_detail'] = df['new_car_detail'].apply(extract_car_detail)
df_car_detail = pd.DataFrame(df['new_car_detail'].tolist())

# Apply car overview extraction
df['new_car_overview'] = df['new_car_overview'].apply(car_overview_dict_creator)
df_car_overview = pd.DataFrame(df['new_car_overview'].tolist())

# Apply car features extraction
df['new_car_feature'] = df['new_car_feature'].apply(car_feature_dict_creator)
feature_df = pd.json_normalize(df['new_car_feature']).fillna(0).astype(int)

# Apply car specs extraction
df['new_car_specs'] = df['new_car_specs'].apply(car_spec_dict_creator)
df_car_specs = pd.DataFrame(df['new_car_specs'].tolist())

# Combine all dataframes
df_combined = pd.concat([df_car_detail, df_car_overview, feature_df, df_car_specs], axis=1)

# Add city column and save to CSV
df_combined['city'] = 'Bangalore'

df_combined.to_csv('Bangalore_cars.csv', index=False)


import pandas as pd
import json

# Load data from Excel
df = pd.read_excel(r"C:\Users\Vishwa\Desktop\GUVI captone\CAR\chennai_cars.xlsx")

# Function to extract car detail
def extract_car_detail(detail):
    return json.loads(detail.replace("'", '"').replace('None', 'null'))

# Apply car detail extraction
df['new_car_detail'] = df['new_car_detail'].apply(extract_car_detail)
df_car_detail = pd.DataFrame(df['new_car_detail'].tolist())

# Apply car overview extraction
df['new_car_overview'] = df['new_car_overview'].apply(car_overview_dict_creator)
df_car_overview = pd.DataFrame(df['new_car_overview'].tolist())

# Apply car features extraction
df['new_car_feature'] = df['new_car_feature'].apply(car_feature_dict_creator)
feature_df = pd.json_normalize(df['new_car_feature']).fillna(0).astype(int)

# Apply car specs extraction
df['new_car_specs'] = df['new_car_specs'].apply(car_spec_dict_creator)
df_car_specs = pd.DataFrame(df['new_car_specs'].tolist())

# Combine all dataframes
df_combined = pd.concat([df_car_detail, df_car_overview, feature_df, df_car_specs], axis=1)

# Add city column and save to CSV
df_combined['city'] = 'chennai'

df_combined.to_csv('chennai_cars.csv', index=False)


import pandas as pd
import json

# Load data from Excel
df = pd.read_excel(r"C:\Users\Vishwa\Desktop\GUVI captone\CAR\jaipur_cars.xlsx")

# Function to extract car detail
def extract_car_detail(detail):
    return json.loads(detail.replace("'", '"').replace('None', 'null'))

# Apply car detail extraction
df['new_car_detail'] = df['new_car_detail'].apply(extract_car_detail)
df_car_detail = pd.DataFrame(df['new_car_detail'].tolist())

# Apply car overview extraction
df['new_car_overview'] = df['new_car_overview'].apply(car_overview_dict_creator)
df_car_overview = pd.DataFrame(df['new_car_overview'].tolist())

# Apply car features extraction
df['new_car_feature'] = df['new_car_feature'].apply(car_feature_dict_creator)
feature_df = pd.json_normalize(df['new_car_feature']).fillna(0).astype(int)

# Apply car specs extraction
df['new_car_specs'] = df['new_car_specs'].apply(car_spec_dict_creator)
df_car_specs = pd.DataFrame(df['new_car_specs'].tolist())

# Combine all dataframes
df_combined = pd.concat([df_car_detail, df_car_overview, feature_df, df_car_specs], axis=1)

# Add city column and save to CSV
df_combined['city'] = 'Jaipur'

df_combined.to_csv('jaipur_cars.csv', index=False)


import pandas as pd
import json

# Load data from Excel
df = pd.read_excel(r"C:\Users\Vishwa\Desktop\GUVI captone\CAR\kolkata_cars.xlsx")

# Function to extract car detail
def extract_car_detail(detail):
    return json.loads(detail.replace("'", '"').replace('None', 'null'))

# Apply car detail extraction
df['new_car_detail'] = df['new_car_detail'].apply(extract_car_detail)
df_car_detail = pd.DataFrame(df['new_car_detail'].tolist())

# Apply car overview extraction
df['new_car_overview'] = df['new_car_overview'].apply(car_overview_dict_creator)
df_car_overview = pd.DataFrame(df['new_car_overview'].tolist())

# Apply car features extraction
df['new_car_feature'] = df['new_car_feature'].apply(car_feature_dict_creator)
feature_df = pd.json_normalize(df['new_car_feature']).fillna(0).astype(int)

# Apply car specs extraction
df['new_car_specs'] = df['new_car_specs'].apply(car_spec_dict_creator)
df_car_specs = pd.DataFrame(df['new_car_specs'].tolist())

# Combine all dataframes
df_combined = pd.concat([df_car_detail, df_car_overview, feature_df, df_car_specs], axis=1)

# Add city column and save to CSV
df_combined['city'] = 'Kolkata'

df_combined.to_csv('kolkata_cars.csv', index=False)


import pandas as pd
import json

# Load data from Excel
df = pd.read_excel(r"C:\Users\Vishwa\Desktop\GUVI captone\CAR\delhi_cars.xlsx")

# Function to extract car detail
def extract_car_detail(detail):
    return json.loads(detail.replace("'", '"').replace('None', 'null'))

# Apply car detail extraction
df['new_car_detail'] = df['new_car_detail'].apply(extract_car_detail)
df_car_detail = pd.DataFrame(df['new_car_detail'].tolist())

# Apply car overview extraction
df['new_car_overview'] = df['new_car_overview'].apply(car_overview_dict_creator)
df_car_overview = pd.DataFrame(df['new_car_overview'].tolist())

# Apply car features extraction
df['new_car_feature'] = df['new_car_feature'].apply(car_feature_dict_creator)
feature_df = pd.json_normalize(df['new_car_feature']).fillna(0).astype(int)

# Apply car specs extraction
df['new_car_specs'] = df['new_car_specs'].apply(car_spec_dict_creator)
df_car_specs = pd.DataFrame(df['new_car_specs'].tolist())

# Combine all dataframes
df_combined = pd.concat([df_car_detail, df_car_overview, feature_df, df_car_specs], axis=1)

# Add city column and save to CSV
df_combined['city'] = 'Delhi'

df_combined.to_csv('delhi_cars.csv', index=False)


import pandas as pd
import json

# Load data from Excel
df = pd.read_excel(r"C:\Users\Vishwa\Desktop\GUVI captone\CAR\hyderabad_cars.xlsx")

# Function to extract car detail
def extract_car_detail(detail):
    return json.loads(detail.replace("'", '"').replace('None', 'null'))

# Apply car detail extraction
df['new_car_detail'] = df['new_car_detail'].apply(extract_car_detail)
df_car_detail = pd.DataFrame(df['new_car_detail'].tolist())

# Apply car overview extraction
df['new_car_overview'] = df['new_car_overview'].apply(car_overview_dict_creator)
df_car_overview = pd.DataFrame(df['new_car_overview'].tolist())

# Apply car features extraction
df['new_car_feature'] = df['new_car_feature'].apply(car_feature_dict_creator)
feature_df = pd.json_normalize(df['new_car_feature']).fillna(0).astype(int)

# Apply car specs extraction
df['new_car_specs'] = df['new_car_specs'].apply(car_spec_dict_creator)
df_car_specs = pd.DataFrame(df['new_car_specs'].tolist())

# Combine all dataframes
df_combined = pd.concat([df_car_detail, df_car_overview, feature_df, df_car_specs], axis=1)

# Add city column and save to CSV
df_combined['city'] = 'Hyderabad'

df_combined.to_csv('hyderabad_cars.csv', index=False)


import pandas as pd

# List of CSV file paths
csv_files = [
    'Bangalore_cars.csv',
    'chennai_cars.csv',
    'jaipur_cars.csv',
    'delhi_cars.csv',
    'kolkata_cars.csv',
    'hyderabad_cars.csv',
    
   
]

# Load and concatenate all CSV files
df_combined = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)

# Save the combined DataFrame to a new CSV file
output_path = 'all_cities_cars_concatenated.csv'
df_combined.to_csv(output_path, index=False)

print(f"Combined CSV saved to: {output_path}")

Combined CSV saved to: all_cities_cars_concatenated.csv


import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("all_cities_cars_concatenated.csv")

# Define unrelated values
unrelated_Insurance_Validity = ['Petrol', 'Diesel', '1', '2']
unrelated_Mileage = ['20.88 km/kg', '31.59 km/kg', '26.49 km/kg', '35.6 km/kg', '28 km/kg', '30.48 km/kg', '26.08 km/kg', '31.12 km/kg', '18.9 km/kg', '26.11 km/kg', '26.6 km/kg', '30.47 km/kg', '21.1 km/kg']
unrelated_Torque = [25.1, 35.7, 11, 20.4, 25, 7.8, 10.4, 32.6, 24, 33, 50, 13, 16, 19, 20, 22.6, 8.5, 13.5, 12.9, 23.6, 28.3, 12, 11.8, 16.1, '110 (11.2)', '210 / 1900', '11.4 kgm at 4,000 rpm', '14.9 KGM at 3000 RPM', '22.4 kgm at 1750-2750rpm', '13.1 kgm', '4.8 kgm', '25 KGM', '14.9', '12.7', '9.4', '6.1 kgm']
unrelated_Value_Configuration = ['16 Modules 48 Cells', '23 Modules 69 Cells']
unrelated_Fuel_Supply_System = ['3 Phase AC Induction Motors', 'Electric', 'Distribution Type Fuel Injection']
unrelated_Compression_Ratio = ['73.5 mm x 73.5 mm', '81 x 87.3 mm', '12+-0.3', '12.0 ±0.3', '12.0+-.03', '15.5', '16.5', '18.5', '22.2:1', '17.9', '12.5:1', ':1', '10:01', '21:01', '16:01', '9:01', '10:01', '10.0', '11.0', '11.0:1', '10.5']
unrelated_Acceleration = ['44.04m']
unrelated_Rear_Brake_Type = ['228.6 mm dia', 'drums on rear wheels']

# Function to replace unrelated values with NaN
def replace_unrelated_with_nan(series, unrelated_values):
    return series.apply(lambda x: np.nan if x in unrelated_values else x)

# Replace unrelated values with NaN in relevant columns
df['Insurance Validity'] = replace_unrelated_with_nan(df['Insurance Validity'], unrelated_Insurance_Validity)
df['Mileage'] = replace_unrelated_with_nan(df['Mileage'], unrelated_Mileage)
df['Torque'] = replace_unrelated_with_nan(df['Torque'], unrelated_Torque)
df['Value Configuration'] = replace_unrelated_with_nan(df['Value Configuration'], unrelated_Value_Configuration)
df['Fuel Suppy System'] = replace_unrelated_with_nan(df['Fuel Suppy System'], unrelated_Fuel_Supply_System)
df['Compression Ratio'] = replace_unrelated_with_nan(df['Compression Ratio'], unrelated_Compression_Ratio)
df['Acceleration'] = replace_unrelated_with_nan(df['Acceleration'], unrelated_Acceleration)
df['Rear Brake Type'] = replace_unrelated_with_nan(df['Rear Brake Type'], unrelated_Rear_Brake_Type)

# Standardize the 'Super Charger' column
df['Super Charger'] = df['Super Charger'].str.lower()  # Convert to lowercase
df['Super Charger'] = df['Super Charger'].replace({'yes': 'Yes', 'no': 'No'})  # Standardize values

# Standardize the 'Turbo Charger' column
df['Turbo Charger'] = df['Turbo Charger'].str.lower()  # Convert to lowercase
df['Turbo Charger'] = df['Turbo Charger'].replace({'yes': 'Yes', 'no': 'No'})  # Replace ambiguous values

def clean_kerb_weight(value):
    # Remove any non-numeric characters except for '-' (used in ranges)
    cleaned_value = ''.join([c for c in value if c.isdigit() or c == '-'])
    
    if '-' in cleaned_value and cleaned_value.count('-') == 1:
        # If there's a range, take the average of the two values
        min_val, max_val = cleaned_value.split('-')
        if min_val.isdigit() and max_val.isdigit():
            return (int(min_val) + int(max_val)) / 2
        else:
            return np.nan  # Return NaN if the range is invalid
    elif cleaned_value.isdigit():
        # Return the numeric value as an integer
        return int(cleaned_value)
    else:
        return np.nan  # Return NaN if the cleaned value is not valid

# Apply the cleaning function to the 'Kerb Weight' column
df['Kerb Weight'] = df['Kerb Weight'].apply(lambda x: clean_kerb_weight(str(x)))

# Display cleaned unique values
unique_values = df['Kerb Weight'].unique()

# Save the cleaned DataFrame
df.to_csv('all_cities_cars_cleaned.csv', index=False)


import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("all_cities_cars_cleaned.csv")

# Define patterns for removing units
columns_with_units = {
    
    'Seats': r'(\d+)',
    'Engine Displacement': r'(\d+)',
    'Mileage': r'([\d.]+)\s*kmpl',
    'Max Power': r'([\d.]+)',
    'Torque': r'([\d.]+)',
    'BoreXStroke': r'(\d+)\s*X\s*(\d+)',
    'Length': r'(\d+)',
    'Width': r'(\d+)',
    'Height': r'(\d+)',
    'Turning Radius': r'([\d.]+)\s*metres',
    'Wheel Base': r'(\d+)',
    'Front Tread': r'(\d+)',
    'Rear Tread': r'(\d+)',
    'Kerb Weight': r'(\d+)',
    'Gross Weight': r'(\d+)',
    'Gear Box': r'(\d+)',
    'Top Speed': r'(\d+)',
    'Acceleration': r'([\d.]+)\s*Seconds',
    'Cargo Volume': r'(\d+)',
    'Ground Clearance Unladen': r'(\d+)',
    'Wheel Size': r'R(\d+)',
    'Alloy Wheel Size': r'R(\d+)',
    'km': r'(\d+)'  # Note: This pattern is generic and may need adjustment
}

# Function to remove units from column values
def remove_units(series, pattern):
    # Convert the series to string, apply the regex, and return the cleaned data
    return series.astype(str).str.replace(pattern, r'\1', regex=True).replace('nan', np.nan)

# Apply the function to clean specified columns
for column, pattern in columns_with_units.items():
    if column in df.columns:
        df[column] = remove_units(df[column], pattern)

# Save the cleaned DataFrame
df.to_csv('all_cities_cars_cleaned_1.csv', index=False)


import pandas as pd
import re

# Load the dataset
df = pd.read_csv("all_cities_cars_cleaned.csv")

# Function to clean units and commas from a series
def clean_values(series, unit_patterns):
    # Convert the series to string to ensure .str methods can be applied
    cleaned_series = series.astype(str)
    # Remove commas
    cleaned_series = cleaned_series.str.replace(',', '', regex=True)
    # Apply all unit patterns
    for pattern in unit_patterns:
        cleaned_series = cleaned_series.str.replace(pattern, '', regex=True).str.strip()
    return cleaned_series

# Define patterns to remove
unit_patterns = [
    
    r'\s*kg',  # Remove weight unit
    r'\s*kgm',  # Remove torque unit
    r'\s*cc',  # Remove engine displacement unit
    r'\s*kmpl',  # Remove mileage unit
    r'\s*bhp',  # Remove power unit
    r'\s*Nm',  # Remove torque unit
    r'\s*mm',  # Remove dimensions unit
    r'\s*metres',  # Remove turning radius unit
    r'\s*Seconds',  # Remove acceleration unit
    r'\s*litres',  # Remove cargo volume unit
    r'\s*R\d+',  # Remove wheel size prefix
    r'\s*X\s*\d+',  # Remove bore x stroke separator
    r'\s*km'  # Remove km unit
]

# List of columns to clean
columns_to_clean = [
    'Seats', 'Engine Displacement', 'Mileage', 'Max Power', 'Torque',
    'BoreX Stroke', 'Length', 'Width', 'Height', 'Turning Radius', 'Wheel Base',
    'Front Tread', 'Rear Tread', 'Kerb Weight', 'Gross Weight', 'Gear Box',
    'Top Speed', 'Acceleration', 'Cargo Volume', 'Ground Clearance Unladen',
    'Wheel Size', 'Alloy Wheel Size', 'km'  
]

# Apply the function to clean specified columns
for column in columns_to_clean:
    if column in df.columns:
        df[column] = clean_values(df[column], unit_patterns)

# Save the cleaned DataFrame
df.to_csv('all_cities_cars_cleaned_1.csv', index=False)


import pandas as pd
import re

# Load the dataset
df = pd.read_csv("all_cities_cars_cleaned_1.csv", low_memory=False)

# Function to clean specific units and symbols
def clean_units(series, patterns):
    # Convert to string, then apply the regex replacements
    cleaned_series = series.astype(str)
    for pattern in patterns:
        cleaned_series = cleaned_series.str.replace(pattern, '', regex=True).str.strip()
    # Convert 'nan' strings back to actual NaN values
    cleaned_series = cleaned_series.replace('nan', pd.NA)
    return cleaned_series

# Define patterns to remove units and symbols
unit_patterns = {
    'Max Power': [r'bhp', r'@[\d]+rpm'],
    'Torque': [r'Nm', r'nm'],
    'Seats': [r'Seats'],
    'Cargo Volume': [r'-litres', r'-'],
    'Top Speed': [r'Kmph', r'/hr'],
    'Turning Radius': [r'meters?', r'metres?'],
    'Drive Type': [r'X\d+'],  # If you want to keep it as it is (like 4X2), do not apply changes here
    'Gear Box': [r'\s*Speed', r'-Speed'],
    'Gross Weight': [r'Kg'],
    'Kerb Weight': [r'Kg'],
}

# Apply cleaning for each specified column
for column, patterns in unit_patterns.items():
    if column in df.columns:
        df[column] = clean_units(df[column], patterns)

# Save the cleaned DataFrame
df.to_csv('all_cities_cars_cleaned_2.csv', index=False)


import pandas as pd
import re

# Load the dataset
df = pd.read_csv("all_cities_cars_cleaned_2.csv", low_memory=False)

# Function to clean specific units and symbols
def clean_units(series, patterns):
    # Convert the series to string, ensuring NaNs are handled
    cleaned_series = series.astype(str).replace('nan', '')
    for pattern in patterns:
        cleaned_series = cleaned_series.str.replace(pattern, '', regex=True).str.strip()
    return cleaned_series

# Define patterns to remove units and symbols
unit_patterns = {
    'Max Power': [r'b?hp', r'@[\d]+rpm', r'PS@rpm', r'@ \d+', r'(\(.*\))'],
    'Torque': [r'nm?', r'Nm', r'kgm', r'at[\s\d]+rpm', r'(\(.*\))'],
    'Cargo Volumn': [r'-litres', r'-', r'litres', r'liters', r'Litres', r'ltrs', r'itre', r'iters', r'lits', r'litrs', r'lts', r'trs', r'iter', r'it',r'-litres',r'L',r'l'],
    'Top Speed': [r'Kmph', r'/hr', r'ph'],
    'Turning Radius': [r'meters?', r'metres?', r'(\(.*\))', r'Meters', r'm'],
    'Gear Box': [r'\s*Speed', r'-Speed', r'G-DCT', r'-', r'IMT', r'CVT', 'speed DCT', 'IVT', 'speed', 'iMT'],
    'Gross Weight': [r'Kg'],
    'Kerb Weight': [r'Kg', r's'],
    'Acceleration': [r'seconds?', r'sec'],
}

# Apply cleaning for each specified column
for column, patterns in unit_patterns.items():
    if column in df.columns:
        df[column] = clean_units(df[column], patterns)

# Save the cleaned DataFrame
df.to_csv('all_cities_cars_cleaned_3.csv', index=False)

# Display the cleaned DataFrame
print(df.head())

   it      ft         bt      km transmission  ownerNo      owner      oem  \
0   0  Petrol  Hatchback  120000       Manual        3  3rd Owner   Maruti   
1   0  Petrol        SUV   32706       Manual        2  2nd Owner     Ford   
2   0  Petrol  Hatchback   11949       Manual        1  1st Owner     Tata   
3   0  Petrol      Sedan   17794       Manual        1  1st Owner  Hyundai   
4   0  Diesel        SUV   60000       Manual        1  1st Owner   Maruti   

                model  modelYear  centralVariantId               variantName  \
0      Maruti Celerio       2015              3979                       VXI   
1       Ford Ecosport       2018              6087  1.5 Petrol Titanium BSIV   
2          Tata Tiago       2018              2983           1.2 Revotron XZ   
3       Hyundai Xcent       2014              1867        1.2 Kappa S Option   
4  Maruti SX4 S Cross       2015              4277             DDiS 200 Zeta   

         price priceActual  priceSaving  priceFixedText  \
0     ₹ 4 Lakh         NaN          NaN             NaN   
1  ₹ 8.11 Lakh         NaN          NaN             NaN   
2  ₹ 5.85 Lakh         NaN          NaN             NaN   
3  ₹ 4.62 Lakh         NaN          NaN             NaN   
4  ₹ 7.90 Lakh         NaN          NaN             NaN   

                                        trendingText Registration Year  \
0  {'imgUrl': 'https://stimg.cardekho.com/used-ca...              2015   
1  {'imgUrl': 'https://stimg.cardekho.com/used-ca...          Feb 2018   
2  {'imgUrl': 'https://stimg.cardekho.com/used-ca...         Sept 2018   
3  {'imgUrl': 'https://stimg.cardekho.com/used-ca...          Dec 2014   
4  {'imgUrl': 'https://stimg.cardekho.com/used-ca...              2015   

      Insurance Validity Fuel Type  Seats    Kms Driven   RTO     Ownership  \
0  Third Party insurance    Petrol    5.0  1,20,000 Kms  KA51   Third Owner   
1          Comprehensive    Petrol    5.0    32,706 Kms  KA05  Second Owner   
2          Comprehensive    Petrol    5.0    11,949 Kms  KA03   First Owner   
3          Comprehensive    Petrol    5.0    17,794 Kms  KA53   First Owner   
4  Third Party insurance    Diesel    5.0    60,000 Kms  KA04   First Owner   

   Engine Displacement Transmission  Year of Manufacture  Power Steering  \
0                998.0       Manual               2015.0               1   
1               1497.0       Manual               2018.0               1   
2               1199.0       Manual               2018.0               1   
3               1197.0       Manual               2014.0               1   
4               1248.0       Manual               2015.0               1   

   Power Windows Front  Air Conditioner  Heater  Adjustable Head Lights  \
0                    1                1       1                       1   
1                    1                1       1                       1   
2                    1                1       1                       1   
3                    1                1       1                       1   
4                    1                1       1                       1   

   Manually Adjustable Exterior Rear View Mirror  Centeral Locking  \
0                                              1                 1   
1                                              0                 1   
2                                              0                 1   
3                                              0                 1   
4                                              0                 1   

   Child Safety Locks  Power Windows Rear  Remote Trunk Opener  \
0                   1                   1                    1   
1                   1                   1                    1   
2                   1                   1                    1   
3                   1                   1                    1   
4                   1                   1                    1   

   Remote Fuel Lid Opener  Low Fuel Warning Light  Accessory Power Outlet  \
0                       1                       1                       1   
1                       1                       1                       1   
2                       1                       1                       1   
3                       0                       1                       1   
4                       1                       1                       1   

   Vanity Mirror  Rear Seat Headrest  Cup Holders Front  Digital Odometer  \
0              1                   1                  1                 1   
1              1                   1                  1                 1   
2              1                   1                  1                 1   
3              1                   1                  1                 1   
4              1                   1                  1                 1   

   Electronic Multi Tripmeter  Fabric Upholstery  Glove Compartment  \
0                           1                  1                  1   
1                           1                  1                  1   
2                           1                  1                  1   
3                           1                  1                  1   
4                           1                  1                  1   

   Digital Clock  Wheel Covers  Power Antenna  Chrome Grille  \
0              1             1              1              1   
1              1             0              0              1   
2              1             1              1              1   
3              1             0              1              1   
4              1             0              1              1   

   Day Night Rear View Mirror  Passenger Side Rear View Mirror  \
0                           1                                1   
1                           0                                1   
2                           0                                1   
3                           1                                1   
4                           0                                1   

   Halogen Headlamps  Rear Seat Belts  Door Ajar Warning  Side Impact Beams  \
0                  1                1                  1                  1   
1                  1                1                  1                  1   
2                  1                1                  1                  1   
3                  1                1                  1                  1   
4                  1                1                  1                  1   

   Front Impact Beams  Adjustable Seats  Centrally Mounted Fuel Tank  \
0                   1                 1                            1   
1                   1                 1                            1   
2                   1                 1                            1   
3                   1                 1                            1   
4                   1                 1                            1   

   Engine Immobilizer  Anti Theft Device  Fog Lights Front  \
0                   1                  1                 0   
1                   1                  1                 1   
2                   1                  1                 1   
3                   1                  1                 1   
4                   1                  1                 1   

   Anti Lock Braking System  Cd Player  Trunk Light  \
0                         0          0            0   
1                         1          1            1   
2                         1          1            1   
3                         1          1            1   
4                         1          0            1   

   Multifunction Steering Wheel  Navigation System  Smart Access Card Entry  \
0                             0                  0                        0   
1                             1                  1                        1   
2                             1                  1                        0   
3                             1                  0                        0   
4                             1                  1                        0   

   Engine Start Stop Button  Gear Shift Indicator  Luggage Hook And Net  \
0                         0                     0                     0   
1                         1                     1                     1   
2                         0                     0                     0   
3                         0                     0                     0   
4                         1                     1                     0   

   Adjustable Steering  Tachometer  Leather Steering Wheel  \
0                    0           0                       0   
1                    1           1                       1   
2                    1           1                       0   
3                    1           1                       0   
4                    1           1                       0   

   Outside Temperature Display  Height Adjustable Driver Seat  \
0                            0                              0   
1                            1                              1   
2                            1                              1   
3                            0                              1   
4                            1                              1   

   Power Adjustable Exterior Rear View Mirror  \
0                                           0   
1                                           1   
2                                           1   
3                                           1   
4                                           1   

   Electric Folding Rear View Mirror  Rear Window Wiper  Rear Window Washer  \
0                                  0                  0                   0   
1                                  1                  1                   1   
2                                  0                  1                   1   
3                                  1                  0                   0   
4                                  1                  1                   1   

   Rear Window Defogger  Alloy Wheels  Integrated Antenna  \
0                     0             0                   0   
1                     1             1                   1   
2                     1             0                   0   
3                     1             1                   0   
4                     1             1                   0   

   Outside Rear View Mirror Turn Indicators  Roof Rail  Power Door Locks  \
0                                         0          0                 0   
1                                         1          1                 1   
2                                         1          0                 1   
3                                         1          0                 1   
4                                         1          1                 1   

   Driver Air Bag  Passenger Air Bag  Seat Belt Warning  Keyless Entry  \
0               0                  0                  0              0   
1               1                  1                  1              1   
2               1                  1                  1              0   
3               0                  0                  1              1   
4               1                  1                  1              1   

   Engine Check Warning  Crash Sensor  Ebd  Follow Me Home Headlamps  \
0                     0             0    0                         0   
1                     1             1    1                         1   
2                     1             1    1                         1   
3                     0             0    1                         0   
4                     1             1    1                         0   

   Rear Camera  Speed Sensing Auto Door Lock  \
0            0                             0   
1            1                             1   
2            0                             1   
3            0                             0   
4            1                             0   

   Pretensioners And Force Limiter Seatbelts  Impact Sensing Auto Door Lock  \
0                                          0                              0   
1                                          1                              1   
2                                          1                              0   
3                                          0                              0   
4                                          0                              0   

   No Of Airbags  Radio  Speakers Front  Speakers Rear  Integrated2Din Audio  \
0              0      0               0              0                     0   
1              1      1               1              1                     1   
2              0      1               1              1                     1   
3              0      1               1              1                     1   
4              0      1               1              1                     1   

   Usb Auxiliary Input  Bluetooth  Touch Screen  Number Of Speaker  \
0                    0          0             0                  0   
1                    1          1             1                  1   
2                    1          1             0                  1   
3                    1          1             0                  0   
4                    1          1             1                  0   

   Glove Box Cooling  Driving Experience Control Eco  Tinted Glass  \
0                  0                               0             0   
1                  0                               0             0   
2                  1                               1             1   
3                  1                               0             0   
4                  0                               0             1   

   Rear Spoiler  Chrome Garnish  Vehicle Stability Control System  \
0             0               0                                 0   
1             0               0                                 0   
2             1               1                                 1   
3             0               1                                 0   
4             0               0                                 0   

   Rear Reading Lamp  Rear Seat Centre Arm Rest  Cup Holders Rear  \
0                  0                          0                 0   
1                  0                          0                 0   
2                  0                          0                 0   
3                  1                          1                 1   
4                  0                          1                 1   

   Rear ACVents  Air Quality Control  Height Adjustable Front Seat Belts  \
0             0                    0                                   0   
1             0                    0                                   0   
2             0                    0                                   0   
3             1                    0                                   0   
4             0                    1                                   1   

   Cruise Control  Voice Control  Audio System Remote Control  Leather Seats  \
0               0              0                            0              0   
1               0              0                            0              0   
2               0              0                            0              0   
3               0              0                            0              0   
4               1              1                            1              0   

   Fog Lights Rear  Traction Control  Seat Lumbar Support  Battery Saver  \
0                0                 0                    0              0   
1                0                 0                    0              0   
2                0                 0                    0              0   
3                0                 0                    0              0   
4                0                 0                    0              0   

   Lane Change Indicator  Sun Roof  Automatic Driving Lights  \
0                      0         0                         0   
1                      0         0                         0   
2                      0         0                         0   
3                      0         0                         0   
4                      0         0                         0   

   Anti Theft Alarm  Automatic Head Lamps  Isofix Child Seat Mounts  \
0                 0                     0                         0   
1                 0                     0                         0   
2                 0                     0                         0   
3                 0                     0                         0   
4                 0                     0                         0   

   Hill Assist  Tailgate Ajar  Brake Assist  Steering Wheel Gearshift Paddles  \
0            0              0             0                                 0   
1            0              0             0                                 0   
2            0              0             0                                 0   
3            0              0             0                                 0   
4            0              0             0                                 0   

   LEDTaillights  Cigarette Lighter  Rain Sensing Wiper  Drive Modes  \
0              0                  0                   0            0   
1              0                  0                   0            0   
2              0                  0                   0            0   
3              0                  0                   0            0   
4              0                  0                   0            0   

   Active Noise Cancellation  Adjustable Headrest  Hands Free Tailgate  \
0                          0                    0                    0   
1                          0                    0                    0   
2                          0                    0                    0   
3                          0                    0                    0   
4                          0                    0                    0   

   Dual Tone Dashboard  Leather Wrap Gear Shift Selector  \
0                    0                                 0   
1                    0                                 0   
2                    0                                 0   
3                    0                                 0   
4                    0                                 0   

   Dual Tone Body Colour  LEDDRLs  LEDHeadlights  Cornering Headlamps  \
0                      0        0              0                    0   
1                      0        0              0                    0   
2                      0        0              0                    0   
3                      0        0              0                    0   
4                      0        0              0                    0   

   Cornering Foglamps  Side Air Bag Front  Side Air Bag Rear  \
0                   0                   0                  0   
1                   0                   0                  0   
2                   0                   0                  0   
3                   0                   0                  0   
4                   0                   0                  0   

   Tyre Pressure Monitor  Clutch Lock  Anti Pinch Power Windows  Knee Airbags  \
0                      0            0                         0             0   
1                      0            0                         0             0   
2                      0            0                         0             0   
3                      0            0                         0             0   
4                      0            0                         0             0   

   Apple Car Play  Android Auto  Mirror Link  Wireless Phone Charging  \
0               0             0            0                        0   
1               0             0            0                        0   
2               0             0            0                        0   
3               0             0            0                        0   
4               0             0            0                        0   

   Compass  Moon Roof  Projector Headlamps  Speed Alert  \
0        0          0                    0            0   
1        0          0                    0            0   
2        0          0                    0            0   
3        0          0                    0            0   
4        0          0                    0            0   

   Eletronic Stability Control  Touch Screen Size  Xenon Headlamps  \
0                            0                  0                0   
1                            0                  0                0   
2                            0                  0                0   
3                            0                  0                0   
4                            0                  0                0   

   Cd Changer  Power Boot  Rear Folding Table  Smoke Headlamps  Dvd Player  \
0           0           0                   0                0           0   
1           0           0                   0                0           0   
2           0           0                   0                0           0   
3           0           0                   0                0           0   
4           0           0                   0                0           0   

   Internal Storage  Rear Entertainment System  Remote Engine Start Stop  \
0                 0                          0                         0   
1                 0                          0                         0   
2                 0                          0                         0   
3                 0                          0                         0   
4                 0                          0                         0   

   Ventilated Seats  LEDFog Lamps  View360Camera  Geo Fence Alert  \
0                 0             0              0                0   
1                 0             0              0                0   
2                 0             0              0                0   
3                 0             0              0                0   
4                 0             0              0                0   

   Steering Mounted Tripmeter  Remote Climate Control  \
0                           0                       0   
1                           0                       0   
2                           0                       0   
3                           0                       0   
4                           0                       0   

   Remote Horn Light Control  Heated Wing Mirror  Side Stepper  \
0                          0                   0             0   
1                          0                   0             0   
2                          0                   0             0   
3                          0                   0             0   
4                          0                   0             0   

   Blind Spot Monitor  Hill Descent Control  Heads Up Display  \
0                   0                     0                 0   
1                   0                     0                 0   
2                   0                     0                 0   
3                   0                     0                 0   
4                   0                     0                 0   

   Sos Emergency Assistance  Cassette Player  Find My Car Location  \
0                         0                0                     0   
1                         0                0                     0   
2                         0                0                     0   
3                         0                0                     0   
4                         0                0                     0   

   Wifi Connectivity  Headlamp Washers  Real Time Vehicle Tracking  \
0                  0               0.0                           0   
1                  0               0.0                           0   
2                  0               0.0                           0   
3                  0               0.0                           0   
4                  0               0.0                           0   

   Roof Carrier  Smart Key Band  Lane Watch Camera  Removable Convertible Top  \
0             0             0.0                  0                          0   
1             0             0.0                  0                          0   
2             0             0.0                  0                          0   
3             0             0.0                  0                          0   
4             0             0.0                  0                          0   

   Power Folding3rd Row Seat  Mileage   Engine Max Power  Torque  Seats.1  \
0                        0.0    23.10   998 CC     67.04      90      5.0   
1                        0.0    17.00  1497 CC    121.31     150      5.0   
2                        0.0    23.84  1199 CC        84     114      5.0   
3                        0.0    19.10  1197 CC     81.86  113.75      5.0   
4                        0.0    23.65  1248 CC      88.5     200      5.0   

    Color               Engine Type  Displacement        Max Torque  \
0   White               K10B Engine         998.0      90Nm@3500rpm   
1   White      Ti-VCT Petrol Engine        1497.0     150Nm@4500rpm   
2     Red           Revotron Engine        1199.0     114Nm@3500rpm   
3  Others  Kappa VTVT Petrol Engine        1197.0  113.75Nm@4000rpm   
4    Gray    DDiS 200 Diesel Engine        1248.0     200Nm@1750rpm   

   No of Cylinder  Values per Cylinder Value Configuration Fuel Suppy System  \
0             3.0                  4.0                DOHC              MPFi   
1             3.0                  4.0                DOHC  Direct Injection   
2             3.0                  4.0                DOHC              MPFi   
3             4.0                  4.0                DOHC  Direct Injection   
4             4.0                  4.0                DOHC               NaN   

  BoreX Stroke Compression Ratio Turbo Charger Super Charger  Length   Width  \
0           73               NaN            No            No  3715.0  1635.0   
1         79.5               NaN            No            No  3998.0  1765.0   
2         77.8            10.8:1            No            No  3746.0  1647.0   
3          NaN               NaN            No            No  3995.0  1660.0   
4    69.6 x 82               NaN           Yes            No  4300.0  1785.0   

  Height Wheel Base  Front Tread Rear Tread Kerb Weight Gross Weight Gear Box  \
0   1565       2425       1420.0       1410       835.0         1250        5   
1   1647       2519          NaN        NaN      1242.0         1660        5   
2   1535       2400       1400.0       1420      1012.0                     5   
3   1520       2425       1479.0       1493      1180.0                     5   
4   1595       2600          NaN        NaN      1230.0         1670        5   

  Drive Type  Seating Capacity Steering Type Turning Radius Front Brake Type  \
0        FWD               5.0         Power            4.7  Ventilated Disc   
1        FWD               5.0         Power            5.3  Ventilated Disc   
2        FWD               5.0         Power            4.9             Disc   
3        FWD               5.0         Power            4.7            Disc    
4        FWD               5.0         Power            5.2  Ventilated Disc   

  Rear Brake Type Top Speed Acceleration         Tyre Type  No Door Numbers  \
0            Drum       150        15.05  Tubeless, Radial              5.0   
1            Drum                          Tubeless,Radial              4.0   
2            Drum       150         14.3          Tubeless              5.0   
3            Drum       172         14.2   Tubeless,Radial              4.0   
4      Solid Disc       190           12   Tubeless,Radial              5.0   

  Cargo Volumn  Wheel Size  Alloy Wheel Size  Ground Clearance Unladen  \
0          235         NaN               NaN                       NaN   
1          352        16.0              16.0                       NaN   
2          242        14.0              14.0                       NaN   
3          407        14.0              14.0                       NaN   
4          353        16.0              16.0                       NaN   

        city  
0  Bangalore  
1  Bangalore  
2  Bangalore  
3  Bangalore  
4  Bangalore  

[44]
import pandas as pd
import numpy as np

# Read the dataset
df = pd.read_csv("all_cities_cars_cleaned_3.csv")

# Function to clean the 'Kerb Weight' column
def clean_kerb_weight(value):
    # Remove any non-numeric characters except for '-' (used in ranges)
    cleaned_value = ''.join([c for c in value if c.isdigit() or c == '-'])
    
    if '-' in cleaned_value and cleaned_value.count('-') == 1:
        # If there's a range, take the average of the two values
        min_val, max_val = cleaned_value.split('-')
        if min_val.isdigit() and max_val.isdigit():
            return (int(min_val) + int(max_val)) / 2
        else:
            return np.nan  # Return NaN if the range is invalid
    elif cleaned_value.isdigit():
        # Return the numeric value as an integer
        return int(cleaned_value)
    else:
        return np.nan  # Return NaN if the cleaned value is not valid

# Apply the cleaning function to the 'Kerb Weight' column
df['Kerb Weight'] = df['Kerb Weight'].apply(lambda x: clean_kerb_weight(str(x)))

# Display cleaned unique values
unique_values = df['Kerb Weight'].unique()
print(unique_values)
df.to_csv('all_cars_cleaned.csv', index=False)
[ 8350. 12420. 10120. 11800. 12300. 15510. 10700. 14400. 11050.  8700.
 12000. 10660. 19000. 15620. 16750. 11200. 13150. 10490. 16000.  8900.
 22000. 10500.  8450. 15850. 15950. 19400. 16500. 11400.  8850. 11700.
 16550. 19550. 13750. 15150.  8800. 13290. 17350.  7620. 19900. 12500.
 15350. 19800.  7050. 25350. 18250. 10600. 23450. 19700.  7500. 13050.
 10950.  8150. 12060. 12250. 13200. 17000.  9600.  8500. 17200. 13600.
 13760.  9800. 10150. 12600. 13800. 11920. 10250. 10400. 11350. 18650.
  8600.  7300. 16520. 18350. 13450. 18200.  9250.  9225.  7600. 10860.
  9100. 11790. 15250. 17300.  9000. 13000. 14650. 20200. 13500.  8400.
 14450. 15800. 16080. 11000. 18300.  7550. 10200. 18790. 10850.  8550.
 16700.  9350. 20100.  9470.  9300. 20600. 14550. 15370. 23600. 17450.
 12380. 19540. 13900. 12850. 10800. 11090. 12740. 11580. 13950. 18850.
  9500. 13250. 11900. 13400. 15300. 12400. 12960. 10420. 19600. 10440.
 12550.  9850.  8975. 12350. 11070. 11150. 12200. 10610. 18400.  8250.
 11500. 16400. 12100. 11030. 13040. 18000. 16800. 10300. 11750. 17800.
 10720. 10650. 14900. 12625. 17700. 12050.  8950. 14600. 14500. 10390.
  7450.  7840. 16410.  9700. 12750. 11600. 11250.  9400. 14250. 12900.
 21950.  8650. 16350. 13300. 15400. 18900. 10450. 16600. 17850. 11380.
 11650. 12280. 21520. 12800. 18800. 10550. 11950. 11060. 12880.  9375.
 10840.  8100. 11550. 14700. 10880.  7555. 17250.  8200. 14030. 19150.
 10100. 10640.  7700.  7790.  8375.  6990. 16200.  9900. 20140.  8775.
 17150.  9150. 17100. 10485. 15200. 14950. 12770. 11300. 17750. 12080.
 16300. 10140.    nan 13100. 11450. 10530. 20950. 12810. 21600. 21750.
 15500. 11225. 11850. 15550. 15700. 12520. 14300. 12010. 12700. 10900.
  7850.  9820. 14390. 17030. 10360. 14000. 17900. 11840. 15900.  9725.
 14875.  9950. 10350. 15100.  7650. 20450. 11210.  9390. 18450. 20000.
 17950. 16250.  7200. 15430.  7740. 12525. 12650. 23700. 17600. 18600.
 10590.  6000.  9450. 11540. 10050. 13510. 11125. 15670. 17400. 15980.
 17550. 14850. 13685. 11775.  7270. 17500.  7100. 11875. 10460. 10425.
  8000. 13350. 11820. 17730.  6900. 10970. 18150. 15750. 15650. 22400.
 11425. 10920. 10480.  9200. 16100. 20400. 15450. 14750. 12580. 16150.
 11520. 16850. 21450. 10665. 25000. 22300. 13090. 11525. 21320.  7465.
 13550.  6250.  8300.  7570. 21150. 11100. 11730. 12460. 16900. 14150.
  9650. 11630.  9430. 15600. 22200. 11460.  8750. 12450. 11980. 23300.
 18550.  9050. 14050. 10690. 17610. 12330. 22800. 19950. 14680. 12980.
 10290. 18050. 10410.  8525. 21500. 25050.  9170. 19200. 12180. 16440.
  9240. 19450. 11420. 20300.  6500. 18160. 11870. 17960.  9210. 14200.
 29620. 13540. 10630.  9205.  8425. 15000. 17990. 10620. 23500. 16450.
 13120. 10580. 11370. 25150.  8225. 17050. 18700.  8420.  8820. 10735.
 12150. 17790.  6350. 15050. 18570. 10245. 10520. 11075. 18950. 10355.
 13020. 25500. 14040. 12780. 10750. 10875.  9420. 27500. 10675. 12680.
 17650. 20010. 16120. 11480. 22100. 16680. 14350. 10220. 16950.  6750.
 12120. 23760. 16650. 12340.  9130.  8460. 13850.  8050. 19650. 11470.
 21550. 13060. 17760. 12110. 11240. 13890.  7250.  9550.  9750. 24550.
 18710. 18510. 18500. 14100. 15470. 19050.  6650.  9930. 15790.  8540.
 12890. 13700. 12480. 14590. 16810.  9510. 13650. 20270. 21860. 19500.
 22275. 22700.  9075. 24600. 18750. 21840. 10870. 10295. 26000. 18660.
 21000. 10210. 17870. 21100. 25600. 22450. 11680. 16670. 19300. 24890.
 19250. 20640.  8470. 20800. 19940. 29000. 27000. 17290. 16280. 14970.
 14800. 10310. 18100. 16140. 10270. 10000. 12390. 11110. 12160. 19350.
 10575. 22350. 11530. 11675. 23100.  9925. 11040. 18740. 22500. 15610.
 18240. 12170. 12610. 15270. 12950.  6950. 12310. 12925. 11880. 10230.
 11610. 10330. 24400.  9280. 10075.  9980. 12320.  8860. 19100.  7220.
 18130. 21850. 10130. 17660. 26750. 15330. 10710. 16510. 12690. 24100.
 16050. 12040. 11020. 10930. 24250. 10225. 11310.]

C:\Users\Vishwa\AppData\Local\Temp\ipykernel_9164\837103721.py:5: DtypeWarning: Columns (203,222,232,236) have mixed types. Specify dtype option on import or set low_memory=False.
  df = pd.read_csv("all_cities_cars_cleaned_3.csv")

[51]
import pandas as pd
import numpy as np
import re

# Load the dataset
df = pd.read_csv("all_cities_cars_cleaned_3.csv")

# List of unrelated values
unrelated_drive_type = [4, '4x2', '2WD', '4WD', '2 WD', '4 WD', '4x4']
unrelated_cargo_volumn = ["347 (3rd Row Folded)", "385/1405", 260950]

# Function to replace unrelated values with NaN
def replace_unrelated_with_nan(series, unrelated_values):
    return series.apply(lambda x: np.nan if x in unrelated_values else x)

# Replace unrelated values with NaN in relevant columns
df['Cargo Volumn'] = replace_unrelated_with_nan(df['Cargo Volumn'], unrelated_cargo_volumn)
df['Drive Type'] = replace_unrelated_with_nan(df['Drive Type'], unrelated_drive_type)

# List of columns to drop
columns_to_drop = [
    'owner', 'trendingText', 'Registration Year', 'Fuel Type', 'Kms Driven',
    'Ownership', 'Transmission', 'Year of Manufacture', 'priceActual',
    'priceSaving', 'priceFixedText', 'Engine', 'Seats.1', 'Displacement',
    'Max Torque', 'Seating Capacity','BoreX Stroke','Compression Ratio',
    'Ground Clearance Unladen'
]

# Drop the specified columns
df = df.drop(columns=columns_to_drop, errors='ignore')

# Function to clean units and symbols from strings
def clean_units(series, patterns):
    cleaned_series = series.astype(str)  # Convert to string to avoid errors
    for pattern in patterns:
        cleaned_series = cleaned_series.str.replace(pattern, '', regex=True).str.strip()
    return cleaned_series

# Split mixed "Max Power" and "Torque" values if needed
def split_max_power_torque(row):
    if 'Max Power' in row and 'Torque' in row:
        max_power, torque = row['Max Power'], row['Torque']
        if pd.isnull(torque) and not pd.isnull(max_power):
            split_values = re.split(r',', max_power)
            if len(split_values) == 2:
                row['Max Power'] = split_values[0]
                row['Torque'] = split_values[1]
    return row

# Apply the function to each row
df = df.apply(split_max_power_torque, axis=1)

# Define patterns to clean "Max Power" and "Torque" columns
max_power_patterns = [r'b?hp', r'@[\d]+rpm', r'PS@rpm', r'@ \d+', r'(\(.*\))', r'HP']
torque_patterns = [r'nm?', r'Nm', r'kgm', r'at[\s\d]+rpm', r'(\(.*\))', r'rpm', r'NM',r'm']

# Clean the "Max Power" and "Torque" columns
df['Max Power'] = clean_units(df['Max Power'], max_power_patterns)
df['Torque'] = clean_units(df['Torque'], torque_patterns)

# Function to clean units and handle combined values
def clean_weight_height(series, unit_patterns):
    cleaned_series = series.astype(str)  # Convert to string to avoid errors
    cleaned_series = cleaned_series.str.split('/').str[0].str.strip()  # Handle combined values
    for pattern in unit_patterns:
        cleaned_series = cleaned_series.str.replace(pattern, '', regex=True).str.strip()
    return cleaned_series

# Define patterns to remove specific units
weight_height_patterns = [r'kg', r'mm', r'cm', r'/', r'\s+', r'\(\d+\)']

# Clean the "Kerb Weight", "Gross Weight", and "Height" columns
df['Kerb Weight'] = clean_weight_height(df['Kerb Weight'], weight_height_patterns)
df['Gross Weight'] = clean_weight_height(df['Gross Weight'], weight_height_patterns)
df['Height'] = clean_weight_height(df['Height'], weight_height_patterns)

# Convert strings to numeric data types
df['Kerb Weight'] = pd.to_numeric(df['Kerb Weight'], errors='coerce')
df['Gross Weight'] = pd.to_numeric(df['Gross Weight'], errors='coerce')
df['Height'] = pd.to_numeric(df['Height'], errors='coerce')

# Function to clean and standardize the "Turning Radius" column
def clean_turning_radius(series):
    cleaned_series = series.astype(str)  # Convert to string to avoid errors
    cleaned_series = cleaned_series.str.replace(r'(Meter|Metre|trs|M|m)', '', flags=re.IGNORECASE, regex=True)
    cleaned_series = cleaned_series.str.strip()  # Remove extra spaces
    cleaned_series = pd.to_numeric(cleaned_series, errors='coerce')  # Convert to numeric
    return cleaned_series

# Apply the function to the "Turning Radius" column
df['Turning Radius'] = clean_turning_radius(df['Turning Radius'])

# Function to clean and standardize the "Top Speed" and "Acceleration" columns
def clean_top_speed(series):
    cleaned_series = series.astype(str)  # Convert to string to avoid errors
    cleaned_series = cleaned_series.str.replace(r'(Km/Hour|/h|kmph|km/h|km)', '', flags=re.IGNORECASE, regex=True)
    cleaned_series = cleaned_series.str.strip()  # Remove extra spaces
    cleaned_series = pd.to_numeric(cleaned_series, errors='coerce')  # Convert to numeric
    return cleaned_series

def clean_acceleration(series):
    cleaned_series = series.astype(str)  # Convert to string to avoid errors
    cleaned_series = cleaned_series.str.replace(r'(sconds|Sec|s)', 'seconds', flags=re.IGNORECASE, regex=True)
    cleaned_series = cleaned_series.str.extract(r'(\d+(\.\d+)?)')  # Extract numeric part
    cleaned_series = pd.to_numeric(cleaned_series[0], errors='coerce')  # Convert to numeric
    return cleaned_series

# Apply the functions to clean the "Top Speed" and "Acceleration" columns
df['Top Speed'] = clean_top_speed(df['Top Speed'])
df['Acceleration'] = clean_acceleration(df['Acceleration'])

# Save the cleaned DataFrame
df.to_csv('all_cities_cars_cleaned_final.csv', index=False)

# Display the cleaned DataFrame
print(df.head())

C:\Users\Vishwa\AppData\Local\Temp\ipykernel_9164\895732070.py:6: DtypeWarning: Columns (203,222,232,236) have mixed types. Specify dtype option on import or set low_memory=False.
  df = pd.read_csv("all_cities_cars_cleaned_3.csv")

   it      ft         bt      km transmission  ownerNo      oem  \
0   0  Petrol  Hatchback  120000       Manual        3   Maruti   
1   0  Petrol        SUV   32706       Manual        2     Ford   
2   0  Petrol  Hatchback   11949       Manual        1     Tata   
3   0  Petrol      Sedan   17794       Manual        1  Hyundai   
4   0  Diesel        SUV   60000       Manual        1   Maruti   

                model  modelYear  centralVariantId               variantName  \
0      Maruti Celerio       2015              3979                       VXI   
1       Ford Ecosport       2018              6087  1.5 Petrol Titanium BSIV   
2          Tata Tiago       2018              2983           1.2 Revotron XZ   
3       Hyundai Xcent       2014              1867        1.2 Kappa S Option   
4  Maruti SX4 S Cross       2015              4277             DDiS 200 Zeta   

         price     Insurance Validity  Seats   RTO  Engine Displacement  \
0     ₹ 4 Lakh  Third Party insurance    5.0  KA51                998.0   
1  ₹ 8.11 Lakh          Comprehensive    5.0  KA05               1497.0   
2  ₹ 5.85 Lakh          Comprehensive    5.0  KA03               1199.0   
3  ₹ 4.62 Lakh          Comprehensive    5.0  KA53               1197.0   
4  ₹ 7.90 Lakh  Third Party insurance    5.0  KA04               1248.0   

   Power Steering  Power Windows Front  Air Conditioner  Heater  \
0               1                    1                1       1   
1               1                    1                1       1   
2               1                    1                1       1   
3               1                    1                1       1   
4               1                    1                1       1   

   Adjustable Head Lights  Manually Adjustable Exterior Rear View Mirror  \
0                       1                                              1   
1                       1                                              0   
2                       1                                              0   
3                       1                                              0   
4                       1                                              0   

   Centeral Locking  Child Safety Locks  Power Windows Rear  \
0                 1                   1                   1   
1                 1                   1                   1   
2                 1                   1                   1   
3                 1                   1                   1   
4                 1                   1                   1   

   Remote Trunk Opener  Remote Fuel Lid Opener  Low Fuel Warning Light  \
0                    1                       1                       1   
1                    1                       1                       1   
2                    1                       1                       1   
3                    1                       0                       1   
4                    1                       1                       1   

   Accessory Power Outlet  Vanity Mirror  Rear Seat Headrest  \
0                       1              1                   1   
1                       1              1                   1   
2                       1              1                   1   
3                       1              1                   1   
4                       1              1                   1   

   Cup Holders Front  Digital Odometer  Electronic Multi Tripmeter  \
0                  1                 1                           1   
1                  1                 1                           1   
2                  1                 1                           1   
3                  1                 1                           1   
4                  1                 1                           1   

   Fabric Upholstery  Glove Compartment  Digital Clock  Wheel Covers  \
0                  1                  1              1             1   
1                  1                  1              1             0   
2                  1                  1              1             1   
3                  1                  1              1             0   
4                  1                  1              1             0   

   Power Antenna  Chrome Grille  Day Night Rear View Mirror  \
0              1              1                           1   
1              0              1                           0   
2              1              1                           0   
3              1              1                           1   
4              1              1                           0   

   Passenger Side Rear View Mirror  Halogen Headlamps  Rear Seat Belts  \
0                                1                  1                1   
1                                1                  1                1   
2                                1                  1                1   
3                                1                  1                1   
4                                1                  1                1   

   Door Ajar Warning  Side Impact Beams  Front Impact Beams  Adjustable Seats  \
0                  1                  1                   1                 1   
1                  1                  1                   1                 1   
2                  1                  1                   1                 1   
3                  1                  1                   1                 1   
4                  1                  1                   1                 1   

   Centrally Mounted Fuel Tank  Engine Immobilizer  Anti Theft Device  \
0                            1                   1                  1   
1                            1                   1                  1   
2                            1                   1                  1   
3                            1                   1                  1   
4                            1                   1                  1   

   Fog Lights Front  Anti Lock Braking System  Cd Player  Trunk Light  \
0                 0                         0          0            0   
1                 1                         1          1            1   
2                 1                         1          1            1   
3                 1                         1          1            1   
4                 1                         1          0            1   

   Multifunction Steering Wheel  Navigation System  Smart Access Card Entry  \
0                             0                  0                        0   
1                             1                  1                        1   
2                             1                  1                        0   
3                             1                  0                        0   
4                             1                  1                        0   

   Engine Start Stop Button  Gear Shift Indicator  Luggage Hook And Net  \
0                         0                     0                     0   
1                         1                     1                     1   
2                         0                     0                     0   
3                         0                     0                     0   
4                         1                     1                     0   

   Adjustable Steering  Tachometer  Leather Steering Wheel  \
0                    0           0                       0   
1                    1           1                       1   
2                    1           1                       0   
3                    1           1                       0   
4                    1           1                       0   

   Outside Temperature Display  Height Adjustable Driver Seat  \
0                            0                              0   
1                            1                              1   
2                            1                              1   
3                            0                              1   
4                            1                              1   

   Power Adjustable Exterior Rear View Mirror  \
0                                           0   
1                                           1   
2                                           1   
3                                           1   
4                                           1   

   Electric Folding Rear View Mirror  Rear Window Wiper  Rear Window Washer  \
0                                  0                  0                   0   
1                                  1                  1                   1   
2                                  0                  1                   1   
3                                  1                  0                   0   
4                                  1                  1                   1   

   Rear Window Defogger  Alloy Wheels  Integrated Antenna  \
0                     0             0                   0   
1                     1             1                   1   
2                     1             0                   0   
3                     1             1                   0   
4                     1             1                   0   

   Outside Rear View Mirror Turn Indicators  Roof Rail  Power Door Locks  \
0                                         0          0                 0   
1                                         1          1                 1   
2                                         1          0                 1   
3                                         1          0                 1   
4                                         1          1                 1   

   Driver Air Bag  Passenger Air Bag  Seat Belt Warning  Keyless Entry  \
0               0                  0                  0              0   
1               1                  1                  1              1   
2               1                  1                  1              0   
3               0                  0                  1              1   
4               1                  1                  1              1   

   Engine Check Warning  Crash Sensor  Ebd  Follow Me Home Headlamps  \
0                     0             0    0                         0   
1                     1             1    1                         1   
2                     1             1    1                         1   
3                     0             0    1                         0   
4                     1             1    1                         0   

   Rear Camera  Speed Sensing Auto Door Lock  \
0            0                             0   
1            1                             1   
2            0                             1   
3            0                             0   
4            1                             0   

   Pretensioners And Force Limiter Seatbelts  Impact Sensing Auto Door Lock  \
0                                          0                              0   
1                                          1                              1   
2                                          1                              0   
3                                          0                              0   
4                                          0                              0   

   No Of Airbags  Radio  Speakers Front  Speakers Rear  Integrated2Din Audio  \
0              0      0               0              0                     0   
1              1      1               1              1                     1   
2              0      1               1              1                     1   
3              0      1               1              1                     1   
4              0      1               1              1                     1   

   Usb Auxiliary Input  Bluetooth  Touch Screen  Number Of Speaker  \
0                    0          0             0                  0   
1                    1          1             1                  1   
2                    1          1             0                  1   
3                    1          1             0                  0   
4                    1          1             1                  0   

   Glove Box Cooling  Driving Experience Control Eco  Tinted Glass  \
0                  0                               0             0   
1                  0                               0             0   
2                  1                               1             1   
3                  1                               0             0   
4                  0                               0             1   

   Rear Spoiler  Chrome Garnish  Vehicle Stability Control System  \
0             0               0                                 0   
1             0               0                                 0   
2             1               1                                 1   
3             0               1                                 0   
4             0               0                                 0   

   Rear Reading Lamp  Rear Seat Centre Arm Rest  Cup Holders Rear  \
0                  0                          0                 0   
1                  0                          0                 0   
2                  0                          0                 0   
3                  1                          1                 1   
4                  0                          1                 1   

   Rear ACVents  Air Quality Control  Height Adjustable Front Seat Belts  \
0             0                    0                                   0   
1             0                    0                                   0   
2             0                    0                                   0   
3             1                    0                                   0   
4             0                    1                                   1   

   Cruise Control  Voice Control  Audio System Remote Control  Leather Seats  \
0               0              0                            0              0   
1               0              0                            0              0   
2               0              0                            0              0   
3               0              0                            0              0   
4               1              1                            1              0   

   Fog Lights Rear  Traction Control  Seat Lumbar Support  Battery Saver  \
0                0                 0                    0              0   
1                0                 0                    0              0   
2                0                 0                    0              0   
3                0                 0                    0              0   
4                0                 0                    0              0   

   Lane Change Indicator  Sun Roof  Automatic Driving Lights  \
0                      0         0                         0   
1                      0         0                         0   
2                      0         0                         0   
3                      0         0                         0   
4                      0         0                         0   

   Anti Theft Alarm  Automatic Head Lamps  Isofix Child Seat Mounts  \
0                 0                     0                         0   
1                 0                     0                         0   
2                 0                     0                         0   
3                 0                     0                         0   
4                 0                     0                         0   

   Hill Assist  Tailgate Ajar  Brake Assist  Steering Wheel Gearshift Paddles  \
0            0              0             0                                 0   
1            0              0             0                                 0   
2            0              0             0                                 0   
3            0              0             0                                 0   
4            0              0             0                                 0   

   LEDTaillights  Cigarette Lighter  Rain Sensing Wiper  Drive Modes  \
0              0                  0                   0            0   
1              0                  0                   0            0   
2              0                  0                   0            0   
3              0                  0                   0            0   
4              0                  0                   0            0   

   Active Noise Cancellation  Adjustable Headrest  Hands Free Tailgate  \
0                          0                    0                    0   
1                          0                    0                    0   
2                          0                    0                    0   
3                          0                    0                    0   
4                          0                    0                    0   

   Dual Tone Dashboard  Leather Wrap Gear Shift Selector  \
0                    0                                 0   
1                    0                                 0   
2                    0                                 0   
3                    0                                 0   
4                    0                                 0   

   Dual Tone Body Colour  LEDDRLs  LEDHeadlights  Cornering Headlamps  \
0                      0        0              0                    0   
1                      0        0              0                    0   
2                      0        0              0                    0   
3                      0        0              0                    0   
4                      0        0              0                    0   

   Cornering Foglamps  Side Air Bag Front  Side Air Bag Rear  \
0                   0                   0                  0   
1                   0                   0                  0   
2                   0                   0                  0   
3                   0                   0                  0   
4                   0                   0                  0   

   Tyre Pressure Monitor  Clutch Lock  Anti Pinch Power Windows  Knee Airbags  \
0                      0            0                         0             0   
1                      0            0                         0             0   
2                      0            0                         0             0   
3                      0            0                         0             0   
4                      0            0                         0             0   

   Apple Car Play  Android Auto  Mirror Link  Wireless Phone Charging  \
0               0             0            0                        0   
1               0             0            0                        0   
2               0             0            0                        0   
3               0             0            0                        0   
4               0             0            0                        0   

   Compass  Moon Roof  Projector Headlamps  Speed Alert  \
0        0          0                    0            0   
1        0          0                    0            0   
2        0          0                    0            0   
3        0          0                    0            0   
4        0          0                    0            0   

   Eletronic Stability Control  Touch Screen Size  Xenon Headlamps  \
0                            0                  0                0   
1                            0                  0                0   
2                            0                  0                0   
3                            0                  0                0   
4                            0                  0                0   

   Cd Changer  Power Boot  Rear Folding Table  Smoke Headlamps  Dvd Player  \
0           0           0                   0                0           0   
1           0           0                   0                0           0   
2           0           0                   0                0           0   
3           0           0                   0                0           0   
4           0           0                   0                0           0   

   Internal Storage  Rear Entertainment System  Remote Engine Start Stop  \
0                 0                          0                         0   
1                 0                          0                         0   
2                 0                          0                         0   
3                 0                          0                         0   
4                 0                          0                         0   

   Ventilated Seats  LEDFog Lamps  View360Camera  Geo Fence Alert  \
0                 0             0              0                0   
1                 0             0              0                0   
2                 0             0              0                0   
3                 0             0              0                0   
4                 0             0              0                0   

   Steering Mounted Tripmeter  Remote Climate Control  \
0                           0                       0   
1                           0                       0   
2                           0                       0   
3                           0                       0   
4                           0                       0   

   Remote Horn Light Control  Heated Wing Mirror  Side Stepper  \
0                          0                   0             0   
1                          0                   0             0   
2                          0                   0             0   
3                          0                   0             0   
4                          0                   0             0   

   Blind Spot Monitor  Hill Descent Control  Heads Up Display  \
0                   0                     0                 0   
1                   0                     0                 0   
2                   0                     0                 0   
3                   0                     0                 0   
4                   0                     0                 0   

   Sos Emergency Assistance  Cassette Player  Find My Car Location  \
0                         0                0                     0   
1                         0                0                     0   
2                         0                0                     0   
3                         0                0                     0   
4                         0                0                     0   

   Wifi Connectivity  Headlamp Washers  Real Time Vehicle Tracking  \
0                  0               0.0                           0   
1                  0               0.0                           0   
2                  0               0.0                           0   
3                  0               0.0                           0   
4                  0               0.0                           0   

   Roof Carrier  Smart Key Band  Lane Watch Camera  Removable Convertible Top  \
0             0             0.0                  0                          0   
1             0             0.0                  0                          0   
2             0             0.0                  0                          0   
3             0             0.0                  0                          0   
4             0             0.0                  0                          0   

   Power Folding3rd Row Seat  Mileage Max Power  Torque   Color  \
0                        0.0    23.10     67.04      90   White   
1                        0.0    17.00    121.31     150   White   
2                        0.0    23.84        84     114     Red   
3                        0.0    19.10     81.86  113.75  Others   
4                        0.0    23.65      88.5     200    Gray   

                Engine Type  No of Cylinder  Values per Cylinder  \
0               K10B Engine             3.0                  4.0   
1      Ti-VCT Petrol Engine             3.0                  4.0   
2           Revotron Engine             3.0                  4.0   
3  Kappa VTVT Petrol Engine             4.0                  4.0   
4    DDiS 200 Diesel Engine             4.0                  4.0   

  Value Configuration Fuel Suppy System Turbo Charger Super Charger  Length  \
0                DOHC              MPFi            No            No  3715.0   
1                DOHC  Direct Injection            No            No  3998.0   
2                DOHC              MPFi            No            No  3746.0   
3                DOHC  Direct Injection            No            No  3995.0   
4                DOHC               NaN           Yes            No  4300.0   

    Width  Height Wheel Base  Front Tread Rear Tread  Kerb Weight  \
0  1635.0  1565.0       2425       1420.0     1410.0        835.0   
1  1765.0  1647.0       2519          NaN        NaN       1242.0   
2  1647.0  1535.0       2400       1400.0     1420.0       1012.0   
3  1660.0  1520.0       2425       1479.0     1493.0       1180.0   
4  1785.0  1595.0       2600          NaN        NaN       1230.0   

   Gross Weight Gear Box Drive Type Steering Type  Turning Radius  \
0        1250.0        5        FWD         Power             4.7   
1        1660.0        5        FWD         Power             5.3   
2           NaN        5        FWD         Power             4.9   
3           NaN        5        FWD         Power             4.7   
4        1670.0        5        FWD         Power             5.2   

  Front Brake Type Rear Brake Type  Top Speed  Acceleration         Tyre Type  \
0  Ventilated Disc            Drum      150.0         15.05  Tubeless, Radial   
1  Ventilated Disc            Drum        NaN           NaN   Tubeless,Radial   
2             Disc            Drum      150.0         14.30          Tubeless   
3            Disc             Drum      172.0         14.20   Tubeless,Radial   
4  Ventilated Disc      Solid Disc      190.0         12.00   Tubeless,Radial   

   No Door Numbers Cargo Volumn  Wheel Size  Alloy Wheel Size       city  
0              5.0          235         NaN               NaN  Bangalore  
1              4.0          352        16.0              16.0  Bangalore  
2              5.0          242        14.0              14.0  Bangalore  
3              4.0          407        14.0              14.0  Bangalore  
4              5.0          353        16.0              16.0  Bangalore  

[53]

import pandas as pd
df=pd.read_csv("all_cities_cars_cleaned_final_1.csv")

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
df.isnull().sum()
C:\Users\Vishwa\AppData\Local\Temp\ipykernel_9164\4286351908.py:2: DtypeWarning: Columns (205,218) have mixed types. Specify dtype option on import or set low_memory=False.
  df=pd.read_csv("all_cities_cars_cleaned_final_1.csv")

it                                                  0
ft                                                  0
bt                                                  4
km                                                  0
transmission                                        0
ownerNo                                             0
oem                                                 0
model                                               0
modelYear                                           0
centralVariantId                                    0
variantName                                         0
price                                               0
Insurance Validity                                  8
Seats                                               6
RTO                                               894
Engine Displacement                                 4
Power Steering                                      0
Power Windows Front                                 0
Air Conditioner                                     0
Heater                                              0
Adjustable Head Lights                              0
Manually Adjustable Exterior Rear View Mirror       0
Centeral Locking                                    0
Child Safety Locks                                  0
Power Windows Rear                                  0
Remote Trunk Opener                                 0
Remote Fuel Lid Opener                              0
Low Fuel Warning Light                              0
Accessory Power Outlet                              0
Vanity Mirror                                       0
Rear Seat Headrest                                  0
Cup Holders Front                                   0
Digital Odometer                                    0
Electronic Multi Tripmeter                          0
Fabric Upholstery                                   0
Glove Compartment                                   0
Digital Clock                                       0
Wheel Covers                                        0
Power Antenna                                       0
Chrome Grille                                       0
Day Night Rear View Mirror                          0
Passenger Side Rear View Mirror                     0
Halogen Headlamps                                   0
Rear Seat Belts                                     0
Door Ajar Warning                                   0
Side Impact Beams                                   0
Front Impact Beams                                  0
Adjustable Seats                                    0
Centrally Mounted Fuel Tank                         0
Engine Immobilizer                                  0
Anti Theft Device                                   0
Fog Lights Front                                    0
Anti Lock Braking System                            0
Cd Player                                           0
Trunk Light                                         0
Multifunction Steering Wheel                        0
Navigation System                                   0
Smart Access Card Entry                             0
Engine Start Stop Button                            0
Gear Shift Indicator                                0
Luggage Hook And Net                                0
Adjustable Steering                                 0
Tachometer                                          0
Leather Steering Wheel                              0
Outside Temperature Display                         0
Height Adjustable Driver Seat                       0
Power Adjustable Exterior Rear View Mirror          0
Electric Folding Rear View Mirror                   0
Rear Window Wiper                                   0
Rear Window Washer                                  0
Rear Window Defogger                                0
Alloy Wheels                                        0
Integrated Antenna                                  0
Outside Rear View Mirror Turn Indicators            0
Roof Rail                                           0
Power Door Locks                                    0
Driver Air Bag                                      0
Passenger Air Bag                                   0
Seat Belt Warning                                   0
Keyless Entry                                       0
Engine Check Warning                                0
Crash Sensor                                        0
Ebd                                                 0
Follow Me Home Headlamps                            0
Rear Camera                                         0
Speed Sensing Auto Door Lock                        0
Pretensioners And Force Limiter Seatbelts           0
Impact Sensing Auto Door Lock                       0
No Of Airbags                                       0
Radio                                               0
Speakers Front                                      0
Speakers Rear                                       0
Integrated2Din Audio                                0
Usb Auxiliary Input                                 0
Bluetooth                                           0
Touch Screen                                        0
Number Of Speaker                                   0
Glove Box Cooling                                   0
Driving Experience Control Eco                      0
Tinted Glass                                        0
Rear Spoiler                                        0
Chrome Garnish                                      0
Vehicle Stability Control System                    0
Rear Reading Lamp                                   0
Rear Seat Centre Arm Rest                           0
Cup Holders Rear                                    0
Rear ACVents                                        0
Air Quality Control                                 0
Height Adjustable Front Seat Belts                  0
Cruise Control                                      0
Voice Control                                       0
Audio System Remote Control                         0
Leather Seats                                       0
Fog Lights Rear                                     0
Traction Control                                    0
Seat Lumbar Support                                 0
Battery Saver                                       0
Lane Change Indicator                               0
Sun Roof                                            0
Automatic Driving Lights                            0
Anti Theft Alarm                                    0
Automatic Head Lamps                                0
Isofix Child Seat Mounts                            0
Hill Assist                                         0
Tailgate Ajar                                       0
Brake Assist                                        0
Steering Wheel Gearshift Paddles                    0
LEDTaillights                                       0
Cigarette Lighter                                   0
Rain Sensing Wiper                                  0
Drive Modes                                         0
Active Noise Cancellation                           0
Adjustable Headrest                                 0
Hands Free Tailgate                                 0
Dual Tone Dashboard                                 0
Leather Wrap Gear Shift Selector                    0
Dual Tone Body Colour                               0
LEDDRLs                                             0
LEDHeadlights                                       0
Cornering Headlamps                                 0
Cornering Foglamps                                  0
Side Air Bag Front                                  0
Side Air Bag Rear                                   0
Tyre Pressure Monitor                               0
Clutch Lock                                         0
Anti Pinch Power Windows                            0
Knee Airbags                                        0
Apple Car Play                                      0
Android Auto                                        0
Mirror Link                                         0
Wireless Phone Charging                             0
Compass                                             0
Moon Roof                                           0
Projector Headlamps                                 0
Speed Alert                                         0
Eletronic Stability Control                         0
Touch Screen Size                                   0
Xenon Headlamps                                     0
Cd Changer                                          0
Power Boot                                          0
Rear Folding Table                                  0
Smoke Headlamps                                     0
Dvd Player                                          0
Internal Storage                                    0
Rear Entertainment System                           0
Remote Engine Start Stop                            0
Ventilated Seats                                    0
LEDFog Lamps                                        0
View360Camera                                       0
Geo Fence Alert                                     0
Steering Mounted Tripmeter                          0
Remote Climate Control                              0
Remote Horn Light Control                           0
Heated Wing Mirror                                  0
Side Stepper                                        0
Blind Spot Monitor                                  0
Hill Descent Control                                0
Heads Up Display                                    0
Sos Emergency Assistance                            0
Cassette Player                                     0
Find My Car Location                                0
Wifi Connectivity                                   0
Headlamp Washers                                 1483
Real Time Vehicle Tracking                          0
Roof Carrier                                        0
Smart Key Band                                   1483
Lane Watch Camera                                   0
Removable Convertible Top                           0
Power Folding3rd Row Seat                        2501
Mileage                                           323
Max Power                                          60
Torque                                              0
Color                                               3
Engine Type                                       295
No of Cylinder                                     31
Values per Cylinder                                51
Value Configuration                              2218
Fuel Suppy System                                1732
Turbo Charger                                    1040
Super Charger                                    1962
Length                                             79
Width                                              83
Height                                             89
Wheel Base                                        163
Front Tread                                      3558
Rear Tread                                       3570
Kerb Weight                                        60
Gross Weight                                     4617
Gear Box                                          273
Drive Type                                       1940
Steering Type                                     255
Turning Radius                                   1624
Front Brake Type                                   96
Rear Brake Type                                    96
Top Speed                                        3787
Acceleration                                     3514
Tyre Type                                          77
No Door Numbers                                    11
Cargo Volumn                                     1609
Wheel Size                                       3324
Alloy Wheel Size                                 3324
city                                                0
dtype: int64
[57]
df=pd.read_csv("all_cities_cars_cleaned_final_filled.csv")
unique_values = df['Torque'].unique()
print(unique_values)
---------------------------------------------------------------------------
FileNotFoundError Traceback (most recent call last)
Cell In[57], line 1 ----> 1 df=pd.read_csv("all_cities_cars_cleaned_final_filled.csv") 2 unique_values = df['Torque'].unique() 3 print(unique_values)
File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:1026, in read_csv(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options, dtype_backend) 1013 kwds_defaults = _refine_defaults_read( 1014 dialect, 1015 delimiter, (...) 1022 dtype_backend=dtype_backend, 1023 ) 1024 kwds.update(kwds_defaults) -> 1026 return _read(filepath_or_buffer, kwds)
File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:620, in _read(filepath_or_buffer, kwds) 617 _validate_names(kwds.get("names", None)) 619 # Create the parser. --> 620 parser = TextFileReader(filepath_or_buffer, **kwds) 622 if chunksize or iterator: 623 return parser
File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:1620, in TextFileReader.__init__(self, f, engine, **kwds) 1617 self.options["has_index_names"] = kwds["has_index_names"] 1619 self.handles: IOHandles | None = None -> 1620 self._engine = self._make_engine(f, self.engine)
File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:1880, in TextFileReader._make_engine(self, f, engine) 1878 if "b" not in mode: 1879 mode += "b" -> 1880 self.handles = get_handle( 1881 f, 1882 mode, 1883 encoding=self.options.get("encoding", None), 1884 compression=self.options.get("compression", None), 1885 memory_map=self.options.get("memory_map", False), 1886 is_text=is_text, 1887 errors=self.options.get("encoding_errors", "strict"), 1888 storage_options=self.options.get("storage_options", None), 1889 ) 1890 assert self.handles is not None 1891 f = self.handles.handle
File ~\anaconda3\Lib\site-packages\pandas\io\common.py:873, in get_handle(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options) 868 elif isinstance(handle, str): 869 # Check whether the filename is to be opened in binary mode. 870 # Binary mode does not support 'encoding' and 'newline'. 871 if ioargs.encoding and "b" not in ioargs.mode: 872 # Encoding --> 873 handle = open( 874 handle, 875 ioargs.mode, 876 encoding=ioargs.encoding, 877 errors=errors, 878 newline="", 879 ) 880 else: 881 # Binary mode 882 handle = open(handle, ioargs.mode)
FileNotFoundError: [Errno 2] No such file or directory: 'all_cities_cars_cleaned_final_filled.csv'
[59]
import pandas as pd
import numpy as np
import re

# Load the dataset
df = pd.read_csv("all_cities_cars_cleaned_final.csv")

# Function to extract numeric values from strings
def extract_numeric(value):
    # Remove non-numeric characters and convert to float
    match = re.search(r'\d+(\.\d+)?', str(value))
    return float(match.group()) if match else np.nan

# Apply the function to the 'Max Power' column
df['Max Power'] = df['Max Power'].apply(extract_numeric)

# Function to clean and convert price column values
def convert_price(price):
    try:
        price = str(price).replace('₹', '').replace(',', '').strip()
        if 'Lakh' in price:
            return float(price.replace('Lakh', '').strip()) * 100000
        elif 'Thousand' in price:
            return float(price.replace('Thousand', '').strip()) * 1000
        else:
            return float(price)
    except ValueError:
        return np.nan

# Apply conversion function to the 'price' column
df['price'] = df['price'].apply(convert_price)

# Handle NaN and inf values before converting to Int64
df['price'] = pd.to_numeric(df['price'], errors='coerce')


# Calculate the median of the 'price' column
price_median = df['price'].median()

# Fill NaN values with the median
df['price'].fillna(price_median, inplace=True)

# Round the 'price' column to avoid floating-point precision issues
df['price'] = df['price'].round()

# Convert 'price' to integer
df['price'] = df['price'].astype('Int64')

# Ensure 'Seats' column is cleaned and converted

df['Seats'] = df['Seats'].astype('Int64')  # Fill NaN with 0 and convert to Int64

# Save the cleaned DataFrame
df.to_csv('all_cities_cars_cleaned_final_1.csv', index=False)

# Display the cleaned DataFrame
print(df.head())

C:\Users\Vishwa\AppData\Local\Temp\ipykernel_9164\237207696.py:6: DtypeWarning: Columns (205,218) have mixed types. Specify dtype option on import or set low_memory=False.
  df = pd.read_csv("all_cities_cars_cleaned_final.csv")
C:\Users\Vishwa\AppData\Local\Temp\ipykernel_9164\237207696.py:41: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.


  df['price'].fillna(price_median, inplace=True)

   it      ft         bt      km transmission  ownerNo      oem  \
0   0  Petrol  Hatchback  120000       Manual        3   Maruti   
1   0  Petrol        SUV   32706       Manual        2     Ford   
2   0  Petrol  Hatchback   11949       Manual        1     Tata   
3   0  Petrol      Sedan   17794       Manual        1  Hyundai   
4   0  Diesel        SUV   60000       Manual        1   Maruti   

                model  modelYear  centralVariantId               variantName  \
0      Maruti Celerio       2015              3979                       VXI   
1       Ford Ecosport       2018              6087  1.5 Petrol Titanium BSIV   
2          Tata Tiago       2018              2983           1.2 Revotron XZ   
3       Hyundai Xcent       2014              1867        1.2 Kappa S Option   
4  Maruti SX4 S Cross       2015              4277             DDiS 200 Zeta   

    price     Insurance Validity  Seats   RTO  Engine Displacement  \
0  400000  Third Party insurance      5  KA51                998.0   
1  811000          Comprehensive      5  KA05               1497.0   
2  585000          Comprehensive      5  KA03               1199.0   
3  462000          Comprehensive      5  KA53               1197.0   
4  790000  Third Party insurance      5  KA04               1248.0   

   Power Steering  Power Windows Front  Air Conditioner  Heater  \
0               1                    1                1       1   
1               1                    1                1       1   
2               1                    1                1       1   
3               1                    1                1       1   
4               1                    1                1       1   

   Adjustable Head Lights  Manually Adjustable Exterior Rear View Mirror  \
0                       1                                              1   
1                       1                                              0   
2                       1                                              0   
3                       1                                              0   
4                       1                                              0   

   Centeral Locking  Child Safety Locks  Power Windows Rear  \
0                 1                   1                   1   
1                 1                   1                   1   
2                 1                   1                   1   
3                 1                   1                   1   
4                 1                   1                   1   

   Remote Trunk Opener  Remote Fuel Lid Opener  Low Fuel Warning Light  \
0                    1                       1                       1   
1                    1                       1                       1   
2                    1                       1                       1   
3                    1                       0                       1   
4                    1                       1                       1   

   Accessory Power Outlet  Vanity Mirror  Rear Seat Headrest  \
0                       1              1                   1   
1                       1              1                   1   
2                       1              1                   1   
3                       1              1                   1   
4                       1              1                   1   

   Cup Holders Front  Digital Odometer  Electronic Multi Tripmeter  \
0                  1                 1                           1   
1                  1                 1                           1   
2                  1                 1                           1   
3                  1                 1                           1   
4                  1                 1                           1   

   Fabric Upholstery  Glove Compartment  Digital Clock  Wheel Covers  \
0                  1                  1              1             1   
1                  1                  1              1             0   
2                  1                  1              1             1   
3                  1                  1              1             0   
4                  1                  1              1             0   

   Power Antenna  Chrome Grille  Day Night Rear View Mirror  \
0              1              1                           1   
1              0              1                           0   
2              1              1                           0   
3              1              1                           1   
4              1              1                           0   

   Passenger Side Rear View Mirror  Halogen Headlamps  Rear Seat Belts  \
0                                1                  1                1   
1                                1                  1                1   
2                                1                  1                1   
3                                1                  1                1   
4                                1                  1                1   

   Door Ajar Warning  Side Impact Beams  Front Impact Beams  Adjustable Seats  \
0                  1                  1                   1                 1   
1                  1                  1                   1                 1   
2                  1                  1                   1                 1   
3                  1                  1                   1                 1   
4                  1                  1                   1                 1   

   Centrally Mounted Fuel Tank  Engine Immobilizer  Anti Theft Device  \
0                            1                   1                  1   
1                            1                   1                  1   
2                            1                   1                  1   
3                            1                   1                  1   
4                            1                   1                  1   

   Fog Lights Front  Anti Lock Braking System  Cd Player  Trunk Light  \
0                 0                         0          0            0   
1                 1                         1          1            1   
2                 1                         1          1            1   
3                 1                         1          1            1   
4                 1                         1          0            1   

   Multifunction Steering Wheel  Navigation System  Smart Access Card Entry  \
0                             0                  0                        0   
1                             1                  1                        1   
2                             1                  1                        0   
3                             1                  0                        0   
4                             1                  1                        0   

   Engine Start Stop Button  Gear Shift Indicator  Luggage Hook And Net  \
0                         0                     0                     0   
1                         1                     1                     1   
2                         0                     0                     0   
3                         0                     0                     0   
4                         1                     1                     0   

   Adjustable Steering  Tachometer  Leather Steering Wheel  \
0                    0           0                       0   
1                    1           1                       1   
2                    1           1                       0   
3                    1           1                       0   
4                    1           1                       0   

   Outside Temperature Display  Height Adjustable Driver Seat  \
0                            0                              0   
1                            1                              1   
2                            1                              1   
3                            0                              1   
4                            1                              1   

   Power Adjustable Exterior Rear View Mirror  \
0                                           0   
1                                           1   
2                                           1   
3                                           1   
4                                           1   

   Electric Folding Rear View Mirror  Rear Window Wiper  Rear Window Washer  \
0                                  0                  0                   0   
1                                  1                  1                   1   
2                                  0                  1                   1   
3                                  1                  0                   0   
4                                  1                  1                   1   

   Rear Window Defogger  Alloy Wheels  Integrated Antenna  \
0                     0             0                   0   
1                     1             1                   1   
2                     1             0                   0   
3                     1             1                   0   
4                     1             1                   0   

   Outside Rear View Mirror Turn Indicators  Roof Rail  Power Door Locks  \
0                                         0          0                 0   
1                                         1          1                 1   
2                                         1          0                 1   
3                                         1          0                 1   
4                                         1          1                 1   

   Driver Air Bag  Passenger Air Bag  Seat Belt Warning  Keyless Entry  \
0               0                  0                  0              0   
1               1                  1                  1              1   
2               1                  1                  1              0   
3               0                  0                  1              1   
4               1                  1                  1              1   

   Engine Check Warning  Crash Sensor  Ebd  Follow Me Home Headlamps  \
0                     0             0    0                         0   
1                     1             1    1                         1   
2                     1             1    1                         1   
3                     0             0    1                         0   
4                     1             1    1                         0   

   Rear Camera  Speed Sensing Auto Door Lock  \
0            0                             0   
1            1                             1   
2            0                             1   
3            0                             0   
4            1                             0   

   Pretensioners And Force Limiter Seatbelts  Impact Sensing Auto Door Lock  \
0                                          0                              0   
1                                          1                              1   
2                                          1                              0   
3                                          0                              0   
4                                          0                              0   

   No Of Airbags  Radio  Speakers Front  Speakers Rear  Integrated2Din Audio  \
0              0      0               0              0                     0   
1              1      1               1              1                     1   
2              0      1               1              1                     1   
3              0      1               1              1                     1   
4              0      1               1              1                     1   

   Usb Auxiliary Input  Bluetooth  Touch Screen  Number Of Speaker  \
0                    0          0             0                  0   
1                    1          1             1                  1   
2                    1          1             0                  1   
3                    1          1             0                  0   
4                    1          1             1                  0   

   Glove Box Cooling  Driving Experience Control Eco  Tinted Glass  \
0                  0                               0             0   
1                  0                               0             0   
2                  1                               1             1   
3                  1                               0             0   
4                  0                               0             1   

   Rear Spoiler  Chrome Garnish  Vehicle Stability Control System  \
0             0               0                                 0   
1             0               0                                 0   
2             1               1                                 1   
3             0               1                                 0   
4             0               0                                 0   

   Rear Reading Lamp  Rear Seat Centre Arm Rest  Cup Holders Rear  \
0                  0                          0                 0   
1                  0                          0                 0   
2                  0                          0                 0   
3                  1                          1                 1   
4                  0                          1                 1   

   Rear ACVents  Air Quality Control  Height Adjustable Front Seat Belts  \
0             0                    0                                   0   
1             0                    0                                   0   
2             0                    0                                   0   
3             1                    0                                   0   
4             0                    1                                   1   

   Cruise Control  Voice Control  Audio System Remote Control  Leather Seats  \
0               0              0                            0              0   
1               0              0                            0              0   
2               0              0                            0              0   
3               0              0                            0              0   
4               1              1                            1              0   

   Fog Lights Rear  Traction Control  Seat Lumbar Support  Battery Saver  \
0                0                 0                    0              0   
1                0                 0                    0              0   
2                0                 0                    0              0   
3                0                 0                    0              0   
4                0                 0                    0              0   

   Lane Change Indicator  Sun Roof  Automatic Driving Lights  \
0                      0         0                         0   
1                      0         0                         0   
2                      0         0                         0   
3                      0         0                         0   
4                      0         0                         0   

   Anti Theft Alarm  Automatic Head Lamps  Isofix Child Seat Mounts  \
0                 0                     0                         0   
1                 0                     0                         0   
2                 0                     0                         0   
3                 0                     0                         0   
4                 0                     0                         0   

   Hill Assist  Tailgate Ajar  Brake Assist  Steering Wheel Gearshift Paddles  \
0            0              0             0                                 0   
1            0              0             0                                 0   
2            0              0             0                                 0   
3            0              0             0                                 0   
4            0              0             0                                 0   

   LEDTaillights  Cigarette Lighter  Rain Sensing Wiper  Drive Modes  \
0              0                  0                   0            0   
1              0                  0                   0            0   
2              0                  0                   0            0   
3              0                  0                   0            0   
4              0                  0                   0            0   

   Active Noise Cancellation  Adjustable Headrest  Hands Free Tailgate  \
0                          0                    0                    0   
1                          0                    0                    0   
2                          0                    0                    0   
3                          0                    0                    0   
4                          0                    0                    0   

   Dual Tone Dashboard  Leather Wrap Gear Shift Selector  \
0                    0                                 0   
1                    0                                 0   
2                    0                                 0   
3                    0                                 0   
4                    0                                 0   

   Dual Tone Body Colour  LEDDRLs  LEDHeadlights  Cornering Headlamps  \
0                      0        0              0                    0   
1                      0        0              0                    0   
2                      0        0              0                    0   
3                      0        0              0                    0   
4                      0        0              0                    0   

   Cornering Foglamps  Side Air Bag Front  Side Air Bag Rear  \
0                   0                   0                  0   
1                   0                   0                  0   
2                   0                   0                  0   
3                   0                   0                  0   
4                   0                   0                  0   

   Tyre Pressure Monitor  Clutch Lock  Anti Pinch Power Windows  Knee Airbags  \
0                      0            0                         0             0   
1                      0            0                         0             0   
2                      0            0                         0             0   
3                      0            0                         0             0   
4                      0            0                         0             0   

   Apple Car Play  Android Auto  Mirror Link  Wireless Phone Charging  \
0               0             0            0                        0   
1               0             0            0                        0   
2               0             0            0                        0   
3               0             0            0                        0   
4               0             0            0                        0   

   Compass  Moon Roof  Projector Headlamps  Speed Alert  \
0        0          0                    0            0   
1        0          0                    0            0   
2        0          0                    0            0   
3        0          0                    0            0   
4        0          0                    0            0   

   Eletronic Stability Control  Touch Screen Size  Xenon Headlamps  \
0                            0                  0                0   
1                            0                  0                0   
2                            0                  0                0   
3                            0                  0                0   
4                            0                  0                0   

   Cd Changer  Power Boot  Rear Folding Table  Smoke Headlamps  Dvd Player  \
0           0           0                   0                0           0   
1           0           0                   0                0           0   
2           0           0                   0                0           0   
3           0           0                   0                0           0   
4           0           0                   0                0           0   

   Internal Storage  Rear Entertainment System  Remote Engine Start Stop  \
0                 0                          0                         0   
1                 0                          0                         0   
2                 0                          0                         0   
3                 0                          0                         0   
4                 0                          0                         0   

   Ventilated Seats  LEDFog Lamps  View360Camera  Geo Fence Alert  \
0                 0             0              0                0   
1                 0             0              0                0   
2                 0             0              0                0   
3                 0             0              0                0   
4                 0             0              0                0   

   Steering Mounted Tripmeter  Remote Climate Control  \
0                           0                       0   
1                           0                       0   
2                           0                       0   
3                           0                       0   
4                           0                       0   

   Remote Horn Light Control  Heated Wing Mirror  Side Stepper  \
0                          0                   0             0   
1                          0                   0             0   
2                          0                   0             0   
3                          0                   0             0   
4                          0                   0             0   

   Blind Spot Monitor  Hill Descent Control  Heads Up Display  \
0                   0                     0                 0   
1                   0                     0                 0   
2                   0                     0                 0   
3                   0                     0                 0   
4                   0                     0                 0   

   Sos Emergency Assistance  Cassette Player  Find My Car Location  \
0                         0                0                     0   
1                         0                0                     0   
2                         0                0                     0   
3                         0                0                     0   
4                         0                0                     0   

   Wifi Connectivity  Headlamp Washers  Real Time Vehicle Tracking  \
0                  0               0.0                           0   
1                  0               0.0                           0   
2                  0               0.0                           0   
3                  0               0.0                           0   
4                  0               0.0                           0   

   Roof Carrier  Smart Key Band  Lane Watch Camera  Removable Convertible Top  \
0             0             0.0                  0                          0   
1             0             0.0                  0                          0   
2             0             0.0                  0                          0   
3             0             0.0                  0                          0   
4             0             0.0                  0                          0   

   Power Folding3rd Row Seat  Mileage  Max Power  Torque   Color  \
0                        0.0    23.10      67.04      90   White   
1                        0.0    17.00     121.31     150   White   
2                        0.0    23.84      84.00     114     Red   
3                        0.0    19.10      81.86  113.75  Others   
4                        0.0    23.65      88.50     200    Gray   

                Engine Type  No of Cylinder  Values per Cylinder  \
0               K10B Engine             3.0                  4.0   
1      Ti-VCT Petrol Engine             3.0                  4.0   
2           Revotron Engine             3.0                  4.0   
3  Kappa VTVT Petrol Engine             4.0                  4.0   
4    DDiS 200 Diesel Engine             4.0                  4.0   

  Value Configuration Fuel Suppy System Turbo Charger Super Charger  Length  \
0                DOHC              MPFi            No            No  3715.0   
1                DOHC  Direct Injection            No            No  3998.0   
2                DOHC              MPFi            No            No  3746.0   
3                DOHC  Direct Injection            No            No  3995.0   
4                DOHC               NaN           Yes            No  4300.0   

    Width  Height Wheel Base  Front Tread Rear Tread  Kerb Weight  \
0  1635.0  1565.0       2425       1420.0     1410.0        835.0   
1  1765.0  1647.0       2519          NaN        NaN       1242.0   
2  1647.0  1535.0       2400       1400.0     1420.0       1012.0   
3  1660.0  1520.0       2425       1479.0     1493.0       1180.0   
4  1785.0  1595.0       2600          NaN        NaN       1230.0   

   Gross Weight Gear Box Drive Type Steering Type  Turning Radius  \
0        1250.0        5        FWD         Power             4.7   
1        1660.0        5        FWD         Power             5.3   
2           NaN        5        FWD         Power             4.9   
3           NaN        5        FWD         Power             4.7   
4        1670.0        5        FWD         Power             5.2   

  Front Brake Type Rear Brake Type  Top Speed  Acceleration         Tyre Type  \
0  Ventilated Disc            Drum      150.0         15.05  Tubeless, Radial   
1  Ventilated Disc            Drum        NaN           NaN   Tubeless,Radial   
2             Disc            Drum      150.0         14.30          Tubeless   
3            Disc             Drum      172.0         14.20   Tubeless,Radial   
4  Ventilated Disc      Solid Disc      190.0         12.00   Tubeless,Radial   

   No Door Numbers Cargo Volumn  Wheel Size  Alloy Wheel Size       city  
0              5.0          235         NaN               NaN  Bangalore  
1              4.0          352        16.0              16.0  Bangalore  
2              5.0          242        14.0              14.0  Bangalore  
3              4.0          407        14.0              14.0  Bangalore  
4              5.0          353        16.0              16.0  Bangalore  

[73]
import pandas as pd
import numpy as np
import re

# Load the dataset
df = pd.read_csv("all_cities_cars_cleaned_final_1.csv")

# Function to clean and convert column values to numeric
def clean_and_convert_to_numeric(series):
    series = series.astype(str)  # Ensure the series is of type string
    # Remove non-numeric characters
    series = series.str.replace(r'[^\d.]', '', regex=True).str.strip()
    return pd.to_numeric(series, errors='coerce')  # Convert to numeric, with errors set to 'coerce'

# Define numerical columns
numerical_columns = [
    'Engine Displacement','Mileage', 'Max Power', 
    'No of Cylinder', 'Values per Cylinder',
    'Length', 'Width', 'Height', 'Wheel Base', 
    'Front Tread', 'Rear Tread', 'Kerb Weight', 'Gross Weight', 'Gear Box', 
    'Turning Radius','Top Speed', 'Acceleration','No Door Numbers', 
    'Cargo Volumn', 'Wheel Size', 'Alloy Wheel Size'
]

# Clean and convert numerical columns
for col in numerical_columns:
    if col in df.columns:
        df[col] = clean_and_convert_to_numeric(df[col])

# Fill missing values for numerical columns using median
for col in numerical_columns:
    if col in df.columns:
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)

# Fill missing values for categorical columns using mode
categorical_columns = [
    'Tyre Type', 'Rear Brake Type', 'Front Brake Type','RTO','Steering Type', 
    'Turbo Charger', 'Super Charger', 'Fuel Suppy System', 'Color', 
    'Engine Type', 'bt', 'Value Configuration', 'Drive Type'
]

for col in categorical_columns:
    if col in df.columns:
        mode_value = df[col].mode()[0]
        df[col] = df[col].fillna(mode_value)

df['Torque'] =  pd.to_numeric(df['Torque'],errors='coerce')


# Save the cleaned DataFrame
df.to_csv(r"C:\Users\Vishwa\Desktop\GUVI captone\CAR\all_cities_cars_cleaned_final_filled.csv", index=False)

# Display the cleaned DataFrame
print(df.head())

C:\Users\Vishwa\AppData\Local\Temp\ipykernel_9164\3609763924.py:6: DtypeWarning: Columns (205,218) have mixed types. Specify dtype option on import or set low_memory=False.
  df = pd.read_csv("all_cities_cars_cleaned_final_1.csv")

   it      ft         bt      km transmission  ownerNo      oem  \
0   0  Petrol  Hatchback  120000       Manual        3   Maruti   
1   0  Petrol        SUV   32706       Manual        2     Ford   
2   0  Petrol  Hatchback   11949       Manual        1     Tata   
3   0  Petrol      Sedan   17794       Manual        1  Hyundai   
4   0  Diesel        SUV   60000       Manual        1   Maruti   

                model  modelYear  centralVariantId               variantName  \
0      Maruti Celerio       2015              3979                       VXI   
1       Ford Ecosport       2018              6087  1.5 Petrol Titanium BSIV   
2          Tata Tiago       2018              2983           1.2 Revotron XZ   
3       Hyundai Xcent       2014              1867        1.2 Kappa S Option   
4  Maruti SX4 S Cross       2015              4277             DDiS 200 Zeta   

    price     Insurance Validity  Seats   RTO  Engine Displacement  \
0  400000  Third Party insurance    5.0  KA51                998.0   
1  811000          Comprehensive    5.0  KA05               1497.0   
2  585000          Comprehensive    5.0  KA03               1199.0   
3  462000          Comprehensive    5.0  KA53               1197.0   
4  790000  Third Party insurance    5.0  KA04               1248.0   

   Power Steering  Power Windows Front  Air Conditioner  Heater  \
0               1                    1                1       1   
1               1                    1                1       1   
2               1                    1                1       1   
3               1                    1                1       1   
4               1                    1                1       1   

   Adjustable Head Lights  Manually Adjustable Exterior Rear View Mirror  \
0                       1                                              1   
1                       1                                              0   
2                       1                                              0   
3                       1                                              0   
4                       1                                              0   

   Centeral Locking  Child Safety Locks  Power Windows Rear  \
0                 1                   1                   1   
1                 1                   1                   1   
2                 1                   1                   1   
3                 1                   1                   1   
4                 1                   1                   1   

   Remote Trunk Opener  Remote Fuel Lid Opener  Low Fuel Warning Light  \
0                    1                       1                       1   
1                    1                       1                       1   
2                    1                       1                       1   
3                    1                       0                       1   
4                    1                       1                       1   

   Accessory Power Outlet  Vanity Mirror  Rear Seat Headrest  \
0                       1              1                   1   
1                       1              1                   1   
2                       1              1                   1   
3                       1              1                   1   
4                       1              1                   1   

   Cup Holders Front  Digital Odometer  Electronic Multi Tripmeter  \
0                  1                 1                           1   
1                  1                 1                           1   
2                  1                 1                           1   
3                  1                 1                           1   
4                  1                 1                           1   

   Fabric Upholstery  Glove Compartment  Digital Clock  Wheel Covers  \
0                  1                  1              1             1   
1                  1                  1              1             0   
2                  1                  1              1             1   
3                  1                  1              1             0   
4                  1                  1              1             0   

   Power Antenna  Chrome Grille  Day Night Rear View Mirror  \
0              1              1                           1   
1              0              1                           0   
2              1              1                           0   
3              1              1                           1   
4              1              1                           0   

   Passenger Side Rear View Mirror  Halogen Headlamps  Rear Seat Belts  \
0                                1                  1                1   
1                                1                  1                1   
2                                1                  1                1   
3                                1                  1                1   
4                                1                  1                1   

   Door Ajar Warning  Side Impact Beams  Front Impact Beams  Adjustable Seats  \
0                  1                  1                   1                 1   
1                  1                  1                   1                 1   
2                  1                  1                   1                 1   
3                  1                  1                   1                 1   
4                  1                  1                   1                 1   

   Centrally Mounted Fuel Tank  Engine Immobilizer  Anti Theft Device  \
0                            1                   1                  1   
1                            1                   1                  1   
2                            1                   1                  1   
3                            1                   1                  1   
4                            1                   1                  1   

   Fog Lights Front  Anti Lock Braking System  Cd Player  Trunk Light  \
0                 0                         0          0            0   
1                 1                         1          1            1   
2                 1                         1          1            1   
3                 1                         1          1            1   
4                 1                         1          0            1   

   Multifunction Steering Wheel  Navigation System  Smart Access Card Entry  \
0                             0                  0                        0   
1                             1                  1                        1   
2                             1                  1                        0   
3                             1                  0                        0   
4                             1                  1                        0   

   Engine Start Stop Button  Gear Shift Indicator  Luggage Hook And Net  \
0                         0                     0                     0   
1                         1                     1                     1   
2                         0                     0                     0   
3                         0                     0                     0   
4                         1                     1                     0   

   Adjustable Steering  Tachometer  Leather Steering Wheel  \
0                    0           0                       0   
1                    1           1                       1   
2                    1           1                       0   
3                    1           1                       0   
4                    1           1                       0   

   Outside Temperature Display  Height Adjustable Driver Seat  \
0                            0                              0   
1                            1                              1   
2                            1                              1   
3                            0                              1   
4                            1                              1   

   Power Adjustable Exterior Rear View Mirror  \
0                                           0   
1                                           1   
2                                           1   
3                                           1   
4                                           1   

   Electric Folding Rear View Mirror  Rear Window Wiper  Rear Window Washer  \
0                                  0                  0                   0   
1                                  1                  1                   1   
2                                  0                  1                   1   
3                                  1                  0                   0   
4                                  1                  1                   1   

   Rear Window Defogger  Alloy Wheels  Integrated Antenna  \
0                     0             0                   0   
1                     1             1                   1   
2                     1             0                   0   
3                     1             1                   0   
4                     1             1                   0   

   Outside Rear View Mirror Turn Indicators  Roof Rail  Power Door Locks  \
0                                         0          0                 0   
1                                         1          1                 1   
2                                         1          0                 1   
3                                         1          0                 1   
4                                         1          1                 1   

   Driver Air Bag  Passenger Air Bag  Seat Belt Warning  Keyless Entry  \
0               0                  0                  0              0   
1               1                  1                  1              1   
2               1                  1                  1              0   
3               0                  0                  1              1   
4               1                  1                  1              1   

   Engine Check Warning  Crash Sensor  Ebd  Follow Me Home Headlamps  \
0                     0             0    0                         0   
1                     1             1    1                         1   
2                     1             1    1                         1   
3                     0             0    1                         0   
4                     1             1    1                         0   

   Rear Camera  Speed Sensing Auto Door Lock  \
0            0                             0   
1            1                             1   
2            0                             1   
3            0                             0   
4            1                             0   

   Pretensioners And Force Limiter Seatbelts  Impact Sensing Auto Door Lock  \
0                                          0                              0   
1                                          1                              1   
2                                          1                              0   
3                                          0                              0   
4                                          0                              0   

   No Of Airbags  Radio  Speakers Front  Speakers Rear  Integrated2Din Audio  \
0              0      0               0              0                     0   
1              1      1               1              1                     1   
2              0      1               1              1                     1   
3              0      1               1              1                     1   
4              0      1               1              1                     1   

   Usb Auxiliary Input  Bluetooth  Touch Screen  Number Of Speaker  \
0                    0          0             0                  0   
1                    1          1             1                  1   
2                    1          1             0                  1   
3                    1          1             0                  0   
4                    1          1             1                  0   

   Glove Box Cooling  Driving Experience Control Eco  Tinted Glass  \
0                  0                               0             0   
1                  0                               0             0   
2                  1                               1             1   
3                  1                               0             0   
4                  0                               0             1   

   Rear Spoiler  Chrome Garnish  Vehicle Stability Control System  \
0             0               0                                 0   
1             0               0                                 0   
2             1               1                                 1   
3             0               1                                 0   
4             0               0                                 0   

   Rear Reading Lamp  Rear Seat Centre Arm Rest  Cup Holders Rear  \
0                  0                          0                 0   
1                  0                          0                 0   
2                  0                          0                 0   
3                  1                          1                 1   
4                  0                          1                 1   

   Rear ACVents  Air Quality Control  Height Adjustable Front Seat Belts  \
0             0                    0                                   0   
1             0                    0                                   0   
2             0                    0                                   0   
3             1                    0                                   0   
4             0                    1                                   1   

   Cruise Control  Voice Control  Audio System Remote Control  Leather Seats  \
0               0              0                            0              0   
1               0              0                            0              0   
2               0              0                            0              0   
3               0              0                            0              0   
4               1              1                            1              0   

   Fog Lights Rear  Traction Control  Seat Lumbar Support  Battery Saver  \
0                0                 0                    0              0   
1                0                 0                    0              0   
2                0                 0                    0              0   
3                0                 0                    0              0   
4                0                 0                    0              0   

   Lane Change Indicator  Sun Roof  Automatic Driving Lights  \
0                      0         0                         0   
1                      0         0                         0   
2                      0         0                         0   
3                      0         0                         0   
4                      0         0                         0   

   Anti Theft Alarm  Automatic Head Lamps  Isofix Child Seat Mounts  \
0                 0                     0                         0   
1                 0                     0                         0   
2                 0                     0                         0   
3                 0                     0                         0   
4                 0                     0                         0   

   Hill Assist  Tailgate Ajar  Brake Assist  Steering Wheel Gearshift Paddles  \
0            0              0             0                                 0   
1            0              0             0                                 0   
2            0              0             0                                 0   
3            0              0             0                                 0   
4            0              0             0                                 0   

   LEDTaillights  Cigarette Lighter  Rain Sensing Wiper  Drive Modes  \
0              0                  0                   0            0   
1              0                  0                   0            0   
2              0                  0                   0            0   
3              0                  0                   0            0   
4              0                  0                   0            0   

   Active Noise Cancellation  Adjustable Headrest  Hands Free Tailgate  \
0                          0                    0                    0   
1                          0                    0                    0   
2                          0                    0                    0   
3                          0                    0                    0   
4                          0                    0                    0   

   Dual Tone Dashboard  Leather Wrap Gear Shift Selector  \
0                    0                                 0   
1                    0                                 0   
2                    0                                 0   
3                    0                                 0   
4                    0                                 0   

   Dual Tone Body Colour  LEDDRLs  LEDHeadlights  Cornering Headlamps  \
0                      0        0              0                    0   
1                      0        0              0                    0   
2                      0        0              0                    0   
3                      0        0              0                    0   
4                      0        0              0                    0   

   Cornering Foglamps  Side Air Bag Front  Side Air Bag Rear  \
0                   0                   0                  0   
1                   0                   0                  0   
2                   0                   0                  0   
3                   0                   0                  0   
4                   0                   0                  0   

   Tyre Pressure Monitor  Clutch Lock  Anti Pinch Power Windows  Knee Airbags  \
0                      0            0                         0             0   
1                      0            0                         0             0   
2                      0            0                         0             0   
3                      0            0                         0             0   
4                      0            0                         0             0   

   Apple Car Play  Android Auto  Mirror Link  Wireless Phone Charging  \
0               0             0            0                        0   
1               0             0            0                        0   
2               0             0            0                        0   
3               0             0            0                        0   
4               0             0            0                        0   

   Compass  Moon Roof  Projector Headlamps  Speed Alert  \
0        0          0                    0            0   
1        0          0                    0            0   
2        0          0                    0            0   
3        0          0                    0            0   
4        0          0                    0            0   

   Eletronic Stability Control  Touch Screen Size  Xenon Headlamps  \
0                            0                  0                0   
1                            0                  0                0   
2                            0                  0                0   
3                            0                  0                0   
4                            0                  0                0   

   Cd Changer  Power Boot  Rear Folding Table  Smoke Headlamps  Dvd Player  \
0           0           0                   0                0           0   
1           0           0                   0                0           0   
2           0           0                   0                0           0   
3           0           0                   0                0           0   
4           0           0                   0                0           0   

   Internal Storage  Rear Entertainment System  Remote Engine Start Stop  \
0                 0                          0                         0   
1                 0                          0                         0   
2                 0                          0                         0   
3                 0                          0                         0   
4                 0                          0                         0   

   Ventilated Seats  LEDFog Lamps  View360Camera  Geo Fence Alert  \
0                 0             0              0                0   
1                 0             0              0                0   
2                 0             0              0                0   
3                 0             0              0                0   
4                 0             0              0                0   

   Steering Mounted Tripmeter  Remote Climate Control  \
0                           0                       0   
1                           0                       0   
2                           0                       0   
3                           0                       0   
4                           0                       0   

   Remote Horn Light Control  Heated Wing Mirror  Side Stepper  \
0                          0                   0             0   
1                          0                   0             0   
2                          0                   0             0   
3                          0                   0             0   
4                          0                   0             0   

   Blind Spot Monitor  Hill Descent Control  Heads Up Display  \
0                   0                     0                 0   
1                   0                     0                 0   
2                   0                     0                 0   
3                   0                     0                 0   
4                   0                     0                 0   

   Sos Emergency Assistance  Cassette Player  Find My Car Location  \
0                         0                0                     0   
1                         0                0                     0   
2                         0                0                     0   
3                         0                0                     0   
4                         0                0                     0   

   Wifi Connectivity  Headlamp Washers  Real Time Vehicle Tracking  \
0                  0               0.0                           0   
1                  0               0.0                           0   
2                  0               0.0                           0   
3                  0               0.0                           0   
4                  0               0.0                           0   

   Roof Carrier  Smart Key Band  Lane Watch Camera  Removable Convertible Top  \
0             0             0.0                  0                          0   
1             0             0.0                  0                          0   
2             0             0.0                  0                          0   
3             0             0.0                  0                          0   
4             0             0.0                  0                          0   

   Power Folding3rd Row Seat  Mileage  Max Power  Torque   Color  \
0                        0.0    23.10      67.04   90.00   White   
1                        0.0    17.00     121.31  150.00   White   
2                        0.0    23.84      84.00  114.00     Red   
3                        0.0    19.10      81.86  113.75  Others   
4                        0.0    23.65      88.50  200.00    Gray   

                Engine Type  No of Cylinder  Values per Cylinder  \
0               K10B Engine             3.0                  4.0   
1      Ti-VCT Petrol Engine             3.0                  4.0   
2           Revotron Engine             3.0                  4.0   
3  Kappa VTVT Petrol Engine             4.0                  4.0   
4    DDiS 200 Diesel Engine             4.0                  4.0   

  Value Configuration Fuel Suppy System Turbo Charger Super Charger  Length  \
0                DOHC              MPFi            No            No  3715.0   
1                DOHC  Direct Injection            No            No  3998.0   
2                DOHC              MPFi            No            No  3746.0   
3                DOHC  Direct Injection            No            No  3995.0   
4                DOHC              MPFI           Yes            No  4300.0   

    Width  Height  Wheel Base  Front Tread  Rear Tread  Kerb Weight  \
0  1635.0  1565.0      2425.0       1420.0      1410.0        835.0   
1  1765.0  1647.0      2519.0       1490.0      1495.0       1242.0   
2  1647.0  1535.0      2400.0       1400.0      1420.0       1012.0   
3  1660.0  1520.0      2425.0       1479.0      1493.0       1180.0   
4  1785.0  1595.0      2600.0       1490.0      1495.0       1230.0   

   Gross Weight  Gear Box Drive Type Steering Type  Turning Radius  \
0        1250.0       5.0        FWD         Power             4.7   
1        1660.0       5.0        FWD         Power             5.3   
2        1505.0       5.0        FWD         Power             4.9   
3        1505.0       5.0        FWD         Power             4.7   
4        1670.0       5.0        FWD         Power             5.2   

  Front Brake Type Rear Brake Type  Top Speed  Acceleration         Tyre Type  \
0  Ventilated Disc            Drum      150.0         15.05  Tubeless, Radial   
1  Ventilated Disc            Drum      170.0         12.90   Tubeless,Radial   
2             Disc            Drum      150.0         14.30          Tubeless   
3            Disc             Drum      172.0         14.20   Tubeless,Radial   
4  Ventilated Disc      Solid Disc      190.0         12.00   Tubeless,Radial   

   No Door Numbers  Cargo Volumn  Wheel Size  Alloy Wheel Size       city  
0              5.0         235.0        16.0              16.0  Bangalore  
1              4.0         352.0        16.0              16.0  Bangalore  
2              5.0         242.0        14.0              14.0  Bangalore  
3              4.0         407.0        14.0              14.0  Bangalore  
4              5.0         353.0        16.0              16.0  Bangalore  

[75]
df=pd.read_csv("all_cities_cars_cleaned_final_filled.csv")
df.isnull().sum()
it                                                  0
ft                                                  0
bt                                                  0
km                                                  0
transmission                                        0
ownerNo                                             0
oem                                                 0
model                                               0
modelYear                                           0
centralVariantId                                    0
variantName                                         0
price                                               0
Insurance Validity                                  8
Seats                                               6
RTO                                                 0
Engine Displacement                                 0
Power Steering                                      0
Power Windows Front                                 0
Air Conditioner                                     0
Heater                                              0
Adjustable Head Lights                              0
Manually Adjustable Exterior Rear View Mirror       0
Centeral Locking                                    0
Child Safety Locks                                  0
Power Windows Rear                                  0
Remote Trunk Opener                                 0
Remote Fuel Lid Opener                              0
Low Fuel Warning Light                              0
Accessory Power Outlet                              0
Vanity Mirror                                       0
Rear Seat Headrest                                  0
Cup Holders Front                                   0
Digital Odometer                                    0
Electronic Multi Tripmeter                          0
Fabric Upholstery                                   0
Glove Compartment                                   0
Digital Clock                                       0
Wheel Covers                                        0
Power Antenna                                       0
Chrome Grille                                       0
Day Night Rear View Mirror                          0
Passenger Side Rear View Mirror                     0
Halogen Headlamps                                   0
Rear Seat Belts                                     0
Door Ajar Warning                                   0
Side Impact Beams                                   0
Front Impact Beams                                  0
Adjustable Seats                                    0
Centrally Mounted Fuel Tank                         0
Engine Immobilizer                                  0
Anti Theft Device                                   0
Fog Lights Front                                    0
Anti Lock Braking System                            0
Cd Player                                           0
Trunk Light                                         0
Multifunction Steering Wheel                        0
Navigation System                                   0
Smart Access Card Entry                             0
Engine Start Stop Button                            0
Gear Shift Indicator                                0
Luggage Hook And Net                                0
Adjustable Steering                                 0
Tachometer                                          0
Leather Steering Wheel                              0
Outside Temperature Display                         0
Height Adjustable Driver Seat                       0
Power Adjustable Exterior Rear View Mirror          0
Electric Folding Rear View Mirror                   0
Rear Window Wiper                                   0
Rear Window Washer                                  0
Rear Window Defogger                                0
Alloy Wheels                                        0
Integrated Antenna                                  0
Outside Rear View Mirror Turn Indicators            0
Roof Rail                                           0
Power Door Locks                                    0
Driver Air Bag                                      0
Passenger Air Bag                                   0
Seat Belt Warning                                   0
Keyless Entry                                       0
Engine Check Warning                                0
Crash Sensor                                        0
Ebd                                                 0
Follow Me Home Headlamps                            0
Rear Camera                                         0
Speed Sensing Auto Door Lock                        0
Pretensioners And Force Limiter Seatbelts           0
Impact Sensing Auto Door Lock                       0
No Of Airbags                                       0
Radio                                               0
Speakers Front                                      0
Speakers Rear                                       0
Integrated2Din Audio                                0
Usb Auxiliary Input                                 0
Bluetooth                                           0
Touch Screen                                        0
Number Of Speaker                                   0
Glove Box Cooling                                   0
Driving Experience Control Eco                      0
Tinted Glass                                        0
Rear Spoiler                                        0
Chrome Garnish                                      0
Vehicle Stability Control System                    0
Rear Reading Lamp                                   0
Rear Seat Centre Arm Rest                           0
Cup Holders Rear                                    0
Rear ACVents                                        0
Air Quality Control                                 0
Height Adjustable Front Seat Belts                  0
Cruise Control                                      0
Voice Control                                       0
Audio System Remote Control                         0
Leather Seats                                       0
Fog Lights Rear                                     0
Traction Control                                    0
Seat Lumbar Support                                 0
Battery Saver                                       0
Lane Change Indicator                               0
Sun Roof                                            0
Automatic Driving Lights                            0
Anti Theft Alarm                                    0
Automatic Head Lamps                                0
Isofix Child Seat Mounts                            0
Hill Assist                                         0
Tailgate Ajar                                       0
Brake Assist                                        0
Steering Wheel Gearshift Paddles                    0
LEDTaillights                                       0
Cigarette Lighter                                   0
Rain Sensing Wiper                                  0
Drive Modes                                         0
Active Noise Cancellation                           0
Adjustable Headrest                                 0
Hands Free Tailgate                                 0
Dual Tone Dashboard                                 0
Leather Wrap Gear Shift Selector                    0
Dual Tone Body Colour                               0
LEDDRLs                                             0
LEDHeadlights                                       0
Cornering Headlamps                                 0
Cornering Foglamps                                  0
Side Air Bag Front                                  0
Side Air Bag Rear                                   0
Tyre Pressure Monitor                               0
Clutch Lock                                         0
Anti Pinch Power Windows                            0
Knee Airbags                                        0
Apple Car Play                                      0
Android Auto                                        0
Mirror Link                                         0
Wireless Phone Charging                             0
Compass                                             0
Moon Roof                                           0
Projector Headlamps                                 0
Speed Alert                                         0
Eletronic Stability Control                         0
Touch Screen Size                                   0
Xenon Headlamps                                     0
Cd Changer                                          0
Power Boot                                          0
Rear Folding Table                                  0
Smoke Headlamps                                     0
Dvd Player                                          0
Internal Storage                                    0
Rear Entertainment System                           0
Remote Engine Start Stop                            0
Ventilated Seats                                    0
LEDFog Lamps                                        0
View360Camera                                       0
Geo Fence Alert                                     0
Steering Mounted Tripmeter                          0
Remote Climate Control                              0
Remote Horn Light Control                           0
Heated Wing Mirror                                  0
Side Stepper                                        0
Blind Spot Monitor                                  0
Hill Descent Control                                0
Heads Up Display                                    0
Sos Emergency Assistance                            0
Cassette Player                                     0
Find My Car Location                                0
Wifi Connectivity                                   0
Headlamp Washers                                 1483
Real Time Vehicle Tracking                          0
Roof Carrier                                        0
Smart Key Band                                   1483
Lane Watch Camera                                   0
Removable Convertible Top                           0
Power Folding3rd Row Seat                        2501
Mileage                                             0
Max Power                                           0
Torque                                            129
Color                                               0
Engine Type                                         0
No of Cylinder                                      0
Values per Cylinder                                 0
Value Configuration                                 0
Fuel Suppy System                                   0
Turbo Charger                                       0
Super Charger                                       0
Length                                              0
Width                                               0
Height                                              0
Wheel Base                                          0
Front Tread                                         0
Rear Tread                                          0
Kerb Weight                                         0
Gross Weight                                        0
Gear Box                                            0
Drive Type                                          0
Steering Type                                       0
Turning Radius                                      0
Front Brake Type                                    0
Rear Brake Type                                     0
Top Speed                                           0
Acceleration                                        0
Tyre Type                                           0
No Door Numbers                                     0
Cargo Volumn                                        0
Wheel Size                                          0
Alloy Wheel Size                                    0
city                                                0
dtype: int64
[77]
df.dtypes
it                                                 int64
ft                                                object
bt                                                object
km                                                 int64
transmission                                      object
ownerNo                                            int64
oem                                               object
model                                             object
modelYear                                          int64
centralVariantId                                   int64
variantName                                       object
price                                              int64
Insurance Validity                                object
Seats                                            float64
RTO                                               object
Engine Displacement                              float64
Power Steering                                     int64
Power Windows Front                                int64
Air Conditioner                                    int64
Heater                                             int64
Adjustable Head Lights                             int64
Manually Adjustable Exterior Rear View Mirror      int64
Centeral Locking                                   int64
Child Safety Locks                                 int64
Power Windows Rear                                 int64
Remote Trunk Opener                                int64
Remote Fuel Lid Opener                             int64
Low Fuel Warning Light                             int64
Accessory Power Outlet                             int64
Vanity Mirror                                      int64
Rear Seat Headrest                                 int64
Cup Holders Front                                  int64
Digital Odometer                                   int64
Electronic Multi Tripmeter                         int64
Fabric Upholstery                                  int64
Glove Compartment                                  int64
Digital Clock                                      int64
Wheel Covers                                       int64
Power Antenna                                      int64
Chrome Grille                                      int64
Day Night Rear View Mirror                         int64
Passenger Side Rear View Mirror                    int64
Halogen Headlamps                                  int64
Rear Seat Belts                                    int64
Door Ajar Warning                                  int64
Side Impact Beams                                  int64
Front Impact Beams                                 int64
Adjustable Seats                                   int64
Centrally Mounted Fuel Tank                        int64
Engine Immobilizer                                 int64
Anti Theft Device                                  int64
Fog Lights Front                                   int64
Anti Lock Braking System                           int64
Cd Player                                          int64
Trunk Light                                        int64
Multifunction Steering Wheel                       int64
Navigation System                                  int64
Smart Access Card Entry                            int64
Engine Start Stop Button                           int64
Gear Shift Indicator                               int64
Luggage Hook And Net                               int64
Adjustable Steering                                int64
Tachometer                                         int64
Leather Steering Wheel                             int64
Outside Temperature Display                        int64
Height Adjustable Driver Seat                      int64
Power Adjustable Exterior Rear View Mirror         int64
Electric Folding Rear View Mirror                  int64
Rear Window Wiper                                  int64
Rear Window Washer                                 int64
Rear Window Defogger                               int64
Alloy Wheels                                       int64
Integrated Antenna                                 int64
Outside Rear View Mirror Turn Indicators           int64
Roof Rail                                          int64
Power Door Locks                                   int64
Driver Air Bag                                     int64
Passenger Air Bag                                  int64
Seat Belt Warning                                  int64
Keyless Entry                                      int64
Engine Check Warning                               int64
Crash Sensor                                       int64
Ebd                                                int64
Follow Me Home Headlamps                           int64
Rear Camera                                        int64
Speed Sensing Auto Door Lock                       int64
Pretensioners And Force Limiter Seatbelts          int64
Impact Sensing Auto Door Lock                      int64
No Of Airbags                                      int64
Radio                                              int64
Speakers Front                                     int64
Speakers Rear                                      int64
Integrated2Din Audio                               int64
Usb Auxiliary Input                                int64
Bluetooth                                          int64
Touch Screen                                       int64
Number Of Speaker                                  int64
Glove Box Cooling                                  int64
Driving Experience Control Eco                     int64
Tinted Glass                                       int64
Rear Spoiler                                       int64
Chrome Garnish                                     int64
Vehicle Stability Control System                   int64
Rear Reading Lamp                                  int64
Rear Seat Centre Arm Rest                          int64
Cup Holders Rear                                   int64
Rear ACVents                                       int64
Air Quality Control                                int64
Height Adjustable Front Seat Belts                 int64
Cruise Control                                     int64
Voice Control                                      int64
Audio System Remote Control                        int64
Leather Seats                                      int64
Fog Lights Rear                                    int64
Traction Control                                   int64
Seat Lumbar Support                                int64
Battery Saver                                      int64
Lane Change Indicator                              int64
Sun Roof                                           int64
Automatic Driving Lights                           int64
Anti Theft Alarm                                   int64
Automatic Head Lamps                               int64
Isofix Child Seat Mounts                           int64
Hill Assist                                        int64
Tailgate Ajar                                      int64
Brake Assist                                       int64
Steering Wheel Gearshift Paddles                   int64
LEDTaillights                                      int64
Cigarette Lighter                                  int64
Rain Sensing Wiper                                 int64
Drive Modes                                        int64
Active Noise Cancellation                          int64
Adjustable Headrest                                int64
Hands Free Tailgate                                int64
Dual Tone Dashboard                                int64
Leather Wrap Gear Shift Selector                   int64
Dual Tone Body Colour                              int64
LEDDRLs                                            int64
LEDHeadlights                                      int64
Cornering Headlamps                                int64
Cornering Foglamps                                 int64
Side Air Bag Front                                 int64
Side Air Bag Rear                                  int64
Tyre Pressure Monitor                              int64
Clutch Lock                                        int64
Anti Pinch Power Windows                           int64
Knee Airbags                                       int64
Apple Car Play                                     int64
Android Auto                                       int64
Mirror Link                                        int64
Wireless Phone Charging                            int64
Compass                                            int64
Moon Roof                                          int64
Projector Headlamps                                int64
Speed Alert                                        int64
Eletronic Stability Control                        int64
Touch Screen Size                                  int64
Xenon Headlamps                                    int64
Cd Changer                                         int64
Power Boot                                         int64
Rear Folding Table                                 int64
Smoke Headlamps                                    int64
Dvd Player                                         int64
Internal Storage                                   int64
Rear Entertainment System                          int64
Remote Engine Start Stop                           int64
Ventilated Seats                                   int64
LEDFog Lamps                                       int64
View360Camera                                      int64
Geo Fence Alert                                    int64
Steering Mounted Tripmeter                         int64
Remote Climate Control                             int64
Remote Horn Light Control                          int64
Heated Wing Mirror                                 int64
Side Stepper                                       int64
Blind Spot Monitor                                 int64
Hill Descent Control                               int64
Heads Up Display                                   int64
Sos Emergency Assistance                           int64
Cassette Player                                    int64
Find My Car Location                               int64
Wifi Connectivity                                  int64
Headlamp Washers                                 float64
Real Time Vehicle Tracking                         int64
Roof Carrier                                       int64
Smart Key Band                                   float64
Lane Watch Camera                                  int64
Removable Convertible Top                          int64
Power Folding3rd Row Seat                        float64
Mileage                                          float64
Max Power                                        float64
Torque                                           float64
Color                                             object
Engine Type                                       object
No of Cylinder                                   float64
Values per Cylinder                              float64
Value Configuration                               object
Fuel Suppy System                                 object
Turbo Charger                                     object
Super Charger                                     object
Length                                           float64
Width                                            float64
Height                                           float64
Wheel Base                                       float64
Front Tread                                      float64
Rear Tread                                       float64
Kerb Weight                                      float64
Gross Weight                                     float64
Gear Box                                         float64
Drive Type                                        object
Steering Type                                     object
Turning Radius                                   float64
Front Brake Type                                  object
Rear Brake Type                                   object
Top Speed                                        float64
Acceleration                                     float64
Tyre Type                                         object
No Door Numbers                                  float64
Cargo Volumn                                     float64
Wheel Size                                       float64
Alloy Wheel Size                                 float64
city                                              object
dtype: object
[79]
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Load the dataset
df = pd.read_csv("all_cities_cars_cleaned_final_filled.csv")

# Define categorical columns and numerical columns
categorical_columns = [
    'transmission', 'ft', 'bt', 'Drive Type', 'City', 'Steering Type', 'Engine Type', 
    'Tyre Type', 'Color', 'Insurance Validity', 'RTO', 'Value Configuration', 
    'Front Brake Type', 'Rear Brake Type', 'oem', 'model', 'variantName','city',
    'Fuel Suppy System', 'Turbo Charger', 'Super Charger', 'Drive Type', 'Steering Type'
]

numerical_columns = [
    'it', 'km', 'centralVariantId', 'modelYear', 'ownerNo', 'Mileage', 
    'Seats', 'Engine Displacement', 'Max Power', 'Torque',
    'Length', 'Width', 'Height', 'Wheel Base', 
    'Front Tread', 'Gear Box', 'Turning Radius', 'Rear Tread', 'Kerb Weight', 
    'Rear Brake Type', 'Top Speed', 'Acceleration', 'No Door Numbers', 'Cargo Volumn',
    'No of Cylinder', 'Values per Cylinder', 'Gross Weight', 'Wheel Size', 'Alloy Wheel Size'
]

# Apply Label Encoding to categorical columns
label_encoder = LabelEncoder()
for column in categorical_columns:
    if column in df.columns:  # Check if column exists in DataFrame
        df[column] = label_encoder.fit_transform(df[column].astype(str))

# Normalize numerical columns
min_max_scaler = MinMaxScaler()
df[numerical_columns] = min_max_scaler.fit_transform(df[numerical_columns])

# Fill missing values for numerical columns using median
for col in numerical_columns:
    if col in df.columns:
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)

# Fill missing values for categorical columns using mode
for col in categorical_columns:
    if col in df.columns:
        mode_value = df[col].mode()[0]
        df[col] = df[col].fillna(mode_value)

# Remove outliers using IQR method, including 'price'
def remove_outliers_iqr(df, columns):
    for col in columns:
        if col in df.columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    return df

# Apply outlier removal to specific columns
outlier_columns = numerical_columns + ['price']  # Include 'price' for outlier detection
df = remove_outliers_iqr(df, outlier_columns)

# Save the processed DataFrame
df.to_csv('all_cities_cars_cleaned_final_processed.csv', index=False)

# Display the processed DataFrame
print(df.head())
      it  ft  bt        km  transmission  ownerNo  oem  model  modelYear  \
12   0.0   4   2  0.004182             0      0.2    8     66   0.868421   
54   0.0   4   2  0.008052             1      0.2    9     90   0.894737   
60   0.0   4   2  0.001818             0      0.2   27    238   0.973684   
74   0.0   4   2  0.008028             0      0.4    8     66   0.815789   
105  0.0   4   2  0.011704             0      0.2    8     66   0.868421   

     centralVariantId  variantName   price  Insurance Validity  Seats  RTO  \
12           0.586045         1794  825000                   0  0.375  133   
54           0.613270         1353  715000                   3  0.375  138   
60           0.669611           24  550000                   3  0.375  164   
74           0.120346          160  537000                   0  0.375  133   
105          0.120346          160  755000                   5  0.375  135   

     Engine Displacement  Power Steering  Power Windows Front  \
12                0.2398               1                    1   
54                0.2394               1                    1   
60                0.1998               1                    1   
74                0.2398               1                    1   
105               0.2398               1                    1   

     Air Conditioner  Heater  Adjustable Head Lights  \
12                 1       1                       1   
54                 1       1                       1   
60                 1       1                       1   
74                 1       1                       1   
105                1       1                       1   

     Manually Adjustable Exterior Rear View Mirror  Centeral Locking  \
12                                               0                 1   
54                                               0                 1   
60                                               1                 1   
74                                               0                 1   
105                                              0                 1   

     Child Safety Locks  Power Windows Rear  Remote Trunk Opener  \
12                    1                   1                    1   
54                    1                   1                    0   
60                    1                   1                    0   
74                    1                   1                    0   
105                   1                   1                    0   

     Remote Fuel Lid Opener  Low Fuel Warning Light  Accessory Power Outlet  \
12                        0                       1                       1   
54                        0                       1                       1   
60                        0                       1                       1   
74                        0                       1                       1   
105                       0                       1                       1   

     Vanity Mirror  Rear Seat Headrest  Cup Holders Front  Digital Odometer  \
12               1                   1                  1                 1   
54               1                   1                  1                 1   
60               0                   1                  0                 1   
74               1                   1                  1                 1   
105              1                   1                  1                 1   

     Electronic Multi Tripmeter  Fabric Upholstery  Glove Compartment  \
12                            1                  1                  1   
54                            1                  1                  1   
60                            1                  1                  1   
74                            1                  1                  1   
105                           1                  1                  1   

     Digital Clock  Wheel Covers  Power Antenna  Chrome Grille  \
12               1             0              0              1   
54               1             1              1              1   
60               0             1              1              0   
74               1             0              0              1   
105              1             0              0              1   

     Day Night Rear View Mirror  Passenger Side Rear View Mirror  \
12                            0                                1   
54                            0                                1   
60                            0                                1   
74                            1                                1   
105                           1                                1   

     Halogen Headlamps  Rear Seat Belts  Door Ajar Warning  Side Impact Beams  \
12                   0                1                  1                  1   
54                   1                1                  1                  1   
60                   1                1                  0                  1   
74                   1                1                  1                  1   
105                  1                1                  1                  1   

     Front Impact Beams  Adjustable Seats  Centrally Mounted Fuel Tank  \
12                    1                 1                            1   
54                    1                 1                            1   
60                    1                 1                            1   
74                    1                 1                            1   
105                   1                 1                            1   

     Engine Immobilizer  Anti Theft Device  Fog Lights Front  \
12                    1                  1                 1   
54                    1                  1                 1   
60                    1                  1                 0   
74                    1                  1                 1   
105                   1                  1                 1   

     Anti Lock Braking System  Cd Player  Trunk Light  \
12                          1          1            1   
54                          1          0            0   
60                          1          0            0   
74                          1          1            1   
105                         1          1            1   

     Multifunction Steering Wheel  Navigation System  Smart Access Card Entry  \
12                              1                  1                        1   
54                              1                  0                        0   
60                              0                  1                        0   
74                              1                  0                        0   
105                             1                  0                        0   

     Engine Start Stop Button  Gear Shift Indicator  Luggage Hook And Net  \
12                          1                     1                     0   
54                          0                     1                     0   
60                          0                     0                     0   
74                          0                     0                     0   
105                         0                     0                     0   

     Adjustable Steering  Tachometer  Leather Steering Wheel  \
12                     1           1                       1   
54                     0           1                       0   
60                     0           1                       0   
74                     1           1                       1   
105                    1           1                       1   

     Outside Temperature Display  Height Adjustable Driver Seat  \
12                             1                              1   
54                             0                              0   
60                             0                              0   
74                             1                              1   
105                            1                              1   

     Power Adjustable Exterior Rear View Mirror  \
12                                            1   
54                                            1   
60                                            0   
74                                            1   
105                                           1   

     Electric Folding Rear View Mirror  Rear Window Wiper  Rear Window Washer  \
12                                   1                  1                   1   
54                                   0                  0                   0   
60                                   0                  0                   0   
74                                   1                  1                   1   
105                                  1                  1                   1   

     Rear Window Defogger  Alloy Wheels  Integrated Antenna  \
12                      1             1                   1   
54                      0             0                   0   
60                      0             0                   0   
74                      1             1                   1   
105                     1             1                   1   

     Outside Rear View Mirror Turn Indicators  Roof Rail  Power Door Locks  \
12                                          1          0                 1   
54                                          0          0                 1   
60                                          0          0                 0   
74                                          1          0                 1   
105                                         1          0                 1   

     Driver Air Bag  Passenger Air Bag  Seat Belt Warning  Keyless Entry  \
12                1                  1                  1              1   
54                1                  1                  1              1   
60                1                  1                  1              1   
74                1                  1                  1              1   
105               1                  1                  1              1   

     Engine Check Warning  Crash Sensor  Ebd  Follow Me Home Headlamps  \
12                      1             1    1                         0   
54                      1             1    1                         0   
60                      1             1    1                         0   
74                      0             1    1                         0   
105                     0             1    1                         0   

     Rear Camera  Speed Sensing Auto Door Lock  \
12             1                             1   
54             0                             1   
60             1                             0   
74             1                             0   
105            1                             0   

     Pretensioners And Force Limiter Seatbelts  Impact Sensing Auto Door Lock  \
12                                           0                              0   
54                                           1                              1   
60                                           0                              0   
74                                           0                              0   
105                                          0                              0   

     No Of Airbags  Radio  Speakers Front  Speakers Rear  \
12               1      1               1              1   
54               1      1               1              1   
60               1      1               1              0   
74               0      1               1              1   
105              0      1               1              1   

     Integrated2Din Audio  Usb Auxiliary Input  Bluetooth  Touch Screen  \
12                      1                    1          1             1   
54                      1                    1          1             0   
60                      1                    1          1             1   
74                      1                    1          1             1   
105                     1                    1          1             1   

     Number Of Speaker  Glove Box Cooling  Driving Experience Control Eco  \
12                   1                  0                               1   
54                   1                  1                               0   
60                   1                  0                               0   
74                   1                  0                               0   
105                  1                  0                               0   

     Tinted Glass  Rear Spoiler  Chrome Garnish  \
12              0             0               1   
54              0             1               0   
60              0             1               0   
74              0             0               1   
105             0             0               1   

     Vehicle Stability Control System  Rear Reading Lamp  \
12                                  0                  1   
54                                  0                  0   
60                                  0                  0   
74                                  0                  0   
105                                 0                  0   

     Rear Seat Centre Arm Rest  Cup Holders Rear  Rear ACVents  \
12                           0                 0             0   
54                           0                 0             1   
60                           0                 0             0   
74                           0                 1             0   
105                          0                 1             0   

     Air Quality Control  Height Adjustable Front Seat Belts  Cruise Control  \
12                     1                                   0               1   
54                     0                                   0               0   
60                     0                                   0               0   
74                     1                                   0               0   
105                    1                                   0               0   

     Voice Control  Audio System Remote Control  Leather Seats  \
12               1                            0              0   
54               0                            1              0   
60               1                            0              0   
74               0                            0              0   
105              0                            0              0   

     Fog Lights Rear  Traction Control  Seat Lumbar Support  Battery Saver  \
12                 0                 1                    0              0   
54                 0                 0                    1              1   
60                 0                 0                    1              0   
74                 0                 0                    0              0   
105                0                 0                    0              0   

     Lane Change Indicator  Sun Roof  Automatic Driving Lights  \
12                       1         0                         0   
54                       1         0                         0   
60                       1         0                         0   
74                       1         0                         0   
105                      1         0                         0   

     Anti Theft Alarm  Automatic Head Lamps  Isofix Child Seat Mounts  \
12                  0                     0                         0   
54                  0                     0                         0   
60                  0                     0                         0   
74                  0                     0                         0   
105                 0                     0                         0   

     Hill Assist  Tailgate Ajar  Brake Assist  \
12             0              0             1   
54             0              1             0   
60             0              0             0   
74             0              0             0   
105            0              0             0   

     Steering Wheel Gearshift Paddles  LEDTaillights  Cigarette Lighter  \
12                                  1              1                  0   
54                                  0              0                  0   
60                                  0              1                  0   
74                                  0              0                  0   
105                                 0              0                  0   

     Rain Sensing Wiper  Drive Modes  Active Noise Cancellation  \
12                    0            0                          0   
54                    0            0                          0   
60                    0            0                          0   
74                    0            0                          0   
105                   0            0                          0   

     Adjustable Headrest  Hands Free Tailgate  Dual Tone Dashboard  \
12                     0                    0                    0   
54                     0                    0                    1   
60                     0                    0                    0   
74                     0                    0                    0   
105                    0                    0                    0   

     Leather Wrap Gear Shift Selector  Dual Tone Body Colour  LEDDRLs  \
12                                  0                      0        0   
54                                  0                      0        0   
60                                  0                      0        1   
74                                  0                      0        0   
105                                 0                      0        0   

     LEDHeadlights  Cornering Headlamps  Cornering Foglamps  \
12               0                    0                   0   
54               0                    0                   0   
60               0                    0                   0   
74               0                    0                   0   
105              0                    0                   0   

     Side Air Bag Front  Side Air Bag Rear  Tyre Pressure Monitor  \
12                    0                  0                      0   
54                    0                  0                      0   
60                    0                  0                      0   
74                    0                  0                      0   
105                   0                  0                      0   

     Clutch Lock  Anti Pinch Power Windows  Knee Airbags  Apple Car Play  \
12             0                         0             0               0   
54             1                         0             0               0   
60             0                         0             0               1   
74             0                         0             0               0   
105            0                         0             0               0   

     Android Auto  Mirror Link  Wireless Phone Charging  Compass  Moon Roof  \
12              0            0                        0        0          0   
54              0            0                        0        0          0   
60              1            0                        0        0          0   
74              0            0                        0        0          0   
105             0            0                        0        0          0   

     Projector Headlamps  Speed Alert  Eletronic Stability Control  \
12                     0            0                            0   
54                     0            0                            0   
60                     0            1                            0   
74                     0            0                            0   
105                    0            0                            0   

     Touch Screen Size  Xenon Headlamps  Cd Changer  Power Boot  \
12                   0                0           0           0   
54                   0                0           0           0   
60                   0                0           0           0   
74                   0                0           0           0   
105                  0                0           0           0   

     Rear Folding Table  Smoke Headlamps  Dvd Player  Internal Storage  \
12                    0                0           0                 0   
54                    0                0           0                 0   
60                    0                0           0                 0   
74                    0                0           0                 0   
105                   0                0           0                 0   

     Rear Entertainment System  Remote Engine Start Stop  Ventilated Seats  \
12                           0                         0                 0   
54                           0                         0                 0   
60                           0                         0                 0   
74                           0                         0                 0   
105                          0                         0                 0   

     LEDFog Lamps  View360Camera  Geo Fence Alert  Steering Mounted Tripmeter  \
12              0              0                0                           0   
54              0              0                0                           0   
60              0              0                0                           0   
74              0              0                0                           0   
105             0              0                0                           0   

     Remote Climate Control  Remote Horn Light Control  Heated Wing Mirror  \
12                        0                          0                   0   
54                        0                          0                   0   
60                        0                          0                   0   
74                        0                          0                   0   
105                       0                          0                   0   

     Side Stepper  Blind Spot Monitor  Hill Descent Control  Heads Up Display  \
12              0                   0                     0                 0   
54              0                   0                     0                 0   
60              0                   0                     0                 0   
74              0                   0                     0                 0   
105             0                   0                     0                 0   

     Sos Emergency Assistance  Cassette Player  Find My Car Location  \
12                          0                0                     0   
54                          0                0                     0   
60                          0                0                     0   
74                          0                0                     0   
105                         0                0                     0   

     Wifi Connectivity  Headlamp Washers  Real Time Vehicle Tracking  \
12                   0               0.0                           0   
54                   0               0.0                           0   
60                   0               0.0                           0   
74                   0               0.0                           0   
105                  0               0.0                           0   

     Roof Carrier  Smart Key Band  Lane Watch Camera  \
12              0             0.0                  0   
54              0             0.0                  0   
60              0             0.0                  0   
74              0             0.0                  0   
105             0             0.0                  0   

     Removable Convertible Top  Power Folding3rd Row Seat   Mileage  \
12                           0                        0.0  0.083659   
54                           0                        0.0  0.086669   
60                           0                        0.0  0.112248   
74                           0                        0.0  0.089678   
105                          0                        0.0  0.089678   

     Max Power    Torque  Color  Engine Type  No of Cylinder  \
12    0.000075  0.123119     57          476        0.095238   
54    0.000067  0.131414     57          320        0.095238   
60    0.000049  0.100604     86          344        0.047619   
74    0.000075  0.123119    138          476        0.095238   
105   0.000075  0.123119     57          476        0.095238   

     Values per Cylinder  Value Configuration  Fuel Suppy System  \
12              0.029851                    6                 61   
54              0.029851                    1                 46   
60              0.029851                    1                 50   
74              0.029851                    6                 61   
105             0.029851                    6                 61   

     Turbo Charger  Super Charger    Length     Width    Height  Wheel Base  \
12               0              0  0.394293  0.350617  0.362093    0.452459   
54               0              0  0.406350  0.400000  0.306931    0.478689   
60               0              0  0.304260  0.208642  0.263083    0.381639   
74               0              0  0.394293  0.350617  0.362093    0.452459   
105              0              0  0.394293  0.350617  0.362093    0.452459   

     Front Tread  Rear Tread  Kerb Weight  Gross Weight  Gear Box  Drive Type  \
12          0.57    0.473602     0.197290      0.202811  0.013699           5   
54          0.57    0.473602     0.220152      0.202811  0.013699           5   
60          0.57    0.473602     0.063506      0.202811  0.013699           5   
74          0.57    0.473602     0.197290      0.202811  0.013699           5   
105         0.57    0.473602     0.197290      0.202811  0.013699           5   

     Steering Type  Turning Radius  Front Brake Type  Rear Brake Type  \
12               6        0.000176                 5         0.205882   
54               6        0.000192                 5         0.205882   
60               1        0.000144                 5         0.205882   
74               6        0.000176                 5         0.205882   
105              6        0.000176                 5         0.205882   

     Top Speed  Acceleration  Tyre Type  No Door Numbers  Cargo Volumn  \
12    0.400000      0.375940         26             0.75      0.001246   
54    0.391304      0.357143         26             0.75      0.000981   
60    0.391304      0.345865         26             0.75      0.000958   
74    0.400000      0.375940         26             0.75      0.001246   
105   0.400000      0.375940         26             0.75      0.001246   

     Wheel Size  Alloy Wheel Size  city  
12     0.333333          0.333333     0  
54     0.444444          0.444444     0  
60     0.444444          0.444444     0  
74     0.333333          0.333333     0  
105    0.333333          0.333333     0  

[81]
import pandas as pd

# Load the dataset
df = pd.read_csv("all_cities_cars_cleaned_final_processed.csv")

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Descriptive Statistics for Numerical Columns
print("\nDescriptive Statistics for Numerical Columns:")
print(df.describe(include=[float, int]))

# Mean of each numerical column
mean_values = df.mean()
print("\nMean values of numerical columns:")
print(mean_values)

# Median of each numerical column
median_values = df.median()
print("\nMedian values of numerical columns:")
print(median_values)

# Mode of each numerical column
mode_values = df.mode().iloc[0]  # Mode can return multiple values, we take the first
print("\nMode values of numerical columns:")
print(mode_values)

# Standard Deviation of each numerical column
std_dev_values = df.std()
print("\nStandard deviation of numerical columns:")
print(std_dev_values)

# Additional statistics if needed
# Variance
variance_values = df.var()
print("\nVariance of numerical columns:")
print(variance_values)

# Count of unique values in each column
unique_counts = df.nunique()
print("\nUnique value counts in each column:")
print(unique_counts)

# Check for missing values
missing_values = df.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

# Display correlation matrix
print("\nCorrelation matrix:")
print(df.corr())



First few rows of the DataFrame:
    it  ft  bt        km  transmission  ownerNo  oem  model  modelYear  \
0  0.0   4   2  0.004182             0      0.2    8     66   0.868421   
1  0.0   4   2  0.008052             1      0.2    9     90   0.894737   
2  0.0   4   2  0.001818             0      0.2   27    238   0.973684   
3  0.0   4   2  0.008028             0      0.4    8     66   0.815789   
4  0.0   4   2  0.011704             0      0.2    8     66   0.868421   

   centralVariantId  variantName   price  Insurance Validity  Seats  RTO  \
0          0.586045         1794  825000                   0  0.375  133   
1          0.613270         1353  715000                   3  0.375  138   
2          0.669611           24  550000                   3  0.375  164   
3          0.120346          160  537000                   0  0.375  133   
4          0.120346          160  755000                   5  0.375  135   

   Engine Displacement  Power Steering  Power Windows Front  Air Conditioner  \
0               0.2398               1                    1                1   
1               0.2394               1                    1                1   
2               0.1998               1                    1                1   
3               0.2398               1                    1                1   
4               0.2398               1                    1                1   

   Heater  Adjustable Head Lights  \
0       1                       1   
1       1                       1   
2       1                       1   
3       1                       1   
4       1                       1   

   Manually Adjustable Exterior Rear View Mirror  Centeral Locking  \
0                                              0                 1   
1                                              0                 1   
2                                              1                 1   
3                                              0                 1   
4                                              0                 1   

   Child Safety Locks  Power Windows Rear  Remote Trunk Opener  \
0                   1                   1                    1   
1                   1                   1                    0   
2                   1                   1                    0   
3                   1                   1                    0   
4                   1                   1                    0   

   Remote Fuel Lid Opener  Low Fuel Warning Light  Accessory Power Outlet  \
0                       0                       1                       1   
1                       0                       1                       1   
2                       0                       1                       1   
3                       0                       1                       1   
4                       0                       1                       1   

   Vanity Mirror  Rear Seat Headrest  Cup Holders Front  Digital Odometer  \
0              1                   1                  1                 1   
1              1                   1                  1                 1   
2              0                   1                  0                 1   
3              1                   1                  1                 1   
4              1                   1                  1                 1   

   Electronic Multi Tripmeter  Fabric Upholstery  Glove Compartment  \
0                           1                  1                  1   
1                           1                  1                  1   
2                           1                  1                  1   
3                           1                  1                  1   
4                           1                  1                  1   

   Digital Clock  Wheel Covers  Power Antenna  Chrome Grille  \
0              1             0              0              1   
1              1             1              1              1   
2              0             1              1              0   
3              1             0              0              1   
4              1             0              0              1   

   Day Night Rear View Mirror  Passenger Side Rear View Mirror  \
0                           0                                1   
1                           0                                1   
2                           0                                1   
3                           1                                1   
4                           1                                1   

   Halogen Headlamps  Rear Seat Belts  Door Ajar Warning  Side Impact Beams  \
0                  0                1                  1                  1   
1                  1                1                  1                  1   
2                  1                1                  0                  1   
3                  1                1                  1                  1   
4                  1                1                  1                  1   

   Front Impact Beams  Adjustable Seats  Centrally Mounted Fuel Tank  \
0                   1                 1                            1   
1                   1                 1                            1   
2                   1                 1                            1   
3                   1                 1                            1   
4                   1                 1                            1   

   Engine Immobilizer  Anti Theft Device  Fog Lights Front  \
0                   1                  1                 1   
1                   1                  1                 1   
2                   1                  1                 0   
3                   1                  1                 1   
4                   1                  1                 1   

   Anti Lock Braking System  Cd Player  Trunk Light  \
0                         1          1            1   
1                         1          0            0   
2                         1          0            0   
3                         1          1            1   
4                         1          1            1   

   Multifunction Steering Wheel  Navigation System  Smart Access Card Entry  \
0                             1                  1                        1   
1                             1                  0                        0   
2                             0                  1                        0   
3                             1                  0                        0   
4                             1                  0                        0   

   Engine Start Stop Button  Gear Shift Indicator  Luggage Hook And Net  \
0                         1                     1                     0   
1                         0                     1                     0   
2                         0                     0                     0   
3                         0                     0                     0   
4                         0                     0                     0   

   Adjustable Steering  Tachometer  Leather Steering Wheel  \
0                    1           1                       1   
1                    0           1                       0   
2                    0           1                       0   
3                    1           1                       1   
4                    1           1                       1   

   Outside Temperature Display  Height Adjustable Driver Seat  \
0                            1                              1   
1                            0                              0   
2                            0                              0   
3                            1                              1   
4                            1                              1   

   Power Adjustable Exterior Rear View Mirror  \
0                                           1   
1                                           1   
2                                           0   
3                                           1   
4                                           1   

   Electric Folding Rear View Mirror  Rear Window Wiper  Rear Window Washer  \
0                                  1                  1                   1   
1                                  0                  0                   0   
2                                  0                  0                   0   
3                                  1                  1                   1   
4                                  1                  1                   1   

   Rear Window Defogger  Alloy Wheels  Integrated Antenna  \
0                     1             1                   1   
1                     0             0                   0   
2                     0             0                   0   
3                     1             1                   1   
4                     1             1                   1   

   Outside Rear View Mirror Turn Indicators  Roof Rail  Power Door Locks  \
0                                         1          0                 1   
1                                         0          0                 1   
2                                         0          0                 0   
3                                         1          0                 1   
4                                         1          0                 1   

   Driver Air Bag  Passenger Air Bag  Seat Belt Warning  Keyless Entry  \
0               1                  1                  1              1   
1               1                  1                  1              1   
2               1                  1                  1              1   
3               1                  1                  1              1   
4               1                  1                  1              1   

   Engine Check Warning  Crash Sensor  Ebd  Follow Me Home Headlamps  \
0                     1             1    1                         0   
1                     1             1    1                         0   
2                     1             1    1                         0   
3                     0             1    1                         0   
4                     0             1    1                         0   

   Rear Camera  Speed Sensing Auto Door Lock  \
0            1                             1   
1            0                             1   
2            1                             0   
3            1                             0   
4            1                             0   

   Pretensioners And Force Limiter Seatbelts  Impact Sensing Auto Door Lock  \
0                                          0                              0   
1                                          1                              1   
2                                          0                              0   
3                                          0                              0   
4                                          0                              0   

   No Of Airbags  Radio  Speakers Front  Speakers Rear  Integrated2Din Audio  \
0              1      1               1              1                     1   
1              1      1               1              1                     1   
2              1      1               1              0                     1   
3              0      1               1              1                     1   
4              0      1               1              1                     1   

   Usb Auxiliary Input  Bluetooth  Touch Screen  Number Of Speaker  \
0                    1          1             1                  1   
1                    1          1             0                  1   
2                    1          1             1                  1   
3                    1          1             1                  1   
4                    1          1             1                  1   

   Glove Box Cooling  Driving Experience Control Eco  Tinted Glass  \
0                  0                               1             0   
1                  1                               0             0   
2                  0                               0             0   
3                  0                               0             0   
4                  0                               0             0   

   Rear Spoiler  Chrome Garnish  Vehicle Stability Control System  \
0             0               1                                 0   
1             1               0                                 0   
2             1               0                                 0   
3             0               1                                 0   
4             0               1                                 0   

   Rear Reading Lamp  Rear Seat Centre Arm Rest  Cup Holders Rear  \
0                  1                          0                 0   
1                  0                          0                 0   
2                  0                          0                 0   
3                  0                          0                 1   
4                  0                          0                 1   

   Rear ACVents  Air Quality Control  Height Adjustable Front Seat Belts  \
0             0                    1                                   0   
1             1                    0                                   0   
2             0                    0                                   0   
3             0                    1                                   0   
4             0                    1                                   0   

   Cruise Control  Voice Control  Audio System Remote Control  Leather Seats  \
0               1              1                            0              0   
1               0              0                            1              0   
2               0              1                            0              0   
3               0              0                            0              0   
4               0              0                            0              0   

   Fog Lights Rear  Traction Control  Seat Lumbar Support  Battery Saver  \
0                0                 1                    0              0   
1                0                 0                    1              1   
2                0                 0                    1              0   
3                0                 0                    0              0   
4                0                 0                    0              0   

   Lane Change Indicator  Sun Roof  Automatic Driving Lights  \
0                      1         0                         0   
1                      1         0                         0   
2                      1         0                         0   
3                      1         0                         0   
4                      1         0                         0   

   Anti Theft Alarm  Automatic Head Lamps  Isofix Child Seat Mounts  \
0                 0                     0                         0   
1                 0                     0                         0   
2                 0                     0                         0   
3                 0                     0                         0   
4                 0                     0                         0   

   Hill Assist  Tailgate Ajar  Brake Assist  Steering Wheel Gearshift Paddles  \
0            0              0             1                                 1   
1            0              1             0                                 0   
2            0              0             0                                 0   
3            0              0             0                                 0   
4            0              0             0                                 0   

   LEDTaillights  Cigarette Lighter  Rain Sensing Wiper  Drive Modes  \
0              1                  0                   0            0   
1              0                  0                   0            0   
2              1                  0                   0            0   
3              0                  0                   0            0   
4              0                  0                   0            0   

   Active Noise Cancellation  Adjustable Headrest  Hands Free Tailgate  \
0                          0                    0                    0   
1                          0                    0                    0   
2                          0                    0                    0   
3                          0                    0                    0   
4                          0                    0                    0   

   Dual Tone Dashboard  Leather Wrap Gear Shift Selector  \
0                    0                                 0   
1                    1                                 0   
2                    0                                 0   
3                    0                                 0   
4                    0                                 0   

   Dual Tone Body Colour  LEDDRLs  LEDHeadlights  Cornering Headlamps  \
0                      0        0              0                    0   
1                      0        0              0                    0   
2                      0        1              0                    0   
3                      0        0              0                    0   
4                      0        0              0                    0   

   Cornering Foglamps  Side Air Bag Front  Side Air Bag Rear  \
0                   0                   0                  0   
1                   0                   0                  0   
2                   0                   0                  0   
3                   0                   0                  0   
4                   0                   0                  0   

   Tyre Pressure Monitor  Clutch Lock  Anti Pinch Power Windows  Knee Airbags  \
0                      0            0                         0             0   
1                      0            1                         0             0   
2                      0            0                         0             0   
3                      0            0                         0             0   
4                      0            0                         0             0   

   Apple Car Play  Android Auto  Mirror Link  Wireless Phone Charging  \
0               0             0            0                        0   
1               0             0            0                        0   
2               1             1            0                        0   
3               0             0            0                        0   
4               0             0            0                        0   

   Compass  Moon Roof  Projector Headlamps  Speed Alert  \
0        0          0                    0            0   
1        0          0                    0            0   
2        0          0                    0            1   
3        0          0                    0            0   
4        0          0                    0            0   

   Eletronic Stability Control  Touch Screen Size  Xenon Headlamps  \
0                            0                  0                0   
1                            0                  0                0   
2                            0                  0                0   
3                            0                  0                0   
4                            0                  0                0   

   Cd Changer  Power Boot  Rear Folding Table  Smoke Headlamps  Dvd Player  \
0           0           0                   0                0           0   
1           0           0                   0                0           0   
2           0           0                   0                0           0   
3           0           0                   0                0           0   
4           0           0                   0                0           0   

   Internal Storage  Rear Entertainment System  Remote Engine Start Stop  \
0                 0                          0                         0   
1                 0                          0                         0   
2                 0                          0                         0   
3                 0                          0                         0   
4                 0                          0                         0   

   Ventilated Seats  LEDFog Lamps  View360Camera  Geo Fence Alert  \
0                 0             0              0                0   
1                 0             0              0                0   
2                 0             0              0                0   
3                 0             0              0                0   
4                 0             0              0                0   

   Steering Mounted Tripmeter  Remote Climate Control  \
0                           0                       0   
1                           0                       0   
2                           0                       0   
3                           0                       0   
4                           0                       0   

   Remote Horn Light Control  Heated Wing Mirror  Side Stepper  \
0                          0                   0             0   
1                          0                   0             0   
2                          0                   0             0   
3                          0                   0             0   
4                          0                   0             0   

   Blind Spot Monitor  Hill Descent Control  Heads Up Display  \
0                   0                     0                 0   
1                   0                     0                 0   
2                   0                     0                 0   
3                   0                     0                 0   
4                   0                     0                 0   

   Sos Emergency Assistance  Cassette Player  Find My Car Location  \
0                         0                0                     0   
1                         0                0                     0   
2                         0                0                     0   
3                         0                0                     0   
4                         0                0                     0   

   Wifi Connectivity  Headlamp Washers  Real Time Vehicle Tracking  \
0                  0               0.0                           0   
1                  0               0.0                           0   
2                  0               0.0                           0   
3                  0               0.0                           0   
4                  0               0.0                           0   

   Roof Carrier  Smart Key Band  Lane Watch Camera  Removable Convertible Top  \
0             0             0.0                  0                          0   
1             0             0.0                  0                          0   
2             0             0.0                  0                          0   
3             0             0.0                  0                          0   
4             0             0.0                  0                          0   

   Power Folding3rd Row Seat   Mileage  Max Power    Torque  Color  \
0                        0.0  0.083659   0.000075  0.123119     57   
1                        0.0  0.086669   0.000067  0.131414     57   
2                        0.0  0.112248   0.000049  0.100604     86   
3                        0.0  0.089678   0.000075  0.123119    138   
4                        0.0  0.089678   0.000075  0.123119     57   

   Engine Type  No of Cylinder  Values per Cylinder  Value Configuration  \
0          476        0.095238             0.029851                    6   
1          320        0.095238             0.029851                    1   
2          344        0.047619             0.029851                    1   
3          476        0.095238             0.029851                    6   
4          476        0.095238             0.029851                    6   

   Fuel Suppy System  Turbo Charger  Super Charger    Length     Width  \
0                 61              0              0  0.394293  0.350617   
1                 46              0              0  0.406350  0.400000   
2                 50              0              0  0.304260  0.208642   
3                 61              0              0  0.394293  0.350617   
4                 61              0              0  0.394293  0.350617   

     Height  Wheel Base  Front Tread  Rear Tread  Kerb Weight  Gross Weight  \
0  0.362093    0.452459         0.57    0.473602     0.197290      0.202811   
1  0.306931    0.478689         0.57    0.473602     0.220152      0.202811   
2  0.263083    0.381639         0.57    0.473602     0.063506      0.202811   
3  0.362093    0.452459         0.57    0.473602     0.197290      0.202811   
4  0.362093    0.452459         0.57    0.473602     0.197290      0.202811   

   Gear Box  Drive Type  Steering Type  Turning Radius  Front Brake Type  \
0  0.013699           5              6        0.000176                 5   
1  0.013699           5              6        0.000192                 5   
2  0.013699           5              1        0.000144                 5   
3  0.013699           5              6        0.000176                 5   
4  0.013699           5              6        0.000176                 5   

   Rear Brake Type  Top Speed  Acceleration  Tyre Type  No Door Numbers  \
0         0.205882   0.400000      0.375940         26             0.75   
1         0.205882   0.391304      0.357143         26             0.75   
2         0.205882   0.391304      0.345865         26             0.75   
3         0.205882   0.400000      0.375940         26             0.75   
4         0.205882   0.400000      0.375940         26             0.75   

   Cargo Volumn  Wheel Size  Alloy Wheel Size  city  
0      0.001246    0.333333          0.333333     0  
1      0.000981    0.444444          0.444444     0  
2      0.000958    0.444444          0.444444     0  
3      0.001246    0.333333          0.333333     0  
4      0.001246    0.333333          0.333333     0  

Descriptive Statistics for Numerical Columns:
          it          ft          bt          km  transmission     ownerNo  \
count  931.0  931.000000  931.000000  931.000000    931.000000  931.000000   
mean     0.0    3.440387    3.833512    0.009050      0.854995    0.255639   
std      0.0    1.194720    2.655324    0.006085      0.352296    0.103060   
min      0.0    0.000000    2.000000    0.000143      0.000000    0.000000   
25%      0.0    4.000000    2.000000    0.003991      1.000000    0.200000   
50%      0.0    4.000000    2.000000    0.007636      1.000000    0.200000   
75%      0.0    4.000000    7.000000    0.012727      1.000000    0.400000   
max      0.0    4.000000    8.000000    0.027405      1.000000    0.600000   

              oem       model   modelYear  centralVariantId  variantName  \
count  931.000000  931.000000  931.000000        931.000000   931.000000   
mean    16.042965  143.564984    0.861072          0.484849  1172.528464   
std      9.601315   89.622547    0.088472          0.239237   708.623601   
min      2.000000   27.000000    0.578947          0.038763     0.000000   
25%      8.000000   66.000000    0.815789          0.234968   211.500000   
50%      9.000000   90.000000    0.868421          0.527540  1413.000000   
75%     27.000000  238.000000    0.947368          0.669657  1764.000000   
max     31.000000  300.000000    1.000000          0.980438  2116.000000   

              price  Insurance Validity    Seats         RTO  \
count  9.310000e+02          931.000000  931.000  931.000000   
mean   5.335349e+05            1.878625    0.375  268.597207   
std    2.046234e+05            1.425303    0.000  124.357350   
min    8.000000e+04            0.000000    0.375    7.000000   
25%    3.800000e+05            0.000000    0.375  141.500000   
50%    5.230000e+05            3.000000    0.375  277.000000   
75%    6.865000e+05            3.000000    0.375  403.000000   
max    1.150000e+06            5.000000    0.375  456.000000   

       Engine Displacement  Power Steering  Power Windows Front  \
count           931.000000      931.000000           931.000000   
mean              0.234080        0.978518             0.923738   
std               0.024868        0.145063             0.265560   
min               0.159800        0.000000             0.000000   
25%               0.239400        1.000000             1.000000   
50%               0.239600        1.000000             1.000000   
75%               0.239800        1.000000             1.000000   
max               0.319200        1.000000             1.000000   

       Air Conditioner      Heater  Adjustable Head Lights  \
count       931.000000  931.000000              931.000000   
mean          0.974221    0.965628                0.948443   
std           0.158560    0.182280                0.221251   
min           0.000000    0.000000                0.000000   
25%           1.000000    1.000000                1.000000   
50%           1.000000    1.000000                1.000000   
75%           1.000000    1.000000                1.000000   
max           1.000000    1.000000                1.000000   

       Manually Adjustable Exterior Rear View Mirror  Centeral Locking  \
count                                     931.000000        931.000000   
mean                                        0.270677          0.918367   
std                                         0.444548          0.273951   
min                                         0.000000          0.000000   
25%                                         0.000000          1.000000   
50%                                         0.000000          1.000000   
75%                                         1.000000          1.000000   
max                                         1.000000          1.000000   

       Child Safety Locks  Power Windows Rear  Remote Trunk Opener  \
count          931.000000          931.000000           931.000000   
mean             0.865736            0.783029             0.402793   
std              0.341119            0.412404             0.490723   
min              0.000000            0.000000             0.000000   
25%              1.000000            1.000000             0.000000   
50%              1.000000            1.000000             0.000000   
75%              1.000000            1.000000             1.000000   
max              1.000000            1.000000             1.000000   

       Remote Fuel Lid Opener  Low Fuel Warning Light  Accessory Power Outlet  \
count              931.000000              931.000000              931.000000   
mean                 0.258861                0.968851                0.970999   
std                  0.438245                0.173814                0.167900   
min                  0.000000                0.000000                0.000000   
25%                  0.000000                1.000000                1.000000   
50%                  0.000000                1.000000                1.000000   
75%                  1.000000                1.000000                1.000000   
max                  1.000000                1.000000                1.000000   

       Vanity Mirror  Rear Seat Headrest  Cup Holders Front  Digital Odometer  \
count     931.000000          931.000000         931.000000        931.000000   
mean        0.654135            0.854995           0.689581          0.866810   
std         0.475905            0.352296           0.462914          0.339963   
min         0.000000            0.000000           0.000000          0.000000   
25%         0.000000            1.000000           0.000000          1.000000   
50%         1.000000            1.000000           1.000000          1.000000   
75%         1.000000            1.000000           1.000000          1.000000   
max         1.000000            1.000000           1.000000          1.000000   

       Electronic Multi Tripmeter  Fabric Upholstery  Glove Compartment  \
count                  931.000000         931.000000         931.000000   
mean                     0.928034           0.949517           0.975295   
std                      0.258570           0.219058           0.155307   
min                      0.000000           0.000000           0.000000   
25%                      1.000000           1.000000           1.000000   
50%                      1.000000           1.000000           1.000000   
75%                      1.000000           1.000000           1.000000   
max                      1.000000           1.000000           1.000000   

       Digital Clock  Wheel Covers  Power Antenna  Chrome Grille  \
count     931.000000    931.000000     931.000000     931.000000   
mean        0.871106      0.489796       0.522019       0.520945   
std         0.335262      0.500165       0.499783       0.499830   
min         0.000000      0.000000       0.000000       0.000000   
25%         1.000000      0.000000       0.000000       0.000000   
50%         1.000000      0.000000       1.000000       1.000000   
75%         1.000000      1.000000       1.000000       1.000000   
max         1.000000      1.000000       1.000000       1.000000   

       Day Night Rear View Mirror  Passenger Side Rear View Mirror  \
count                  931.000000                       931.000000   
mean                     0.613319                         0.970999   
std                      0.487251                         0.167900   
min                      0.000000                         0.000000   
25%                      0.000000                         1.000000   
50%                      1.000000                         1.000000   
75%                      1.000000                         1.000000   
max                      1.000000                         1.000000   

       Halogen Headlamps  Rear Seat Belts  Door Ajar Warning  \
count         931.000000       931.000000         931.000000   
mean            0.862513         0.944146           0.661654   
std             0.344545         0.229763           0.473401   
min             0.000000         0.000000           0.000000   
25%             1.000000         1.000000           0.000000   
50%             1.000000         1.000000           1.000000   
75%             1.000000         1.000000           1.000000   
max             1.000000         1.000000           1.000000   

       Side Impact Beams  Front Impact Beams  Adjustable Seats  \
count         931.000000          931.000000        931.000000   
mean            0.711063            0.619764          0.972073   
std             0.453512            0.485706          0.164852   
min             0.000000            0.000000          0.000000   
25%             0.000000            0.000000          1.000000   
50%             1.000000            1.000000          1.000000   
75%             1.000000            1.000000          1.000000   
max             1.000000            1.000000          1.000000   

       Centrally Mounted Fuel Tank  Engine Immobilizer  Anti Theft Device  \
count                   931.000000          931.000000         931.000000   
mean                      0.684211            0.928034           0.551020   
std                       0.465079            0.258570           0.497657   
min                       0.000000            0.000000           0.000000   
25%                       0.000000            1.000000           0.000000   
50%                       1.000000            1.000000           1.000000   
75%                       1.000000            1.000000           1.000000   
max                       1.000000            1.000000           1.000000   

       Fog Lights Front  Anti Lock Braking System   Cd Player  Trunk Light  \
count        931.000000                931.000000  931.000000   931.000000   
mean           0.599356                  0.802363    0.296455     0.471536   
std            0.490292                  0.398431    0.456940     0.499457   
min            0.000000                  0.000000    0.000000     0.000000   
25%            0.000000                  1.000000    0.000000     0.000000   
50%            1.000000                  1.000000    0.000000     0.000000   
75%            1.000000                  1.000000    1.000000     1.000000   
max            1.000000                  1.000000    1.000000     1.000000   

       Multifunction Steering Wheel  Navigation System  \
count                    931.000000         931.000000   
mean                       0.615467           0.310419   
std                        0.486746           0.462914   
min                        0.000000           0.000000   
25%                        0.000000           0.000000   
50%                        1.000000           0.000000   
75%                        1.000000           1.000000   
max                        1.000000           1.000000   

       Smart Access Card Entry  Engine Start Stop Button  \
count               931.000000                931.000000   
mean                  0.125671                  0.203008   
std                   0.331657                  0.402454   
min                   0.000000                  0.000000   
25%                   0.000000                  0.000000   
50%                   0.000000                  0.000000   
75%                   0.000000                  0.000000   
max                   1.000000                  1.000000   

       Gear Shift Indicator  Luggage Hook And Net  Adjustable Steering  \
count            931.000000            931.000000           931.000000   
mean               0.366273              0.013963             0.779807   
std                0.482044              0.117402             0.414600   
min                0.000000              0.000000             0.000000   
25%                0.000000              0.000000             1.000000   
50%                0.000000              0.000000             1.000000   
75%                1.000000              0.000000             1.000000   
max                1.000000              1.000000             1.000000   

       Tachometer  Leather Steering Wheel  Outside Temperature Display  \
count  931.000000              931.000000                   931.000000   
mean     0.874329                0.268528                     0.245972   
std      0.331657                0.443432                     0.430894   
min      0.000000                0.000000                     0.000000   
25%      1.000000                0.000000                     0.000000   
50%      1.000000                0.000000                     0.000000   
75%      1.000000                1.000000                     0.000000   
max      1.000000                1.000000                     1.000000   

       Height Adjustable Driver Seat  \
count                     931.000000   
mean                        0.483351   
std                         0.499991   
min                         0.000000   
25%                         0.000000   
50%                         0.000000   
75%                         1.000000   
max                         1.000000   

       Power Adjustable Exterior Rear View Mirror  \
count                                  931.000000   
mean                                     0.721805   
std                                      0.448351   
min                                      0.000000   
25%                                      0.000000   
50%                                      1.000000   
75%                                      1.000000   
max                                      1.000000   

       Electric Folding Rear View Mirror  Rear Window Wiper  \
count                         931.000000         931.000000   
mean                            0.444683           0.329753   
std                             0.497198           0.470376   
min                             0.000000           0.000000   
25%                             0.000000           0.000000   
50%                             0.000000           0.000000   
75%                             1.000000           1.000000   
max                             1.000000           1.000000   

       Rear Window Washer  Rear Window Defogger  Alloy Wheels  \
count          931.000000            931.000000    931.000000   
mean             0.277121              0.513426      0.402793   
std              0.447818              0.500088      0.490723   
min              0.000000              0.000000      0.000000   
25%              0.000000              0.000000      0.000000   
50%              0.000000              1.000000      0.000000   
75%              1.000000              1.000000      1.000000   
max              1.000000              1.000000      1.000000   

       Integrated Antenna  Outside Rear View Mirror Turn Indicators  \
count          931.000000                                931.000000   
mean             0.397422                                  0.526316   
std              0.489628                                  0.499575   
min              0.000000                                  0.000000   
25%              0.000000                                  0.000000   
50%              0.000000                                  1.000000   
75%              1.000000                                  1.000000   
max              1.000000                                  1.000000   

        Roof Rail  Power Door Locks  Driver Air Bag  Passenger Air Bag  \
count  931.000000        931.000000      931.000000         931.000000   
mean     0.254565          0.796992        0.790548           0.721805   
std      0.435851          0.402454        0.407136           0.448351   
min      0.000000          0.000000        0.000000           0.000000   
25%      0.000000          1.000000        1.000000           0.000000   
50%      0.000000          1.000000        1.000000           1.000000   
75%      1.000000          1.000000        1.000000           1.000000   
max      1.000000          1.000000        1.000000           1.000000   

       Seat Belt Warning  Keyless Entry  Engine Check Warning  Crash Sensor  \
count         931.000000     931.000000            931.000000    931.000000   
mean            0.882922       0.824919              0.657358      0.783029   
std             0.321687       0.380240              0.474848      0.412404   
min             0.000000       0.000000              0.000000      0.000000   
25%             1.000000       1.000000              0.000000      1.000000   
50%             1.000000       1.000000              1.000000      1.000000   
75%             1.000000       1.000000              1.000000      1.000000   
max             1.000000       1.000000              1.000000      1.000000   

              Ebd  Follow Me Home Headlamps  Rear Camera  \
count  931.000000                931.000000   931.000000   
mean     0.752954                  0.135338     0.466165   
std      0.431526                  0.342268     0.499122   
min      0.000000                  0.000000     0.000000   
25%      1.000000                  0.000000     0.000000   
50%      1.000000                  0.000000     0.000000   
75%      1.000000                  0.000000     1.000000   
max      1.000000                  1.000000     1.000000   

       Speed Sensing Auto Door Lock  \
count                    931.000000   
mean                       0.481203   
std                        0.499915   
min                        0.000000   
25%                        0.000000   
50%                        0.000000   
75%                        1.000000   
max                        1.000000   

       Pretensioners And Force Limiter Seatbelts  \
count                                 931.000000   
mean                                    0.389903   
std                                     0.487990   
min                                     0.000000   
25%                                     0.000000   
50%                                     0.000000   
75%                                     1.000000   
max                                     1.000000   

       Impact Sensing Auto Door Lock  No Of Airbags       Radio  \
count                     931.000000     931.000000  931.000000   
mean                        0.278195       0.610097    0.867884   
std                         0.448351       0.487990    0.338799   
min                         0.000000       0.000000    0.000000   
25%                         0.000000       0.000000    1.000000   
50%                         0.000000       1.000000    1.000000   
75%                         1.000000       1.000000    1.000000   
max                         1.000000       1.000000    1.000000   

       Speakers Front  Speakers Rear  Integrated2Din Audio  \
count      931.000000     931.000000            931.000000   
mean         0.873255       0.688507              0.668099   
std          0.332866       0.463353              0.471149   
min          0.000000       0.000000              0.000000   
25%          1.000000       0.000000              0.000000   
50%          1.000000       1.000000              1.000000   
75%          1.000000       1.000000              1.000000   
max          1.000000       1.000000              1.000000   

       Usb Auxiliary Input   Bluetooth  Touch Screen  Number Of Speaker  \
count           931.000000  931.000000    931.000000         931.000000   
mean              0.755102    0.711063      0.497315           0.657358   
std               0.430258    0.453512      0.500262           0.474848   
min               0.000000    0.000000      0.000000           0.000000   
25%               1.000000    0.000000      0.000000           0.000000   
50%               1.000000    1.000000      0.000000           1.000000   
75%               1.000000    1.000000      1.000000           1.000000   
max               1.000000    1.000000      1.000000           1.000000   

       Glove Box Cooling  Driving Experience Control Eco  Tinted Glass  \
count         931.000000                      931.000000    931.000000   
mean            0.158969                        0.166488      0.208378   
std             0.365844                        0.372718      0.406367   
min             0.000000                        0.000000      0.000000   
25%             0.000000                        0.000000      0.000000   
50%             0.000000                        0.000000      0.000000   
75%             0.000000                        0.000000      0.000000   
max             1.000000                        1.000000      1.000000   

       Rear Spoiler  Chrome Garnish  Vehicle Stability Control System  \
count    931.000000      931.000000                        931.000000   
mean       0.481203        0.288937                          0.034372   
std        0.499915        0.453512                          0.182280   
min        0.000000        0.000000                          0.000000   
25%        0.000000        0.000000                          0.000000   
50%        0.000000        0.000000                          0.000000   
75%        1.000000        1.000000                          0.000000   
max        1.000000        1.000000                          1.000000   

       Rear Reading Lamp  Rear Seat Centre Arm Rest  Cup Holders Rear  \
count         931.000000                 931.000000        931.000000   
mean            0.220193                   0.222342          0.343716   
std             0.414600                   0.416043          0.475203   
min             0.000000                   0.000000          0.000000   
25%             0.000000                   0.000000          0.000000   
50%             0.000000                   0.000000          0.000000   
75%             0.000000                   0.000000          1.000000   
max             1.000000                   1.000000          1.000000   

       Rear ACVents  Air Quality Control  Height Adjustable Front Seat Belts  \
count    931.000000           931.000000                          931.000000   
mean       0.189044             0.247046                            0.190118   
std        0.391754             0.431526                            0.392605   
min        0.000000             0.000000                            0.000000   
25%        0.000000             0.000000                            0.000000   
50%        0.000000             0.000000                            0.000000   
75%        0.000000             0.000000                            0.000000   
max        1.000000             1.000000                            1.000000   

       Cruise Control  Voice Control  Audio System Remote Control  \
count      931.000000     931.000000                   931.000000   
mean         0.098818       0.364125                     0.121375   
std          0.298579       0.481442                     0.326738   
min          0.000000       0.000000                     0.000000   
25%          0.000000       0.000000                     0.000000   
50%          0.000000       0.000000                     0.000000   
75%          0.000000       1.000000                     0.000000   
max          1.000000       1.000000                     1.000000   

       Leather Seats  Fog Lights Rear  Traction Control  Seat Lumbar Support  \
count     931.000000       931.000000        931.000000           931.000000   
mean        0.040816         0.134264          0.045113             0.298604   
std         0.197971         0.341119          0.207663             0.457892   
min         0.000000         0.000000          0.000000             0.000000   
25%         0.000000         0.000000          0.000000             0.000000   
50%         0.000000         0.000000          0.000000             0.000000   
75%         0.000000         0.000000          0.000000             1.000000   
max         1.000000         1.000000          1.000000             1.000000   

       Battery Saver  Lane Change Indicator    Sun Roof  \
count     931.000000             931.000000  931.000000   
mean        0.129968               0.285714    0.068743   
std         0.336449               0.451997    0.253153   
min         0.000000               0.000000    0.000000   
25%         0.000000               0.000000    0.000000   
50%         0.000000               0.000000    0.000000   
75%         0.000000               1.000000    0.000000   
max         1.000000               1.000000    1.000000   

       Automatic Driving Lights  Anti Theft Alarm  Automatic Head Lamps  \
count                931.000000        931.000000            931.000000   
mean                   0.017186          0.276047              0.085929   
std                    0.130033          0.447281              0.280410   
min                    0.000000          0.000000              0.000000   
25%                    0.000000          0.000000              0.000000   
50%                    0.000000          0.000000              0.000000   
75%                    0.000000          1.000000              0.000000   
max                    1.000000          1.000000              1.000000   

       Isofix Child Seat Mounts  Hill Assist  Tailgate Ajar  Brake Assist  \
count                931.000000   931.000000     931.000000    931.000000   
mean                   0.293233     0.061224       0.207304      0.053706   
std                    0.455489     0.239870       0.405593      0.225557   
min                    0.000000     0.000000       0.000000      0.000000   
25%                    0.000000     0.000000       0.000000      0.000000   
50%                    0.000000     0.000000       0.000000      0.000000   
75%                    1.000000     0.000000       0.000000      0.000000   
max                    1.000000     1.000000       1.000000      1.000000   

       Steering Wheel Gearshift Paddles  LEDTaillights  Cigarette Lighter  \
count                        931.000000     931.000000         931.000000   
mean                           0.029001       0.157895           0.009667   
std                            0.167900       0.364838           0.097897   
min                            0.000000       0.000000           0.000000   
25%                            0.000000       0.000000           0.000000   
50%                            0.000000       0.000000           0.000000   
75%                            0.000000       0.000000           0.000000   
max                            1.000000       1.000000           1.000000   

       Rain Sensing Wiper  Drive Modes  Active Noise Cancellation  \
count          931.000000   931.000000                      931.0   
mean             0.047261     0.042965                        0.0   
std              0.212311     0.202886                        0.0   
min              0.000000     0.000000                        0.0   
25%              0.000000     0.000000                        0.0   
50%              0.000000     0.000000                        0.0   
75%              0.000000     0.000000                        0.0   
max              1.000000     1.000000                        0.0   

       Adjustable Headrest  Hands Free Tailgate  Dual Tone Dashboard  \
count           931.000000           931.000000           931.000000   
mean              0.250269             0.003222             0.351235   
std               0.433400             0.056705             0.477613   
min               0.000000             0.000000             0.000000   
25%               0.000000             0.000000             0.000000   
50%               0.000000             0.000000             0.000000   
75%               0.500000             0.000000             1.000000   
max               1.000000             1.000000             1.000000   

       Leather Wrap Gear Shift Selector  Dual Tone Body Colour     LEDDRLs  \
count                        931.000000             931.000000  931.000000   
mean                           0.036520               0.004296    0.270677   
std                            0.187681               0.065442    0.444548   
min                            0.000000               0.000000    0.000000   
25%                            0.000000               0.000000    0.000000   
50%                            0.000000               0.000000    0.000000   
75%                            0.000000               0.000000    1.000000   
max                            1.000000               1.000000    1.000000   

       LEDHeadlights  Cornering Headlamps  Cornering Foglamps  \
count     931.000000           931.000000          931.000000   
mean        0.042965             0.017186            0.026853   
std         0.202886             0.130033            0.161740   
min         0.000000             0.000000            0.000000   
25%         0.000000             0.000000            0.000000   
50%         0.000000             0.000000            0.000000   
75%         0.000000             0.000000            0.000000   
max         1.000000             1.000000            1.000000   

       Side Air Bag Front  Side Air Bag Rear  Tyre Pressure Monitor  \
count          931.000000         931.000000             931.000000   
mean             0.021482           0.002148               0.064447   
std              0.145063           0.046324               0.245679   
min              0.000000           0.000000               0.000000   
25%              0.000000           0.000000               0.000000   
50%              0.000000           0.000000               0.000000   
75%              0.000000           0.000000               0.000000   
max              1.000000           1.000000               1.000000   

       Clutch Lock  Anti Pinch Power Windows  Knee Airbags  Apple Car Play  \
count   931.000000                931.000000         931.0      931.000000   
mean      0.035446                  0.119227           0.0        0.272825   
std       0.185003                  0.324229           0.0        0.445651   
min       0.000000                  0.000000           0.0        0.000000   
25%       0.000000                  0.000000           0.0        0.000000   
50%       0.000000                  0.000000           0.0        0.000000   
75%       0.000000                  0.000000           0.0        1.000000   
max       1.000000                  1.000000           0.0        1.000000   

       Android Auto  Mirror Link  Wireless Phone Charging  Compass  \
count    931.000000        931.0               931.000000    931.0   
mean       0.272825          0.0                 0.036520      0.0   
std        0.445651          0.0                 0.187681      0.0   
min        0.000000          0.0                 0.000000      0.0   
25%        0.000000          0.0                 0.000000      0.0   
50%        0.000000          0.0                 0.000000      0.0   
75%        1.000000          0.0                 0.000000      0.0   
max        1.000000          0.0                 1.000000      0.0   

        Moon Roof  Projector Headlamps  Speed Alert  \
count  931.000000           931.000000   931.000000   
mean     0.025779             0.124597     0.324382   
std      0.158560             0.330439     0.468395   
min      0.000000             0.000000     0.000000   
25%      0.000000             0.000000     0.000000   
50%      0.000000             0.000000     0.000000   
75%      0.000000             0.000000     1.000000   
max      1.000000             1.000000     1.000000   

       Eletronic Stability Control  Touch Screen Size  Xenon Headlamps  \
count                   931.000000         931.000000            931.0   
mean                      0.059076           0.127820              0.0   
std                       0.235894           0.334068              0.0   
min                       0.000000           0.000000              0.0   
25%                       0.000000           0.000000              0.0   
50%                       0.000000           0.000000              0.0   
75%                       0.000000           0.000000              0.0   
max                       1.000000           1.000000              0.0   

       Cd Changer  Power Boot  Rear Folding Table  Smoke Headlamps  \
count       931.0  931.000000               931.0       931.000000   
mean          0.0    0.024705                 0.0         0.041890   
std           0.0    0.155307                 0.0         0.200446   
min           0.0    0.000000                 0.0         0.000000   
25%           0.0    0.000000                 0.0         0.000000   
50%           0.0    0.000000                 0.0         0.000000   
75%           0.0    0.000000                 0.0         0.000000   
max           0.0    1.000000                 0.0         1.000000   

       Dvd Player  Internal Storage  Rear Entertainment System  \
count  931.000000             931.0                      931.0   
mean     0.020408               0.0                        0.0   
std      0.141468               0.0                        0.0   
min      0.000000               0.0                        0.0   
25%      0.000000               0.0                        0.0   
50%      0.000000               0.0                        0.0   
75%      0.000000               0.0                        0.0   
max      1.000000               0.0                        0.0   

       Remote Engine Start Stop  Ventilated Seats  LEDFog Lamps  \
count                931.000000             931.0    931.000000   
mean                   0.011815               0.0      0.046187   
std                    0.108112               0.0      0.210002   
min                    0.000000               0.0      0.000000   
25%                    0.000000               0.0      0.000000   
50%                    0.000000               0.0      0.000000   
75%                    0.000000               0.0      0.000000   
max                    1.000000               0.0      1.000000   

       View360Camera  Geo Fence Alert  Steering Mounted Tripmeter  \
count     931.000000       931.000000                       931.0   
mean        0.005371         0.010741                         0.0   
std         0.073126         0.103137                         0.0   
min         0.000000         0.000000                         0.0   
25%         0.000000         0.000000                         0.0   
50%         0.000000         0.000000                         0.0   
75%         0.000000         0.000000                         0.0   
max         1.000000         1.000000                         0.0   

       Remote Climate Control  Remote Horn Light Control  Heated Wing Mirror  \
count              931.000000                      931.0               931.0   
mean                 0.008593                        0.0                 0.0   
std                  0.092348                        0.0                 0.0   
min                  0.000000                        0.0                 0.0   
25%                  0.000000                        0.0                 0.0   
50%                  0.000000                        0.0                 0.0   
75%                  0.000000                        0.0                 0.0   
max                  1.000000                        0.0                 0.0   

       Side Stepper  Blind Spot Monitor  Hill Descent Control  \
count         931.0               931.0                 931.0   
mean            0.0                 0.0                   0.0   
std             0.0                 0.0                   0.0   
min             0.0                 0.0                   0.0   
25%             0.0                 0.0                   0.0   
50%             0.0                 0.0                   0.0   
75%             0.0                 0.0                   0.0   
max             0.0                 0.0                   0.0   

       Heads Up Display  Sos Emergency Assistance  Cassette Player  \
count             931.0                931.000000            931.0   
mean                0.0                  0.011815              0.0   
std                 0.0                  0.108112              0.0   
min                 0.0                  0.000000              0.0   
25%                 0.0                  0.000000              0.0   
50%                 0.0                  0.000000              0.0   
75%                 0.0                  0.000000              0.0   
max                 0.0                  1.000000              0.0   

       Find My Car Location  Wifi Connectivity  Headlamp Washers  \
count            931.000000         931.000000             766.0   
mean               0.019334           0.008593               0.0   
std                0.137770           0.092348               0.0   
min                0.000000           0.000000               0.0   
25%                0.000000           0.000000               0.0   
50%                0.000000           0.000000               0.0   
75%                0.000000           0.000000               0.0   
max                1.000000           1.000000               0.0   

       Real Time Vehicle Tracking  Roof Carrier  Smart Key Band  \
count                  931.000000         931.0      766.000000   
mean                     0.002148           0.0        0.001305   
std                      0.046324           0.0        0.036131   
min                      0.000000           0.0        0.000000   
25%                      0.000000           0.0        0.000000   
50%                      0.000000           0.0        0.000000   
75%                      0.000000           0.0        0.000000   
max                      1.000000           0.0        1.000000   

       Lane Watch Camera  Removable Convertible Top  \
count              931.0                      931.0   
mean                 0.0                        0.0   
std                  0.0                        0.0   
min                  0.0                        0.0   
25%                  0.0                        0.0   
50%                  0.0                        0.0   
75%                  0.0                        0.0   
max                  0.0                        0.0   

       Power Folding3rd Row Seat     Mileage   Max Power      Torque  \
count                      644.0  931.000000  931.000000  931.000000   
mean                         0.0    0.098373    0.000065    0.136174   
std                          0.0    0.018157    0.000012    0.037990   
min                          0.0    0.056575    0.000033    0.078090   
25%                          0.0    0.084412    0.000058    0.121934   
50%                          0.0    0.097201    0.000067    0.126674   
75%                          0.0    0.112248    0.000075    0.129044   
max                          0.0    0.148360    0.000110    0.247541   

            Color  Engine Type  No of Cylinder  Values per Cylinder  \
count  931.000000   931.000000      931.000000         9.310000e+02   
mean    86.070892   262.929108        0.079024         2.985075e-02   
std     42.624837   177.355791        0.022578         3.506025e-16   
min      1.000000     1.000000        0.047619         2.985075e-02   
25%     57.000000    47.500000        0.047619         2.985075e-02   
50%     86.000000   278.000000        0.095238         2.985075e-02   
75%    116.000000   473.000000        0.095238         2.985075e-02   
max    138.000000   476.000000        0.095238         2.985075e-02   

       Value Configuration  Fuel Suppy System  Turbo Charger  Super Charger  \
count           931.000000         931.000000     931.000000     931.000000   
mean              2.593985          42.252417       0.156821       0.001074   
std               2.354252          16.366162       0.363827       0.032774   
min               1.000000           3.000000       0.000000       0.000000   
25%               1.000000          46.000000       0.000000       0.000000   
50%               1.000000          46.000000       0.000000       0.000000   
75%               6.000000          50.000000       0.000000       0.000000   
max              10.000000          67.000000       1.000000       1.000000   

           Length       Width      Height  Wheel Base  Front Tread  \
count  931.000000  931.000000  931.000000  931.000000   931.000000   
mean     0.360300    0.335630    0.346392    0.410257     0.569280   
std      0.063389    0.069595    0.060170    0.037982     0.002586   
min      0.182878    0.185185    0.196605    0.333115     0.560000   
25%      0.311093    0.329630    0.306931    0.382623     0.570000   
50%      0.394293    0.345679    0.342291    0.400000     0.570000   
75%      0.410370    0.362963    0.377652    0.445902     0.570000   
max      0.512460    0.469136    0.561528    0.485246     0.570000   

         Rear Tread  Kerb Weight  Gross Weight      Gear Box  Drive Type  \
count  9.310000e+02   931.000000  9.310000e+02  9.310000e+02  931.000000   
mean   4.736025e-01     0.164883  2.028112e-01  1.369863e-02    5.002148   
std    2.832590e-15     0.059005  4.526591e-15  2.516701e-16    0.046324   
min    4.736025e-01     0.031753  2.028112e-01  1.369863e-02    5.000000   
25%    4.736025e-01     0.135478  2.028112e-01  1.369863e-02    5.000000   
50%    4.736025e-01     0.187130  2.028112e-01  1.369863e-02    5.000000   
75%    4.736025e-01     0.211685  2.028112e-01  1.369863e-02    5.000000   
max    4.736025e-01     0.296359  2.028112e-01  1.369863e-02    6.000000   

       Steering Type  Turning Radius  Front Brake Type  Rear Brake Type  \
count     931.000000      931.000000        931.000000     9.310000e+02   
mean        3.718582        0.000153          8.673469     2.058824e-01   
std         2.439872        0.000033          7.005124     2.777049e-15   
min         1.000000        0.000080          5.000000     2.058824e-01   
25%         1.000000        0.000128          5.000000     2.058824e-01   
50%         6.000000        0.000160          5.000000     2.058824e-01   
75%         6.000000        0.000176          5.000000     2.058824e-01   
max         6.000000        0.000224         24.000000     2.058824e-01   

        Top Speed  Acceleration   Tyre Type  No Door Numbers  Cargo Volumn  \
count  931.000000    931.000000  931.000000       931.000000    931.000000   
mean     0.378864      0.369737   24.088077         0.697637      0.001123   
std      0.022050      0.031761    5.356413         0.101784      0.000218   
min      0.304348      0.300752    0.000000         0.500000      0.000540   
25%      0.366348      0.345865   23.000000         0.750000      0.000958   
50%      0.391304      0.345865   26.000000         0.750000      0.001230   
75%      0.391304      0.387218   26.000000         0.750000      0.001246   
max      0.400000      0.436466   33.000000         0.750000      0.001499   

       Wheel Size  Alloy Wheel Size        city  
count  931.000000        931.000000  931.000000  
mean     0.387278          0.387278    2.622986  
std      0.081516          0.081516    1.736598  
min      0.222222          0.222222    0.000000  
25%      0.333333          0.333333    1.000000  
50%      0.444444          0.444444    3.000000  
75%      0.444444          0.444444    4.000000  
max      0.444444          0.444444    5.000000  

Mean values of numerical columns:
it                                                    0.000000
ft                                                    3.440387
bt                                                    3.833512
km                                                    0.009050
transmission                                          0.854995
ownerNo                                               0.255639
oem                                                  16.042965
model                                               143.564984
modelYear                                             0.861072
centralVariantId                                      0.484849
variantName                                        1172.528464
price                                            533534.908700
Insurance Validity                                    1.878625
Seats                                                 0.375000
RTO                                                 268.597207
Engine Displacement                                   0.234080
Power Steering                                        0.978518
Power Windows Front                                   0.923738
Air Conditioner                                       0.974221
Heater                                                0.965628
Adjustable Head Lights                                0.948443
Manually Adjustable Exterior Rear View Mirror         0.270677
Centeral Locking                                      0.918367
Child Safety Locks                                    0.865736
Power Windows Rear                                    0.783029
Remote Trunk Opener                                   0.402793
Remote Fuel Lid Opener                                0.258861
Low Fuel Warning Light                                0.968851
Accessory Power Outlet                                0.970999
Vanity Mirror                                         0.654135
Rear Seat Headrest                                    0.854995
Cup Holders Front                                     0.689581
Digital Odometer                                      0.866810
Electronic Multi Tripmeter                            0.928034
Fabric Upholstery                                     0.949517
Glove Compartment                                     0.975295
Digital Clock                                         0.871106
Wheel Covers                                          0.489796
Power Antenna                                         0.522019
Chrome Grille                                         0.520945
Day Night Rear View Mirror                            0.613319
Passenger Side Rear View Mirror                       0.970999
Halogen Headlamps                                     0.862513
Rear Seat Belts                                       0.944146
Door Ajar Warning                                     0.661654
Side Impact Beams                                     0.711063
Front Impact Beams                                    0.619764
Adjustable Seats                                      0.972073
Centrally Mounted Fuel Tank                           0.684211
Engine Immobilizer                                    0.928034
Anti Theft Device                                     0.551020
Fog Lights Front                                      0.599356
Anti Lock Braking System                              0.802363
Cd Player                                             0.296455
Trunk Light                                           0.471536
Multifunction Steering Wheel                          0.615467
Navigation System                                     0.310419
Smart Access Card Entry                               0.125671
Engine Start Stop Button                              0.203008
Gear Shift Indicator                                  0.366273
Luggage Hook And Net                                  0.013963
Adjustable Steering                                   0.779807
Tachometer                                            0.874329
Leather Steering Wheel                                0.268528
Outside Temperature Display                           0.245972
Height Adjustable Driver Seat                         0.483351
Power Adjustable Exterior Rear View Mirror            0.721805
Electric Folding Rear View Mirror                     0.444683
Rear Window Wiper                                     0.329753
Rear Window Washer                                    0.277121
Rear Window Defogger                                  0.513426
Alloy Wheels                                          0.402793
Integrated Antenna                                    0.397422
Outside Rear View Mirror Turn Indicators              0.526316
Roof Rail                                             0.254565
Power Door Locks                                      0.796992
Driver Air Bag                                        0.790548
Passenger Air Bag                                     0.721805
Seat Belt Warning                                     0.882922
Keyless Entry                                         0.824919
Engine Check Warning                                  0.657358
Crash Sensor                                          0.783029
Ebd                                                   0.752954
Follow Me Home Headlamps                              0.135338
Rear Camera                                           0.466165
Speed Sensing Auto Door Lock                          0.481203
Pretensioners And Force Limiter Seatbelts             0.389903
Impact Sensing Auto Door Lock                         0.278195
No Of Airbags                                         0.610097
Radio                                                 0.867884
Speakers Front                                        0.873255
Speakers Rear                                         0.688507
Integrated2Din Audio                                  0.668099
Usb Auxiliary Input                                   0.755102
Bluetooth                                             0.711063
Touch Screen                                          0.497315
Number Of Speaker                                     0.657358
Glove Box Cooling                                     0.158969
Driving Experience Control Eco                        0.166488
Tinted Glass                                          0.208378
Rear Spoiler                                          0.481203
Chrome Garnish                                        0.288937
Vehicle Stability Control System                      0.034372
Rear Reading Lamp                                     0.220193
Rear Seat Centre Arm Rest                             0.222342
Cup Holders Rear                                      0.343716
Rear ACVents                                          0.189044
Air Quality Control                                   0.247046
Height Adjustable Front Seat Belts                    0.190118
Cruise Control                                        0.098818
Voice Control                                         0.364125
Audio System Remote Control                           0.121375
Leather Seats                                         0.040816
Fog Lights Rear                                       0.134264
Traction Control                                      0.045113
Seat Lumbar Support                                   0.298604
Battery Saver                                         0.129968
Lane Change Indicator                                 0.285714
Sun Roof                                              0.068743
Automatic Driving Lights                              0.017186
Anti Theft Alarm                                      0.276047
Automatic Head Lamps                                  0.085929
Isofix Child Seat Mounts                              0.293233
Hill Assist                                           0.061224
Tailgate Ajar                                         0.207304
Brake Assist                                          0.053706
Steering Wheel Gearshift Paddles                      0.029001
LEDTaillights                                         0.157895
Cigarette Lighter                                     0.009667
Rain Sensing Wiper                                    0.047261
Drive Modes                                           0.042965
Active Noise Cancellation                             0.000000
Adjustable Headrest                                   0.250269
Hands Free Tailgate                                   0.003222
Dual Tone Dashboard                                   0.351235
Leather Wrap Gear Shift Selector                      0.036520
Dual Tone Body Colour                                 0.004296
LEDDRLs                                               0.270677
LEDHeadlights                                         0.042965
Cornering Headlamps                                   0.017186
Cornering Foglamps                                    0.026853
Side Air Bag Front                                    0.021482
Side Air Bag Rear                                     0.002148
Tyre Pressure Monitor                                 0.064447
Clutch Lock                                           0.035446
Anti Pinch Power Windows                              0.119227
Knee Airbags                                          0.000000
Apple Car Play                                        0.272825
Android Auto                                          0.272825
Mirror Link                                           0.000000
Wireless Phone Charging                               0.036520
Compass                                               0.000000
Moon Roof                                             0.025779
Projector Headlamps                                   0.124597
Speed Alert                                           0.324382
Eletronic Stability Control                           0.059076
Touch Screen Size                                     0.127820
Xenon Headlamps                                       0.000000
Cd Changer                                            0.000000
Power Boot                                            0.024705
Rear Folding Table                                    0.000000
Smoke Headlamps                                       0.041890
Dvd Player                                            0.020408
Internal Storage                                      0.000000
Rear Entertainment System                             0.000000
Remote Engine Start Stop                              0.011815
Ventilated Seats                                      0.000000
LEDFog Lamps                                          0.046187
View360Camera                                         0.005371
Geo Fence Alert                                       0.010741
Steering Mounted Tripmeter                            0.000000
Remote Climate Control                                0.008593
Remote Horn Light Control                             0.000000
Heated Wing Mirror                                    0.000000
Side Stepper                                          0.000000
Blind Spot Monitor                                    0.000000
Hill Descent Control                                  0.000000
Heads Up Display                                      0.000000
Sos Emergency Assistance                              0.011815
Cassette Player                                       0.000000
Find My Car Location                                  0.019334
Wifi Connectivity                                     0.008593
Headlamp Washers                                      0.000000
Real Time Vehicle Tracking                            0.002148
Roof Carrier                                          0.000000
Smart Key Band                                        0.001305
Lane Watch Camera                                     0.000000
Removable Convertible Top                             0.000000
Power Folding3rd Row Seat                             0.000000
Mileage                                               0.098373
Max Power                                             0.000065
Torque                                                0.136174
Color                                                86.070892
Engine Type                                         262.929108
No of Cylinder                                        0.079024
Values per Cylinder                                   0.029851
Value Configuration                                   2.593985
Fuel Suppy System                                    42.252417
Turbo Charger                                         0.156821
Super Charger                                         0.001074
Length                                                0.360300
Width                                                 0.335630
Height                                                0.346392
Wheel Base                                            0.410257
Front Tread                                           0.569280
Rear Tread                                            0.473602
Kerb Weight                                           0.164883
Gross Weight                                          0.202811
Gear Box                                              0.013699
Drive Type                                            5.002148
Steering Type                                         3.718582
Turning Radius                                        0.000153
Front Brake Type                                      8.673469
Rear Brake Type                                       0.205882
Top Speed                                             0.378864
Acceleration                                          0.369737
Tyre Type                                            24.088077
No Door Numbers                                       0.697637
Cargo Volumn                                          0.001123
Wheel Size                                            0.387278
Alloy Wheel Size                                      0.387278
city                                                  2.622986
dtype: float64

Median values of numerical columns:
it                                                    0.000000
ft                                                    4.000000
bt                                                    2.000000
km                                                    0.007636
transmission                                          1.000000
ownerNo                                               0.200000
oem                                                   9.000000
model                                                90.000000
modelYear                                             0.868421
centralVariantId                                      0.527540
variantName                                        1413.000000
price                                            523000.000000
Insurance Validity                                    3.000000
Seats                                                 0.375000
RTO                                                 277.000000
Engine Displacement                                   0.239600
Power Steering                                        1.000000
Power Windows Front                                   1.000000
Air Conditioner                                       1.000000
Heater                                                1.000000
Adjustable Head Lights                                1.000000
Manually Adjustable Exterior Rear View Mirror         0.000000
Centeral Locking                                      1.000000
Child Safety Locks                                    1.000000
Power Windows Rear                                    1.000000
Remote Trunk Opener                                   0.000000
Remote Fuel Lid Opener                                0.000000
Low Fuel Warning Light                                1.000000
Accessory Power Outlet                                1.000000
Vanity Mirror                                         1.000000
Rear Seat Headrest                                    1.000000
Cup Holders Front                                     1.000000
Digital Odometer                                      1.000000
Electronic Multi Tripmeter                            1.000000
Fabric Upholstery                                     1.000000
Glove Compartment                                     1.000000
Digital Clock                                         1.000000
Wheel Covers                                          0.000000
Power Antenna                                         1.000000
Chrome Grille                                         1.000000
Day Night Rear View Mirror                            1.000000
Passenger Side Rear View Mirror                       1.000000
Halogen Headlamps                                     1.000000
Rear Seat Belts                                       1.000000
Door Ajar Warning                                     1.000000
Side Impact Beams                                     1.000000
Front Impact Beams                                    1.000000
Adjustable Seats                                      1.000000
Centrally Mounted Fuel Tank                           1.000000
Engine Immobilizer                                    1.000000
Anti Theft Device                                     1.000000
Fog Lights Front                                      1.000000
Anti Lock Braking System                              1.000000
Cd Player                                             0.000000
Trunk Light                                           0.000000
Multifunction Steering Wheel                          1.000000
Navigation System                                     0.000000
Smart Access Card Entry                               0.000000
Engine Start Stop Button                              0.000000
Gear Shift Indicator                                  0.000000
Luggage Hook And Net                                  0.000000
Adjustable Steering                                   1.000000
Tachometer                                            1.000000
Leather Steering Wheel                                0.000000
Outside Temperature Display                           0.000000
Height Adjustable Driver Seat                         0.000000
Power Adjustable Exterior Rear View Mirror            1.000000
Electric Folding Rear View Mirror                     0.000000
Rear Window Wiper                                     0.000000
Rear Window Washer                                    0.000000
Rear Window Defogger                                  1.000000
Alloy Wheels                                          0.000000
Integrated Antenna                                    0.000000
Outside Rear View Mirror Turn Indicators              1.000000
Roof Rail                                             0.000000
Power Door Locks                                      1.000000
Driver Air Bag                                        1.000000
Passenger Air Bag                                     1.000000
Seat Belt Warning                                     1.000000
Keyless Entry                                         1.000000
Engine Check Warning                                  1.000000
Crash Sensor                                          1.000000
Ebd                                                   1.000000
Follow Me Home Headlamps                              0.000000
Rear Camera                                           0.000000
Speed Sensing Auto Door Lock                          0.000000
Pretensioners And Force Limiter Seatbelts             0.000000
Impact Sensing Auto Door Lock                         0.000000
No Of Airbags                                         1.000000
Radio                                                 1.000000
Speakers Front                                        1.000000
Speakers Rear                                         1.000000
Integrated2Din Audio                                  1.000000
Usb Auxiliary Input                                   1.000000
Bluetooth                                             1.000000
Touch Screen                                          0.000000
Number Of Speaker                                     1.000000
Glove Box Cooling                                     0.000000
Driving Experience Control Eco                        0.000000
Tinted Glass                                          0.000000
Rear Spoiler                                          0.000000
Chrome Garnish                                        0.000000
Vehicle Stability Control System                      0.000000
Rear Reading Lamp                                     0.000000
Rear Seat Centre Arm Rest                             0.000000
Cup Holders Rear                                      0.000000
Rear ACVents                                          0.000000
Air Quality Control                                   0.000000
Height Adjustable Front Seat Belts                    0.000000
Cruise Control                                        0.000000
Voice Control                                         0.000000
Audio System Remote Control                           0.000000
Leather Seats                                         0.000000
Fog Lights Rear                                       0.000000
Traction Control                                      0.000000
Seat Lumbar Support                                   0.000000
Battery Saver                                         0.000000
Lane Change Indicator                                 0.000000
Sun Roof                                              0.000000
Automatic Driving Lights                              0.000000
Anti Theft Alarm                                      0.000000
Automatic Head Lamps                                  0.000000
Isofix Child Seat Mounts                              0.000000
Hill Assist                                           0.000000
Tailgate Ajar                                         0.000000
Brake Assist                                          0.000000
Steering Wheel Gearshift Paddles                      0.000000
LEDTaillights                                         0.000000
Cigarette Lighter                                     0.000000
Rain Sensing Wiper                                    0.000000
Drive Modes                                           0.000000
Active Noise Cancellation                             0.000000
Adjustable Headrest                                   0.000000
Hands Free Tailgate                                   0.000000
Dual Tone Dashboard                                   0.000000
Leather Wrap Gear Shift Selector                      0.000000
Dual Tone Body Colour                                 0.000000
LEDDRLs                                               0.000000
LEDHeadlights                                         0.000000
Cornering Headlamps                                   0.000000
Cornering Foglamps                                    0.000000
Side Air Bag Front                                    0.000000
Side Air Bag Rear                                     0.000000
Tyre Pressure Monitor                                 0.000000
Clutch Lock                                           0.000000
Anti Pinch Power Windows                              0.000000
Knee Airbags                                          0.000000
Apple Car Play                                        0.000000
Android Auto                                          0.000000
Mirror Link                                           0.000000
Wireless Phone Charging                               0.000000
Compass                                               0.000000
Moon Roof                                             0.000000
Projector Headlamps                                   0.000000
Speed Alert                                           0.000000
Eletronic Stability Control                           0.000000
Touch Screen Size                                     0.000000
Xenon Headlamps                                       0.000000
Cd Changer                                            0.000000
Power Boot                                            0.000000
Rear Folding Table                                    0.000000
Smoke Headlamps                                       0.000000
Dvd Player                                            0.000000
Internal Storage                                      0.000000
Rear Entertainment System                             0.000000
Remote Engine Start Stop                              0.000000
Ventilated Seats                                      0.000000
LEDFog Lamps                                          0.000000
View360Camera                                         0.000000
Geo Fence Alert                                       0.000000
Steering Mounted Tripmeter                            0.000000
Remote Climate Control                                0.000000
Remote Horn Light Control                             0.000000
Heated Wing Mirror                                    0.000000
Side Stepper                                          0.000000
Blind Spot Monitor                                    0.000000
Hill Descent Control                                  0.000000
Heads Up Display                                      0.000000
Sos Emergency Assistance                              0.000000
Cassette Player                                       0.000000
Find My Car Location                                  0.000000
Wifi Connectivity                                     0.000000
Headlamp Washers                                      0.000000
Real Time Vehicle Tracking                            0.000000
Roof Carrier                                          0.000000
Smart Key Band                                        0.000000
Lane Watch Camera                                     0.000000
Removable Convertible Top                             0.000000
Power Folding3rd Row Seat                             0.000000
Mileage                                               0.097201
Max Power                                             0.000067
Torque                                                0.126674
Color                                                86.000000
Engine Type                                         278.000000
No of Cylinder                                        0.095238
Values per Cylinder                                   0.029851
Value Configuration                                   1.000000
Fuel Suppy System                                    46.000000
Turbo Charger                                         0.000000
Super Charger                                         0.000000
Length                                                0.394293
Width                                                 0.345679
Height                                                0.342291
Wheel Base                                            0.400000
Front Tread                                           0.570000
Rear Tread                                            0.473602
Kerb Weight                                           0.187130
Gross Weight                                          0.202811
Gear Box                                              0.013699
Drive Type                                            5.000000
Steering Type                                         6.000000
Turning Radius                                        0.000160
Front Brake Type                                      5.000000
Rear Brake Type                                       0.205882
Top Speed                                             0.391304
Acceleration                                          0.345865
Tyre Type                                            26.000000
No Door Numbers                                       0.750000
Cargo Volumn                                          0.001230
Wheel Size                                            0.444444
Alloy Wheel Size                                      0.444444
city                                                  3.000000
dtype: float64

Mode values of numerical columns:
it                                                    0.000000
ft                                                    4.000000
bt                                                    2.000000
km                                                    0.001818
transmission                                          1.000000
ownerNo                                               0.200000
oem                                                   8.000000
model                                               238.000000
modelYear                                             0.947368
centralVariantId                                      0.510502
variantName                                        1764.000000
price                                            350000.000000
Insurance Validity                                    3.000000
Seats                                                 0.375000
RTO                                                 409.000000
Engine Displacement                                   0.239800
Power Steering                                        1.000000
Power Windows Front                                   1.000000
Air Conditioner                                       1.000000
Heater                                                1.000000
Adjustable Head Lights                                1.000000
Manually Adjustable Exterior Rear View Mirror         0.000000
Centeral Locking                                      1.000000
Child Safety Locks                                    1.000000
Power Windows Rear                                    1.000000
Remote Trunk Opener                                   0.000000
Remote Fuel Lid Opener                                0.000000
Low Fuel Warning Light                                1.000000
Accessory Power Outlet                                1.000000
Vanity Mirror                                         1.000000
Rear Seat Headrest                                    1.000000
Cup Holders Front                                     1.000000
Digital Odometer                                      1.000000
Electronic Multi Tripmeter                            1.000000
Fabric Upholstery                                     1.000000
Glove Compartment                                     1.000000
Digital Clock                                         1.000000
Wheel Covers                                          0.000000
Power Antenna                                         1.000000
Chrome Grille                                         1.000000
Day Night Rear View Mirror                            1.000000
Passenger Side Rear View Mirror                       1.000000
Halogen Headlamps                                     1.000000
Rear Seat Belts                                       1.000000
Door Ajar Warning                                     1.000000
Side Impact Beams                                     1.000000
Front Impact Beams                                    1.000000
Adjustable Seats                                      1.000000
Centrally Mounted Fuel Tank                           1.000000
Engine Immobilizer                                    1.000000
Anti Theft Device                                     1.000000
Fog Lights Front                                      1.000000
Anti Lock Braking System                              1.000000
Cd Player                                             0.000000
Trunk Light                                           0.000000
Multifunction Steering Wheel                          1.000000
Navigation System                                     0.000000
Smart Access Card Entry                               0.000000
Engine Start Stop Button                              0.000000
Gear Shift Indicator                                  0.000000
Luggage Hook And Net                                  0.000000
Adjustable Steering                                   1.000000
Tachometer                                            1.000000
Leather Steering Wheel                                0.000000
Outside Temperature Display                           0.000000
Height Adjustable Driver Seat                         0.000000
Power Adjustable Exterior Rear View Mirror            1.000000
Electric Folding Rear View Mirror                     0.000000
Rear Window Wiper                                     0.000000
Rear Window Washer                                    0.000000
Rear Window Defogger                                  1.000000
Alloy Wheels                                          0.000000
Integrated Antenna                                    0.000000
Outside Rear View Mirror Turn Indicators              1.000000
Roof Rail                                             0.000000
Power Door Locks                                      1.000000
Driver Air Bag                                        1.000000
Passenger Air Bag                                     1.000000
Seat Belt Warning                                     1.000000
Keyless Entry                                         1.000000
Engine Check Warning                                  1.000000
Crash Sensor                                          1.000000
Ebd                                                   1.000000
Follow Me Home Headlamps                              0.000000
Rear Camera                                           0.000000
Speed Sensing Auto Door Lock                          0.000000
Pretensioners And Force Limiter Seatbelts             0.000000
Impact Sensing Auto Door Lock                         0.000000
No Of Airbags                                         1.000000
Radio                                                 1.000000
Speakers Front                                        1.000000
Speakers Rear                                         1.000000
Integrated2Din Audio                                  1.000000
Usb Auxiliary Input                                   1.000000
Bluetooth                                             1.000000
Touch Screen                                          0.000000
Number Of Speaker                                     1.000000
Glove Box Cooling                                     0.000000
Driving Experience Control Eco                        0.000000
Tinted Glass                                          0.000000
Rear Spoiler                                          0.000000
Chrome Garnish                                        0.000000
Vehicle Stability Control System                      0.000000
Rear Reading Lamp                                     0.000000
Rear Seat Centre Arm Rest                             0.000000
Cup Holders Rear                                      0.000000
Rear ACVents                                          0.000000
Air Quality Control                                   0.000000
Height Adjustable Front Seat Belts                    0.000000
Cruise Control                                        0.000000
Voice Control                                         0.000000
Audio System Remote Control                           0.000000
Leather Seats                                         0.000000
Fog Lights Rear                                       0.000000
Traction Control                                      0.000000
Seat Lumbar Support                                   0.000000
Battery Saver                                         0.000000
Lane Change Indicator                                 0.000000
Sun Roof                                              0.000000
Automatic Driving Lights                              0.000000
Anti Theft Alarm                                      0.000000
Automatic Head Lamps                                  0.000000
Isofix Child Seat Mounts                              0.000000
Hill Assist                                           0.000000
Tailgate Ajar                                         0.000000
Brake Assist                                          0.000000
Steering Wheel Gearshift Paddles                      0.000000
LEDTaillights                                         0.000000
Cigarette Lighter                                     0.000000
Rain Sensing Wiper                                    0.000000
Drive Modes                                           0.000000
Active Noise Cancellation                             0.000000
Adjustable Headrest                                   0.000000
Hands Free Tailgate                                   0.000000
Dual Tone Dashboard                                   0.000000
Leather Wrap Gear Shift Selector                      0.000000
Dual Tone Body Colour                                 0.000000
LEDDRLs                                               0.000000
LEDHeadlights                                         0.000000
Cornering Headlamps                                   0.000000
Cornering Foglamps                                    0.000000
Side Air Bag Front                                    0.000000
Side Air Bag Rear                                     0.000000
Tyre Pressure Monitor                                 0.000000
Clutch Lock                                           0.000000
Anti Pinch Power Windows                              0.000000
Knee Airbags                                          0.000000
Apple Car Play                                        0.000000
Android Auto                                          0.000000
Mirror Link                                           0.000000
Wireless Phone Charging                               0.000000
Compass                                               0.000000
Moon Roof                                             0.000000
Projector Headlamps                                   0.000000
Speed Alert                                           0.000000
Eletronic Stability Control                           0.000000
Touch Screen Size                                     0.000000
Xenon Headlamps                                       0.000000
Cd Changer                                            0.000000
Power Boot                                            0.000000
Rear Folding Table                                    0.000000
Smoke Headlamps                                       0.000000
Dvd Player                                            0.000000
Internal Storage                                      0.000000
Rear Entertainment System                             0.000000
Remote Engine Start Stop                              0.000000
Ventilated Seats                                      0.000000
LEDFog Lamps                                          0.000000
View360Camera                                         0.000000
Geo Fence Alert                                       0.000000
Steering Mounted Tripmeter                            0.000000
Remote Climate Control                                0.000000
Remote Horn Light Control                             0.000000
Heated Wing Mirror                                    0.000000
Side Stepper                                          0.000000
Blind Spot Monitor                                    0.000000
Hill Descent Control                                  0.000000
Heads Up Display                                      0.000000
Sos Emergency Assistance                              0.000000
Cassette Player                                       0.000000
Find My Car Location                                  0.000000
Wifi Connectivity                                     0.000000
Headlamp Washers                                      0.000000
Real Time Vehicle Tracking                            0.000000
Roof Carrier                                          0.000000
Smart Key Band                                        0.000000
Lane Watch Camera                                     0.000000
Removable Convertible Top                             0.000000
Power Folding3rd Row Seat                             0.000000
Mileage                                               0.103897
Max Power                                             0.000075
Torque                                                0.123119
Color                                                86.000000
Engine Type                                         476.000000
No of Cylinder                                        0.095238
Values per Cylinder                                   0.029851
Value Configuration                                   1.000000
Fuel Suppy System                                    46.000000
Turbo Charger                                         0.000000
Super Charger                                         0.000000
Length                                                0.410370
Width                                                 0.333333
Height                                                0.328147
Wheel Base                                            0.400000
Front Tread                                           0.570000
Rear Tread                                            0.473602
Kerb Weight                                           0.194750
Gross Weight                                          0.202811
Gear Box                                              0.013699
Drive Type                                            5.000000
Steering Type                                         6.000000
Turning Radius                                        0.000176
Front Brake Type                                      5.000000
Rear Brake Type                                       0.205882
Top Speed                                             0.391304
Acceleration                                          0.345865
Tyre Type                                            26.000000
No Door Numbers                                       0.750000
Cargo Volumn                                          0.001230
Wheel Size                                            0.444444
Alloy Wheel Size                                      0.444444
city                                                  5.000000
Name: 0, dtype: float64

Standard deviation of numerical columns:
it                                               0.000000e+00
ft                                               1.194720e+00
bt                                               2.655324e+00
km                                               6.084558e-03
transmission                                     3.522955e-01
ownerNo                                          1.030601e-01
oem                                              9.601315e+00
model                                            8.962255e+01
modelYear                                        8.847183e-02
centralVariantId                                 2.392368e-01
variantName                                      7.086236e+02
price                                            2.046234e+05
Insurance Validity                               1.425303e+00
Seats                                            0.000000e+00
RTO                                              1.243573e+02
Engine Displacement                              2.486768e-02
Power Steering                                   1.450634e-01
Power Windows Front                              2.655596e-01
Air Conditioner                                  1.585597e-01
Heater                                           1.822798e-01
Adjustable Head Lights                           2.212507e-01
Manually Adjustable Exterior Rear View Mirror    4.445482e-01
Centeral Locking                                 2.739514e-01
Child Safety Locks                               3.411192e-01
Power Windows Rear                               4.124043e-01
Remote Trunk Opener                              4.907233e-01
Remote Fuel Lid Opener                           4.382448e-01
Low Fuel Warning Light                           1.738145e-01
Accessory Power Outlet                           1.678996e-01
Vanity Mirror                                    4.759050e-01
Rear Seat Headrest                               3.522955e-01
Cup Holders Front                                4.629138e-01
Digital Odometer                                 3.399627e-01
Electronic Multi Tripmeter                       2.585699e-01
Fabric Upholstery                                2.190578e-01
Glove Compartment                                1.553068e-01
Digital Clock                                    3.352623e-01
Wheel Covers                                     5.001646e-01
Power Antenna                                    4.997834e-01
Chrome Grille                                    4.998296e-01
Day Night Rear View Mirror                       4.872513e-01
Passenger Side Rear View Mirror                  1.678996e-01
Halogen Headlamps                                3.445454e-01
Rear Seat Belts                                  2.297628e-01
Door Ajar Warning                                4.734012e-01
Side Impact Beams                                4.535120e-01
Front Impact Beams                               4.857057e-01
Adjustable Seats                                 1.648522e-01
Centrally Mounted Fuel Tank                      4.650794e-01
Engine Immobilizer                               2.585699e-01
Anti Theft Device                                4.976574e-01
Fog Lights Front                                 4.902924e-01
Anti Lock Braking System                         3.984308e-01
Cd Player                                        4.569397e-01
Trunk Light                                      4.994575e-01
Multifunction Steering Wheel                     4.867461e-01
Navigation System                                4.629138e-01
Smart Access Card Entry                          3.316567e-01
Engine Start Stop Button                         4.024543e-01
Gear Shift Indicator                             4.820442e-01
Luggage Hook And Net                             1.174023e-01
Adjustable Steering                              4.145996e-01
Tachometer                                       3.316567e-01
Leather Steering Wheel                           4.434322e-01
Outside Temperature Display                      4.308935e-01
Height Adjustable Driver Seat                    4.999913e-01
Power Adjustable Exterior Rear View Mirror       4.483511e-01
Electric Folding Rear View Mirror                4.971977e-01
Rear Window Wiper                                4.703760e-01
Rear Window Washer                               4.478175e-01
Rear Window Defogger                             5.000883e-01
Alloy Wheels                                     4.907233e-01
Integrated Antenna                               4.896277e-01
Outside Rear View Mirror Turn Indicators         4.995754e-01
Roof Rail                                        4.358505e-01
Power Door Locks                                 4.024543e-01
Driver Air Bag                                   4.071364e-01
Passenger Air Bag                                4.483511e-01
Seat Belt Warning                                3.216865e-01
Keyless Entry                                    3.802403e-01
Engine Check Warning                             4.748481e-01
Crash Sensor                                     4.124043e-01
Ebd                                              4.315256e-01
Follow Me Home Headlamps                         3.422685e-01
Rear Camera                                      4.991220e-01
Speed Sensing Auto Door Lock                     4.999151e-01
Pretensioners And Force Limiter Seatbelts        4.879903e-01
Impact Sensing Auto Door Lock                    4.483511e-01
No Of Airbags                                    4.879903e-01
Radio                                            3.387988e-01
Speakers Front                                   3.328664e-01
Speakers Rear                                    4.633527e-01
Integrated2Din Audio                             4.711488e-01
Usb Auxiliary Input                              4.302578e-01
Bluetooth                                        4.535120e-01
Touch Screen                                     5.002615e-01
Number Of Speaker                                4.748481e-01
Glove Box Cooling                                3.658436e-01
Driving Experience Control Eco                   3.727180e-01
Tinted Glass                                     4.063669e-01
Rear Spoiler                                     4.999151e-01
Chrome Garnish                                   4.535120e-01
Vehicle Stability Control System                 1.822798e-01
Rear Reading Lamp                                4.145996e-01
Rear Seat Centre Arm Rest                        4.160429e-01
Cup Holders Rear                                 4.752031e-01
Rear ACVents                                     3.917541e-01
Air Quality Control                              4.315256e-01
Height Adjustable Front Seat Belts               3.926051e-01
Cruise Control                                   2.985785e-01
Voice Control                                    4.814425e-01
Audio System Remote Control                      3.267379e-01
Leather Seats                                    1.979708e-01
Fog Lights Rear                                  3.411192e-01
Traction Control                                 2.076630e-01
Seat Lumbar Support                              4.578916e-01
Battery Saver                                    3.364487e-01
Lane Change Indicator                            4.519968e-01
Sun Roof                                         2.531531e-01
Automatic Driving Lights                         1.300332e-01
Anti Theft Alarm                                 4.472807e-01
Automatic Head Lamps                             2.804100e-01
Isofix Child Seat Mounts                         4.554891e-01
Hill Assist                                      2.398705e-01
Tailgate Ajar                                    4.055931e-01
Brake Assist                                     2.255572e-01
Steering Wheel Gearshift Paddles                 1.678996e-01
LEDTaillights                                    3.648383e-01
Cigarette Lighter                                9.789723e-02
Rain Sensing Wiper                               2.123107e-01
Drive Modes                                      2.028862e-01
Active Noise Cancellation                        0.000000e+00
Adjustable Headrest                              4.334004e-01
Hands Free Tailgate                              5.670460e-02
Dual Tone Dashboard                              4.776129e-01
Leather Wrap Gear Shift Selector                 1.876806e-01
Dual Tone Body Colour                            6.544155e-02
LEDDRLs                                          4.445482e-01
LEDHeadlights                                    2.028862e-01
Cornering Headlamps                              1.300332e-01
Cornering Foglamps                               1.617401e-01
Side Air Bag Front                               1.450634e-01
Side Air Bag Rear                                4.632405e-02
Tyre Pressure Monitor                            2.456792e-01
Clutch Lock                                      1.850030e-01
Anti Pinch Power Windows                         3.242292e-01
Knee Airbags                                     0.000000e+00
Apple Car Play                                   4.456510e-01
Android Auto                                     4.456510e-01
Mirror Link                                      0.000000e+00
Wireless Phone Charging                          1.876806e-01
Compass                                          0.000000e+00
Moon Roof                                        1.585597e-01
Projector Headlamps                              3.304391e-01
Speed Alert                                      4.683952e-01
Eletronic Stability Control                      2.358941e-01
Touch Screen Size                                3.340682e-01
Xenon Headlamps                                  0.000000e+00
Cd Changer                                       0.000000e+00
Power Boot                                       1.553068e-01
Rear Folding Table                               0.000000e+00
Smoke Headlamps                                  2.004465e-01
Dvd Player                                       1.414679e-01
Internal Storage                                 0.000000e+00
Rear Entertainment System                        0.000000e+00
Remote Engine Start Stop                         1.081120e-01
Ventilated Seats                                 0.000000e+00
LEDFog Lamps                                     2.100025e-01
View360Camera                                    7.312640e-02
Geo Fence Alert                                  1.031368e-01
Steering Mounted Tripmeter                       0.000000e+00
Remote Climate Control                           9.234843e-02
Remote Horn Light Control                        0.000000e+00
Heated Wing Mirror                               0.000000e+00
Side Stepper                                     0.000000e+00
Blind Spot Monitor                               0.000000e+00
Hill Descent Control                             0.000000e+00
Heads Up Display                                 0.000000e+00
Sos Emergency Assistance                         1.081120e-01
Cassette Player                                  0.000000e+00
Find My Car Location                             1.377702e-01
Wifi Connectivity                                9.234843e-02
Headlamp Washers                                 0.000000e+00
Real Time Vehicle Tracking                       4.632405e-02
Roof Carrier                                     0.000000e+00
Smart Key Band                                   3.613147e-02
Lane Watch Camera                                0.000000e+00
Removable Convertible Top                        0.000000e+00
Power Folding3rd Row Seat                        0.000000e+00
Mileage                                          1.815749e-02
Max Power                                        1.231956e-05
Torque                                           3.798981e-02
Color                                            4.262484e+01
Engine Type                                      1.773558e+02
No of Cylinder                                   2.257762e-02
Values per Cylinder                              3.506025e-16
Value Configuration                              2.354252e+00
Fuel Suppy System                                1.636616e+01
Turbo Charger                                    3.638270e-01
Super Charger                                    3.277368e-02
Length                                           6.338859e-02
Width                                            6.959543e-02
Height                                           6.016988e-02
Wheel Base                                       3.798235e-02
Front Tread                                      2.585699e-03
Rear Tread                                       2.832590e-15
Kerb Weight                                      5.900499e-02
Gross Weight                                     4.526591e-15
Gear Box                                         2.516701e-16
Drive Type                                       4.632405e-02
Steering Type                                    2.439872e+00
Turning Radius                                   3.341515e-05
Front Brake Type                                 7.005124e+00
Rear Brake Type                                  2.777049e-15
Top Speed                                        2.204966e-02
Acceleration                                     3.176128e-02
Tyre Type                                        5.356413e+00
No Door Numbers                                  1.017841e-01
Cargo Volumn                                     2.184936e-04
Wheel Size                                       8.151576e-02
Alloy Wheel Size                                 8.151576e-02
city                                             1.736598e+00
dtype: float64

Variance of numerical columns:
it                                               0.000000e+00
ft                                               1.427356e+00
bt                                               7.050747e+00
km                                               3.702184e-05
transmission                                     1.241121e-01
ownerNo                                          1.062139e-02
oem                                              9.218525e+01
model                                            8.032201e+03
modelYear                                        7.827264e-03
centralVariantId                                 5.723425e-02
variantName                                      5.021474e+05
price                                            4.187073e+10
Insurance Validity                               2.031489e+00
Seats                                            0.000000e+00
RTO                                              1.546475e+04
Engine Displacement                              6.184015e-04
Power Steering                                   2.104339e-02
Power Windows Front                              7.052193e-02
Air Conditioner                                  2.514119e-02
Heater                                           3.322592e-02
Adjustable Head Lights                           4.895187e-02
Manually Adjustable Exterior Rear View Mirror    1.976231e-01
Centeral Locking                                 7.504937e-02
Child Safety Locks                               1.163623e-01
Power Windows Rear                               1.700773e-01
Remote Trunk Opener                              2.408094e-01
Remote Fuel Lid Opener                           1.920585e-01
Low Fuel Warning Light                           3.021147e-02
Accessory Power Outlet                           2.819029e-02
Vanity Mirror                                    2.264856e-01
Rear Seat Headrest                               1.241121e-01
Cup Holders Front                                2.142892e-01
Digital Odometer                                 1.155747e-01
Electronic Multi Tripmeter                       6.685839e-02
Fabric Upholstery                                4.798633e-02
Glove Compartment                                2.412021e-02
Digital Clock                                    1.124008e-01
Wheel Covers                                     2.501646e-01
Power Antenna                                    2.497834e-01
Chrome Grille                                    2.498296e-01
Day Night Rear View Mirror                       2.374138e-01
Passenger Side Rear View Mirror                  2.819029e-02
Halogen Headlamps                                1.187115e-01
Rear Seat Belts                                  5.279096e-02
Door Ajar Warning                                2.241087e-01
Side Impact Beams                                2.056732e-01
Front Impact Beams                               2.359101e-01
Adjustable Seats                                 2.717624e-02
Centrally Mounted Fuel Tank                      2.162988e-01
Engine Immobilizer                               6.685839e-02
Anti Theft Device                                2.476629e-01
Fog Lights Front                                 2.403867e-01
Anti Lock Braking System                         1.587471e-01
Cd Player                                        2.087939e-01
Trunk Light                                      2.494577e-01
Multifunction Steering Wheel                     2.369218e-01
Navigation System                                2.142892e-01
Smart Access Card Entry                          1.099962e-01
Engine Start Stop Button                         1.619694e-01
Gear Shift Indicator                             2.323666e-01
Luggage Hook And Net                             1.378331e-02
Adjustable Steering                              1.718929e-01
Tachometer                                       1.099962e-01
Leather Steering Wheel                           1.966321e-01
Outside Temperature Display                      1.856692e-01
Height Adjustable Driver Seat                    2.499913e-01
Power Adjustable Exterior Rear View Mirror       2.010187e-01
Electric Folding Rear View Mirror                2.472056e-01
Rear Window Wiper                                2.212536e-01
Rear Window Washer                               2.005405e-01
Rear Window Defogger                             2.500884e-01
Alloy Wheels                                     2.408094e-01
Integrated Antenna                               2.397353e-01
Outside Rear View Mirror Turn Indicators         2.495756e-01
Roof Rail                                        1.899657e-01
Power Door Locks                                 1.619694e-01
Driver Air Bag                                   1.657600e-01
Passenger Air Bag                                2.010187e-01
Seat Belt Warning                                1.034822e-01
Keyless Entry                                    1.445827e-01
Engine Check Warning                             2.254808e-01
Crash Sensor                                     1.700773e-01
Ebd                                              1.862144e-01
Follow Me Home Headlamps                         1.171477e-01
Rear Camera                                      2.491228e-01
Speed Sensing Auto Door Lock                     2.499151e-01
Pretensioners And Force Limiter Seatbelts        2.381345e-01
Impact Sensing Auto Door Lock                    2.010187e-01
No Of Airbags                                    2.381345e-01
Radio                                            1.147847e-01
Speakers Front                                   1.108000e-01
Speakers Rear                                    2.146957e-01
Integrated2Din Audio                             2.219812e-01
Usb Auxiliary Input                              1.851218e-01
Bluetooth                                        2.056732e-01
Touch Screen                                     2.502616e-01
Number Of Speaker                                2.254808e-01
Glove Box Cooling                                1.338415e-01
Driving Experience Control Eco                   1.389187e-01
Tinted Glass                                     1.651340e-01
Rear Spoiler                                     2.499151e-01
Chrome Garnish                                   2.056732e-01
Vehicle Stability Control System                 3.322592e-02
Rear Reading Lamp                                1.718929e-01
Rear Seat Centre Arm Rest                        1.730917e-01
Cup Holders Rear                                 2.258180e-01
Rear ACVents                                     1.534712e-01
Air Quality Control                              1.862144e-01
Height Adjustable Front Seat Belts               1.541388e-01
Cruise Control                                   8.914914e-02
Voice Control                                    2.317868e-01
Audio System Remote Control                      1.067577e-01
Leather Seats                                    3.919245e-02
Fog Lights Rear                                  1.163623e-01
Traction Control                                 4.312394e-02
Seat Lumbar Support                              2.096647e-01
Battery Saver                                    1.131977e-01
Lane Change Indicator                            2.043011e-01
Sun Roof                                         6.408648e-02
Automatic Driving Lights                         1.690863e-02
Anti Theft Alarm                                 2.000601e-01
Automatic Head Lamps                             7.862975e-02
Isofix Child Seat Mounts                         2.074703e-01
Hill Assist                                      5.753785e-02
Tailgate Ajar                                    1.645057e-01
Brake Assist                                     5.087604e-02
Steering Wheel Gearshift Paddles                 2.819029e-02
LEDTaillights                                    1.331070e-01
Cigarette Lighter                                9.583868e-03
Rain Sensing Wiper                               4.507582e-02
Drive Modes                                      4.116281e-02
Active Noise Cancellation                        0.000000e+00
Adjustable Headrest                              1.878359e-01
Hands Free Tailgate                              3.215412e-03
Dual Tone Dashboard                              2.281141e-01
Leather Wrap Gear Shift Selector                 3.522400e-02
Dual Tone Body Colour                            4.282596e-03
LEDDRLs                                          1.976231e-01
LEDHeadlights                                    4.116281e-02
Cornering Headlamps                              1.690863e-02
Cornering Foglamps                               2.615987e-02
Side Air Bag Front                               2.104339e-02
Side Air Bag Rear                                2.145918e-03
Tyre Pressure Monitor                            6.035827e-02
Clutch Lock                                      3.422612e-02
Anti Pinch Power Windows                         1.051246e-01
Knee Airbags                                     0.000000e+00
Apple Car Play                                   1.986048e-01
Android Auto                                     1.986048e-01
Mirror Link                                      0.000000e+00
Wireless Phone Charging                          3.522400e-02
Compass                                          0.000000e+00
Moon Roof                                        2.514119e-02
Projector Headlamps                              1.091900e-01
Speed Alert                                      2.193941e-01
Eletronic Stability Control                      5.564603e-02
Touch Screen Size                                1.116016e-01
Xenon Headlamps                                  0.000000e+00
Cd Changer                                       0.000000e+00
Power Boot                                       2.412021e-02
Rear Folding Table                               0.000000e+00
Smoke Headlamps                                  4.017879e-02
Dvd Player                                       2.001317e-02
Internal Storage                                 0.000000e+00
Rear Entertainment System                        0.000000e+00
Remote Engine Start Stop                         1.168821e-02
Ventilated Seats                                 0.000000e+00
LEDFog Lamps                                     4.410104e-02
View360Camera                                    5.347470e-03
Geo Fence Alert                                  1.063719e-02
Steering Mounted Tripmeter                       0.000000e+00
Remote Climate Control                           8.528233e-03
Remote Horn Light Control                        0.000000e+00
Heated Wing Mirror                               0.000000e+00
Side Stepper                                     0.000000e+00
Blind Spot Monitor                               0.000000e+00
Hill Descent Control                             0.000000e+00
Heads Up Display                                 0.000000e+00
Sos Emergency Assistance                         1.168821e-02
Cassette Player                                  0.000000e+00
Find My Car Location                             1.898063e-02
Wifi Connectivity                                8.528233e-03
Headlamp Washers                                 0.000000e+00
Real Time Vehicle Tracking                       2.145918e-03
Roof Carrier                                     0.000000e+00
Smart Key Band                                   1.305483e-03
Lane Watch Camera                                0.000000e+00
Removable Convertible Top                        0.000000e+00
Power Folding3rd Row Seat                        0.000000e+00
Mileage                                          3.296946e-04
Max Power                                        1.517716e-10
Torque                                           1.443226e-03
Color                                            1.816877e+03
Engine Type                                      3.145508e+04
No of Cylinder                                   5.097490e-04
Values per Cylinder                              1.229221e-31
Value Configuration                              5.542501e+00
Fuel Suppy System                                2.678513e+02
Turbo Charger                                    1.323701e-01
Super Charger                                    1.074114e-03
Length                                           4.018113e-03
Width                                            4.843524e-03
Height                                           3.620415e-03
Wheel Base                                       1.442659e-03
Front Tread                                      6.685839e-06
Rear Tread                                       8.023568e-30
Kerb Weight                                      3.481589e-03
Gross Weight                                     2.049002e-29
Gear Box                                         6.333784e-32
Drive Type                                       2.145918e-03
Steering Type                                    5.952977e+00
Turning Radius                                   1.116572e-09
Front Brake Type                                 4.907176e+01
Rear Brake Type                                  7.712003e-30
Top Speed                                        4.861874e-04
Acceleration                                     1.008779e-03
Tyre Type                                        2.869116e+01
No Door Numbers                                  1.036000e-02
Cargo Volumn                                     4.773944e-08
Wheel Size                                       6.644819e-03
Alloy Wheel Size                                 6.644819e-03
city                                             3.015772e+00
dtype: float64

Unique value counts in each column:
it                                                 1
ft                                                 3
bt                                                 3
km                                               603
transmission                                       2
ownerNo                                            4
oem                                               13
model                                             48
modelYear                                         17
centralVariantId                                 265
variantName                                      234
price                                            417
Insurance Validity                                 6
Seats                                              1
RTO                                              171
Engine Displacement                               24
Power Steering                                     2
Power Windows Front                                2
Air Conditioner                                    2
Heater                                             2
Adjustable Head Lights                             2
Manually Adjustable Exterior Rear View Mirror      2
Centeral Locking                                   2
Child Safety Locks                                 2
Power Windows Rear                                 2
Remote Trunk Opener                                2
Remote Fuel Lid Opener                             2
Low Fuel Warning Light                             2
Accessory Power Outlet                             2
Vanity Mirror                                      2
Rear Seat Headrest                                 2
Cup Holders Front                                  2
Digital Odometer                                   2
Electronic Multi Tripmeter                         2
Fabric Upholstery                                  2
Glove Compartment                                  2
Digital Clock                                      2
Wheel Covers                                       2
Power Antenna                                      2
Chrome Grille                                      2
Day Night Rear View Mirror                         2
Passenger Side Rear View Mirror                    2
Halogen Headlamps                                  2
Rear Seat Belts                                    2
Door Ajar Warning                                  2
Side Impact Beams                                  2
Front Impact Beams                                 2
Adjustable Seats                                   2
Centrally Mounted Fuel Tank                        2
Engine Immobilizer                                 2
Anti Theft Device                                  2
Fog Lights Front                                   2
Anti Lock Braking System                           2
Cd Player                                          2
Trunk Light                                        2
Multifunction Steering Wheel                       2
Navigation System                                  2
Smart Access Card Entry                            2
Engine Start Stop Button                           2
Gear Shift Indicator                               2
Luggage Hook And Net                               2
Adjustable Steering                                2
Tachometer                                         2
Leather Steering Wheel                             2
Outside Temperature Display                        2
Height Adjustable Driver Seat                      2
Power Adjustable Exterior Rear View Mirror         2
Electric Folding Rear View Mirror                  2
Rear Window Wiper                                  2
Rear Window Washer                                 2
Rear Window Defogger                               2
Alloy Wheels                                       2
Integrated Antenna                                 2
Outside Rear View Mirror Turn Indicators           2
Roof Rail                                          2
Power Door Locks                                   2
Driver Air Bag                                     2
Passenger Air Bag                                  2
Seat Belt Warning                                  2
Keyless Entry                                      2
Engine Check Warning                               2
Crash Sensor                                       2
Ebd                                                2
Follow Me Home Headlamps                           2
Rear Camera                                        2
Speed Sensing Auto Door Lock                       2
Pretensioners And Force Limiter Seatbelts          2
Impact Sensing Auto Door Lock                      2
No Of Airbags                                      2
Radio                                              2
Speakers Front                                     2
Speakers Rear                                      2
Integrated2Din Audio                               2
Usb Auxiliary Input                                2
Bluetooth                                          2
Touch Screen                                       2
Number Of Speaker                                  2
Glove Box Cooling                                  2
Driving Experience Control Eco                     2
Tinted Glass                                       2
Rear Spoiler                                       2
Chrome Garnish                                     2
Vehicle Stability Control System                   2
Rear Reading Lamp                                  2
Rear Seat Centre Arm Rest                          2
Cup Holders Rear                                   2
Rear ACVents                                       2
Air Quality Control                                2
Height Adjustable Front Seat Belts                 2
Cruise Control                                     2
Voice Control                                      2
Audio System Remote Control                        2
Leather Seats                                      2
Fog Lights Rear                                    2
Traction Control                                   2
Seat Lumbar Support                                2
Battery Saver                                      2
Lane Change Indicator                              2
Sun Roof                                           2
Automatic Driving Lights                           2
Anti Theft Alarm                                   2
Automatic Head Lamps                               2
Isofix Child Seat Mounts                           2
Hill Assist                                        2
Tailgate Ajar                                      2
Brake Assist                                       2
Steering Wheel Gearshift Paddles                   2
LEDTaillights                                      2
Cigarette Lighter                                  2
Rain Sensing Wiper                                 2
Drive Modes                                        2
Active Noise Cancellation                          1
Adjustable Headrest                                2
Hands Free Tailgate                                2
Dual Tone Dashboard                                2
Leather Wrap Gear Shift Selector                   2
Dual Tone Body Colour                              2
LEDDRLs                                            2
LEDHeadlights                                      2
Cornering Headlamps                                2
Cornering Foglamps                                 2
Side Air Bag Front                                 2
Side Air Bag Rear                                  2
Tyre Pressure Monitor                              2
Clutch Lock                                        2
Anti Pinch Power Windows                           2
Knee Airbags                                       1
Apple Car Play                                     2
Android Auto                                       2
Mirror Link                                        1
Wireless Phone Charging                            2
Compass                                            1
Moon Roof                                          2
Projector Headlamps                                2
Speed Alert                                        2
Eletronic Stability Control                        2
Touch Screen Size                                  2
Xenon Headlamps                                    1
Cd Changer                                         1
Power Boot                                         2
Rear Folding Table                                 1
Smoke Headlamps                                    2
Dvd Player                                         2
Internal Storage                                   1
Rear Entertainment System                          1
Remote Engine Start Stop                           2
Ventilated Seats                                   1
LEDFog Lamps                                       2
View360Camera                                      2
Geo Fence Alert                                    2
Steering Mounted Tripmeter                         1
Remote Climate Control                             2
Remote Horn Light Control                          1
Heated Wing Mirror                                 1
Side Stepper                                       1
Blind Spot Monitor                                 1
Hill Descent Control                               1
Heads Up Display                                   1
Sos Emergency Assistance                           2
Cassette Player                                    1
Find My Car Location                               2
Wifi Connectivity                                  2
Headlamp Washers                                   1
Real Time Vehicle Tracking                         2
Roof Carrier                                       1
Smart Key Band                                     2
Lane Watch Camera                                  1
Removable Convertible Top                          1
Power Folding3rd Row Seat                          1
Mileage                                           82
Max Power                                         52
Torque                                            38
Color                                             38
Engine Type                                       68
No of Cylinder                                     2
Values per Cylinder                                1
Value Configuration                                4
Fuel Suppy System                                 18
Turbo Charger                                      2
Super Charger                                      2
Length                                            35
Width                                             29
Height                                            38
Wheel Base                                        24
Front Tread                                        2
Rear Tread                                         1
Kerb Weight                                      111
Gross Weight                                       1
Gear Box                                           1
Drive Type                                         2
Steering Type                                      4
Turning Radius                                    15
Front Brake Type                                   4
Rear Brake Type                                    1
Top Speed                                         18
Acceleration                                      19
Tyre Type                                          7
No Door Numbers                                    2
Cargo Volumn                                      33
Wheel Size                                         3
Alloy Wheel Size                                   3
city                                               6
dtype: int64

Missing values in each column:
it                                                 0
ft                                                 0
bt                                                 0
km                                                 0
transmission                                       0
ownerNo                                            0
oem                                                0
model                                              0
modelYear                                          0
centralVariantId                                   0
variantName                                        0
price                                              0
Insurance Validity                                 0
Seats                                              0
RTO                                                0
Engine Displacement                                0
Power Steering                                     0
Power Windows Front                                0
Air Conditioner                                    0
Heater                                             0
Adjustable Head Lights                             0
Manually Adjustable Exterior Rear View Mirror      0
Centeral Locking                                   0
Child Safety Locks                                 0
Power Windows Rear                                 0
Remote Trunk Opener                                0
Remote Fuel Lid Opener                             0
Low Fuel Warning Light                             0
Accessory Power Outlet                             0
Vanity Mirror                                      0
Rear Seat Headrest                                 0
Cup Holders Front                                  0
Digital Odometer                                   0
Electronic Multi Tripmeter                         0
Fabric Upholstery                                  0
Glove Compartment                                  0
Digital Clock                                      0
Wheel Covers                                       0
Power Antenna                                      0
Chrome Grille                                      0
Day Night Rear View Mirror                         0
Passenger Side Rear View Mirror                    0
Halogen Headlamps                                  0
Rear Seat Belts                                    0
Door Ajar Warning                                  0
Side Impact Beams                                  0
Front Impact Beams                                 0
Adjustable Seats                                   0
Centrally Mounted Fuel Tank                        0
Engine Immobilizer                                 0
Anti Theft Device                                  0
Fog Lights Front                                   0
Anti Lock Braking System                           0
Cd Player                                          0
Trunk Light                                        0
Multifunction Steering Wheel                       0
Navigation System                                  0
Smart Access Card Entry                            0
Engine Start Stop Button                           0
Gear Shift Indicator                               0
Luggage Hook And Net                               0
Adjustable Steering                                0
Tachometer                                         0
Leather Steering Wheel                             0
Outside Temperature Display                        0
Height Adjustable Driver Seat                      0
Power Adjustable Exterior Rear View Mirror         0
Electric Folding Rear View Mirror                  0
Rear Window Wiper                                  0
Rear Window Washer                                 0
Rear Window Defogger                               0
Alloy Wheels                                       0
Integrated Antenna                                 0
Outside Rear View Mirror Turn Indicators           0
Roof Rail                                          0
Power Door Locks                                   0
Driver Air Bag                                     0
Passenger Air Bag                                  0
Seat Belt Warning                                  0
Keyless Entry                                      0
Engine Check Warning                               0
Crash Sensor                                       0
Ebd                                                0
Follow Me Home Headlamps                           0
Rear Camera                                        0
Speed Sensing Auto Door Lock                       0
Pretensioners And Force Limiter Seatbelts          0
Impact Sensing Auto Door Lock                      0
No Of Airbags                                      0
Radio                                              0
Speakers Front                                     0
Speakers Rear                                      0
Integrated2Din Audio                               0
Usb Auxiliary Input                                0
Bluetooth                                          0
Touch Screen                                       0
Number Of Speaker                                  0
Glove Box Cooling                                  0
Driving Experience Control Eco                     0
Tinted Glass                                       0
Rear Spoiler                                       0
Chrome Garnish                                     0
Vehicle Stability Control System                   0
Rear Reading Lamp                                  0
Rear Seat Centre Arm Rest                          0
Cup Holders Rear                                   0
Rear ACVents                                       0
Air Quality Control                                0
Height Adjustable Front Seat Belts                 0
Cruise Control                                     0
Voice Control                                      0
Audio System Remote Control                        0
Leather Seats                                      0
Fog Lights Rear                                    0
Traction Control                                   0
Seat Lumbar Support                                0
Battery Saver                                      0
Lane Change Indicator                              0
Sun Roof                                           0
Automatic Driving Lights                           0
Anti Theft Alarm                                   0
Automatic Head Lamps                               0
Isofix Child Seat Mounts                           0
Hill Assist                                        0
Tailgate Ajar                                      0
Brake Assist                                       0
Steering Wheel Gearshift Paddles                   0
LEDTaillights                                      0
Cigarette Lighter                                  0
Rain Sensing Wiper                                 0
Drive Modes                                        0
Active Noise Cancellation                          0
Adjustable Headrest                                0
Hands Free Tailgate                                0
Dual Tone Dashboard                                0
Leather Wrap Gear Shift Selector                   0
Dual Tone Body Colour                              0
LEDDRLs                                            0
LEDHeadlights                                      0
Cornering Headlamps                                0
Cornering Foglamps                                 0
Side Air Bag Front                                 0
Side Air Bag Rear                                  0
Tyre Pressure Monitor                              0
Clutch Lock                                        0
Anti Pinch Power Windows                           0
Knee Airbags                                       0
Apple Car Play                                     0
Android Auto                                       0
Mirror Link                                        0
Wireless Phone Charging                            0
Compass                                            0
Moon Roof                                          0
Projector Headlamps                                0
Speed Alert                                        0
Eletronic Stability Control                        0
Touch Screen Size                                  0
Xenon Headlamps                                    0
Cd Changer                                         0
Power Boot                                         0
Rear Folding Table                                 0
Smoke Headlamps                                    0
Dvd Player                                         0
Internal Storage                                   0
Rear Entertainment System                          0
Remote Engine Start Stop                           0
Ventilated Seats                                   0
LEDFog Lamps                                       0
View360Camera                                      0
Geo Fence Alert                                    0
Steering Mounted Tripmeter                         0
Remote Climate Control                             0
Remote Horn Light Control                          0
Heated Wing Mirror                                 0
Side Stepper                                       0
Blind Spot Monitor                                 0
Hill Descent Control                               0
Heads Up Display                                   0
Sos Emergency Assistance                           0
Cassette Player                                    0
Find My Car Location                               0
Wifi Connectivity                                  0
Headlamp Washers                                 165
Real Time Vehicle Tracking                         0
Roof Carrier                                       0
Smart Key Band                                   165
Lane Watch Camera                                  0
Removable Convertible Top                          0
Power Folding3rd Row Seat                        287
Mileage                                            0
Max Power                                          0
Torque                                             0
Color                                              0
Engine Type                                        0
No of Cylinder                                     0
Values per Cylinder                                0
Value Configuration                                0
Fuel Suppy System                                  0
Turbo Charger                                      0
Super Charger                                      0
Length                                             0
Width                                              0
Height                                             0
Wheel Base                                         0
Front Tread                                        0
Rear Tread                                         0
Kerb Weight                                        0
Gross Weight                                       0
Gear Box                                           0
Drive Type                                         0
Steering Type                                      0
Turning Radius                                     0
Front Brake Type                                   0
Rear Brake Type                                    0
Top Speed                                          0
Acceleration                                       0
Tyre Type                                          0
No Door Numbers                                    0
Cargo Volumn                                       0
Wheel Size                                         0
Alloy Wheel Size                                   0
city                                               0
dtype: int64

Correlation matrix:

IOPub data rate exceeded.
The Jupyter server will temporarily stop sending output
to the client in order to avoid crashing it.
To change this limit, set the config variable
`--ServerApp.iopub_data_rate_limit`.

Current values:
ServerApp.iopub_data_rate_limit=1000000.0 (bytes/sec)
ServerApp.rate_limit_window=3.0 (secs)


[83]
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("all_cities_cars_cleaned_final_processed.csv")

# Set the style for the plots
sns.set(style="whitegrid")

# Box plot for 'price'
def plot_boxplot_price(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(y=df['price'], color='lightblue')
    plt.title('Box Plot of Car Prices')
    plt.ylabel('Price')
    plt.show()

# Histogram for 'Mileage'
def plot_histogram_mileage(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Mileage'], bins=30, kde=True, color='skyblue')
    plt.title('Histogram of Mileage')
    plt.xlabel('Mileage')
    plt.ylabel('Frequency')
    plt.show()

# Scatter plot comparing two specific columns
def plot_scatter_comparison(df, x_column, y_column):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df[x_column], y=df[y_column], alpha=0.7, color='purple')
    plt.title(f'Scatter Plot of {x_column} vs. {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

# Plot box plot for 'price'
plot_boxplot_price(df)

# Plot histogram for 'Mileage'
plot_histogram_mileage(df)

# Example scatter plot comparing 'Mileage' and 'Max Power'
plot_scatter_comparison(df, 'Mileage', 'Max Power')

C:\Users\Vishwa\anaconda3\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):


[85]
def plot_pairplot(df):
    sns.pairplot(df[['Mileage', 'Max Power', 'Torque', 'price']])
    plt.suptitle('Pair Plot of Selected Features', y=1.02)
    plt.show()

# Plot pair plot
plot_pairplot(df)

C:\Users\Vishwa\anaconda3\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
C:\Users\Vishwa\anaconda3\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
C:\Users\Vishwa\anaconda3\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
C:\Users\Vishwa\anaconda3\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):


[87]
def plot_facet_grid(df, col):
    g = sns.FacetGrid(df, col=col, col_wrap=4, height=4)
    g.map(sns.histplot, 'Mileage', bins=20, kde=True)
    plt.show()

# Example facet grid for 'City'
plot_facet_grid(df, 'city')

C:\Users\Vishwa\anaconda3\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
C:\Users\Vishwa\anaconda3\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
C:\Users\Vishwa\anaconda3\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
C:\Users\Vishwa\anaconda3\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
C:\Users\Vishwa\anaconda3\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):
C:\Users\Vishwa\anaconda3\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):


[142]
def plot_histogram(df, column_name, bins=30):
    plt.figure(figsize=(12, 6))
    sns.histplot(df[column_name], bins=bins, kde=False, color='skyblue')
    plt.title(f'Histogram of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.show()

# Example histogram for 'modelYear'
plot_histogram(df, 'modelYear')
C:\Users\Vishwa\anaconda3\Lib\site-packages\seaborn\_oldcore.py:1119: FutureWarning: use_inf_as_na option is deprecated and will be removed in a future version. Convert inf values to NaN before operating instead.
  with pd.option_context('mode.use_inf_as_na', True):


[144]
def plot_scatter(df, x_column, y_column):
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x=df[x_column], y=df[y_column], color='coral')
    plt.title(f'Scatter Plot of {x_column} vs {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

# Example scatter plot for 'price' vs 'km'
plot_scatter(df, 'price', 'km')
---------------------------------------------------------------------------
KeyError Traceback (most recent call last)
File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:3805, in Index.get_loc(self, key) 3804 try: -> 3805 return self._engine.get_loc(casted_key) 3806 except KeyError as err:
File index.pyx:167, in pandas._libs.index.IndexEngine.get_loc()
File index.pyx:196, in pandas._libs.index.IndexEngine.get_loc()
File pandas\\_libs\\hashtable_class_helper.pxi:7081, in pandas._libs.hashtable.PyObjectHashTable.get_item()
File pandas\\_libs\\hashtable_class_helper.pxi:7089, in pandas._libs.hashtable.PyObjectHashTable.get_item()
KeyError: 'km'
The above exception was the direct cause of the following exception:
KeyError Traceback (most recent call last)
Cell In[144], line 10 7 plt.show() 9 # Example scatter plot for 'price' vs 'km' ---> 10 plot_scatter(df, 'price', 'km')
Cell In[144], line 3, in plot_scatter(df, x_column, y_column) 1 def plot_scatter(df, x_column, y_column): 2 plt.figure(figsize=(12, 6)) ----> 3 sns.scatterplot(x=df[x_column], y=df[y_column], color='coral') 4 plt.title(f'Scatter Plot of {x_column} vs {y_column}') 5 plt.xlabel(x_column)
File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4102, in DataFrame.__getitem__(self, key) 4100 if self.columns.nlevels > 1: 4101 return self._getitem_multilevel(key) -> 4102 indexer = self.columns.get_loc(key) 4103 if is_integer(indexer): 4104 indexer = [indexer]
File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:3812, in Index.get_loc(self, key) 3807 if isinstance(casted_key, slice) or ( 3808 isinstance(casted_key, abc.Iterable) 3809 and any(isinstance(x, slice) for x in casted_key) 3810 ): 3811 raise InvalidIndexError(key) -> 3812 raise KeyError(key) from err 3813 except TypeError: 3814 # If we have a listlike key, _check_indexing_error will raise 3815 # InvalidIndexError. Otherwise we fall through and re-raise 3816 # the TypeError. 3817 self._check_indexing_error(key)
KeyError: 'km'
<Figure size 1200x600 with 0 Axes>
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column_name):
    plt.figure(figsize=(12, 6))
    sns.histplot(df[column_name], bins=30, color='skyblue', kde=True)  # You can adjust the number of bins
    plt.title(f'Histogram of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.show()

# Example histogram for 'km'
plot_histogram(df, 'km')

[145]
import pandas as pd

# Load the dataset
df = pd.read_csv("all_cities_cars_cleaned_final_processed.csv")

# Columns to drop
columns_to_drop = [
    'Power Steering', 'Power Windows Front', 'Air Conditioner', 'Heater', 
    'Adjustable Head Lights', 'Manually Adjustable Exterior Rear View Mirror', 
    'Centeral Locking', 'Child Safety Locks', 'Power Windows Rear', 
    'Remote Trunk Opener', 'Remote Fuel Lid Opener', 'Low Fuel Warning Light', 
    'Accessory Power Outlet', 'Vanity Mirror', 'Rear Seat Headrest', 
    'Cup Holders Front', 'Digital Odometer', 'Electronic Multi Tripmeter', 
    'Fabric Upholstery', 'Glove Compartment', 'Digital Clock', 'Wheel Covers', 
    'Power Antenna', 'Chrome Grille', 'Day Night Rear View Mirror', 
    'Passenger Side Rear View Mirror', 'Halogen Headlamps', 'Rear Seat Belts', 
    'Door Ajar Warning', 'Side Impact Beams', 'Front Impact Beams', 
    'Adjustable Seats', 'Centrally Mounted Fuel Tank', 'Engine Immobilizer', 
    'Anti Theft Device', 'Fog Lights Front', 'Anti Lock Braking System', 
    'Cd Player', 'Trunk Light', 'Multifunction Steering Wheel', 
    'Navigation System', 'Smart Access Card Entry', 'Engine Start Stop Button', 
    'Gear Shift Indicator', 'Luggage Hook And Net', 'Adjustable Steering', 
    'Tachometer', 'Leather Steering Wheel', 'Outside Temperature Display', 
    'Height Adjustable Driver Seat', 'Power Adjustable Exterior Rear View Mirror', 
    'Electric Folding Rear View Mirror', 'Rear Window Wiper', 
    'Rear Window Washer', 'Rear Window Defogger', 'Alloy Wheels', 
    'Integrated Antenna', 'Outside Rear View Mirror Turn Indicators', 
    'Roof Rail', 'Power Door Locks', 'Driver Air Bag', 'Passenger Air Bag', 
    'Seat Belt Warning', 'Keyless Entry', 'Engine Check Warning', 
    'Crash Sensor', 'Ebd', 'Follow Me Home Headlamps', 'Rear Camera', 
    'Speed Sensing Auto Door Lock', 'Pretensioners And Force Limiter Seatbelts', 
    'Impact Sensing Auto Door Lock', 'No Of Airbags', 'Radio', 
    'Speakers Front', 'Speakers Rear', 'Integrated2Din Audio', 
    'Usb Auxiliary Input', 'Bluetooth', 'Touch Screen', 'Number Of Speaker', 
    'Glove Box Cooling', 'Driving Experience Control Eco', 'Tinted Glass', 
    'Rear Spoiler', 'Chrome Garnish', 'Vehicle Stability Control System', 
    'Rear Reading Lamp', 'Rear Seat Centre Arm Rest', 'Cup Holders Rear', 
    'Rear ACVents', 'Air Quality Control', 'Height Adjustable Front Seat Belts', 
    'Cruise Control', 'Voice Control', 'Audio System Remote Control', 
    'Leather Seats', 'Fog Lights Rear', 'Traction Control', 
    'Seat Lumbar Support', 'Battery Saver', 'Lane Change Indicator', 
    'Sun Roof', 'Automatic Driving Lights', 'Anti Theft Alarm', 
    'Automatic Head Lamps', 'Isofix Child Seat Mounts', 'Hill Assist', 
    'Tailgate Ajar', 'Brake Assist', 'Steering Wheel Gearshift Paddles', 
    'LEDTaillights', 'Cigarette Lighter', 'Rain Sensing Wiper', 
    'Drive Modes', 'Active Noise Cancellation', 'Adjustable Headrest', 
    'Hands Free Tailgate', 'Dual Tone Dashboard', 'Leather Wrap Gear Shift Selector', 
    'Dual Tone Body Colour', 'LEDDRLs', 'LEDHeadlights', 'Cornering Headlamps', 
    'Cornering Foglamps', 'Side Air Bag Front', 'Side Air Bag Rear', 
    'Tyre Pressure Monitor', 'Clutch Lock', 'Anti Pinch Power Windows', 
    'Knee Airbags', 'Apple Car Play', 'Android Auto', 'Mirror Link', 
    'Wireless Phone Charging', 'Compass', 'Moon Roof', 'Projector Headlamps', 
    'Speed Alert', 'Eletronic Stability Control', 'Touch Screen Size', 
    'Xenon Headlamps', 'Cd Changer', 'Power Boot', 'Rear Folding Table', 
    'Smoke Headlamps', 'Dvd Player', 'Internal Storage', 'Rear Entertainment System', 
    'Remote Engine Start Stop', 'Ventilated Seats', 'LEDFog Lamps', 
    'View360Camera', 'Geo Fence Alert', 'Steering Mounted Tripmeter', 
    'Remote Climate Control', 'Remote Horn Light Control', 'Heated Wing Mirror', 
    'Side Stepper', 'Blind Spot Monitor', 'Hill Descent Control', 
    'Heads Up Display', 'Sos Emergency Assistance', 'Cassette Player', 
    'Find My Car Location', 'Wifi Connectivity', 'Headlamp Washers', 
    'Real Time Vehicle Tracking', 'Roof Carrier', 'Smart Key Band', 
    'Lane Watch Camera', 'Removable Convertible Top', 'Power Folding3rd Row Seat', 
    'Max Power', 'Torque','Engine Type', 'No of Cylinder', 
    'Values per Cylinder', 'Value Configuration', 'Fuel Suppy System', 
    'Turbo Charger', 'Super Charger', 'Length', 'Width', 'Height', 
    'Wheel Base', 'Front Tread', 'Rear Tread', 'Kerb Weight', 'Gross Weight', 
    'Gear Box', 'Drive Type', 'Steering Type', 'Turning Radius', 
    'Front Brake Type', 'Rear Brake Type', 'Top Speed', 'Acceleration', 
    'Tyre Type', 'No Door Numbers', 'Cargo Volumn', 'Wheel Size', 
    'Alloy Wheel Size'
]

# Drop the columns
df = df.drop(columns=columns_to_drop)

# Save the updated dataset
df.to_csv(r'C:\Users\Vishwa\Desktop\GUVI captone\CAR\dropped_dataset.csv', index=False)

[149]
import pandas as pd
import numpy as np

# Load the preprocessed dataset
df = pd.read_csv('dropped_dataset.csv')


# Separate features and target variable
X = df.drop('price', axis=1)
y = df['price']

# Compute correlation of each feature with the target variable
correlation_with_target = X.corrwith(y).abs()

# Define a function to select features based on correlation with the target variable
def select_features_by_correlation(correlation_with_target, threshold):
    relevant_features = correlation_with_target[correlation_with_target > threshold].index.tolist()
    return relevant_features

# Set the correlation threshold
correlation_threshold = 0.1

# Select features based on the correlation threshold
selected_features = select_features_by_correlation(correlation_with_target, correlation_threshold)

# Include 'price' in the output to save as well
selected_features.append('price')

# Create a DataFrame with selected features
X_selected = df[selected_features]

# Save the selected features to a new CSV file
X_selected.to_csv(r"C:\Users\Vishwa\Desktop\GUVI captone\CAR\selected_features_correlation_matrix.csv", index=False)

# Print the selected features
print("Selected Features:", selected_features)
Selected Features: ['ft', 'bt', 'km', 'transmission', 'ownerNo', 'oem', 'model', 'modelYear', 'centralVariantId', 'variantName', 'Engine Displacement', 'Mileage', 'price']

C:\Users\Vishwa\anaconda3\Lib\site-packages\numpy\lib\function_base.py:2897: RuntimeWarning: invalid value encountered in divide
  c /= stddev[:, None]
C:\Users\Vishwa\anaconda3\Lib\site-packages\numpy\lib\function_base.py:2898: RuntimeWarning: invalid value encountered in divide
  c /= stddev[None, :]

[151]
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('selected_features_correlation_matrix.csv')

# Separate features and target variable
X = df.drop('price', axis=1)  # Features
y = df['price']               # Target variable

# Perform the train-test split
# Common split ratio: 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print shapes of the resulting datasets
print(f"Training set features shape: {X_train.shape}")
print(f"Testing set features shape: {X_test.shape}")
print(f"Training set target shape: {y_train.shape}")
print(f"Testing set target shape: {y_test.shape}")
Training set features shape: (744, 12)
Testing set features shape: (187, 12)
Training set target shape: (744,)
Testing set target shape: (187,)

[153]
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Initialize the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Linear Regression:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R2): {r2:.2f}")
Linear Regression:
Mean Absolute Error (MAE): 91943.58
Mean Squared Error (MSE): 12913432426.30
R-squared (R2): 0.69

[156]

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Linear Regression:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R2): {r2:.2f}")
Linear Regression:
Mean Absolute Error (MAE): 91943.58
Mean Squared Error (MSE): 12913432426.30
R-squared (R2): 0.69

[158]
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Initialize the model
model = DecisionTreeRegressor()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Decision Tree Regressor:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R2): {r2:.2f}")

Decision Tree Regressor:
Mean Absolute Error (MAE): 75516.04
Mean Squared Error (MSE): 9720060160.43
R-squared (R2): 0.76

[160]
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Initialize the model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Random Forest Regressor:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R2): {r2:.2f}")

Random Forest Regressor:
Mean Absolute Error (MAE): 60074.70
Mean Squared Error (MSE): 6161310000.36
R-squared (R2): 0.85

[162]
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Initialize the model
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Gradient Boosting Regressor:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R2): {r2:.2f}")
Gradient Boosting Regressor:
Mean Absolute Error (MAE): 59949.80
Mean Squared Error (MSE): 5891892995.73
R-squared (R2): 0.86

[164]
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import make_scorer, mean_absolute_error, mean_squared_error, r2_score

# Load the preprocessed dataset
df = pd.read_csv('selected_features_correlation_matrix.csv')

# Separate features and target variable
X = df.drop('price', axis=1)
y = df['price']

# Define the models
models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree Regressor': DecisionTreeRegressor(),
    'Random Forest Regressor': RandomForestRegressor(),
    'Gradient Boosting Regressor': GradientBoostingRegressor(),
}

# Define the cross-validation procedure
cv_folds = 5  # Number of folds for cross-validation
scoring = {
    'MAE': make_scorer(mean_absolute_error),
    'MSE': make_scorer(mean_squared_error),
    'R2': make_scorer(r2_score)
}

results = {}
for name, model in models.items():
    print(f"Training and evaluating {name}...")
    
    # Perform cross-validation
    cv_results = {}
    for metric, scorer in scoring.items():
        scores = cross_val_score(model, X, y, cv=cv_folds, scoring=scorer)
        cv_results[metric] = scores.mean()
    
    results[name] = cv_results

# Print results
for name, metrics in results.items():
    print(f"{name}:")
    for metric, score in metrics.items():
        print(f"  {metric}: {score:.2f}")
    print()

Training and evaluating Linear Regression...
Training and evaluating Decision Tree Regressor...
Training and evaluating Random Forest Regressor...
Training and evaluating Gradient Boosting Regressor...
Linear Regression:
  MAE: 93787.22
  MSE: 14100360629.75
  R2: 0.65

Decision Tree Regressor:
  MAE: 86646.71
  MSE: 11730974489.68
  R2: 0.70

Random Forest Regressor:
  MAE: 68842.32
  MSE: 7716905555.66
  R2: 0.81

Gradient Boosting Regressor:
  MAE: 65993.02
  MSE: 7174471547.04
  R2: 0.82


[165]
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# Load the dataset
df = pd.read_csv('selected_features_correlation_matrix.csv')

# Separate features and target variable
X = df.drop('price', axis=1)
y = df['price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Define the models
models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree Regressor': DecisionTreeRegressor(random_state=42),
    'Random Forest Regressor': RandomForestRegressor(n_estimators=100, random_state=42),
    'Gradient Boosting Regressor': GradientBoostingRegressor(random_state=42)
}
# Define cross-validation strategy
cv = 5  # Number of cross-validation folds

# Train and evaluate each model
for name, model in models.items():
    # Perform cross-validation
    cv_scores = cross_val_score(model, X_train, y_train, cv=cv, scoring='neg_mean_absolute_error')
    
    # Train the model on the full training data
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Calculate performance metrics
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # Output the results
    print(f'{name}:')
    print(f'  Cross-Validation MAE: {-cv_scores.mean():.2f} (+/- {cv_scores.std():.2f})')
    print(f'  Test Set MAE: {mae:.2f}')
    print(f'  Test Set MSE: {mse:.2f}')
    print(f'  Test Set R-squared: {r2:.2f}\n')

Linear Regression:
  Cross-Validation MAE: 89695.04 (+/- 5443.70)
  Test Set MAE: 91943.58
  Test Set MSE: 12913432426.30
  Test Set R-squared: 0.69

Decision Tree Regressor:
  Cross-Validation MAE: 84735.27 (+/- 5796.97)
  Test Set MAE: 78427.81
  Test Set MSE: 10086844919.79
  Test Set R-squared: 0.76

Random Forest Regressor:
  Cross-Validation MAE: 63980.66 (+/- 6005.01)
  Test Set MAE: 60074.70
  Test Set MSE: 6161310000.36
  Test Set R-squared: 0.85

Gradient Boosting Regressor:
  Cross-Validation MAE: 62843.34 (+/- 6365.97)
  Test Set MAE: 59949.80
  Test Set MSE: 5891892995.73
  Test Set R-squared: 0.86


[166]
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
import joblib

# Load the dataset
df = pd.read_csv("selected_features_correlation_matrix.csv")

# Step 1: Feature Engineering

# Create a new feature 'car_age' from 'modelYear'
df['car_age'] = 2024 - df['modelYear']

# Create a new feature 'km_per_year' by dividing 'km' by 'car_age'
df['km_per_year'] = df['km'] / df['car_age']

# Interaction feature: Create a feature by multiplying 'Engine Displacement' with 'Mileage'
df['engine_displacement_mileage'] = df['Engine Displacement'] * df['Mileage']

# Log transformation: Apply log transformation to 'km' to reduce skewness
df['log_km'] = np.log1p(df['km'])

# Drop the original 'km' column after log transformation
df = df.drop(columns=['km'])

# Define features and target variable in the specified order
features = [
    'ft', 'bt', 'transmission', 'ownerNo', 'oem', 'model', 'modelYear', 
    'centralVariantId', 'variantName', 'Engine Displacement', 'Mileage', 
    'car_age', 'km_per_year', 'engine_displacement_mileage', 'log_km'
]
X = df[features]
y = df['price']  # Target variable

# Step 2: Imputation and Scaling

# Impute missing values with the mean
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)  # Features

# Scale numerical features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Step 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Model Training with Hyperparameter Tuning

# Initialize the Gradient Boosting Regressor
gbr = GradientBoostingRegressor(random_state=42)

# Define the hyperparameter grid
param_grid = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 5, 7],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2', None]
}

# Perform GridSearchCV to find the best hyperparameters
grid_search = GridSearchCV(estimator=gbr, param_grid=param_grid, cv=5, n_jobs=-1, scoring='r2', verbose=2)
grid_search.fit(X_train, y_train)

# Get the best model from GridSearchCV
best_model = grid_search.best_estimator_

# Step 5: Model Evaluation

# Make predictions on the test set
y_pred = best_model.predict(X_test)

# Evaluate the model
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

print(f"Best Hyperparameters: {grid_search.best_params_}")
print(f"R2 Score: {r2}")
print(f"RMSE: {rmse}")

# Save the model
output_path = r"C:\Users\Vishwa\Desktop\GUVI captone\CAR\gradient_boosting_model.joblib"
joblib.dump(best_model, output_path)

print(f"Model saved to {output_path}")

Fitting 5 folds for each of 729 candidates, totalling 3645 fits
Best Hyperparameters: {'learning_rate': 0.1, 'max_depth': 3, 'max_features': None, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 200}
R2 Score: 0.85510121986678
RMSE: 77396.676115138
Model saved to C:\Users\Vishwa\Desktop\GUVI captone\CAR\gradient_boosting_model.joblib

