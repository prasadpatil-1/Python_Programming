# Accept N number form user store it in List and return frequnecy
#Input : 13 5 45 7 4 56 5 34 2 5 65
# Enter search element : 5 
#Output : 3


def CountFrequency(lst,No):

    Count = 0

    for i in lst:
        if i == No:
            Count = Count + 1
    return Count

def main():

    Value1 = int(input("Enter the Number of Elements :"))

    Elements = list(map(int, input("Enter Elements :").split()))

    Value2 = int(input("Enter element to search :"))

    Ret = CountFrequency(Elements,Value2)

    print("Frequency of element is :",Ret)


if __name__ == "__main__":
    main()