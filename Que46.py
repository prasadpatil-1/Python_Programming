CheckDivisible = lambda No : (No % 3 == 0) and (No % 5 == 0)

def main():
    Data = list(map(int, input("Enter elements :").split()))

    Ret = list(filter(CheckDivisible , Data))

    print("Numbers Divisible by 3 and 5 :",Ret)

if __name__ == "__main__":
    main()