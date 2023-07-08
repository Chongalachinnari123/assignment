n = int(input("enter the digit:"))
k = n-1
hollow_spaces_count = -1
for i in range(1, n+1):
  spaces = " " * k
  stars = "* " * i
  print(spaces+stars)
  k = k - 1