'''
5)Sets ---> sets is a collection of unique elements
       ---> It is a unordered data
       ---> Duplicate values are not allowed
       ---> Items are no stored in index order
       ---> It is represented in {}
Eg:-
'''
any = {1,2,2,3,4}
an = {68,64}
print(any | an)
print(any.union(an))

'''
Methods
-------
A)Union() ---> It will give all values from 2 sets together in once
Syntax : variable_name.union(another variable)
B)Intersection()---> To get the common elements from both sets
Syntax : Variable_name.intersection(another Variable)
Eg:-
'''
any = {1,2,2,3,4}
an = {2,3}
print(any & an)
print(any.intersection(an))

'''
C)Difference() ---> To get the different values from the set
Syntax : Variable_name.different(another variable)
Eg:-
'''
any = {1,2,2,3,4}
an = {3,26,89}
print(any - an)
print(any.difference(an))
print(an.difference(any))

'''
D)Add() ---> To add new elements into se
Syntax : variable_name.add(element)
Eg:-
'''
any = {1,2,3,4}
any.add(5)
print(any)

'''
E)Update() ---> to add multiple elements into set
Syntax : variable_name.update([elements])
Eg:-
'''
any = {1,2,3,4}
any.update([5,6])
print(any)

'''
F)Remove() ---> Used to remove element from the set but it through error(key error) if element not in set
Syntax : variable_name.remove(element)
Eg:-
'''
any = {1,2,2,3,4}
any.remove(2)
print(any)

'''
G)Discard() ---> Used to remove element from the set but it never through error if element not in set
Syntax : variable_name.discard(element)
Eg:-
'''
any = {1,2,2,3,4}
any.discard(5)
print(any)


























