list = input("enter list:")
list = list.split(",")
newlist = []

for i in list:
     i = int(i)
     newlist.append(i)
     
for item in newlist:
          if 100%item == 0:
             print(float(item))
             
          else:
               print("print it is not divisible by zero")
               continue