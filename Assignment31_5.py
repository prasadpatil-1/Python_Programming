# Accept the directory name and count every files in it every five minutes
# Write the result into : DirectoryCountLog.txt

import schedule 
import sys
import os
import time
import datetime

def ScanDirectory(Directory_Name):

    ret = CheckDirectory(Directory_Name)

    if ret == False:
        print("Directory Scan Error : The Directory Does not Exists")

    else:
        total_files = 0 

        for FolderName , SubFolder , FileName in os.walk(Directory_Name):            
            for file in FileName:
                total_files = total_files + 1
        
        if (os.path.exists("DirectoryCountLog.txt")):
            fobj = open("DirectoryCountLog.txt","a")

        else:
            fobj = open("DirectoryCountLog.txt","w")

        timestamp = datetime.datetime.now()
        finaltime = timestamp.strftime("%d-%m-%Y %I-%M-%S %p")
        final_time = finaltime.replace("-" , "_")

        fobj.write(f"Directory Path : {Directory_Name}\n")
        fobj.write(f"Number of files : {total_files} \n")
        fobj.write(f"Date and time : {final_time}\n")
    
        fobj.close()

        print("Waiting for next schedule ...")

def CheckDirectory(Directory_Name):
    ret = False

    ret = os.path.exists(Directory_Name)

    if ret == True:
        ret = os.path.isdir(Directory_Name)

    return ret

def main():
    if (len(sys.argv) == 2):

        print("Directory Scan Application is Running....")

        schedule.every(5).minutes.do(ScanDirectory , sys.argv[1])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")
        print("Please run program as :")
        print("python filename.py DirectoryName ")


if __name__ == "__main__":
    main()