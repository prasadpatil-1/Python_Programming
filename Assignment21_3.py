import threading

counter = 0
lock = threading.Lock()             # creating lock


def Increment():
    global counter                  # a global variable
    
    with lock:
        for i in range ( 1 , 6):
            counter = counter + 1

            print("Counter after Increment :  ",counter)

    print()


def main():

    thread1 = threading.Thread(target = Increment )
    thread2 = threading.Thread(target = Increment )
    thread3 = threading.Thread(target = Increment )

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

if __name__ == "__main__":
    main()