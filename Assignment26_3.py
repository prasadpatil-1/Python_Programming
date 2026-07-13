class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter Value1 :"))
        self.Value2 = int(input("Enter Value2 :"))
    
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multipliction(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        return self.Value1 / self.Value2
    
    def Display(self):
        print("Addition is :",self.Addition())
        print("Substraction is :",self.Substraction())
        print("Multiplication is :",self.Multipliction())
        print("Division is :",self.Division())


aobj1 = Arithmetic()   

aobj1.Accept()
aobj1.Addition()
aobj1.Substraction()
aobj1.Multipliction()
aobj1.Division()
aobj1.Display()
print()

aobj2 = Arithmetic()   

aobj2.Accept()
aobj2.Addition()
aobj2.Substraction()
aobj2.Multipliction()
aobj2.Division()
aobj2.Display()
print()

aobj3 = Arithmetic()   

aobj3.Accept()
aobj3.Addition()
aobj3.Substraction()
aobj3.Multipliction()
aobj3.Division()
aobj3.Display()
