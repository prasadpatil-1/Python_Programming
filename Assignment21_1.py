import threading

def ChkPrime(No):
    print("Prime Numbers : ")

    for value in No:

        flag = True
        if value <= 1 :
            continue

        for i in range(2 , value):
            if value % i == 0 :
                flag = False
                break

        if flag == True:
            print(value)
               
    print()

def DisplayNonPrime(No):

    print("Non Prime Numbers : ")

    for value in No:
        if value <= 1 :
            print(value)
        for i in range(2 , value):
            if value % i == 0 :
                print(value)
                break

def main():
    Data = list()
    size = int(input("Enter number of elements : "))

    for i in range(1 , size+1):
        no = int(input(f"Enter {i} element : "))
        Data.append(no)

    Prime = threading.Thread(target = ChkPrime , args = (Data ,))
    NonPrime = threading.Thread(target = DisplayNonPrime , args = (Data ,))

    Prime.start()
    Prime.join()

    NonPrime.start()
    NonPrime.join()

if __name__ == "__main__":
    main()