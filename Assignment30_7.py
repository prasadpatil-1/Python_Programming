# Accepts the source file path from the user
# Accepts the destination directory path
# Copies the source file to the destination directory
# Adds the current date and time to the backup filename
# Stores backup details in backup_log.txt
# Uses the shutil module for copying

import sys
import os
import schedule
import datetime
import time
import shutil

def FileBackup(Source_path , Destination_path):
    ret = False

    border = "="*70
    ret = os.path.exists(Source_path)

    if ret == False:
        print("File Backup Error : The Source path does not exists")
        return

    ret = os.path.isfile(Source_path)

    if ret == False:
        print("File Backup Error : The entered source path is invalid")
        return

    ret = os.path.exists(Destination_path)

    if ret == False:
        print("File Backup Error : The destination path does not exists")
        return

    ret = os.path.isdir(Destination_path)

    if ret == False:
        print("File Backup Error : The entered path is not an directory")
        return 

    filename = os.path.basename(Source_path)
    name , extension = os.path.splitext(filename)

    timestamp = datetime.datetime.now()
    timestamp = timestamp.strftime("%d-%m-%Y %I-%M-%S %p")
    timestamp = timestamp.replace(" ","_")
    timestamp = timestamp.replace("-","_")

    filename = f"{name}_{timestamp}{extension}"

    complete_path = os.path.join(Destination_path , filename)
    shutil.copy2(Source_path , complete_path)

    log_file = os.path.join(Destination_path , "backup_log.txt")

    fbackup = open(log_file,"a")
    fbackup.write(border+"\n")
    fbackup.write(f"Source File :  {Source_path} \n")
    fbackup.write(f"Backup File :  {complete_path} \n ")
    fbackup.write(f"Backup Time : { timestamp} \n ")
    fbackup.write(f"Backup Size : {os.path.getsize(complete_path)} bytes \n")
    fbackup.write(border+"\n")

    fbackup.close()

    print("Backup Successful")
    print("Waiting for next schedule ....")

def main():
    if(len(sys.argv) == 3):

        border = "="*70

        print(border+"\n")
        print("Marvellous Backup Utility")
        print(border+"\n")

        schedule.every().minutes.do(FileBackup ,sys.argv[1] , sys.argv[2])

        print("Backup Started......")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Please enter the path of destination directory path after file name")



if __name__ == "__main__":
    main()