import os
from cryptography.fernet import Fernet
import sys
import argparse
import functions

parser = argparse.ArgumentParser(description='Encryption tool to encrypt and decrypt files on your computer')
parser.add_argument('filepath', help='The path to a file that the program will work with')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-e', '--encrypt', action='store_true', help='Encrypts the file that is specified')
group.add_argument('-d', '--decrypt', action='store_true', help='Decrypts the file that is specified')
args = parser.parse_args()

if(not(os.path.isfile(args.filepath))):
    print("The path you entered is not a file")
    sys.exit(0)

if(args.encrypt):
    key = functions.check_password()
    with open(args.filepath, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(args.filepath,'wb') as f:
        f.write(encrypted)
elif(args.decrypt):
    key = functions.check_password()
    with open(args.filepath, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(args.filepath,'wb') as f:
        f.write(decrypted)
else:
    print("You did not enter the command correctly, enter \'python pass.py -h\' for help")
