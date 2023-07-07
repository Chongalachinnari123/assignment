string = list(input("enter the string"))
count = 0
for i in string:
    if i.isdigit():
        count += 30
        continue
print(count)
       
    
    