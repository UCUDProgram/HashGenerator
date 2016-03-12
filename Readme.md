Purpose of this project is to create a python script that will aid in determining the ease of a password hack attempt


To run the python script, There are two command-line arguments 
    First is the word you are trying to check for security status
    Second is the file, which has the path of all the files you want to check
    
    
For example, python PWDCheckcript.py password PasswordFilesList.txt will iterate
throuth each file in PasswordFilesList.txt and print that file found password, each
time that the file has that password in its list

Currently, It uses a sha256 hash for comparison.  The premise for that is latter
development will allow the user to pass in the hash string and what encryption 
they use.


