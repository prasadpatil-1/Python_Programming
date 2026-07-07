# Accept N number form user store it in List and check prime
#Input : 13 5 45 7 4 56 10 34 2 5 8
#Output : 54

import MarvellousNum

def ListPrime(No):
    Sum = 0

    for i in No:
        if MarvellousNum.ChkPrime(i):
            Sum = Sum + i

    return Sum


def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = ListPrime(Data)
    print("Addition of prime numbers is :", Ret)


if __name__ == "__main__":
    main()