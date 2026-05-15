'''
1.Program to convert 24 Hours clock into normal clock.
'''
time = input("Enter 24 hours time : ")
parts = time.split(":")
hour = int(parts[0])
print(parts[1])
min = int(parts[1])
convert = hour - 12
print(f"{time} is converted into {hour - 12}: {min} pm")

'''
1.List ---> List is a collection of different data type.
       ---> It is represented by []
       ---> It is mutable
Eg:-
'''
any = [1,"python",[1,2]]
print(any)

any = [1,"python",[1,2,[34,"This is python 3rd class",78],"python is a language",89],34,[3,4]]
print(any[2][2][1][8])
print(any[2][4])

'''
Methods
--------
A) Append() ---> This method is used to add new item into list, and it will in the last index position.
Syntax : variable_name.append(item)
'''
any = [1,2,3]
any.append(6)
print(any)
any.append([20,90])
print(any)

'''
2)String ---> Can able to modify on that particular variable
         ---> Is is immutable
         Eg:- int,str
Eg:-
'''
so = "python is a"
print(so.replace("python","java"))
print(so)

'''
B)Extend() ---> This method is used to add itterable into list, and it will in the last index position,each value or substring is each index in the list
Syntax : variable_name.extend(itterable)
Eg:-
'''
any = [1,2,3]
any.append([20,90])
print(any)
any.extend([20,90])
print(any)

'''
C)Pop() ---> It is used to remove the item from the list, but will mention here index position in the pop method
Syntax : variable_name.pop(index position)
Eg:-
'''
any = [1,2,3]
any.pop(1)
print(any)

'''
D)Remove() --->It is used to remove the item from the list, but will mention here direct in the remove method
Syntax : variable_name.remove()
Eg:-
'''
any = [1,2,3]
any.remove(2)
print(any)

so = ["python",90,"java"]
so.remove("python")
print(so)





























