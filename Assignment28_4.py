# Accepts two file names from the user 
# First file is an existing file  and second file is a new file 
# Copy all contents from the firrst file into the second file.

import sys 

import os 

try:
    existing_file = sys.argv[1]
    new_file = sys.argv[2]

    if(os.path.exists(existing_file)):
        fobj = open(existing_file , "r")

        data = fobj.read()
            
        fobj1 = open(new_file , "w")
        fobj1.write(data)

        fobj.close()
        fobj1.close()

        print(f"Content of {existing_file} copied into {new_file}")

    else:
        print("File is not present in current directory")

except Exception as eobj:
    print("Exception occured : ",eobj)