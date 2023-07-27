list = [10,20,30,40,50,10,]
n = int(input("enter the digit:"))
for i in list:
    i = int(i)
    if i == n:
        print(i,"is availble in the list at index:",list.index(i))

    