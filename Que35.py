DivisibleBYFive = lambda No : No % 5 == 0

def main():
    Value = int(input("Enter a Number :"))

    DivisibleBYFive(Value)

    print(DivisibleBYFive(Value))


if __name__ == "__main__":
    main()