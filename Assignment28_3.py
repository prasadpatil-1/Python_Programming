# Accept file name form user
# Display file content

import sys
import os
try:
    filename = sys.argv[1]

    if(os.path.exists(filename)):
        fobj = open(filename , "r")

        data = 0

        while True:
            data = fobj.readline()

            if data == "":
                break 
            else:
                print(data)
            
            

        fobj.close()

    else:
        print("File is not present in current directory")

except Exception as eobj:
    print("Exception occured : ",eobj)