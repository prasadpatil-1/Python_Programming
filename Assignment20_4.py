import threading

def NumberOfLower(Chars):
    print("Thread ID is : ",threading.get_ident())
    print("Thread Name is :",threading.current_thread().name)

    Count = 0

    for ch in Chars:
        if ch.islower():
            Count += 1
    print("Number of lowercase characters are :",Count)

def NumberOfUpper(Chars):

    print("Thread ID is : ",threading.get_ident())
    print("Thread Name is :",threading.current_thread().name)

    Count = 0

    for ch in Chars:
        if ch.isupper():
            Count += 1
    print("Number of lowercase characters are :",Count)


def NumberOfDigits(Chars):

    print("Thread ID is : ",threading.get_ident())
    print("Thread Name is :",threading.current_thread().name)

    Count = 0

    for ch in Chars:
        if ch.isdigit():
            Count += 1
    print("Number of lowercase characters are :",Count)

    pass

def main():

    name = input()
    
    Small  = threading.Thread(target=NumberOfLower,args=(name,))
    Capital  = threading.Thread(target=NumberOfUpper,args=(name,))
    Digit = threading.Thread(target=NumberOfDigits,args=(name,))

    Small.start()
    Small.join() 

    Capital.start()
    Capital.join()

    Digit.start()
    Digit.join()

if __name__ == "__main__":
    main()