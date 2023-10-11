try:
    print("outer try 1")#statment-1
    print("outer try 2")#statment-2
    print("outer try 3")#statment-3
    try:
        print("outer try 1")#statment-4       
        print("inner try 2")#statment-5
        print("inner try 3")#statment-6
    except:
        print("except inner block")#statment-7             
    finally:
        print("inner finally block")#statment-8  
    print("normal statment ")#statment-9
except:
    print(10/0)#statment-10           
finally:
    print("outer finally block")#statment-11           
print("outside the blocks")#statment-12

#case-1
# if there is no exception raised ,it will prints 1,2,3,4,5,6,7,8,9,10,11,12 ,and it is normal termination

#case-2
# if exception raised at statement-1 and exception handles,it will prints 10,11,12 and it is normal termination



#case-3
#if exception raised at statement-2 and exception handles,it will prints 1,10,11,12 and it is normal termination

#case-4
#if exception raised at statement-1 and exception does not match,it will prints 11, and it is abnormal termination

#case-5
#if exception raised at statement-2 and exception does not match,it will prints 1,11, and it is abnormal termination


#case-6
#if exception raised at statement-3 and exception does not match,it will prints 1,2,11, and it is abnormal termination

#case-7
#if exception raised at statement-3 and exception handles,it will prints 1,2,10,11,12 and it is normal termination

# case-8
# If an exception raised at stmt-5 and inner except block matched
#1,2,3,4,7,8,9,11,12 Normal Termination

#case-9: If an exception raised at stmt-5 and inner except block not matched but outer
#except block matched
#1,2,3,4,8,10,11,12,Normal Termination



#case-10
# if exception raised at statement-4,matched inner exception ,it will prints the 1,2,3,7,8,9,11,12,it is normal termination

#case-11
# if exception raised at statement-4, does not matched inner exception ,it will prints the  1,2,3,8,11,12, it is abnormal termination


#case-12
# if exception raised at statement-5,matched inner exception ,it will prints the 1,2,3,4,7,9,11,12,it is normal termination

#case-13
# if exception raised at statement-5, does not matched inner exception ,it will prints the 1,2,3,4,8,11,12, it is abnormal termination

# case-14
# if exception raised at statement-6,matched inner exception ,it will prints the 1,2,3,4,5,7,8,9,11,12 ,it is normal termination

# case-15
# if exception raised at statement-6, does not matched inner exception ,it will prints the 1,2,3,4,5,8,10,11,12, it is abnormal termination


# case-16

# if statement-4 raised an exception and does not match the inner exception but matches the outer exception ,it will prints
#   1,2,3,8,10,11,12 

# case-17
#  If an exception raised at stmt-7 and corresponding except block not matched
 # 1,2,3,4,5,6,8,9,11,Abnormal Termination

#case-18:
#If an exception raised at statement-10 then it is always abonormal termination ,it will print 1,2,3,4,5,6,8,9,11,12


 #case-19: If an exception raised at statement-11 or statement-12 then it is always abnormal
#termination.




