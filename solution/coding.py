from cryptography.fernet import Fernet
from smart_solution import settings

key = settings.encryption_key

def encryption(value):
    value = value.encode()
    a = Fernet(key)
    coded_string = a.encrypt(value)
    return coded_string.decode()

def decryption(doc):
    doc = doc.encode()
    a = Fernet(key)
    decoded_string = a.decrypt(doc)
    return decoded_string.decode()