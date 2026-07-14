class BankAccount:

    ROI = 10.5

    def __init__(self):
        self.Name = "Prasad"
        self.Amount = 10000

    def Display(self):
        print("Enter Account holder name : ",self.Name)
        print("Enter Balance : ",self.Amount)

    def Deposite(self):
        Aadd = int(input("Enter Amount to add in balance :"))
        self.Amount  += Aadd

        print("After deposite balance is :",self.Amount)

    def Withdraw(self):
        Asub = int(input("Withdrawal Amount :"))
        if self.Amount < Asub:
            print("Insufficient balance")
        else:
            self.Amount = self.Amount - Asub

        print("After withdraw the balance is :",self.Amount) 
           
    
    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100

        print("The Calculated Instrest is :",Interest)
    
bobj1 = BankAccount()

bobj1.Display()
bobj1.Deposite()
bobj1.Withdraw()
bobj1.CalculateInterest()
print()

bobj2 = BankAccount()

bobj2.Display()
bobj2.Deposite()
bobj2.Withdraw()
bobj2.CalculateInterest()


    
