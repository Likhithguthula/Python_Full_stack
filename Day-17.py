'''
OOPS
-----
1)Class ---> A class is a blue print or a template used to create object.
Eg:-

2)Object --> An object is an instance of a class.
Eg:-
'''
class stu:
    name = 'ABCD'
s1 = stu()
print(s1.name)

class stu:
    def edu(self):
        print("I am studying B.Tech")
    def sports(self):
        print("Cricket")
        print("Vall")
s1 = stu()
s1.edu()
s1.sports()

'''
3)Attributes ---> Attributes are the variables that belongs to a class or an object
Eg:-
'''
class stu:
    name = 'ABCD'
    age = 55
s1 = stu()
print(s1.name)
print(s1.age)

'''
4)Methods ---> The functions defined inside the class is methods
Eg:-
'''
class PFS_DA:
    def python(self):
        PFS_DA = 'Batch_03'
        print('This PFS and DA Batch03')
        
    def Flask(self):
        PFS = 'Batch_03'
        print('This PFS Batch03')
all = PFS_DA()
all.python()
all.Flask()

'''
5)Constructor(__init__) ---> A constructor is a special method that is automatically called when an object is created.
Eg:-
'''
class ATM:
    def __init__(self,Balance,name):
        self.Balance = Balance
        self.name = name
    def Bal_check(self):
        print(f"{self.name} your total balance is {self.Balance + 700}")
    def name_(self):
        print(self.name)
card = ATM(Balance = 50000,name = 'ABCD')
card.Bal_check()
card.name_()

'''
A)Public ---> This can be accessed from anywhere in the program
B)Protected ---> This is represented using a single underscore(_)
C)Private ---> This is represented using a double underscore(__)
Eg:-
'''
class stu:
    __name = 'ABCD'
s1 = stu()
print(s1._stu__name)

'''
6)Encapsulation ---> Is the process of binding data and methods together.
Eg:-
'''
class Bank:
    def __init__(self,balance):
        self.__balance = balance
    def depo_(self,amount):
        self.__balance += amount
    def get_bala(self):
        return self.__balance
acc = Bank(1000)
acc.depo_(10000)
print(acc.get_bala())










