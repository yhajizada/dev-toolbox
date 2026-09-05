import os
from cryptography.fernet import Fernet

class FileEncryptor:
    @staticmethod
    def generate_key(key_path="secret.key"):
        key = Fernet.generate_key()
        with open(key_path, "wb") as key_file:
            key_file.write(key)
        print(f"[+] Key saved successfully to {key_path}")

    @staticmethod
    def encrypt_file(file_path, key_path="secret.key"):
        with open(key_path, "rb") as key_file:
            key = key_file.read()
        fernet = Fernet(key)
        
        with open(file_path, "rb") as file:
            original = file.read()
        
        encrypted = fernet.encrypt(original)
        with open(file_path, "wb") as file:
            file.write(encrypted)
        print(f"[+] {file_path} has been encrypted successfully.")

if __name__ == "__main__":
    print("Dev-Toolbox File Encryptor Utility")