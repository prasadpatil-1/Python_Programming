# Factorial
#Input : from user suppose 5
#Ouput : 120

def Factorial(No):

    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i
    return Fact

def main():

    Value = int(input("Enter Number :"))

    Ret = Factorial(Value)

    print(f"Factorial : {Value} is : {Ret}")

if __name__ == "__main__":
    main()