# !/usr/bin/python
import wordDictHashChk
import sys

def main(word, file):
    # word = sys.argv[1]
    # library = "best15.txt"
    # print word
    
    # library = file
    
    passList = setPasswordFiles(file)
    fileCount = len(passList)
    for x in range(0,fileCount):
        afile = passList[x]
        wordDictHashChk.dictHashGen(afile, word)


    # wordDictHashChk.dictHashGen(library, word)


def setPasswordFiles(afileName):
    f=file(afileName, 'r')
    sourceList = [word.strip() for word in f]
    f.close()
    return sourceList

main(sys.argv[1], sys.argv[2])