# Input : 5

''' Output :
            *   *   *   *   *
            *   *   *   *   *
            *   *   *   *   *
            *   *   *   *   *
            *   *   *   *   *

'''''
def DisplayPattern(No):
     
     for i in range(1,No+1):
        for i in range(1,No+1):
            print("*    ",end="")
        print()
def main():
    Value = int(input("Enter number :"))

    DisplayPattern(Value)

   

if __name__ == "__main__":
    main()