'''
Elif
-----
Eg:-
'''
stu_marks = 56
if stu_marks >= 90:
    print("A+")
elif stu_marks >= 80:
    print("A")
elif stu_marks >= 70:
    print("B+")
elif stu_marks >= 60:
    print("B")
elif stu_marks >= 50:
    print("C+")
elif stu_marks >= 35:
    print("Pass")
else:
    print("Failed")

a = 8
b = 5
c = 90
if a > (b and c):
    print(a)
elif b > (a and c):
    print(b)
else:
    print(c)

a = 8
b = 5
c = 90
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

'''
Nested If
----------
ATM PIN
--------
'''
#SBI_Bank = {"ATM PIN" : "6600"}
#pin = input("Enter 4 digit ATM pin: ")
#if len(pin) == 4:
#    if pin in SBI_Bank['ATM PIN']:
#       print("Wel come to SBI ATM")
#    else:
#        print("Invalid pin")
#else:
#    print("Please enter 4 digit pin")

'''
Statements
-----------
1)For Loop ---> Used to itterate over a sequence
Eg:-
'''
any = "Python"
an = [1,2,3,4]
so = (5,6,7,8)
for j in any:
    print(j)

'''
A)Range() ---> It is a buit in function used to generate numbers inn squance manner
Syntax : range(start,end,step)
B)Else in for ---> once the itteration completed this else will be
C)Break ---> used to exit from the loop based on the condition
D)Continue ---> used to skip the current itteration base on the condition
E)Pass ---> used to give the spaces
Eg:-
'''
for i in range(1,10):
    print(i)
else:
    print("code Entered here")

for i in range(1,10):
    print(i)
    if i == 5:
        break

for i in range(1,10):
    if i == 5:
        continue
    print(i)
        
for i in range(1,10):
    if i == 5:
        pass

'''
2)While ---> It is a combination of for + if
Eg:-
'''
i = 1
while i < 5:
    print(i)
    i += 1














































