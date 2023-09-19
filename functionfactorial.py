#.write a func to find factorial of given number
def function_name(n):
    total = 1
    for i in range(1,n+1):
        total = total * i
    return total
n = int(input("enter the number"))     
a = function_name(n)     
print(a)  