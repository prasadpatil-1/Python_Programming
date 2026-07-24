# Take message from user
# Also take time interval
# Display the message at specific time interval


import schedule 
import sys
import time

def Display(text):
    print(text)

def main():
    if (len(sys.argv) == 3):

        time_interval = int(sys.argv[2])
        schedule.every(time_interval).seconds.do(Display , sys.argv[1])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")
        print("Please run program as :")
        print("python filename.py TextToDisplay time_interval")


if __name__ == "__main__":
    main()