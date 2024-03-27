# Arya Kuttiyan
# Independent Study Computer Science in Healthcare
# 3/19/24
# This program loads in cancer patient data and encrypts the data
import csv # From Analytics Vidhya
import hashlib # From Geeks for Geeks and Analytics Vidhya

# opens file with data
patient_data = open('cancer_patient_data.csv') # From Analytics Vidhya

# reads in the data in the file
csv_reader = csv.reader(patient_data) # From Analytics Vidhya

rows = [] 
# Adds all the rows in the file to a list
for row in csv_reader: # From Analytics Vidhya
    rows.append(row) # From Analytics Vidhya

# Initializes lists of the rows of encrypted data
encrypted_rows = []
encrypted_row = []
i = 0

# Looks at each row of data
for row in rows:
    # Looks at all the data in the row
    for data in row:
        # encrypts the data by hashing it
        # hashing is where data is converted into a fixed length string of letters and numbers

        # encodes the data so that it can be hashed
        # encoding is when data is changed into a different form to make storage and transmission efficient
        encoded_data = data.encode('utf-8') # From Analytics Vidya and Geeks for Geeks

        # Sets up the hashing function
        sha256 = hashlib.sha256() # From Geeks for Geeks

        # Passes in the encoded data so that it can be hashed
        sha256.update(encoded_data) # From Geeks for Geeks

        # This hashes the data
        string_hash = sha256.hexdigest() # From Geeks for Geeks

        # Adds the hashed data to a new row
        encrypted_row.append(string_hash)
    # Adds the row with the hashed data to a new list of rows
    encrypted_rows.append(encrypted_row[i: i + 25])
    i = i + 25

# prints the encrypted data
print(encrypted_rows)
   