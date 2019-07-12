import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import sys
import getpass

def check_password():
    if(not os.path.isfile("current_pword.txt")):
        password = getpass.getpass("Please enter a password that you will remember: ")
        double_check = getpass.getpass("Please enter it again: ")
        if(not(password == double_check)):
            print("Sorry the passwords did not match")
            sys.exit(0)
        with open("current_pword.txt", "w") as f:
            f.write(password)
    else:
        with open("current_pword.txt", "r") as f:
            c_pword = f.read()
        attempt = getpass.getpass("What is your password: ")
        if(attempt == c_pword):
            password = attempt
        else:
            print("You entered the wrong password {}".format(attempt))
            sys.exit(0)  
    my_password = password.encode()
    
    if(not os.path.isfile("salt.txt")):
        salt = os.urandom(16)
        with open("salt.txt", "wb") as f:
            f.write(salt)
    else:
        with open("salt.txt", "rb") as f:
            salt = f.read()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(my_password))
    return key

