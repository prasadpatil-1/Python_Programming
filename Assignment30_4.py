# Print Namaakar at every day 9:00

import schedule
import time

def Display():
    print("Namaskar..")

def main():
    
    schedule.every().day.at("9.00").do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()