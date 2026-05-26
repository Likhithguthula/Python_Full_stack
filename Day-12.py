'''
Built in Function
------------------
1)input()
2)type()
3)max()
4)min()
5)len()
6)print()

Recursive Function ---> A recursive function ha calls itself to solve a problem by breaking it into small or simple sub-problems
Eg:-
'''
def fac(num):
    if num == 1:
        return 1
    return num * fac(num - 1)
print(fac(5))

def even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
even(7)

'''
Return ---> This ends a function execution and sends a value back to the code that called the function
Eg:-
'''
def add(a,b):
    return a+b
res = add(4,5)
print(res)

'''
Lambda Function ---> A lambda function is a small anonamus functions
                ---> Lambda can take n mumber of arguments, but only one expression
Syntax : lambda arguments : expression
Eg:-
'''
so = lambda a,b,c : a+b+c+a
print(so(3,4,9))





















































