# IN list , Count how many prime numbers exits between 1 to N by using multiproceesing Pool

import multiprocessing
import os

def CountPrime(Num):
    Count = 0 

    for i in range(2,Num+1):
        flag = True
        for j in range(2 , i):
            if i % j == 0 :
                flag = False
                break
    
        if flag == True:
            Count = Count+1

    print("Process is running with PID : ",os.getpid())
    print(f"{Count} prime number exist between 1 and {Num} ") 

    return Count


def main():
    Data = list()
    size = int(input("Enter number of elements : "))

    for i in range(1 , size+1):
        no = int(input(f"Enter {i} element : "))
        Data.append(no)

    pobj = multiprocessing.Pool()

    Ret = list((pobj.map(CountPrime , Data)))

    pobj.close()
    pobj.join()

    print(Ret)
    

if __name__ == "__main__":
    main()