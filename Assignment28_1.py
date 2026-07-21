# Acccept file name from user
# Count lines in file


import sys
import os

try:
    filename = sys.argv[1]

    if(os.path.exists(filename)):
        fobj = open(filename , "r")

        data = 0
        line = 0 

        while True:
            data = fobj.readline()
            if data == "":
                break 
            line = line + 1    

        print(f"Total number of lines in {filename} : ",line)

        fobj.close()

    else:
        print("File is not present in current directory")

except Exception as eobj:
    print("Exception occured : ",eobj)