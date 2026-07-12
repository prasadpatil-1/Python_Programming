# write a program that calculates factorials of multiple numbers simultaneously using multiprocessing.Pool.
#
#   Output Format :
#                   Process ID : 1240
#                   Input Number : 20
#                   Factorial : 2432902008176640000


import multiprocessing
import os 

def calculateFactorial(Num):
    fact = 1 

    for i in range(1 , Num+1 ):
        fact = fact*i

    print("Process ID : ",os.getpid())
    print("Input Number : ",Num)
    print("Factorial : ",fact)
    print()

    return fact


def main():
    Data = list()
    size = int(input("Enter number of elements : "))

    for i in range(1 , size+1):
        no = int(input(f"Enter {i} element : "))
        Data.append(no)

    pobj = multiprocessing.Pool()

    print()

    Ret = pobj.map(calculateFactorial ,Data)

    pobj.close()
    pobj.join()

    print("Result : ",Ret)
    
if __name__ == "__main__":
    main()