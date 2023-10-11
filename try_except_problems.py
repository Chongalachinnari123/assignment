#Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
# list = [2,4,0,10,12]
# try:
#     for item in list:
#         if item / 2  :
#             print(item,"it is divisible by 2")
# except ZeroDivisionError:
#     print(item,"it is zero division error")

# def ZeroDivisionError():
#      numbers = [1, 2,0,3, 4]

#      for num in numbers:
#         try:
#               result = 10 / num
#               print("Result:", result)     
#         except:    
#               print("it is zero division error")
# ZeroDivisionError()

#2
#Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer
# def value_error():
#     list = [1,2,"chinnari",5,8]
#     for num in list:
#         try:
#             result = 10/item
#             print(result)
#         except value_error:
#             print("it is value error")
# value_error()  
# 
 
# Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
               

# def function():
#     try:
#         n = input("enter the digit:")
#         m = input("enter the digit:")
#         result = n/m
#         print(result)
#     except TypeError:
#         a = int(input("enter the digit:"))
#         b = int(input("enter the digit:"))
#         result = a/b
#         print(result)
# function()
#5
#Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input
# def Keyboard_Interrupt():
#     try:
#         x=int(input("enter the value:"))
#     except KeyboardInterrupt:
#         print("chinnari")
# Keyboard_Interrupt()

#6
#Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
def arithmetic_error():
 
        try:
            arithmetic = 5/0
            print(arithmetic)
        except ArithmeticError:
            print('You have just made an Arithmetic error')
arithmetic_error() 


def index_error():
    try:
        my_string = "Geeksforgeeks"
        print(my_string[-61])
    except IndexError:
        my_string = "Geeksforgeeks"
        print(my_string[5])
        
index_error()            