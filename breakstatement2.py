a = int(input("enter number:"))
for i in range(a):
    if i %2 == 0:
        print(i,"is divisible by 2")
        continue
print(i,"it is  not divisible by 2")