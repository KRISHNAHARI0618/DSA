a = ["10","Twnty","Thirty"]
print(a)

try:
    res= 5/0
    resq = "100"/20
    total = int(a[0])+int(a[5])
except (ValueError,TypeError,IndexError,ZeroDivisionError,SyntaxError) as e:
    print("Unknown Error....")
finally:
    print("Closing the connection...")


print("please check one more time .........")
'''
Compile time error: --> Syntax Error
Run Time Error --> Not Giving Outputs
Logical Error --> While Testing it will come out

'''
print()
def set(age):
    if age < 0:
        raise ValueError("Age should be greater than 0")
    print(f"Age set to {age}")

try:
    set(-5)
except Exception as e:
    print(e)

class InvalidAgeError(Exception):
    def __init__(self, age,msg="Age must be between 0 and 120"):
        self.age = age
        self.msg = msg
        super().__init__(self.msg)
    def __str__(self):
        return f'{self.age} -> {self.msg}'
def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print(f"Age set to :{age}")

try:
    set_age(200)
except InvalidAgeError as e:
    print(e)

class InvalidvillageName(Exception):

    def __init__(self,villageName,msg="Please Enter Chiyyapadu or Chapad"):
        self.villageName= villageName
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.villageName} -> {self.msg}'

def set_villageName(villageName):
    if villageName != "Chiyyapadu" or villageName != "Chapad":
        raise InvalidvillageName(villageName)
    else:
        print(f"Village name set to {villageName}")

try:
    set_villageName("Kadapa")
except InvalidvillageName as e:
    print(e)

try:
    set_villageName("Chiyyapadu")
except InvalidvillageName as e:
    print(e)