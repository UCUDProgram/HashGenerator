#!/usr/bin/python
import sys
import hashlib

def main(word):
    hash = hashlib.sha512('word').hexdigest()
    print hash    
        
#Call to main method  Pass in a dictionary  
main(sys.argv[1])