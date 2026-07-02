def ReversedNumber(No):

    Original = No
    reverse = 0

    while No > 0:
        digit = No % 10
        reverse = reverse * 10 + digit
        No = No // 10
    return reverse


def main():
    Num = int(input("Enter a Number : "))
    Ret = ReversedNumber(Num)
    print("Reversed number is  : ",Ret)
if __name__ == "__main__":
    main()