# #function problems
# #1
def is_between_200_and_500(number):
    if number > 200 and number < 500:
        print("Yes")
    else:
        print("No")

number = int(input("enter the digit:"))
is_between_200_and_500(number)

# #2
def even_odd_numbers(number):
    for i in range(number+1):
        if (i % 2) == 0:
            print(str(i) + " EVEN")
        else:
            print(str(i) + " ODD")

number = int(input("enter the digit:"))
show_numbers(number)
# #3
def get_speed_status(speed):
    if speed < 60:
        print("Normal")
    elif speed >= 60 and speed <80:
        print("Warning")
    elif speed >= 80:
        print("Over Speed")



speed = int(input())
get_speed_status(speed)

# #4
def calculate_percentage(number):
    if number < 1000 :
        msg = (5/100)*number
    else:
        msg = (10/100)*number
    return msg    
    
number = int(input("enter the digit:"))

result = calculate_percentage(number)

print(result)

# #5
def get_weather_report(temperature):
    if temperature < 22:
        print("Cold")
    elif temperature >= 22 and temperature < 35:
        print("Warm")
    elif temperature >= 35:
        print("Hot")
temperature = int(input("enter the digit:"))
get_weather_report(temperature)



# #6
def perimeter_of_square(arg_1):
    
    perimeter = arg_1 * 4
    return perimeter

side = int(input("enter the digit:"))
result = perimeter_of_square(side)
print(result)

# #6 nested functions
def outer_function():
    name = "chinnari"

    def inside_function():
        print(name)

    inside_function()

outer_function()

#7
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function


add_five = outer_function(5)
result = add_five(3)
print(result)  

# #8  function arguments

#positional arguments
def compare(a, b):
    if a > b:
        result = "Win"
    
    elif a == b:
        result = "Draw"
    
    else:
        result = "Lose"
        
    return result

a = int(input("enter the digit:"))
b = int(input("enter the digit:"))

compare_result = compare(a, b)

print(compare_result)

#9 
def function_name(first_name,lastname):
    result = first_name + lastname
    return result
name = function_name("chongala","chinnari")  
print(name) 

#10
def sum_of_squares_m_to_n(m, n):
    total = 0
    for i in range(m,n+1):
        total  = total + i ** 2
    print(total)    
    


m = int(input("enter the digit:"))
n = int(input("enter the digit:"))
sum_of_squares_m_to_n(m,n)

#11
def shuffle_string(string, indices_list):

    list = ""
    for i in indices_list: 
        i = int(i)
        result = string[i]
        list += result
    return list    
string = input()
indices_list = input().split()

result = shuffle_string(string,indices_list)
print(result)
#12
#keyword arguments
def function_name(name,age):
     print(name,"is a",age,"old")
function_name(age=20,name="anusha")
function_name(name="chinnari",age=15)

#13
def function_name(age,name):
     print(name,"is a",age,"old")
function_name(20,name="anusha")

#14
def f1(a,b):
    c=b
    del b
    print(a,"good morning",c)
    
a="chinnu"
b="take care"
f1(a,b)

#15
global variable
a = "amma"
def function_name(a):
   return a
result = function_name(a)
print(result)   

#16
#local variable
def function_name(a):
    
    print(a)
a = "chinnari"
function_name(a)    

#17
x = 10
def change():
    
    global x
 
    
    x = x + 5
    print("Value of x inside a function :", x)
 
 
change()
print("Value of x outside a function :", x)


#18
#default arguments
def function_name(a="welcome",b="chinnari"):
    string = a + " " + b
    return string
result = function_name("hi","anusha")    
print(result)

#19
def function_name(a,b=21):
    print(a,"is age",b,"old")
    return 
function_name("anusha",b=20)

#20
def get_reversed_string(string):
    list = ""
    for i in string:
        list += i
        total = list[::-1]
    return total
        
string = input("enter the string:")

resultant_string = get_reversed_string(string)
print(resultant_string)










