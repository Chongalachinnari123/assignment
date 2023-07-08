
rows = int(input("enter the digit:"))
columns = int(input("enter the digit:"))


for i in range(rows):
    if (i == 0) or (i == (rows - 1)):
        print("* " * columns)
    else:
        number_of_spaces = ("  " * (columns - 2))
        print("* " + number_of_spaces + "* ")