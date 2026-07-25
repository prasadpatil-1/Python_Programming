# Create a new text file every minute
# File name should contain the Current timestamp

import schedule
import time 
import datetime

def CreateFile():
    c_time = datetime.datetime.now()
    c_time =c_time.strftime("%d-%m-%Y %I-%M-%S %p")
    c_time = c_time.replace("-","_")
    c_time = c_time.replace(" ","_")    
    file_name = f"File_%s.txt"%(c_time)

    c_time = datetime.datetime.now()
    c_time = c_time.strftime("%I-%M-%S %p")


    fobj = open(file_name , "w")
    fobj.write(f"Filename : {file_name} \n")
    fobj.write(f"Creation date : {datetime.date.today()} \n")
    fobj.write(f"Creation time : {c_time} \n")

    fobj.close()

def main():
    schedule.every(5).minutes.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()