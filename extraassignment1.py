# Input: ram is good boy
#output:boy good is ram
string = input("enter the string:")
split_string = string.split()
output = ""
result = split_string[::-1]
for i in result:
    output += i + " "
print(output[:-1])
    