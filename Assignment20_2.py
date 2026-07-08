import threading

def EvenFactors(No):
    Sum = 0
    
    print("Even factors are :")

    for i in range(1,No+1):
        if No % i == 0 and i % 2 == 0:
            print(i)
            Sum = Sum + i
    print("Sum of Even factors is :",Sum)

def OddFactors(No):
    Sum = 0
    
    print("odd factors are :")
    
    for i in range(1,No+1):
        if No % i == 0 and i % 2 != 0:
            print(i)
            Sum = Sum + i
    print("Sum of Odd factors is :",Sum)

def main():

    Value = int(input("Enter number :"))
    t1 = threading.Thread(target=EvenFactors,args=(Value,))
    t2 = threading.Thread(target=OddFactors,args=(Value,))

    t1.start()
    t1.join()   

    t2.start()
    t2.join()    
    
    print("Exit from main")

if __name__ == "__main__":
    main()