# Input:ABCDEAABBCCDDFFGGHHGGHHII
#outpu:ABCDEFGHI
string = input("enter the string:")
list = ""
for i in string:
    if  i not in list:
        list += i
print(list)

     