n = int(input("enter the digit:"))
list = []
for i in range(1,51):
    i = int(i)
    if i == n:
        list.remove(i)
    else:
        list.append(i)    

