from functools import reduce

Maximum = lambda No1 , No2 : No1 if No1 < No2 else No2

def main():
    
    Elements = list(map(int , input("Enter elements :").split()))

    Ret = reduce(Maximum , Elements)

    print("Greater number is :",Ret)

if __name__ == "__main__":
    main()