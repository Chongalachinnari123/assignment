string = input("enter the string:")
split_string = string.split(" ")
for i in split_string:
    result = ".".join(i)
    print(result)
