def dec(f):#f(musthaq)
    def inner(n):
        if n=="goverdhan":
            print("hi how are u")
        else:
            f(n)
    return inner
@dec
def b(n):
    print("hello")

b("musthaq")
b("goverdhan")
b("aman")

#2
def function(func):
    def inner():
        print("chinnari is good girl")
        func()
        print("chinnari is bad girl")
    return inner

@function
def say_hello():
    print("chinnari")

say_hello()


def decor1(func):#20
    def inner():
        x=func()
        return x*x
    return inner

def decor2(func):#num (10)
    def inner():
        x=func()
        return 2*x #20
    return inner

@decor2
@decor1
def num():
    return 10
print(num())

#4
def function_1(func):
    def inner():
        x = func
        return x + x
    return inner
def function_2(func):
    def inner():
        x = func()
        return 2 * x
    return inner
@function_1
@function_2
def number():
    return 20
print(num())    


