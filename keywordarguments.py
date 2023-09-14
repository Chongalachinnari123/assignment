#keyword arguments

# Keyword arguments are specified by the parameter name followed by an equal sign and the value.
#keyword arguments are specifes that which value given to the parameter
# In the below example particurly specifes values to given parameter
#1
def function_name(name,age):
    print(name,"is a",age,"old")
function_name(name="anusha",age=20)

#2
#In below example positions of arguments is same but key and values are same 
# that is reason to give to the same output
def function_name(name,age):
     print(name,"is a",age,"old")
function_name(age=20,name="anusha")

#3
def function_name(name,age):
     print(name,"is a",age,"old")
function_name(age=20,name="anusha")
function_name(name="chinnari",age=15)

#4
#in below example position orguments followed by the keyword arguments it gives an output
def function_name(age,name):
     print(name,"is a",age,"old")
function_name(20,name="anusha")
#5
# in below example positon arguments does not follow the keyword arguments it gives error
# def function_name(name,age):
#      print(name,"is a",age,"old")
# function_name(name="anusha",20)




