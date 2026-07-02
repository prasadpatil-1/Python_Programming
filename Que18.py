def SumOfDigit(No):
    count = 0
    sum = 0

    while No > 0:
        digit = No % 10 
        
        No = No // 10
        
        sum = sum + digit

    return sum
    


def main():
    Num = int(input("Enter a Number : "))
    Ret = SumOfDigit(Num)

    print("Count of digits is :",Ret)

if __name__ == "__main__":
    main()