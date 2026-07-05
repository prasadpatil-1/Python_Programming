CheckLength = lambda string : len(string) > 5 


def main():
    Data = input("Enter words :").split()

    Ret = list(filter(CheckLength , Data))

    print("String having greater than length five is :",Ret)

if __name__ == "__main__":
    main()