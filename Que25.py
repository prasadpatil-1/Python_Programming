def AreaOfRectangle(Length , Width):

    Area = Length * Width
    return Area



def main():
    
    Value1 = int(input("Enter the length : "))
    Value2 = int(input("Enter the width :"))

    Ret = AreaOfRectangle(Value1 , Value2)

    print("Area of Rectangle is : ",Ret)


if __name__ == "__main__":
    main()