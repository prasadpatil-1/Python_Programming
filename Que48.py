CountEven = lambda No : No % 2 == 0 and len(CountEven)



def main():
    Numbers = list(map(int , input("Enter numbers : ").split()))

    Ret = filter(CountEven , Numbers)
    
    print("Count of even number is :",Ret)

if __name__ == "__main__":
    main()