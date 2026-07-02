def MultTable(num):
    i = 1
    while(i <= 10):
        print(num * i)
        i += 1


def main():
    Value = int(input("Enter a number : "))
    MultTable(Value)

if __name__ =="__main__":
    main()