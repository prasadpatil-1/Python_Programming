# Accepts a file name & one string from the user 
# Return the frequency of that string in the file.

import sys
import os

try:
    file_name = sys.argv[1]
    to_search = sys.argv[2]

    if (os.path.exists(file_name)):
        fobj = open(file_name , "r")

        data = fobj.read()

        datalist = data.split()

        frequency = 0 

        for word in datalist:
            if word == to_search:
                frequency = frequency + 1

        print(f"{to_search} is present {frequency} times in the {file_name}")

        fobj.close()

    else:
        print("File is not present in current directory")

except Exception as eobj:
    print("Exception occured : ",eobj)