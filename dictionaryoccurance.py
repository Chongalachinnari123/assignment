#Number of occurrences of each letter present in the given string ( String is abbbcccdddeeefffgghhh).
string = input("enter the string")
for chr in string:
    print(string.count(chr))