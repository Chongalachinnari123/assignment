string = input("enter name")
vowels = "A","E","I","O","U"
for i in string:
    if i in vowels:
        print(i,"is present in string")
    else:
        print(i,"is not present in the string")    