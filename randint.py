#randint()(inclusive)
#1
from random import randint
for i in range(3):
    print(randint(1,10))

#2
import random
print(random.randint(100, 200))

#3
import random
list_a = [random.randint(1,20) for i in range(5)]
print(list_a)

#4
import random


dice_roll = random.randint(1, 6)
print("Dice Roll Result:", dice_roll)

#5
import random
Result = random.randint(1, 10)
print(Result)
