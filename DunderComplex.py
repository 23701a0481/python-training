class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def Shownumber(self):
        print(f"{self.real}i+{self.imag}j")
    def __add__(self,num2):
        newreal=self.real/num2.real
        newimag=self.imag/num2.imag
        return Complex(newreal,newimag)
num1=Complex(1,6)
num1.Shownumber()
num3=Complex(2,5)
num3.Shownumber()
num4=num1+(num3)
num4.Shownumber()
OUTPUT:
1i+6j
2i+5j
0.5i+1.2j
