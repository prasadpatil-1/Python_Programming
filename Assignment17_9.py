# Count digit in Number
#Input : 12345
#Output : 5

def ChkLength(No):
    Count = 0

    while No > 0:
        Count = Count + 1
        No = No // 10
    return Count


def main():

    Value = int(input("Enter Number :"))

    Ret = ChkLength(Value)

    print("Digits are : ",Ret)
if __name__ == "__main__":
    main()