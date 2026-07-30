# Design automation script which accept directory name and mail id from user and create log file in that directory which contains information of running processes
# as its name , PID , Username . After creating log file send that log file to the specific mail .


import psutil
import sys
import os 
import time 
import smtplib
from email.message import EmailMessage

def DisplayInformation(DirectoryName , receiver_email , app_password):

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

    SendMail(filename , receiver_email , timestamp , app_password)

def SendMail(logfile ,receiver_email , timestamp , app_password):

    sender_email = "searchhere5@gmail.com"

    subject = "Test mail from python script %s" %timestamp

    body = """ Dear User,

    The scheduled Platform Surveillance task has completed successfully.

    Please find the attached system monitoring log for this execution.

    The report includes:

    * Running processes and their details (PID, Name, User, Status)

    This report has been generated automatically by automation script.

    Thank you for using our automation solution.

    Regards,

    .....

    """
    msg = EmailMessage() 

    msg["From"] = sender_email        
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.set_content(body)           

    fobj = open(logfile , "rb") 

    file_data = fobj.read()        

    fobj.close()

    file_name = os.path.basename(logfile)           

    msg.add_attachment(file_data , maintype ="text" , subtype="plain" , filename = file_name)           

    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)               

    smtp.login(sender_email , app_password)                       

    smtp.send_message(msg)              

    smtp.quit() 

    print("Mail gets send successfully")

def main():
    if(len(sys.argv) == 4):
        DisplayInformation(sys.argv[1] , sys.argv[2] , sys.argv[3])

        print("-------Thank you for using our automation System-------")
    else:
        print("Invalid argument")
        print("Please run the program as : ")
        print(f"{sys.argv[0]} Directory_Name receiver_email app_password")


if __name__ =="__main__":
    main()