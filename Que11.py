def SumOfN(num):
    SumOfN = (num * (num +1)) // 2
    print("Sum of first natural numbe is : ",SumOfN)
    


def main():
    Value = int(input("Enter a number : "))
    SumOfN(Value)

if __name__ =="__main__":
    main()