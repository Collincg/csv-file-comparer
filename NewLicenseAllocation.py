# Collin Graff 
# 06/26/2024
# Program to read 2 separate csv files and with employees in each file. File A contains information on thier employment status.
# File B contains information on whether or not they have an Office 365 license. 
# We want all active employees to have a license and all innactive employees to have their license removed. 
# This will help our department avoid having to purchase more licenses than required. 
# Program used by Rice County, Minnesota 

import csv

# Function to read the second CSV file and get license status
def get_license_status(license_file):
    license_data = {}
    with open(license_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            print("TEST", row[12])
            first_name = row[7]  # First name in the 5th column
            last_name = row[9]   # Last name in the 10th column
            has_license = row[12].strip() == 'Office 365 G1 GCC'
            license_data[(first_name, last_name)] = has_license
    return license_data

# File paths
status_file = "CopyOfAmberReport.csv"
license_file = "CopyOfTuesdayUsers.csv"
final_file = "FinalCSV.csv"

# print("TEST", get_license_status(license_file))

# Read the license status data
license_data = get_license_status(license_file)

# Read the source CSV file and prepare the data
with open(status_file) as status_handle:
    with open(final_file, mode='w', newline='') as final_handle:
        data = {}

        # Read the lines from the source CSV file
        reader = csv.reader(status_handle)
        next(reader)  # Skip the header
        
        for line in reader:
            first_name = line[0]  # First name in the 1st column
            last_name = line[1]   # Last name in the 2nd column
            status = line[5]      # Status in the 6th column
            name_key = (first_name, last_name)

            # Check if the name is already in the dictionary
            if name_key in data:
                if status == 'active':
                    data[name_key]['status'] = status
            else:
                data[name_key] = {'status': status}

        # Create a CSV writer object
        writer = csv.writer(final_handle)
        
        # Write the header
        writer.writerow(['First Name', 'Last Name', 'Status', 'Has Office 365 G1 GCC License'])

        # Write the data to the final CSV file
        for name_key, details in data.items():
            first_name, last_name = name_key
            status = details['status']
            has_license = license_data.get(name_key, False)
            writer.writerow([first_name, last_name, status, has_license])
