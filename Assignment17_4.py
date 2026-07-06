# Summation of Factors
#Input : from user suppose 12
#Ouput : (1+2+3+4+5+6) = 16

def SummationOfFactor(No):

    Sum = 0

    for i in range(1,No):
        if No % i == 0:
            Sum = Sum + i
     
    return Sum

def main():

    Value = int(input("Enter Number :"))

    Ret = SummationOfFactor(Value)

    print(f"Summation of factor {Value} is : {Ret}")

if __name__ == "__main__":
    main()