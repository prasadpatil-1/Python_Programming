# Count digit in Number and display its Addition
#Input : 12345
#Output : 15 (1+2+3+4+5)

def DigitsAdd(No):
    Sum = 0

    while No > 0:
        Digit = No % 10

        Sum = Sum + Digit

        No = No // 10
   
    return Sum
    


def main():

    Value = int(input("Enter Number :"))

    Ret = DigitsAdd(Value)

    print("Addition of Digits is : ",Ret)
if __name__ == "__main__":
    main()