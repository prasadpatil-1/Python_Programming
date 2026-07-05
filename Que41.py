Odd = lambda No : No % 2 != 0

def main():
    Numbers = [11,20,23,24,26]

    MNumbers = list(filter(Odd, Numbers))

    print("List of odd number is :",MNumbers)



if __name__ == "__main__":
    main()