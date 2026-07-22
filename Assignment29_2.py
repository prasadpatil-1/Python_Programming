# Accepts a file name from user
# Opens that file
# Display the entire contents on the console


import sys
import os
try:
    filename = sys.argv[1]

    if(os.path.exists(filename)):
        fobj = open(filename , "r")

        data = fobj.read()

        print(data)
        
        fobj.close()

    else:
        print("File is not present in current directory")

except Exception as eobj:
    print("Exception occured : ",eobj)