# Accepts a file name and a word from the user 
# Check whether that word is present in the file or not.

import sys
import os

try:
    file_name = sys.argv[1]
    to_search = sys.argv[2]

    if (os.path.exists(file_name)):
        fobj = open(file_name , "r")

        data = fobj.read()

        datalist = data.split()

        is_present = False

        for word in datalist:
            if word == to_search:
                is_present = True
                break

        if is_present == True:
            print(f"{to_search} is present in {file_name}")
        else:
            print(f"{to_search} is not present in {file_name}")


        fobj.close()

    else:
        print("File is not present in current directory")

except Exception as eobj:
    print("Exception occured : ",eobj)