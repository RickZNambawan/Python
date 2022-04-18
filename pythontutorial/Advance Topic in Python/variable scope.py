""" LEGB (Local, Enclosing, Global, Built-ins) """


# sample one: global variable
var = "global"  # global variable
def sample():
    var = "local"  # local variables
    print(var)

sample()
print(var)


# sample two: local variable
def sampleTwo(varToFunction):  # local variable to function
    print(varToFunction)

varToFunction = "local only to function"
sampleTwo(varToFunction)


# sample 3: enclosing variable
x = "global"

def outer():
    x = "outer"

    def inner():
        print(x)

    inner()
    print(x)

outer()
print(x)