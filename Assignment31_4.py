# Create a new log file after every 10 minute
# the file should contain current time and date

import schedule 
import os
import time
import datetime

def CreateLogFile():
        
    timestamp = datetime.datetime.now()
    finaltime = timestamp.strftime("%d-%m-%Y %I-%M-%S %p")
    final_time = finaltime.replace("-" , "_")

    file_name = "Marvellous%s.txt"%(final_time)
    
    fobj = open(file_name , "w")

    fobj.write("Log file created successfully \n")
    fobj.write(f"Creation Time : {finaltime} \n")

    fobj.close()

    print("Waiting for next schedule ...")



def main():

    print("Application is Running....")

    schedule.every(10).minutes.do(CreateLogFile )

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()