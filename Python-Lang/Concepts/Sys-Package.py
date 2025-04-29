import sys
import time

sys.stderr.write("This is stdder text \n ")
sys.stderr.flush()

print(sys.argv)

s = [0,6,3,4,7,2]
print(s)
print(*s)


def pizza(size,*toppings,**hotelRatings):
    print(f"pizza sige is {size}")
    for i in toppings:
        print(f"{i}")
    print(hotelRatings)

pizza('large','sugar','sweet','sweetchilli',sharadha=34,simpono=34)


def measure_time(func):
    def wrapper(*args,**kwargs):
        start_time=  time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print(f"the execution start time {end_time-start_time: 1.7f}")
    return wrapper

    def greeting(func):
        def wrapper(*args,**kwargs):
            print('hello')
            func(*args,**kwargs)
    return wrapper

@measure_time
def myName(name):
    print(f"Good Morning ... ")

myName('hari')