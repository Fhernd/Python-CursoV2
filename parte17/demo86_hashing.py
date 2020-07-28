import hashlib
import binascii
import os

# Fuente: https://www.vitoshacademy.com/hashing-passwords-in-python/
def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

print(hash_password('User2k20'))
print()
print(hash_password('Adm1n@2020'))
