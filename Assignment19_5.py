from functools import reduce

def ChkPrime(No):
    if No <=1 :
        return False
    
    for i in range(2,int(No ** 0.5)+1):
        if No % i == 0:
            return False
    return True

Mult = lambda No : No * 2

Maximum = lambda No1 , No2 : max(No1 , No2)

def main():

    Size = int(input("Enter number of elements :"))
    Data = []

    for i in range(Size):
        Value = int(input())
        Data.append(Value)
        
    FData = list(filter(ChkPrime, Data))
    print("List after filter :",FData)

    MData = list(map(Mult,FData))
    print("List after Map :",MData)

    RData = reduce(Maximum,MData)
    print("Reduced data is :",RData)


if __name__ =="__main__":
    main()