from multiprocessing import Pool

def SumOfSquares(n):
    Sum = 0

    for i in range(1, n + 1):
        Sum = Sum + (i * i)

    return Sum

def main():
    Numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    with Pool() as p:
        Result = p.map(SumOfSquares, Numbers)

    print("Sum of squares:")
    print(Result)

if __name__ == "__main__":
    main()