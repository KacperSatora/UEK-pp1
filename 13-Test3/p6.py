class C:
    def __init__(self, count):
        self.count = count

    def m1(self):
        return self.count
    def m2(self):
        self.count += 1
    def m3(self):
        self.count -=1
    def m4(self, n):
        self.count += n


c = C(5)
print(c.m1())
print(c.m2())
print(c.m1())
print(c.m4(-8))
print(c.m1())
print(c.m3())
print(c.m1())
print(c.m4(10))
print(c.m1())