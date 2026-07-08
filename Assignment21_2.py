import threading

def PrintMax(No):
    MaxValue = No[0]

    for i in No:
        if i > MaxValue:
            MaxValue = i

    print("Maximum element : ",MaxValue)

def PrintMin(No):
    MinValue = No[0]

    for i in No:
        if i < MinValue:
            MinValue = i

    print("Minimum element : ",MinValue)

def main():
    Data = list()

    size = int(input("Enter number of elements :"))

    for i in range(1 , size+1):
        no = int(input(f"Enter {i} element : "))
        Data.append(no)

    Max = threading.Thread(target = PrintMax , args = (Data ,))
    Min = threading.Thread(target = PrintMin , args = (Data , ))

    Max.start()
    Min.start()

    Max.join()
    Min.join()

if __name__ == "__main__":
    main()