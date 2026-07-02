def DisplayEven(No):

    for i in range(2 , No+1, 2):
        print(i)

def main():

    num = int(input("Enter a number : "))

    DisplayEven(num)



if __name__ == "__main__":
    main()