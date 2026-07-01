def DivisibleX(num):
    if((num / 3 ) and (num / 5)):
        print("Number is divisible by 3 and 5 :")


def main():
    Value = int(input("Enter a number : "))
    DivisibleX(Value)

if __name__ =="__main__":
    main()