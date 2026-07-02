def CountDigit(No):
    count = 0

    while No > 0:
        count = count + 1   
        No = No // 10
    return count


def main():
    Num = int(input("Enter a Number : "))
    Ret = CountDigit(Num)

    print("Count of digits is :",Ret)

if __name__ == "__main__":
    main()