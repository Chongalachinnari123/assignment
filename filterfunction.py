#filter()
#Syntax
       #filter(function, iterable)
#1
n = [5, 12, 17, 18, 24, 32]

def myFunc(a):
  if  a % 2 == 0:
    return True
  else:
    return  False

adults = filter(myFunc, n)

for b in adults:
  print(b)

#2
list_a = ["a","b","c","d"]
vowels = "a","e","i","o","u"
def function_name(chr):
    if chr in vowels:
        return True
    else:
        return False
vowels_list = filter(function_name,list_a)
for i in vowels_list:
    print(i)
3
def function_name(a):
    if a == "chinnari":
        return True
    
list_a =["chinnari","praveen","sai","anusha"]
list_b = filter(function_name,list_a)

for item in list_b:
    print(item)
4
def function_name(item):
    if item % 2 == 1:
        return True
    else:
        return False
list = [1,3,5,6]
list_a = filter(function_name,list)
for i in list_a:
    print(i)   

 #5
def function_name(items):
    if items == "anusha":
        return True

    
list = ["chinnari","anusha","saimounika"]  
list_a = filter(function_name,list)
for i in list_a:
    print(i)

