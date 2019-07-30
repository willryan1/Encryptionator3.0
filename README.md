# Encryptionator3.0
Tool that encrypts and decrypts files

## Requirements

* Python 3 or higher
* Python module pip3
* Python module cryptograpy

### Installing cryptograpy
```
pip install cryptography
```

### Download Encryptionator3.0
```
git clone https://github.com/willryan1/Encryptionator3.0.git
```

## Usage
```
python3 encryptionator.py [-h] (-e | -d) fileyouwanttoencrypt
```

### Get Help
```
python3 encryptionator.py -h
```
### Remember
You want to be very careful when encrypting and decrypting files. Remember to never delete the file that the password is stored in. There are also easier ways to hide your data from the public.
An example:
Simply change the permissions on a file so a user needs root access to read or write:
```
sudo chown root <file>
sudo chmod 600 <file>
```
However if you want to make sure your data is safe, encrypting is not a bad option.

## Author

* **Will Ryan**
