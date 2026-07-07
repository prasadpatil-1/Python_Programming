# Accept N number form user store it in List and return minimun
#Input : 13 5 45 7 
#Output : 5

from functools import reduce
def Minimum(No1, No2):
    return min(No1,No2)

def main():
    Elements = int(input("Enter Number of elements :"))
    
    Value = list(map(int,input("Enter Numbers :").split()))

    Result = reduce(Minimum,Value)
    print(Result)


if __name__ == "__main__":
    main()