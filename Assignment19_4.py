from functools import reduce

Even = lambda No : No % 2 == 0

Square = lambda No : No * No

Addition = lambda No1 , No2 : No1 + No2

def main():

    Size = int(input("enter number of elements :"))

    Data = []

    print("Enter Elements :")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)


    FData = list(filter(Even, Data))
    print("List after filter :",FData)

    MData = list(map(Square,FData))
    print("List after Map :",MData)

    RData = reduce(Addition,MData)
    print("Reduced data is :",RData)


if __name__ =="__main__":
    main()