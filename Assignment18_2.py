# Accept N number form user store it in List and return maximum
#Input : 13 5 45 7 4 56
#Output : 56

from functools import reduce
def Maximum(No1, No2):
    return max(No1,No2)

def main():
    Elements = int(input("Enter Number of elements :"))
    
    Value = list(map(int,input("Enter Numbers :").split()))

    Result = reduce(Maximum,Value)
    print(Result)


if __name__ == "__main__":
    main()