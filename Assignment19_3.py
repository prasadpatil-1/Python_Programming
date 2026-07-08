from functools import reduce

Limit = lambda No : No >= 70 and No <= 90

Increment = lambda No : No + 10

Product = lambda No1 , No2:No1 * No2

def main():
    Data = [4,34,36,76,68,24,89,23,86,90,45,70]
    print("Enter list elements :",Data)

    FData = list(filter(Limit, Data))
    print("List after filter :",FData)

    MData = list(map(Increment,FData))
    print("List after Map :",MData)

    RData = reduce(Product,MData)
    print("Reduced data is :",RData)


if __name__ =="__main__":
    main()