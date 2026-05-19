'''
Type Conversions
-----------------
---> convert int to string ?
---> convert int to float ?
'''
an = 78
us = str(an)
om = float(an)
print(us)
print(om)

'''
---> String to int
Eg:-
'''
an = "90"
ear = int(an)
print(ear)

'''
---> string to list
Eg:-
'''
an = "90"
by = list[(an)]
print(by)

'''
---> Float to string,int
Eg:-
'''
car = 90.78
print(int(car))
print(str(car))

'''
---> List to string,tuple
Eg:-
'''
Any = [6,7]
print(str(Any))
print(tuple(Any))

'''
---> Tuple to list
Eg:-
'''
how = (4,5)
print(list(how))
print(str(how))

'''
Int as a user-input
--------------------
Eg:-
'''
num = int(input("Enter a number : "))
print(num + 1)

'''
Str as a user-input
--------------------
Eg:-
'''
some = input("Write a text : ")
print(some)

'''
List as a user-input
---------------------
Eg:-
'''
any = list(map(int,input("Enter numbers : ").split()))
print(any)

'''
Tuple as a user-input
---------------------
Eg:-
'''
any = tuple(map(int,input("Enter numbers : ").split()))
print(any)

num = eval(input("Enter : "))
print(type(num))




































