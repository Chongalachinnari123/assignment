user_input = input("enter the user_input:")
vowels = "a","e","i","o","u"
new_list = [i for i in user_input if i in vowels]
print(new_list)