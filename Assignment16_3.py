def Add(No1, No2):
    return No1 + No2

    

def main():
    Value1 = int(input("Enter the first Number :"))
    Value2 = int(input("Enter the second Number :"))

    Ret = Add(Value1, Value2)

    print("Addition is :",Ret)
    

if __name__ == "__main__":
    main()