#1
# lets check the what happend, when there is no error in the try block

numbers = [1, 2,3, 4]

for num in numbers:
    try:
        result = 10 / num
        print("Result:", result)     
    except:    
        print("it is zero division error")
print("it prints outside the try-except block")        

#2
numbers = ["chinnari","sai","anusha"]

for num in numbers:
    try:
         if num == "anusha":
            print(num)
         else:
            print("num is not found")   # here there is no error in the try block
                                        # it does not print except block 
    except:
        print("print the except block")


print("it prints outside the try-except block") 

#3
#lets check what happend ,if there is an error an try block with except block matched

numbers = [1, 2,0,3, 4]

for num in numbers:
    try:                                     # here i am giving statement-2 is an error, 
                                            # and  it will prints statement-1 in try block and except block and out of the try and exception block
                                              # the except block is matched it will prints 1,4,5 ,it an normal termination

        result = 10 / num
        print("Result:", result)     
    except ZeroDivisionError:    
        print("it is zero division error")
print("it prints outside the try-except block")      
                                               

#4
# lets check the exception block is not matched ,if try block having an error
# try:
#     print("anusha")
#     print(10/2+sai)      # here i am giving both satement-1 and statement -2 is errors but it will print except block 
#                          # and  it will print out of the try and except
#     print("chinnari")     # it raise a value error but i am giving zero division error ,exception not matched ,it will prints only stament-1
# except ZeroDivisionError: # it is abnormal termination
#     print("run the code")    
# print("it prints the outside of the function")

#5
try:
    print(10/5)
    print(10/2)  # here i am giving statement-3 is an error 
                 # it will print what ever i am giving in try it prints
except:          # and prints outside the try and except block also
                 # error raised in statement -4 and statement-5 ,it is always  abnormal termination
                 # it will prints the statement-1 and statement-2 and out of the try-except block also
    my_dict = {'name': 'John'}
    print(my_dict['age'])   
print("it prints the outside of the function")



#6

# lets see the examples of the how to use Base exception
# if using BaseException (or) Exception ,it overcome the child 

# try:
#     print("chinnari")
#     print(10/0)
#     print("Hi Aman")
# except (ValueError,ZeroDivisionError):
#     n="chinnari"
#     print(n/2)
# print("Hi")
# output:
# Jeevan
# abnormal termination

#7
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except BaseException as e:
    print("Error: Division by zero!")
    print("Exception details:", e)
   
#8
try:
    print(10/0)
except Exception:     # here i am giving zerodivison error ,but i am giving BaseException in except block,it will prints stament-2 
    print("chinnari")     # and alse  it will print outside the try and except 
print("chinnari is good girl")


#9
#ArithmaticError
# here i am giving value error in try block ,it is not a child error of arithmatic error ,so it is raises an error an value error
# try:
#     value = int("abc")  
# except ArithmeticError as e:
#     print("Caught an exception:", e)
#10
try:
    print(10/0)  
except ArithmeticError as e:       # here i am giving zerodivison error ,it is child error of arithamatic error 
                                   #so it does not raise any error ,it will print stataement-2
    print("exception:", e)

#11

# lets understand the finally block also ,with examples

# if there is errors in try block and handles the exception ,it will prints the all the statemets and also it is normal termination
# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print("Result:", result)
# except (ValueError,ZeroDivisionError):
#     print("exception  not raised")
 
# finally:
#     print("final block is excuted")

# #12
# data = [1, 2, 'three', 4]

# for item in data:
#     try:
#         if 10 / int(item):
#             print("Result:", result)
#         else:
#             print("hi")
#     except (ZeroDivisionError,ValueError):  
#         print("it have value error")
#     finally:
#         print("it will prints the final block")    


#13
# if there is errors in try block and not handles the exception
#it will prints the all the statemets and also it is abnormal termination

# it will prints only statement-1 and final block only
# data = [1, 0, 4]

# for item in data:
#     try:
#         if 10 / int(item):
#             print("Result:", result)
#         else:
#             print("hi")                  
#     except (IndexError,KeyError):  
#         print("it have value error")
#     finally:
#         print("it will prints the final block") 
#14
# it will print 1,5 ,it raises the index error
try:
    result = "chinnari"
    print(result)
    result = [1, 2, 3]
    print(result[5])
    result = 10/10
    print(result)
except(ZeroDivisionError):
    print("it prints the zero division error")
finally:
    print("it prints the final block") 


#15
# let check there is no exception raise ,what will happen
# it is normal termination 
try:
    num = 10
    result = 10 / num
    print(result)
except:
    print("Error: Invalid input. Please enter a valid number.")
 
finally:
    print("This block always executes, regardless of exceptions.")
    


      
        



    


