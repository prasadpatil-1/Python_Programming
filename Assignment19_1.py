Power = lambda No :  2 ** No

def main():

    Value = int(input("Enter Number :"))

    Ret = Power(Value)


    print(f"Power of {Value} is : ",Ret)

if __name__ == "__main__":
    main()