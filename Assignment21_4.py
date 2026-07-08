import threading 

Result = {}

def SumOfElements(numbers):
    total = 0 
    
    for no in numbers:
        total = total + no

    Result.update({"Sum" : total})

def ProductOfElements(numbers):
    product = 1
    
    for no in numbers:
        product = product * no

    Result.update({"Product" : product})



def main():
    Data = list()
    size = int(input("Enter number of elements : "))

    for i in range(1 , size+1):
        no = int(input(f"Enter {i} element :"))
        Data.append(no)

    SumThread = threading.Thread(target = SumOfElements , args = (Data ,))
    ProductThread = threading.Thread(target = ProductOfElements , args = (Data ,))

    SumThread.start()
    ProductThread.start()

    SumThread.join()
    ProductThread.join()

    print("Sum of Elements : ",Result["Sum"])
    print("Product of Elements : " ,Result["Product"])


if __name__ == "__main__":
    main()