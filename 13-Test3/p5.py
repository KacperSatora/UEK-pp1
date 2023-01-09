class C:
    def __init__(self, numbers):
        self.numbers = numbers       

    def __str__(self):
        return f'{"+".join(map(str,self.numbers))}={sum(self.numbers)}'


print(C([1,2]))
print(C([6,0,15]))