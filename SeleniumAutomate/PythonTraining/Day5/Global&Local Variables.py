global_var=20

def func():
    local_var=30
    print(global_var)
    print(local_var)
func()

#Example 2
xy=100 #global var
def cool():
    xy=200 #local Variable
    print(xy)
cool()

#Example 3
xy=200
def cool():
    global xy
    xy=100   #global Variable
    print(xy)
cool()

#Example 4
x=100
def coool():
    global x
    x=200
    print(x)
coool()





