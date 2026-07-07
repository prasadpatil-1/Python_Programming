# Accept N number form user store it in List
#Input : 13 5 45 7 4 56
#Output : 130

from functools import reduce
def Addition(No1, No2):
    return No1 + No2

def main():
    Elements = int(input("Enter Number of elements :"))

    Value = list(map(int,input("Enter Numbers :").split()))

    Result = reduce(Addition,Value)
    print(Result)


if __name__ == "__main__":
    main()