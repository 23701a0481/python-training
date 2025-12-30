class methodOverride1:
    def display(self):
        print('method involved from base')
class methodOverride2(methodOverride1):
    def display(self):print("method invoked from derived class")
ob=methodOverride2()
ob.display()
OUTPUT:
method invoked from derived class
