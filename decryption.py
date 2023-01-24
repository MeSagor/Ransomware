import os
from cryptography.fernet import Fernet

key = b'nbQt0koSj5JvrlF6PtA8fcy7kmKRnBuQpzoWVBkwVoQ='


def decrypt_file(file_name):
    with open(file_name, 'rb') as the_file:
        contents = the_file.read()
    contents_decrypted = Fernet(key).decrypt(contents)
    with open(file_name, 'wb') as the_file:
        the_file.write(contents_decrypted)


pwd = os.getcwd()
total_file = 0
total_unsuccessful_file = 0
for root, dirs, files in os.walk(pwd):
    for name in files:
        if name == 'decryption.py':
            continue
        file_path = os.path.join(root, name)
        try:
            decrypt_file(file_path)
            total_file += 1
        except:
            total_unsuccessful_file += 1

print(f"Root: {pwd}")
print(f"Total Decrypted file: {total_file}")
print(f"Total Decryption failed file: {total_unsuccessful_file}")
