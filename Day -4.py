'''
D)Concatination --> The (+) for int and can, but for the other data types it will act as concatinating the data type
Eg:-
'''
a = 90
b = 8
print(a+b)
any = "python "
so = "Is a language"
print(any + so)
an = [1,2]
am = [3,4]
print(an + am)

'''
3)Tuple ---> collection of different data types seperated by commas, represented in ()
        ---> It is immutable
Methods
--------
E)Count() ---> This is used to count the particular item in the tuple
Syntax : variable_name.count(item)
Eg:-
'''
some = (1,"python",[1,2],(3,4),"python")
print(some.count("python"))

'''
F)Index() ---> Used to find out the index position of the item, and only gives the first occurance
Eg:-
'''
some = (1,[1,2],(3,4),"python")
print(some.index("python"))

any = [1,"python",[1,2,[34,"This is python 3rd class",78],"python is a language",89],34,[3,4]]
print(any[2][2][1][8])
print(any[2][4])

'''
4)Dictionary ---> Dict is a key : value pair, key and value is seperated by : and pair is seperated by comma
             ---> Represented by {}
Eg:-
'''
teja_details = {"Name" : "Teja",1:2,(1,2) : [3,4]}
print(teja_details)

teja_details = {"Name" : "Teja", "age" : 45, "Mob" : "1123456789", "pan" : "GPCM1A42"}
print(teja_details.keys())

'''
G)Values() ---> Used to get all values from the dict
Syntax : dict.values()
Eg:-
'''
teja_details = {"Name" : "Teja", "age" : 45, "Mob" : "1123456789", "pan" : "GPCM1A42"}
print(teja_details.values())

'''
H)Items() ---> Used to get key and values together
Syntax : dict.items()
Eg:-
'''
teja_details = {"Name" : "Teja", "age" : 45, "Mob" : "1123456789", "pan" : "GPCM1A42"}
print(teja_details.items())

details = {"Name" : "Python"}
print(details.keys())
print(details["Name"])

'''
I)Update() ---> Used to add a key : value pair into dict
Syntax : dict.update{key:value})
Eg:-
'''
teja_details.update({"Aadhar" : "123456789123"})
print(teja_details)

'''
J)Clear() ---> Used to remove all the items in the dict
Eg:-
'''
teja_details = {"Name" : "Teja", "age" : 45, "Mob" : "1123456789", "pan" : "GPCM1A42"}
teja_details.clear()
print(teja_details)

































