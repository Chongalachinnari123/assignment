#isdigit()
#1
string = "abc12"
result = string.isdigit()
print(result)

#2
string = "1234"
result = string.isdigit()
print(result)

#3
string = "abc1cd2"
for i in string:
    if i.isdigit():
        print("enter the digit",i)
    else:
        print("enter the digit",i)
#4
string = input("enter the string:")
count = 0
for i in string:
    if i.isdigit():
        count += 1
print(count)

#5
string = input("enter the string:")
result = string.isdigit()
print(result)
