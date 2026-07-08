Multiplication  = lambda No1, No2 : No1 * No2 

def main():

    Value1 = int(input("Enter Number :"))
    Value2 = int(input("Enter Number :"))


    Ret = Multiplication(Value1, Value2)


    print(f"Multiplication of {Value1 , Value2} is : ",Ret)

if __name__ == "__main__":
    main()