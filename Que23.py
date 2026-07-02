def PrintManyNumbers(No):

    for i in range(1 , No + 1):
        if No >= i:
            print(i)        

    

def main():
   
    Num = int(input("Enter a number :"))
    PrintManyNumbers(Num)
    
   

if __name__ == "__main__":
    main()