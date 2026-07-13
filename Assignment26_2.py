class Circle:
    # Class Variable
    PI = 3.14

    # Instance Methods

    def __init__(self):

        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
       
        self.Radius = float(input("Enter the Radius :"))

    def CalculateArea(self):
        
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("The Radius is ",self.Radius)
        print("The Area of Circle is :",self.Area)
        print("The Circumference is ",self.Circumference)


obj1 = Circle()

obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()
print()

obj2 = Circle()

obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()
print()

obj3 = Circle()

obj3.Accept()
obj3.CalculateArea()
obj3.CalculateCircumference()
obj3.Display()