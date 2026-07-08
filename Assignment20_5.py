import threading

def Thread1(No):
    for i in range(1,No+1,1):
        print(i)    

def Thread2(No):
    for i in range(No,0,-1):
        print(i)    

def main():
    
    Value = 50
    print("Thread 1 is Start Running :")
    t1 = threading.Thread(target=Thread1,args=(Value,))

    t2 = threading.Thread(target=Thread2,args=(Value,))

    t1.start()
    t1.join()

    print("Thread 2 is Start Running :")

    t2.start()
    t2.join()
    

if __name__ == "__main__":
    main()