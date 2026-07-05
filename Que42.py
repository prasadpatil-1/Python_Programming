from functools import reduce

Addition = lambda No1 , No2 : No1 + No2

def main():
    elements = list(map(int , input("Enter elements :").split()))

    RNumber = reduce(Addition , elements)

    print("List of Addition of elements is :",RNumber)

if __name__ == "__main__":
    main()