'''
day 11 of my python course

statement
---------
assert
-----> this is a debbuging statement used to test wheather a condition is True
error---> assertion error
eg:

num = 1000
assert num > 10
print("true")

eg:
age = 250
assert age > 100
print("Eligible")

Functions
--------> a function is a block of code which only executes when it is called
--------> you can pass data, known as parameters into a function
--------> tnis is used to avoid repeated lines in code
---->how function was represented ---> def function_name(parameters):
                                            --------
                                            --------
                                        function_name(arguments):
eg:
num = 9
def even(num):
    if num % 2 == 0:
        print(f"{num} EVen")
    else:
        print(f"{num} Odd")
    print(num)
even(num)
even(109)

Ways to pass arguments
----------------------
1) required arguments
------> a function must be called with the new parameters
eg:
 num = 9
def even(num):
    if num % 2 == 0:
        print(f"{num} EVen")
    else:
        print(f"{num} Odd")
    print(num)
even(num1,90)
                      
eg 2:

num = 9
def even(num,num1):
    if num % 2 == 0:
        print(f"{num} EVen")
    else:
        print(f"{num} Odd")
    print(num)
even(109,90)

2) Default arguments
--------------------
BY default, values is defined at paramaters even tho it will take from arguments
eg :
def even(name = "nani", age = 22, Sal = 10000):
    print(name)
    print(age)
    print(Sal)
even("naveen",21,10000)

KEYWORD  arguments
------------------------
----> we can send arguments with key=value syntax. By this , the order of arguments does not matter
eg:
def details(age, Sal, name):
    print(name)
    print(age)
    print(Sal)
details(name="naveen",age = 32,Sal=234234)

VARIBLE Length arguments
------------------------
----> adding a star to the paramaeters name in the function, we recieve a tuple of
        arguments and can access items with indexes
eg:

def details(*name):
    print(name)
details("sai", "naveen", "omkar")
# if we want print the tuple values than
def details(*name):
    print(name[1])
details("sai", "naveen", "omkar")
'''
