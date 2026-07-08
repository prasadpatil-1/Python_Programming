import threading

def EvenList(No):
    Sum = 0

    for i in No:
        if i % 2 == 0:
            print(i)
            Sum = Sum + i
    print("Sum of EvenList is :",Sum)


def OddList(No):
    Sum = 0

    for i in No:
        if i % 2 != 0:
            print(i)
            Sum = Sum + i
    print("Sum of EvenList is :",Sum)
    

def main():

    Size = int(input("Enter the number of elements :"))

    Data = []

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target=EvenList,args=(Data,))
    t2 = threading.Thread(target=OddList,args=(Data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()
