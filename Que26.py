def AreaOfCircle(Radius):

    Area = 3.14 * Radius * Radius
    return Area


def main():
    
    Value = int(input("Enter the radius : "))

    Ret = AreaOfCircle(Value)

    print("Area of Circle is : ",Ret)


if __name__ == "__main__":
    main()