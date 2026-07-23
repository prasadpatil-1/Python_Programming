# Schedule task that execute every five minutes
# Write Current date and time into a file named : Marvellous.txt
# New entries should be appended without removing previous 

import datetime
import time
import schedule

def Display():

    Task = datetime.datetime.now()

    FileName = open("Marvellous.txt","a")
    FileName.write

    FileName.write("Task executed at :" +str(Task)+"\n")

    

    FileName.close()


def main():
    
    print("Automation Script Started")

    schedule.every(5).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()