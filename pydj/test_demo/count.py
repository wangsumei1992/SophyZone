#coding=utf-8
class countor():
    """实现两个数的加减乘除"""
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b