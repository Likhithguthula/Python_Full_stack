'''
Error Handling
---------------
1)Try block ---> The try block, test a block of code for error
2)Except block ---> The except block let hand if the code contain errors...
Ex:-
'''
try:
    print(10/0)
except:
    print('This will handle zeroDivisionError')

try:
    print(Hai)
except:
    print('This is not a python')

'''
3)Else block ---> This will be executed, if the try block has no error in the code...
Ex:-
'''
try:
    print("ANy")
except:
    print('This will handle NameError')
else:
    print("No error")

'''try:
    print(5+"Py")
except NameError:
    print('This will handle NameError')
else:
    print("No error")'''

try:
    print(a)
    print(5+"Py")
except TypeError:
    print('This will handle TypeError')
except NameError:
    print('This will handle NameError')
else:
    print("No error")

'''
4)Finally block ---> This will be excuted eithe try block contain error or not...
Ex:-
'''
try:
    print("Hai")
except:
    print("Error")
else:
    print("no error")
finally:
    print('The end')











