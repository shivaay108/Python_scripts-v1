## simple python program to generate a hash 
# using hashlib and argv


import hashlib

from sys import argv

m  = hashlib.sha256()
m.update(b"this file")
Digest = m.digest()
print(Digest)