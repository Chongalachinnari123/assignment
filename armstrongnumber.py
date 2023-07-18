n = int(input("enter the digit:"))
tostring = str(n)
sum = 0
for i in tostring:
    sum += int(i) ** 3
if (n == sum):
    print("armstrong number")
else:
    print("it is not a armstrong number")        
    