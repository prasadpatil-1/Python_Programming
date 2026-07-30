# Design automation script
# Display information of running processes as its (name , PID , username)

import psutil

def DisplayInformation():

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ["pid" , "name" , "username"])

        print("Name : ",info["name"])
        print("PID : ",info["pid"])
        print("Username : ",info["username"])
        print("\n")

def main():
    DisplayInformation()


if __name__ =="__main__":
    main()