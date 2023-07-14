#format()
string = "my age is {age}"
result = string.format(age=20)
print(result)

#2
string = "my name is {name} and my age is{age}"
result = string.format(name = "chinnari", age=10)
print(result)

#3
string = "my name is{0} and my age is{1}"
result = string.format("chinnari",20)
print(result)

#4

string = "my name is{} and my age is{}"
result = string.format("chinnari",10)
print(result)