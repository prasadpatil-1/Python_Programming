'''
        write a python program using multiprocessing.Pool ti calculate the sum of all even numbers from 1 to N for every number from the given list.
'''

import multiprocessing
import os 

def SumEven(Num):
    total = 0 

    for i in range(2 , Num+1 , 2):
        total = total + i

    print("Process is running with PID : ",os.getpid())
    print("Input Number : ",Num)
    print("Sum of Even numbers : ",total)
    print()

    return total


def main():
    Data = list()
    size = int(input("Enter number of elements : "))

    for i in range(1 , size+1):
        no = int(input(f"Enter {i} element : "))
        Data.append(no)

    pobj = multiprocessing.Pool()

    Ret = pobj.map(SumEven ,Data)

    pobj.close()
    pobj.join()

    print("Result : ",Ret)
    
if __name__ == "__main__":
    main()