# Accepts an existing file name through command line arguments
# Create a new file named as Demo.txt 
# Copies all contents from the given file into Demo.txt
 
import sys 
import os 

try:
    existing_file = sys.argv[1]

    if(os.path.exists(existing_file)):
        fobj = open(existing_file , "r")

        data = fobj.read()

        new_file = "Demo.txt"
                    
        fobj1 = open(new_file , "w")
        fobj1.write(data)

        fobj.close()
        fobj1.close()

        print(f"Content of {existing_file} copied into {new_file}")

    else:
        print("File is not present in current directory")

except Exception as eobj:
    print("Exception occured : ",eobj)