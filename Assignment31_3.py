# Program to scan a specifeied the directory every minute

import os
import schedule
import time
import datetime


def ScanDirectory(DirectoryPath):

    FileCount = 0
    DirectoryCount = 0

    if not os.path.exists(DirectoryPath):
        print("Directory does not exist")
        return

    if not os.path.isdir(DirectoryPath):
        print("Entered path is not a directory")
        return

    for item in os.listdir(DirectoryPath):

        CompletePath = os.path.join(DirectoryPath, item)

        if os.path.isfile(CompletePath):
            FileCount += 1

        elif os.path.isdir(CompletePath):
            DirectoryCount += 1

    CurrentTime = datetime.datetime.now()

    print("Directory Scanned :", DirectoryPath)
    print("Total Files :", FileCount)
    print("Total Subdirectories :", DirectoryCount)
    print("Scan Time :", CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))
    print("----------------------------------------")


def main():

    DirectoryPath = input("Enter directory path : ")

    schedule.every(1).minutes.do(ScanDirectory, DirectoryPath)

    print("Directory scanning started...")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()