from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def compute(self, x, y):
        pass

class Add(Operation):
    def compute(self, x, y):
        return x + y

class Multiply(Operation):
    def compute(self, x, y):
        return x * y

class Power(Operation):
    def compute(self, x, y):
        return x ** y
    
class Calculator:
    def __init__(self, operation: Operation):
        self.operation = operation

    def calculate(self, x, y):
        return self.operation.compute(x, y)

c1 = Calculator(Add())
print(c1.calculate(2, 3))  

c2 = Calculator(Power())
print(c2.calculate(2, 3))  

c3 = Calculator(Multiply())
print(c3.calculate(2, 3))  
