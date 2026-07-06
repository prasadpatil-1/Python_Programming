# Divisible by 5

def Divisible(No):

    if No % 5 == 0:
        return True
    else:
        return False

   
def main():

    Value = int(input("Enter number :"))
    
    Ret = Divisible(Value)

    print(Ret)
if __name__ == "__main__":
    main()