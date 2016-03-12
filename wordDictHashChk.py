#!/usr/bin/python
import sys
import hashlib

# ,out
def dictHashGen(afile, looking):
        dict = importFile(afile)
        dictlen = len(dict)
        fileNamed = getFileName(afile)
        # print fileNamed
        
        # print dict
        # print looking
        lookingHashed = hashlib.sha256(looking).hexdigest()
        # print lookingHashed
        
        # out
        # file = open('test.txt', "w")
        for x in range(0,dictlen):
            # Changed sha512 to sha256
            word = dict[x].replace("'","") 
            # print word
            hashed = hashlib.sha256(word).hexdigest()
            # print hashed
            # file.write(dict[x] + '\t' + hashed + '\n')
            
            if (hashed == lookingHashed):
                print fileNamed + " found the word " + dict[x]
        # file.close()
    
def importFile(aFileName):
    f=file(aFileName, 'r')
    words = [word.strip() for word in f]
    f.close()
    return words
    
def getFileName(pathName):
    return pathName.split("/")[5]
        
def main(afile, answer):
# output):
    wordList = importFile(afile)
    print answer
    # answer = "72ab994fa2eb426c051ef59cad617750bfe06d7cf6311285ff79c19c32afd236"
    dictHashGen(wordList, answer )
    # ,output
        
#Call to main method  Pass in a dictionary  
# main(sys.argv[1], sys.argv[2])

# if __name__ == "__main__":
#     # import sys
#     main(sys.argv[1], sys.argv[2])