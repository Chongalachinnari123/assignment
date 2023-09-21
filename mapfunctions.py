

# map() function
#Syntax:
#   map(fun, iter)
#1
# def function_name(n):
#     return n * 3
# numbers = (1,5,6,7)
# a = map(function_name,numbers)   
# print(list(a))

#2
# def function_name(name):
    
        
#     return 

# name_a = input("enter the string")
# a = map(function_name,name_a)
# print(list(a))

#3
# list_a = ["chinna","mounika","udya"]
# result = list(map(list,list_a))
# print(result)


#4

def function(list_a):
    for item in list_a:
        print(item)
        
list_a = ["chinnari","sai","praveen"]        
result = list(map(function,list_a))
print(result)        
 #5
def function_name(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num
  

numbers = [1, 2, 3, 4, 5]
result = list(map(function_name, numbers))
  

print(result)  

