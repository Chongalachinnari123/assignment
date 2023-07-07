string = input("enter the string:")
for i in string:
    if i.islower():
        print("it is lowercase")
        continue 
    else:
        print("it is uppercase letter")   