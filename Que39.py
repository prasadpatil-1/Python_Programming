Square = lambda No : No * No

def main():
    Numbers = [11,21,51,101,111]

    MNumbers = list(map(Square , Numbers))

    print("Squares of list numbers are : ",MNumbers)


if __name__ == "__main__":
    main()