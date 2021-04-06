print("2016113519 유지훈")

def myfunc1():
    x =  "cool"
    print("1. Computer is " + x)
    
def myfunc2():
    global y
    y = "fantastic"
    print("2. Computer is " + y)
    
myfunc1()
myfunc2()

print("3. Computer is " + y)