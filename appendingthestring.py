string = input("enter the string:").split()
updated_string = input("enter the string")
length = len(string)
string = list(string)
# if length %2 == 0:
#     result = string[length/2]
#     string[result] = "chinnari"
# else:
#     result = string(length)+1/2
if length %2 == 0:
    
    string[int(length/2)] = updated_string
    print(string)
else:

    half = int(length+1)/2
    string[half] = updated_string 
    print(string) 
