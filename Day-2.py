'''
operators
----------
1.Arithmetic
-------------
+,-,*,%,/,//,**
eg:-
'''
print(2*3)
print(4%5 == 0)
print(4/2)
print(6//2)
'''
2.Assignment
-------------
=, +=, -=, %=, *=
eg:-
'''
count = 0
for j in range(1,10):
    count += 1
print(count)
'''
3.Comparision
--------------
==---> Looks for both values equal or not
!=, >=, <=,
eg:-
'''
a = 7
b = 9
print(a == b)
'''
4.Logical
----------
And ---> This operator is used to check both should be True
Or --->
eg:-
'''
a = 15
if a % 3 == 0 and a % 5 == 0:
    print("True")
a = 15
if a % 3 == 0 or a % 5 == 0:
    print("True")
'''
5.Membership
-------------
in 
not in
eg:-
'''
a = 7
b = [1,2,7,8]
print(a in b)

a = 7
b = [1,2,7,8]
print(a not in b)
'''
6.Identity
-----------
is---> this operator looks for the object is same or not
is not---> 
eg:-
'''
a = [1,2]
b = [1,2]
c = a
print(type(a))
print(a == b)
print(id(a))
print(id(b))
print(id(c))
print(a is b)
print(a is c)
print(a is not b)
'''
7.Bitwise
----------
&,|,<<,>>
5 binary -->0101
3 binary -->0011
----------------
            0001
----------------
eg:-
'''
print(5 & 3)
print(5|3)

'''
String ---> String is sequence of char that are enclosed in '',"",'''''' and string is immutable
methods
--------
1.replace()---> used to replace with new substring
syntax : variable_name.replace("old string","new string")
eg:-
'''
any = "python is a language"
print(any.replace("python","java"))
print(any)

'''
2.Split --->used to seperate into parts, and split based on the substring where before substring is one index and after is another index in the list
syntax : variable_name.split("substring")
eg:-
'''
any = "python is a language"
print(any.split())
print(any.split("is"))
print(any.split("$"))

'''
3.Length---> get number of items,substring.
syntax : len(variable_name)
eg:-
'''
any = "python is a language"
print(len(any))

'''
3.Slicing ---> can give the access to get particular index from the string.
syntax : variable_name[starting index : ending index]
eg:-
'''
any = "python is a language"
print(any[3:11])

'''
4.Indexing ---> used to get substring present in that index position ...
sntax : variable_name[index position]
eg:-
'''
any = "python is a language"
print(any[7])
print(any.index(""))
print(any.index("ang"))












