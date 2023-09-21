# # recursive function is nothing but when function calling itself is known as recursive function

# # def factorial(n):
# #     if n == 0:
# #         return 1
# #     else:
# #         return n * factorial(n - 1)
# # def factorial(n):
# #     if n == 0:
# #         return 1
# #     else:
# #         return n * factorial(n-1)
# # n = int(input("enter the number"))        
# # a = factorial(n)
# # print(a)        


# #fibonacci series

# # def fibonacci(n):
# #     if n <= 0:
# #         return 0
# #     elif n == 1:
# #         return 1
# #     else:
# #         return fibonacci(n-1)+fibonacci(n-2) 
# # a = fibonacci(6)  
# # print(a)         

# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     # elif n == 2:
#     #     return [0, 1]
#     else:
#         # fib_seq = fibonacci(n - 1)
#         # fib_seq.append(fib_seq[-1] + fib_seq[-2])
        
#         return fib_seq

# # Example usage:
# n = 10  # Change this to generate a different number of Fibonacci numbers
# fib_seq = fibonacci(n)
# print(f"The first {n} numbers in the Fibonacci sequence are: {fib_seq}")

#4
# def sumnums(n):
#     if n == 1:
#         return 1
#     return n + sumnums(n - 1)


# print(sumnums(3))
# print(sumnums(6))
# print(sumnums(9))

#5
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]


reverseme = 'Desserts'
print(reverse(reverseme))




