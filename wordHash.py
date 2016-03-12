#!/usr/bin/python
import sys
import hashlib

def main(word,hashType):
    
    if hashType == "md5":
        hash = hashlib.md5('word').hexdigest()
    elif hashType == "sha1":
        hash = hashlib.sha1('word').hexdigest()
    elif hashType == "sha224":
        hash = hashlib.sha224('word').hexdigest()
    elif hashType == "sha256":
        hash = hashlib.sha256('word').hexdigest()
    elif hashType == "sha384":
        hash = hashlib.sha384('word').hexdigest()
    elif hashType == "sha512":
        hash = hashlib.sha512('word').hexdigest()

    print hash

main(sys.argv[1], sys.argv[2])