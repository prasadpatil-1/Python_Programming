class Numbers:
    def __init__(self , no):
        self.value = no
    
    def ChkPrime(self):
        if self.value <= 1 :
            return False
            
        isPrime = True
        for i in range(2 , self.value):
            if self.value % i == 0:
                isPrime = False
                break

        if isPrime == True:
            return True
        else:
            return False

    def ChkPerfect(self):
        sum = 0 
            
        for i in range(1 , self.value):
            if self.value % i == 0 :
                sum = sum + i

        if self.value == sum:
            return True
        else:
            return False 
    
    def Factors(self):
        print(f"Factors of {self.value} : ")
        for i in range(1 , self.value+1):
            if self.value % i == 0:
                print(i,"\t",end = "")

    def SumFactors(self):
        sum = 0 
        for i in range(1 , self.value+1):
            if self.value % i == 0:
                sum = sum + i

        return sum


def main():
    no = int(input("Enter the number : "))

    obj1 = Numbers(no)

    Ret = obj1.ChkPrime()
    print(f"Is {no } is prime number ? ",Ret)

    Ret = obj1.ChkPerfect()
    print(f"Is {no} is perfect number ? ",Ret)

    obj1.Factors()
    print()

    Ret = obj1.SumFactors()
    print(f"Sum of factors of {no} : ",Ret)
    


if __name__ == "__main__":
    main()
        