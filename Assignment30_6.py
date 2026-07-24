# Print lunch time every dat at 1.00 PM
# Print Wrap up worj every day at 6.00 PM

import schedule
import time
import datetime

def LunchTime():
    print("Hurry there is a LUNCH TIME",datetime.datetime.now().time())

def Wrap():
    print("Hurry there is a WRAP TIME",datetime.datetime.now().time())


def main():
    
    print("Automation Script Started for Tasks")
    schedule.every().day.at("13:00").do(LunchTime)
    schedule.every().day.at("18:00").do(Wrap)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
