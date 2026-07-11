# problem using map.Pool()
# Input
# Dispaly : Proccess ID, Input , Factorial

import multiprocessing
import os

def CalcFact(Num):
    fact = 1 

    for i in range(1 , Num+1):
        fact = fact*i

    print("Process is Running with PID : ",os.getpid())
    print("Input Number : ",Num)
    print("Factorial : ",fact)

    return fact

def main():
    Data = list()
    size = int(input("Enter the size : "))

    for i in range(1 , size+1):
        no = int(input(f"Enter {i} element : "))
        Data.append(no)

    print("Input list is : ", Data)
    pobj = multiprocessing.Pool()

    Ret = list(pobj.map(CalcFact , Data))

    pobj.close()
    pobj.join()

    print("List after Calculations : ",Ret)

    

if __name__ == "__main__":
    main()