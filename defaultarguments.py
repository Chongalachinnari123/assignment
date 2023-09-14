# Default arguments
#Default arguments have default values assigned to them in the function definition
#If a value is not provided when calling the function, it uses the default value
#1
#1 In below example here 20 is given to parameter value but you can give defalut is 22
def function_name(age=20):
    print("my age is",age)
function_name("22")    

#2
#here name takes default value is chinnari
def function_name(name="chinnari"):
    print("my name is",name)
function_name()  

#3
# Only the a is provided, so it uses the default b of 2.
def power(a, b=2):
    return a ** b

result1 = power(2)
print(result1) 

#4
# non default arguments does not follow the default arguments,
# In below example non default arguments followes default arguments
#SyntaxError: non-default argument follows default argument
# def function_name(a=2, b):
#     return a ** b

# result1 = power(4)
# print(result1) 