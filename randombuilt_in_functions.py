#random() function
# its going to print in between 0 and 1 (not inclusive)
#1
from random import *
for i in range(10):
    print(random())

#2
list = []
for i in range(5):
    list.append(random())
    print(list)

#3
import random

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled List:", my_list)

