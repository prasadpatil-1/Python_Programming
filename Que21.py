def Factors(No):

    for i in range(1, No +1):
        if (No % i == 0):
                print("Factors are :")
           

def main():
   
    Num = int(input("Enter a number :"))

    Factors(Num)
   

if __name__ == "__main__":
    main()