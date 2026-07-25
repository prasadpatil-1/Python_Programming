import sys
import schedule
import os
import time

def DisplayContent(FileName):
    try:
        if (os.path.exists(FileName)):

            if(os.path.getsize(FileName) == 0):
                print("File is empyt")
                return

            else:
                fobj = open(FileName , "r")
                
                content = fobj.read()
                print(content)

                fobj.close()

        else:
            print("File Does not exists")
            return 

    except PermissionError as eobj:
        print(eobj)
    except OSError as eobj:
        print(eobj)

    print("Waiting for next schedule...")    


def main():
    if((len(sys.argv)) == 2):

        print("File Monitoring is Start")
        print("Press CTRL + C to stop ")

        schedule.every().minutes.do(DisplayContent , sys.argv[1])

        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ =="__main__":
    main()