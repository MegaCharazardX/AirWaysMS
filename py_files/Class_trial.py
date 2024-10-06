class _Trial:

    def __init__(self, a : int , b : int):
        self.a = a
        self.b = b
    
    def add(self):
        c = self.a + self.b
        return c
    
    def suctract(self):
        c = self.a - self.b
        return c
    
    def multiply(self):
        c = self.a * self.b
        return c
    
    def divide(self):
        c = self.a / self.b
        return c
    
trial = _Trial("fdsf", 89).add()
print(trial)