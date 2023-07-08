N = int(input("enter the digit:"))
for r in range(1, N+1):
    i=N-(r-1)
    if i> 1 and i< N:
      print("* " + "  " * (i-2) + "* ")
    else:
      print("* " * i)