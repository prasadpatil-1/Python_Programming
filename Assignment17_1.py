import Arithmetic as calc

def main():
    
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    print("Addition is : ",calc.Add(Value1,Value2))

    print("Substraction is :",calc.Sub(Value1,Value2))

    print("Multiplication is :",calc.Mult(Value1,Value2))

    print("Division  is :",calc.Div(Value1,Value2))


if __name__ == "__main__":
    main()

