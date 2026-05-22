##for i in range(1,10):
##    for j in range(1,2):
##        print(j)

'''
Multiplication Table
---------------------
'''
##num = 9
##for j in range(1,11):
##    print(f"{num} x {j} = {j*num}")

'''
Palindrone
-----------
'''
##so = input("Enter a word: ")
##empty_str = ""
##for j in so:
##    empty_str = j + empty_str
##    print(empty_str)
##if empty_str == so:
##    print(f"{so} is palindrome")
##else:
##    print(f"{so} is not a palindrone")

'''
Amstrong number
----------------
'''
##num = int(input("Enter a amstrong number: "))
##amstro = 0
##length = len(str(num))
##for i in str(num):
##    amstro += int(i) ** length
##if amstro == num:
##    print(f"{num} is a amstrong number")
##else:
##    print(f"{num} is not a amstrong number")

'''
Perfect Number
---------------
'''
##num = int(input("Enter a perfect number: "))
##perfect_number = 0
##for j in range(1,num):
##    if num % j == 0:
##        perfect_number += j
##if perfect_number == num:
##    print(f"{num} is a perfect number")
##else:
##    print(f"{num} is a not perfect number")

'''
Prime Numbers
--------------
'''
##num = int(input("Enter the Number: "))
##count = 0
##for k in range(1,num+1):
##    if num % k == 0:
##        count += 1
##if count == 2:
##     print(f"{num} is a prime number")
##else:
##    print(f"{num} is a not prime number")

'''
Star
-----
'''
##star = 5
##for g in range(1,star +1):
##    for d in range(1,g+1):
##        print("*", end = "")
##    print()

##star = 5
##count = 0
##for g in range(1,star +1):
##    for d in range(1,g+1):
##        count += 1
##        print(count, end = " ")
##    print()
##
##star = 5
##count = 0
##for g in range(1,star +1):
##    for d in range(1,g+1):
##        count += 1
##        print(d, end = " ")
##    print()

##star = 5
##for g in range(1,star +1):
##    for d in range(1,g+1):
##        print(chr(64+d), end = " ")
##    print()

'''
Triagle
-------
'''
num = 5
for j in range(1,num+1):
    print(" " *(num-j), end = "")
    for i in range(1,j+1):
        print("*",end = " ")
    print()

num = 5
for j in range(1,num+1):
    print(" " *(num-j), end = "")
    for i in range(1,j+1):
        print(chr(64+i),end = " ")
    print()






































