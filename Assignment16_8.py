# print Star on console 
# Input = 5
#Output *   *   *   *   *

def Display(No):

    for i in range(1, No+1):
        print(f"*    ",end="")  #end="" use to print on same line

    
   
def main():

    Value = int(input("Enter number :"))
    
    Display(Value)

if __name__ == "__main__":
    main()