'''
List Comprehension ---> This list comprehension offers a shortest syntax when we want to create a new list from existing list
Syntax : variable_name = [expression loop condition]
Eg:-
'''
old = [1,2,3,4,5]
new = [so for so in old]
print(new)

old = [1,2,3,4,5]
new = [so for so in old if so % 2 == 0]
print(new)

old = [1,2,3,4,5]
new = [so if so % 2 != 0 else "even" for so in old]
print(new)

old = [23,6,7,90,3,46]
new = [so if so % 2 != 0 else "even" for so in old]
print(new)

'''
Generators ---> Generators in python are a special type of itterable, allowing users to iterate
                over a data efficiently without storing everything in memory...
           ---> They generate values lazily using yield keyword
Why to use generators? ---> Generators does not store the entire dataset in memory, they generate values on the fly or run time.
                       ---> Avoiding the unnecesary storage of data speed up execution.
How it works? ---> It looks like normal function but uses the yield keyword instead of return
              ---> When the function is called, it does not execute immediately. Insead,it return
                    a generator object which can be iterated using loop or the next() function
Eg:-
'''
def simple_gen():
    yield 1
    yield 2
    yield 3
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))


def simple_gen():
    print("start")
    yield 1
    yield 2
    yield 3
    print("end")
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

def any(num):
    for i in range(num):
        yield i*i
a = any(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))

def any(num):
    for i in range(1,num+1):
        yield i*i
a = any(5)
print(next(a))
print(next(a))
print(next(a))

def sqr(num):
    result = []
    for i in range(1,num+1):
        result.append(i*i)
    return result
print(sqr(5))

'''
Removing the AEIOU and aeiou
Eg:-
'''
so = 'Python is a high-level, general-purpose programming language known for its clean syntax, readability, and versatility'
any = ''
for j in so:
    if j not in "AEIOUaeiuo":
        any += j
print(any)

so = 'Python is a high-level, general-purpose programming language known for its clean syntax, readability, and versatility'
any = ''
for j in so:
    if j in "AEIOUaeiuo":
        any += j
print(any)







    
































