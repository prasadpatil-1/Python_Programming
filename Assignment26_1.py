class Demo:

    Value = 10              # Class Variable

    def __init__(self, A , B):
            
            self.no1 = A
            self.no2 = B

            print("Inside Constructor")
            print(self.no1)
            print(self.no2)

    def fun(self, no1 , no2):
            print("Inside Fun")
            print(self.no1)
            print(self.no2)

    def gun(self, no1 , no2):
            print("Inside Gun")
            print(self.no1)
            print(self.no2)

#class Variable
obj1 = Demo(11,21)
obj2 = Demo(51,101)

#Instance Variable

obj1.fun(11,21)
obj2.fun(51,101)

obj1.gun(11,21)
obj2.gun(51,101)