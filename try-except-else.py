# case1:if no exception raised at try-except-else-finally
# try:
#     print("Chinni 1")
# except:
#     print("Jeevan 2")
# else:
#     print("Aman 3")
# finally:
#     print("chandhu 4")
# print("sindhu 5")

# excuting statements are:1,3,4,5------>Normal Termination


# case2: If exception raised at try block and handled

# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(10/2)
# else:
#     print("Hi")
# finally:
#     print("hello")
# print("How are you")

# excecuting statements are:2,4,5--------->Normal Termination



# case3:If exception raised at try and not handled( not matched)
# try:
#     print(10/0)
# except valueError:
#     print(10/2)
# else:
#     print("Hi")
# finally:
#     print("hello")
# print("How are you")
# output:
 # hello
 # executing statements are: 4--------->Abnormal Termination

# case4:if exception raised at exception Block

# try:
#     print("try 1")
# except ZeroDivisionError:
#     print("2"*"2")
# else:
#     print("Hi 3")
# finally:
#     print("hello 4")
# print("How are you 5")

# output:
# try 1
# Hi 3
# hello 4
# How are you 5

# executing statements are: 1,3,4,5--------->NT


# case5: If exception raised at else block:

# try:
#     print("try 1")
# except ZeroDivisionError:
#     print("Hi 2")
# else:
#     print("2"*"2")
# finally:
#     print("hello 4")
# print("How are you 5")

# output:
# try 1
# hello 4
# excuting statements are:1,4-------->AT

# case6: If exception raised at finally block

# try:
#     print("try 1")
# except ZeroDivisionError:
#     print("Hi 2")
# else:
#     print("Jeevan 3")
# finally:
#     print("@"*"4")
# print("How are you 5")

# output:
# try 1
# Jeevan 3

# executing statements are: 1,3---------->AT


# case7: If exception raised at outside finally block

# try:
#     print("try 1")
# except ZeroDivisionError:
#     print("Hi 2")
# else:
#     print("Jeevan 3")
# finally:
#     print("How are you 4")
# print("@"*"4")TypeError

# output:
# try 1
# Jeevan 3
# How are you 4
# executing statements are: 1,3,4------->AT


# case8:If exception raised in try block and handled:

# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Except 2")
# except ZeroDivisionError:
#     print("hello 3")
# else:
#     print("Hi 4")
# finally:
#     print("Hello 5")
# print("How r u 6")


# output:
# Except 2
# Hello 5
# How r u 6
# executing statements are:2,5,6-------->NT


# case9:If exception raised at statement at try block and not handled 1st except block

# try:
#     print(10/0)
# except ValueError:
#     print("Except 2")
# except ZeroDivisionError:
#     print("hello 3")
# else:
#     print("Hi 4")
# finally:
#     print("Hello 5")
# print("How r u 6")


# output:
# hello 3
# Hello 5
# How r u 6
# executing statements are: 3,5,6------>NT


# case10: If exception raised at try Block and not handled at first and second except blocks

# try:
#     print(10/0)
# except ValueError:
#     print("Except 2")
# except ValueError:
#     print("hello 3")
# else:
#     print("Hi 4")
# finally:
#     print("Hello 5")
# print("How r u 6")

# # output:
# # Hello 5
# executing statements are:5-------->AT


# case11:If exception raised at first except block

# try:
#     print("Hi 1")
# except ValueError:
#     print(10/0)
# except ValueError:
#     print("hello 3")
# else:
#     print("Hi 4")
# finally:
#     print("Hello 5")
# print("Outer finally 6")

# output:
# Hi 1
# Hi 4
# Hello 5
# Outer finally 6
# executing statements are:1,4,5,6-------->NT


# case12: If exception raised at second exception block
# try:
#     print("Hi 1")
# except ValueError:
#     print("Jeevan 2")
# except ValueError:
#     print(10/0)
# else:
#     print("Hi 4")
# finally:
#     print("Hello 5")
# print("Outer finally 6")

# output:
# Hi 1
# Hi 4
# Hello 5
# Outer finally 6
# exception raised at:1,4,5,6------->NT


# case13: If exception raised in else block
# try:
#     print("Hi 1")
# except ValueError:
#     print("Jeevan 2")
# except ValueError:
#     print("How are you")
# else:
#     x=int("Jeevan")
#     print(x)
# finally:
#     print("Hello 5")
# print("Outer finally 6")

# output:
# Hi 1
# Hello 5
# executing statements are: 1,5


# case14: If exeception raised in finally block
# try:
#     print("Hi 1")
# except ValueError:
#     print("Jeevan 2")
# except ValueError:
#     print("How are you 3")
# else:
#     x=("Jeevan 4")
#     print(x )
# finally:
#     print(1/0)
# print("Outer finally 6")

# output:
# Hi 1
# Jeevan 4
# executing statements are:1,4------>AT


# case15: If exception raised at else and finally block
# try:
#     print("Hi 1")
# except ValueError:
#     print("Jeevan 2")
# except ValueError:
#     print("How are you 3")
# else:
#     x=int("Jeevan 4")
#     print(x )
# finally:
#     print(1/0)
# print("Outer finally 6")

# output:
# Hi 1
# executing statements are: 1--------->AT


# case16: If exception raised at outer finally block:
# try:
#     print("Hi 1")
# except ValueError:
#     print("Jeevan 2")
# except ValueError:
#     print("How are you 3")
# else:
#     x=("Jeevan 4")
#     print(x )
# finally:
#     print("Inner finally 5")
# print(101/0)

# output:
# Hi 1
# Jeevan 4
# Inner finally 5
# executing statements are:1,4,5-------->AT


# case17: If no exception raised:
# try:
#     print("Try 1")
#     try:
#         print("Inner try 2")
#     except ValueError:
#         print("Inner except 3")
#     except:
#         print("Inner except 4")
#     else:
#         print("inner else 5")

#     finally:
#         print("Inner finally 6")
#     print("Outer finally 7")
# except ValueError:
#     print("outer except 8")
# except:
#     print("outer except 9")
# else:
#     print("Outer else 10")
# finally:
#     print("outer finally 11")
# print("Thanks 12")

# outputs are:
# Try 1
# Inner try 2
# inner else 5
# Inner finally 6
# Outer finally 7
# Outer else 10
# outer finally 11
# Thanks 12
# executing statements are:1,2,5,6,7,10,11,12-------->NT


# case18: If exception raised at outer try Block  and handled

# try:
#     print(10/0)
#     try:
#         print("Inner try 2")
#     except ValueError:
#         print("Inner except 3")
#     except:
#         print("Inner except 4")
#     else:
#         print("inner else 5")

#     finally:
#         print("Inner finally 6")
#     print("Outer finally 7")
# except ValueError:
#     print("outer except 8")
# except:
#     print("outer except 9")
# else:
#     print("Outer else 10")
# finally:
#     print("outer finally 11")
# print("Thanks 12")

# output:
# outer except 9
# outer finally 11
# Thanks 12
# executing statements are: 9,11,12-------->NT


# case19:If exception raised  inner try block and not handled
# try:
#     print("Outer try1 ")
#     try:
#         print(10/0)
#     except ValueError:
#         print("Inner except 3")
#     except:
#         print("Inner except 4")
#     else:
#         print("inner else 5")

#     finally:
#         print("Inner finally 6")
#     print("Outer finally 7")
# except ValueError:
#     print("outer except 8")
# except :
#     print("outer except 9")
# else:
#     print("Outer else 10")
# finally:
#     print("outer finally 11")
# print("Thanks 12")

# output:
# Outer try1 
# Inner except 4
# Inner finally 6
# Outer finally 7
# Outer else 10
# outer finally 11
# Thanks 12

# executin statements are:1,4,6,7,10,11,12-------------->NT


# case20: If exception raised at inner except block 1:
# try:
#     print("Outer try1 ")
#     try:
#         print("inner try 2")
#     except ValueError:
#         print(1/0)
#     except:
#         print("Inner except 4")
#     else:
#         print("inner else 5")

#     finally:
#         print("Inner finally 6")
#     print("Outer finally 7")
# except ValueError:
#     print("outer except 8")
# except :
#     print("outer except 9")
# else:
#     print("Outer else 10")
# finally:
#     print("outer finally 11")
# print("Thanks 12")

# output:
# Outer try1 
# inner try 2
# inner else 5
# Inner finally 6
# Outer finally 7
# Outer else 10
# outer finally 11
# Thanks 12 
# executing statements are:1,2,5,6,7,10,11,12---------->NT


# case21:if exception raised inner except 2 block
# try:
#     print("Outer try1 ")
#     try:
#         print("inner try 2")
#     except ValueError:
#         print("inner except 3")
#     except:
#         print(10/0)
#     else:
#         print("inner else 5")

#     finally:
#         print("Inner finally 6")
#     print("Outer finally 7")
# except ValueError:
#     print("outer except 8")
# except :
#     print("outer except 9")
# else:
#     print("Outer else 10")
# finally:
#     print("outer finally 11")
# print("Thanks 12")

# output:
# Outer try1 
# inner try 2
# inner else 5
# Inner finally 6
# Outer finally 7
# Outer else 10
# outer finally 11
# Thanks 12
# excuting statements are:1,2,5,6,7,10,11,12-------->NT


# case22: If exception raised at inner else block and handled at outer except block
# try:
#     print("Outer try1 ")
#     try:
#         print("inner try 2")
#     except ValueError:
#         print("inner except 3")
#     except:
#         print("Inner except 4")
#     else:
#         print(1/0)

#     finally:
#         print("Inner finally 6")
#     print("Outer finally 7")
# except ValueError:
#     print("outer except 8")
# except :
#     print("outer except 9")
# else:
#     print("Outer else 10")
# finally:
#     print("outer finally 11")
# print("Thanks 12")
# excuting statements are: 1,2,6,9,11,12--------->NT

# case23: If exception raised at inner finally block:
# try:
#     print("Outer try1 ")
#     try:
#         print("inner try 2")
#     except ValueError:
#         print("inner except 3")
#     except:
#         print("Inner except 4")
#     else:
#         print("HI")

#     finally:
#         print(10/0)
#     print("Outer finally 7")
# except ValueError:
#     print("outer except 8")
# except :
#     print("outer except 9")
# else:
#     print("Outer else 10")
# finally:
#     print("outer finally 11")
# print("Thanks 12")

# output:
# inner try 2
# HI
# outer except 9
# outer finally 11
# Thanks 12


# case24: If exception raised at inner try block and outside of finnaly
# try:
#     print("Outer try1 ")
#     try:
#         print("inner try 2")
#     except ValueError:
#         print("inner except 3")
#     except:
#         print("Inner except 4")
#     else:
#         print("HI")

#     finally:
#         print("Inner finally")
#     print(10/0)
# except ValueError:
#     print("outer except 8")
# except :
#     print("outer except 9")
# else:
#     print("Outer else 10")
# finally:
#     print("outer finally 11")
# print("Thanks 12")
# output:
# Outer try1 
# inner try 2
# HI
# Inner finally
# outer except 9
# outer finally 11
# Thanks 12

# case25:if exception raised at outer except block:
# try:
#     print("Outer try1 ")
#     try:
#         print("inner try 2")
#     except ValueError:
#         print("inner except 3")
#     except:
#         print("Inner except 4")
#     else:
#         print("HI 5")

#     finally:
#         print("Inner finally 6")
#     print("Outer finally 7")
# except ValueError:
#     print(10/0)
# except :
#     print("outer except 9")
# else:
#     print("Outer else 10")
# finally:
#     print("outer finally 11")
# print("Thanks 12")
# output:
# Outer try1 
# inner try 2
# HI 5
# Inner finally 6
# Outer finally 7
# Outer else 10
# outer finally 11
# Thanks 12