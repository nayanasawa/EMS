import zipfile
import os
import pandas as pd
from datetime import datetime

# Extract the load_timestamp from the zip file
def extract_load_timestamp(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        timestamp_str = zip_ref.filename.split('/')[-1].split('_')[0]
        load_timestamp = datetime.strptime(timestamp_str, '%Y%m%d%H%M%S%f')
        return load_timestamp

# Function to process CSV files
def process_csv(csv_filename, load_timestamp):
    df = pd.read_csv(csv_filename)
    df['load_timestamp'] = load_timestamp
    return df


# Path to the ZIP file and CSV files
zip_filename = '/home/nineleaps/Downloads/20240305124003123456_Extract 2.zip'
csv_files = ['/home/nineleaps/Downloads/sample2.csv', '/home/nineleaps/Downloads/sample.csv']

# Extracting load_timestamp from the ZIP file name
load_timestamp = extract_load_timestamp(zip_filename)

# Extracting files from the ZIP
with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extractall()

# Processing each CSV file
for csv_file in csv_files:
    # Constructing the full path to the CSV file
    csv_file_path = os.path.join(os.getcwd(), csv_file)

    # Processing the CSV file
    df = process_csv(csv_file_path, load_timestamp)

    # Saving the modified dataframe back to CSV
    output_filename = os.path.splitext(csv_file)[0] + '_updated.csv'
    df.to_csv(output_filename, index=False)

print("Task completed successfully.")
