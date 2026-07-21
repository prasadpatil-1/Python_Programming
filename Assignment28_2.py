# Acccept file name from user
# Count Toatal numbers of worlds in file

import sys
import os
try:
    filename = sys.argv[1]

    if(os.path.exists(filename)):
        fobj = open(filename , "r")
        
        data = fobj.read()

        datalist = data.split()

        print(f"Total number of words in {filename} : ",len(datalist))

        fobj.close()

    else:
        print("File is not present in current directory")

except Exception as eobj:
    print("Exception occured : ",eobj)