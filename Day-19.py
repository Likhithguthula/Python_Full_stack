'''
Polymorphism ---> This means 'many forms'.. it allows the same function, method, or operator
                  to behave differently depending on the object...
1)Method overloading ---> It means defining multiple methods with the same name but different parameters.
Eg:-
'''
class calc:
    def add(self,a,b,c=0):
        return a + b + c
An = calc()
print(An.add(23,6))
print(An.add(23,6,34))

class calc:
    def add(self,a,b):
        return a + b
    def add(self,a,b,c = 0):
        return a + b + c
An = calc()
print(An.add(23,6))
print(An.add(23,6,34))

class calc:
    def add(self,*num):
        return sum(num)
    def add(self,*num):
        return sum(num)
An = calc()
print(An.add(23,6))
print(An.add(23,6,34))

'''
2)Method overriding ---> This occurs when a child class provides its own implemention of a method
                         already defined in the parent class...
Eg:-
'''
class animal:
    def sound(self):
        print("Animal makes sound")
class dog(animal):
    def sound(self):
        print("Dog barks")
ntg = dog()
ntg.sound()

class animal:
    def sound(self):
        print("Animal makes sound")
class dog(animal):
    def sound(self):
        super().sound()
        print("Dog barks")
ntg = dog()
ntg.sound()

'''
3)Operator overloading ---> This allows operators such as +,-,* etc., to perform different actions
                            for user-defined objects.
Note : The operator inside the method will overload a special method or operator given in the call.
Eg:-
'''
class stu:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks + other.marks
so_1 = stu(4)
so = stu(78)
print(so_1 + so)

class stu:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks * other.marks
so_1 = stu(4)
so = stu(78)
print(so_1 + so)

'''
Data Abstraction ---> This is the process of hiding internal implementation details and
                      showing only essential features to the user.
                 ---> It focuses on what an object does rather than how it does it...
Eg:-
'''

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rec(shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b
    def perimeters(self):
        return 2*(self.a * self.b)
an = Rec(10,5)
print(an.area())



















