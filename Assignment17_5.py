#Check Prime or Not 
#Input : from user suppose 5
#Ouput : It is Prime

def ChkPrime(No):
    if No <= 1:
        return False

    for i in range(2,No):
        if No % i == 0:
            return False
    return True

def main():

    Value = int(input("Enter Number :"))

    ChkPrime(Value)

    if ChkPrime(Value):
        print("Its is Prime")
    else:
        print("Its Not Prime")

    

if __name__ == "__main__":
    main()