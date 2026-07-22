# Accepts two file names through command line arguments 
# Compares the contents of both files.
# If both files contains the same contents
# Display success otherwise display failure

import sys
import os 

try :
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    if(os.path.exists(file1) and os.path.exists(file2)):
        fobj1 = open(file1 , "r")
        fobj2 = open(file2 , "r")

        data1 = 0 
        data2 = 0 

        is_same = True

        while(True):
            data1 = fobj1.readline()

            data2 = fobj2.readline()

            if data1 != data2 :
                is_same = False
                break

            if data1 == "" and data2 == "":
                break

        if is_same == True:
            print("Success")
        else:
            print("Failure")

        fobj1.close()
        fobj2.close()

    else:
        print(f"{file1} or {file2} is not in current directory")

except Exception as eobj:
    print("Exception occured : ",eobj)