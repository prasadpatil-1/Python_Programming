# Input : 5

''' Output :
            *   *   *   *   *
            *   *   *   *   
            *   *   *      
            *   *   
            *   

'''''
def DisplayPattern(No):
     
    for i in range(No):
        for j in range(No-i):
            
            print("*    ",end="")
        print()



def main():
    Value = int(input("Enter number :"))

    DisplayPattern(Value)

   

if __name__ == "__main__":
    main()