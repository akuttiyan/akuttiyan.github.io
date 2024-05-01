# Arya Kuttiyan
# Independent Study Computer Science in Healthcare
# 3/19/24
# This program loads in cancer patient data and encrypts the data
import csv # From Analytics Vidhya
import hashlib # From Geeks for Geeks and Analytics Vidhya
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes

#################### Code From PyCryptoDome ##############################################333
# opens file with data
patient_data = open('cs-in-healthcare\code\cancer_patient_data.csv') # From Analytics Vidhya

# reads in the data in the file
csv_reader = csv.reader(patient_data) # From Analytics Vidhya


rows = [] 
# Adds all the rows in the file to a list
for row in csv_reader: # From Analytics Vidhya
    rows.append(row) # From Analytics Vidhya

# Initializes lists of the rows of encrypted data

aes_key = get_random_bytes(16)
hmac_key = get_random_bytes(16)

cipher = AES.new(aes_key, AES.MODE_CTR)

encrypted_rows = []
encrypted_row = []
i = 0
# Looks at each row of data
for row in rows:
    # Looks at all the data in the row
    for data in row:
        encoded_data = data.encode()
        cipher_text = cipher.encrypt(encoded_data)
        hmac = HMAC.new(hmac_key, digestmod=SHA256)
        tag = hmac.update(cipher.nonce + cipher_text).digest()
        encrypted_row.append(cipher_text)

    encrypted_rows.append(encrypted_row[i: i + 25])
    i = i + 25

patient_data.close()

encrypted_file = open("cs-in-healthcare\code\encrypted_file.bin", "wb")
encrypted_file.write(tag)
encrypted_file.write(cipher.nonce)
encrypted_file.write(cipher_text)


#print(encrypted_rows)
        

'''
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
'''