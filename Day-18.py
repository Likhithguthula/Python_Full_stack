'''
Inheritance ---> This allows one class to aquire the properties and methods of another class....
Types
------
1)Single Inheritance ---> A class inherts from a single parent class...(Parent ---> Child)
Eg:-
'''
class father:
    def Land(self):
        print("I am father have 5A")
class ABCD(father):
    def my_own(self):
        print('i have 2A')
fam = ABCD()
fam.Land()

'''
2)Multiple Inheritance ---> (Father,Mother ---> Child) A child class inherts from more than two parent classes.
Eg:-
'''
class father:
    def Land(self):
        print("I am father have 5A")
class mother:
    def gold(self):
        print("My mother have 1kg G")
class son(father,mother):
    def mine(self):
        print('i have ntg')
all = son()
all.Land()
all.gold()

'''
3)Multi_level Inheritance ---> A class inherits from a parent class and another class inherits from that child class.
                                (Grandfather ---> Father ---> Child)
Eg:-
'''
class grandfather:
    def land(self):
        print("My grandfather have 5A of land")
class father(grandfather):
    def flat(self):
        print("Have flat at BNG")
class son(father):
    def Ntg(self):
        print("I own both of their properties")
all = son()
all.land()
all.flat()
all.Ntg()

'''
4)Hierachical Inheritance ---> Multiple child classes inherits from a single parent...
Eg:-
'''
class father():
    def Land(self):
        print("10 A land")
class ABCD(father):
    def mine(self):
        print("Job")
class EFGH(father):
    def bro(self):
        print("Jobless")
EF = EFGH()
EF.Land()
so = ABCD()
so.Land()
        
'''
5)Hybride Inheritance ---> This is the combination of two or more types of inheritance.
Eg:-
'''
class A:
    def some(self):
        print('Class A')
class B:
    def any(self):
        print('Class B')
class C(A):
    def so(self):
        print('Class C')
class D(B,C):
    def All(self):
        print('Class D')
how = D()
how.so()

'''
Super() Method
---------------
Super() ---> Is used to access methods and constructor of the parent of the parent class from the child class
Eg:-
'''
class parent:
    def display(self):
        print('Method Parent')
class child(parent):
    def display(self):
        super().display()
        print('Method Child')
any = child()
any.display()

class Person:
    def __init__(self,name):
        self.name = name
class stu(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def show(self):
        print(f"Name : {self.name}")
        print(f"Roll No : {self.roll}")
any = stu('ABCD',111)
any.show()





































