#Number of occurrences of each vowel present in the string 
string = input("enter the string")
vowels = "a","e","i","o","u"
for item in string:
    if item in vowels:
        print(string.count(item))