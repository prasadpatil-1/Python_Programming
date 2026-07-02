def Factorial(num):
    fact = 1     

    while(num > 0):
        fact = fact * num
        num = num - 1

        print("factorial is : ", fact)
    


def main():
    Value = int(input("Enter a number : "))
    Factorial(Value)

if __name__ =="__main__":
    main()