n = int(input("enter the digit:"))
for i in range(n):
    spaces = "  "*i
    stars = "* "*(n-i)
    print(stars+spaces)