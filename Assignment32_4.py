import sys
import os
import schedule
import time
import shutil
import datetime


def CopyFiles(Source_Directory , Destination_Directory):
    ret = False
    ret = ValidateDirectory(Source_Directory , Destination_Directory)
    if ret == False:
        print("Invalid Argument : Source or Destination path is invalid")
        return

    else:
        log_file_path = os.path.join(Destination_Directory , "Marvellous.log")
        if (os.path.exists(log_file_path)):
            fobj = open(log_file_path,"a")
        else:   
            fobj = open(log_file_path,"w")

        total_files = 0 
        copy_files = 0 
        failed = 0 

        for FolderName , SubFolder , FileName in os.walk(Source_Directory):
            for filename in FileName:
                name , extension = os.path.splitext(filename)

                if filename == "Marvellous.log":
                    continue

                total_files = total_files + 1
                if extension ==".txt":
                    s_path = os.path.join(FolderName , filename)

                    timestamp = datetime.datetime.now()
                    final_time_f = timestamp.strftime("%d-%m-%Y %I-%M-%S %p")
                    final_time = final_time_f.replace("-" , "_")
                    final_time = final_time.replace(" ","_")

                    final_time = f"%s_%s"%(name , final_time)

                    copy_file_name = os.path.join(Destination_Directory , final_time)
                    copy_file_name = f"%s.txt"%(copy_file_name)
                    try:
                        shutil.copy(s_path , copy_file_name)
                        copy_files = copy_files + 1
                    except Exception as eobj:
                        print(f"Exception occured : {eobj}")
                        failed = failed + 1
                    
                    fobj.write(f"="*70+"\n")

                    if(os.path.exists(copy_file_name)):
                        fobj.write(f"Date & Time : {final_time_f}\n")
                        fobj.write(f"Source Path : {s_path} \n")
                        fobj.write(f"Destination Path : {copy_file_name}\n")
                        fobj.write(f"Copied file : {filename}\n")
                        fobj.write(f"File size : {os.path.getsize(copy_file_name)} bytes \n")
                        fobj.write("Status : SUCCESS\n")
                        fobj.write(f"="*70+"\n")
                        
                    else:
                        fobj.write("Status FAILED\n")
                        fobj.write(f"="*70+"\n")
        
        fobj.write(f"Statistics \n")
        fobj.write(f"Total Files Scanned : {total_files}\n ")
        fobj.write(f"Total Files Copied : {copy_files} \n")
        fobj.write(f"Total Files Failed : {failed} \n")
        fobj.write(f"="*70+"\n")

        fobj.close()

    print("Waiting for next scheduling...\n")
                

def ValidateDirectory(Source_Directory , Destination_Directory):
    ret = False
    ret = os.path.exists(Source_Directory)
    if ret == True:
        ret = os.path.isdir(Source_Directory)

        if ret == True:
            ret = os.path.exists(Destination_Directory)
            if ret == True:
                ret = os.path.isdir(Destination_Directory)

    return ret 



def main():
    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        print("Please run the program as :")
        print("python filename.py source_directory_name destinatio_directory_name")

    else:

        print("Application is Running....")

        schedule.every(1).minutes.do(CopyFiles , sys.argv[1] , sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ =="__main__":
    main()