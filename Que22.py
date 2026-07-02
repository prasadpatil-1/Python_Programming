def Calculator(No1 , No2):

    Add = No1 + No2
    print("Addition is :",Add)

    Sub = No1 - No2
    print("Substraction is :",Sub)

    Mult = No1 * No2
    print("Multiplication is :",Mult)

    Div = No1 / No2
    print("Division is :",Div)
           

def main():
    Value1 = int(input("Enter first number :"))
    Value2 = int(input("Enter second number :"))

    Calculator(Value1 , Value2)

   

if __name__ == "__main__":
    main()