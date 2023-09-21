#reduce()
# from functools import reduce

# numbers = [1, 2, 3, 4, 5]
# product = reduce(lambda x, y: x * y, numbers)
# print(product)  

# #2
# from functools import reduce

# strings = ["apple", "banana", "cherry", "date"]
# separator = ", "
# result = reduce(lambda x, y: x + separator + y, strings)
# print(result)  

#3
# from functools import reduce

# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
# flat_list = reduce(lambda x, y: x + y, nested_list)
# print(flat_list)  

#4
# from functools import reduce

# n = 5
# factorial = reduce(lambda x, y: x + y, range(1, n + 1))
# print(factorial) 

#5

from functools import reduce

words = ["apple", "banana", "cherry", "date"]
longest_word = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(longest_word) 





