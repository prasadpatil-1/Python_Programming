import threading

def Even():
    print("First 10 Even number is :")
    
    for i in range(2,21,2):
        print(i)

def Odd():
    print("First 10 odd number is :")

    for i in range(1,20,2):
        print(i)

def main():


    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=Odd)

    t1.start()
    t2.start()

    t1.join()       # waiting for t2 thread
    t2.join()       # waiting for t1 thread
    
    
if __name__ == "__main__":
    main()