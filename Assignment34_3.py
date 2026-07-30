# Design automation script which accept directory name from user and create log file in that directory
# which contains information of running processes as its name , PID , username

import psutil
import sys
import os 
import time 

def DisplayInformation(DirectoryName):

    ret = False

    ret = os.path.exists(DirectoryName)
    if(ret == True):
        ret = os.path.isdir(DirectoryName)
        if(ret == False):
            os.mkdir(DirectoryName)

    else:
        os.mkdir(DirectoryName)

    timestamp = time.strftime("%Y-%m-%d %H-%M-%S")

    filename = "ProcessLog%s.txt"%timestamp

    filename = os.path.join(DirectoryName , filename)

    fobj = open(filename , "w")

    Border = "-"*60

    fobj.write(Border+"\n")
    fobj.write("-------------------------Marvellous Log File-------------------------\n")
    fobj.write(f"Log file gets created at : {timestamp} \n")
    fobj.write(Border+"\n\n")

    fobj.write("------------------Process Information------------------\n")

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ["pid" , "name" , "username"])

        fobj.write(f"Name : {info["name"]}\n")
        fobj.write(f"PID : {info["pid"]}\n")
        fobj.write(f"Username : {info["username"]}\n")
        fobj.write(Border+"\n")

    fobj.write("-------Thank you for using our automation System-------\n")
    fobj.close()
def main():
    if(len(sys.argv) == 2):
        DisplayInformation(sys.argv[1])

        print("-------Thank you for using our automation System-------")
    else:
        print("Invalid argument")
        print("Please run the program as : ")
        print(f"{sys.argv[0]} Directory_Name")


if __name__ =="__main__":
    main()