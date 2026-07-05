from functools import reduce

Product = lambda No1 , No2 : No1 * No2

def main():
    Number = list(map(int ,input("Enter Numbers : ").split()))

    Ret = reduce(Product , Number)

    print("Product is :",Ret)

if __name__ == "__main__":
    main()