'''
        write a python program using multiprocessing.Pool to calculate the sum of all odd numbers from 1 to N for every number from the given list.
'''

import multiprocessing
import os 

def SumOdd(Num):
    total = 0 

    for i in range(1 , Num+1 , 2):
        total = total + i

    print("Process is running with PID : ",os.getpid())
    print("Input Number : ",Num)
    print("Sum of Odd numbers : ",total)
    print()

    return total


def main():
    Data = list()
    size = int(input("Enter number of elements : "))

    for i in range(1 , size+1):
        no = int(input(f"Enter {i} element : "))
        Data.append(no)

    pobj = multiprocessing.Pool()

    Ret = pobj.map(SumOdd ,Data)                    # Pool.map() automatically return list

    pobj.close()
    pobj.join()

    print("Result : ",Ret)
    
if __name__ == "__main__":
    main()