#!/usr/bin/python
import sys
import hashlib

# ,out
def dictHashGen(dict, newfile):
    
        dictlen = len(dict)
        file = open(newfile, "w")
        for x in range(0,dictlen):
            # Changed sha512 to sha256
            hashed = hashlib.sha256('dict[x]').hexdigest()
            file.write(dict[x] + '\t' + hashed + '\n')
        file.close()
    
def importFile(aFileName):
    f=file(aFileName, 'r')
    words = [word.strip() for word in f]
    f.close()
    return words
        
def main(afile,savefile):
    wordList = importFile(afile)
    dictHashGen(wordList, savefile)
  
#Call to main method  Pass in a dictionary  
main(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    # import sys
    main(sys.argv[1], sys.argv[2])