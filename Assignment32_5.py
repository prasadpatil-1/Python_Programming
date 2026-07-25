import sys
import os
import schedule
import time
import datetime


def DeleteEmptyFiles(Directory_Path ):
    ret = False
    ret = ValidateDirectory(Directory_Path )
    if ret == False:
        print("Invalid Argument : Source  path is invalid")
        return

    else:
        empty_files = 0 
        total_files = 0 
        deleted_files = 0 

        dir_path = os.path.join(Directory_Path , "Empty_Files_Log")
        dir_path = f"%s.txt"%(dir_path)

        if(os.path.exists(dir_path)):
                fobj = open(dir_path , "a")
        else:
            fobj = open(dir_path , "w")

        fobj.write(f"="*70+"\n")
        fobj.write("Empty Files Removal Log:\n")
        fobj.write(f"="*70+"\n")

        timestamp = datetime.datetime.now()
        final_time = timestamp.strftime("%d-%m-%Y %I-%M-%S %p")

        for FolderName , SubFolder , FileName in os.walk(Directory_Path):
            for filename in FileName:
                file_path = os.path.join(FolderName , filename)

                if filename == "Empty_Files_Log.txt":
                    continue

                total_files = total_files + 1

                if(os.path.getsize(file_path) == 0):
                    empty_files = empty_files + 1
                    try :
                        os.remove(file_path)
                        deleted_files = deleted_files + 1

                        fobj.write(f"="*70+"\n")
                        fobj.write(f"Deleted File Information \n\n")
                        
                        fobj.write(f"Time of Scan : {final_time} \n")
                        fobj.write(f"File Name : {filename}\n")
                        fobj.write(f"Deleted File Path : {file_path} \n")
                        fobj.write(f"Status : Success \n")

                        fobj.write(f"="*70+"\n\n")

                    except PermissionError as eobj :
                        fobj.write(f"Time of Scan : {final_time} \n")
                        fobj.write(f"File Name : {filename}\n")
                        fobj.write(f"File Path : {file_path} \n")
                        fobj.write("Status : Failed \n")
                        fobj.write("Reason : Permission Denied")

    fobj.write(f"Total Files Scanned : {total_files} \n")
    fobj.write(f"Total Empty Files Found : {empty_files}\n")
    fobj.write(f"Total Empty Files Deleted : {deleted_files} \n ")
    fobj.write(f"="*70+"\n\n")            

    fobj.close()

    print("Waiting for next schedule ...\n")
                                

def ValidateDirectory(Directory_Path ):
    ret = False
    ret = os.path.exists(Directory_Path)
    if ret == True:
        ret = os.path.isdir(Directory_Path)

    return ret 



def main():
    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Please run the program as :")
        print("python filename.py directory_name ")

    else:

        print("Application is Running....")

        schedule.every().seconds.do(DeleteEmptyFiles , sys.argv[1])

        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ =="__main__":
    main()