from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
import sys
from encryption import hmac_key, aes_key

####################################### Code from PyCryptoDome ############################################3


encrypted_file = open("cs-in-healthcare\code\encrypted_file.bin", "rb")

tag = encrypted_file.read(32)
nonce = encrypted_file.read(8)
cipher_text = encrypted_file.read()

print("tag", tag)
print("nonce", nonce)
print("cipher", cipher_text)


try:
    hmac = HMAC.new(hmac_key, digestmod=SHA256)
    tag = hmac.update(nonce + cipher_text).verify(tag)
except ValueError:
        print("The message was modified!")
        sys.exit(1)

cipher = AES.new(aes_key, AES.MODE_CTR, nonce=nonce)
message = cipher.decrypt(cipher_text)
decoded_message = message.decode()

print(decoded_message)

'''
decrypted_rows = []
decrypted_row = []
i = 0
# Looks at each row of data
for row in cipher_text:
    # Looks at all the data in the row
    for data in row:
        # encrypts the data by hashing it
        # hashing is where data is converted into a fixed length string of letters and numbers

        try:
            hmac = HMAC.new(hmac_key, digestmod=SHA256)
            tag = hmac.update(nonce + cipher_text).verify(tag)
        except ValueError:
            print("The message was modified!")
            sys.exit(1)

        cipher = AES.new(aes_key, AES.MODE_CTR, nonce=nonce)
        message = cipher.decrypt(cipher_text)
        decoded_message = message.decode()

        decrypted_row.append(decoded_message)

    decrypted_rows.append(decrypted_row[i: i + 25])
    i = i + 25

    print(decrypted_rows)
'''