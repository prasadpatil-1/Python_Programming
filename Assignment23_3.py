# write a program that counts how many even numbers exist between 1 and N using Pool.map()
#
# Output Format : 
#                   Process ID : 1235
#                   Input Number : 1000000
#                   Even Number Count : 500000


import multiprocessing
import os 

def CountEven(Num):
    count = 0 

    for i in range(2 , Num+1 , 2):
        count = count + 1

    print("Process ID : ",os.getpid())
    print("Input Number : ",Num)
    print("Even Number count : ",count)
    print()

    return count


def main():
    Data = list()
    size = int(input("Enter number of elements : "))

    for i in range(1 , size+1):
        no = int(input(f"Enter {i} element : "))
        Data.append(no)

    pobj = multiprocessing.Pool()

    Ret = pobj.map(CountEven ,Data)

    pobj.close()
    pobj.join()

    print("Result : ",Ret)
    
if __name__ == "__main__":
    main()