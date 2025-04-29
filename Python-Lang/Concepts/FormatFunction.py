# Format Functions

import json
from sys import exception
from textwrap import indent


value = 20
va = f"the price of {value} is less than 30"
print(va)

value = f"......{ value:>} This Is Hari Vardhan reddy........."
print(value)

valueToMoney =  200
print(valueToMoney)


price = 200.9856
fmt = f"The cost is arount {price : .2f}"
print(fmt)

val1 = 25
val2 = 30

print(f"the multiplication of val1 and val2 are {val1 * val2}")

print(f"The price is {'expensive' if val1 > val2 else 'cheap'}")

def myConverter(x):
    return x *0.3048

txt = f"The List is Function of the year dates {myConverter(300)}"
print(txt)

price = 100000
txt = f"The price comma seperator {price:b}"
print(txt)
 
try :
    print(x)
except NameError:
    print("Value is not defined...")
try:
    f = open("demo.txt")
    try :
        f.write("Hello World ...")
    except:
        print("Exception Error araised...")
    finally:
        f.close()
except:
    print("Please create file as it is not already available....")

x = -1

if x > 0:
    raise exception("Please Check the number ....")

print(x)

import re
txt = "peddireddy"

x = re.findall("[a-d]",txt)
print(x)

y = re.findall("d.*",txt)
print(y)

x = {
    "name" : "peddireddy",
    "age" : 40,
    "married" : True,
    "divorsed" : False,
    "children" : ('peddi','reddy','hari'),
    "cars" :[
        {"model":"bmw","price" :25000},
        {"model":"ferarri","price":349000}

    ]
}
print(x)

y = json.dumps(x,indent=4,sort_keys=True)
print(y)

import datetime

x = datetime.datetime.now()
print(x)