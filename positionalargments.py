#positional arguments
#values passed to function based on their positions
#values passed to the parameters based on their positions
def function_name(name,age):
    print(name,"is a",age,"old")
function_name("chinnari",10)  

#2 
# if you are not giving the any value of gievn function ,it will prints an type error 
#function_name() missing 1 required positional argument: 'marks'
def function_name(name,rall_no,marks):
    
    return
function_name("chinnari",20)

#3
# if you are giving extra values to  the given functions,it will be prints an error 
#function_name() takes 2 positional arguments but 3 were given
def function_name(name,age):
    return
function_name("chinnari",20,50)

#4
# in below example firstname is chongala and lastname is chinnari concatenate the two strings it gives chongalachinnari
def function_name(first_name,lastname):
    result = first_name + lastname
    return result
name = function_name("chongala","chinnari")  
print(name) 

#5
def area_rectangle(length,breadth):
    return length*breadth
result =  area_rectangle(30,40)
print(result)   




