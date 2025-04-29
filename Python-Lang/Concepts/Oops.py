from myPackages import calc

class numberList:
    def __init__(self,value):
        self.value = value
    def realValue(self,value):
        self.value = value
    def getValue(self):
        print(f"getting value from {self.value} is  coming")

obj1 = numberList(20)
obj1.realValue(500)
obj1.getValue()

cal = calc.calculate(20,30,40)
print(cal)

class ownNumber:
    def __init__(own,a,b):
        own.a = a
        own.b = b
        own.callHari()
        own.callAkhi()
    def add(own,a,b):
        return a+b
    def callHari(own):
        print("Calling Hari........")
    def callAkhi(own):
        print("Calling Akhi..........")
o1 = ownNumber(20,30)
print(o1.add(20,30))

print(o1.add(30,50))


def mallirava():
    for i in range(10):
        print(i)