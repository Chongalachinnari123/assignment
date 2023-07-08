a  = int(input("enter the digit:"))
for row in range(1,a+1):
    for col in range(1,a+1):
        if row == 1 or col == a or row == col :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            