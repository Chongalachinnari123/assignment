n = int(input("enter number:"))
target = int(input("enter number:"))
count = 0
for i in range(n):
    if count == target:
        continue
    else:
        count += 2
        print(count)
    
    