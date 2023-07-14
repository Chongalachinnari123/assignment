#islower()

#1
string = "abzc"
result = string.islower()
print(result)

#2
string = "ABZ"
result = string.islower()
print(result)

#3
string = input("enter the string:")
for i in string:
    if i.islower():
        print(i)

#4
string = input("enter the string:")
for i in string:
    if i.islower():
        print("it is lower letter")        
#5
string = input("enter the string:")
print(string.islower())