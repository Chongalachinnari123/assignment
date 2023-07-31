#sort()
#1
tuple_a = [10,20,30,50,40]
tuple_a.sort()
print(tuple_a)
#2
tuple_a = [1,2,4,3,7,6]
a = tuple_a.sort()
print(a)
#3
cars = ["ford","bmw","volvo"]
cars.sort()
print(cars)
#4
cars = ["ford","bmw","volvo"]
cars.sort(reverse=True)
print(cars)
#5
cars = ["chinnari","anusha","sai"]
cars.sort(reverse=False)
print(cars)
#6
cars = ["ford","bmw","volvo"]
a =sort(cars,reversed=True)
print(a)

#7
cars = [{
    "car":"ford",
    "year":2005
},{
"car":"ford",
    "year":2000},
     {
        "car":"ford",
    "year":2001
     }
]
cars.sort()
print(cars)
