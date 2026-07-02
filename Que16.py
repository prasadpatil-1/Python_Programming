def CheckPalindrome(No):

    ONo = No
    PNo = 0

    while No > 0:
        digit = No % 10
        PNo = PNo * 10 + digit
        No = No // 10

    if PNo == ONo:
        print("Palindrome")
    else:
        print("Not Palindrome")






def main():
    Num = int(input("Enter a Number : "))
    CheckPalindrome(Num)

if __name__ == "__main__":
    main()