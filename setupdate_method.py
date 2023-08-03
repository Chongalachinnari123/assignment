#update()
# the update() method updates the current set,by adding items from another set
#syntax
#set.update(set)
set_a = {"apple","banana","cherry"}
set_b = {"google","microsoft","apple"}
set_a.update(set_b)
print(set_a)
#2
set_1 = {"a","b",1,2,3}
set_2 = {10,20,30}
set_1.update(set_2)
print(set_1)

#3
list_a = {"chinnari","anusha"}
list_b = {"praveen","sai"}
list_a.update(list_b)
print(list_a)

#4
string_1 = {"chinnari"}
string_2 = string_1.update("anusha")
print(string_2)

#5
string_1 = {"a","b","c"}
string_2 = 