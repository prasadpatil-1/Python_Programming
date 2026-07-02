def CheckPerfect(No):

    Sum = 0

    for i in range(1,No):
        if No % i == 0:
            Sum += i

    if Sum == No:
        return True
    else:
        return False





def main():
    
    Value = int(input("Enter the Number : "))
    CheckPerfect(Value)

    if CheckPerfect(Value):
        print("Perfect Number is :",Value)
    else:
        print("Not Perfect Number ")


if __name__ == "__main__":
    main()