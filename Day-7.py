'''
Condition Statements
---------------------
Ex:-
1)If
2)Nested if
3)Elif
'''
'''
1)If ---> To check the statement is True or False
Eg:-
'''
num = 5
if num % 2 == 0:
    print("Even")
else:
    print("odd")

'''
2)If-Else ---> Else in the if statement, incase the condition becomes false then it will enter into fall-back (else), it will execute whatever inside it
Eg:-
'''
# Finding the Even or Odd number
num = 9
if num % 2 == 0:
    print(f"{num} is a even number")
else:
    print(f"{num} is a odd number")

# Finding the Even or Odd number
num = 4
if num % 2 != 0:
    print(f"{num} is a odd number")
else:
    print(f"{num} is a even number")

# Finding the age limit
age = 16
if age >= 18:
    print("We are eligible to vote")
else:
    print(f"we have to wait for {18-age} more years")

#Finding Greater Number
num_1 = 4
num_2 = 15
if num_1 >= num_2:
    print(f"{num_1} is greater number than {num_2}")
else:
    print(f"{num_2} is greater number than {num_1}")

# Finding the leap year
year = 2000
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

for i in range(2000, 2030):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        print(f"{i} is a leap year")
    else:
        print(f"{i} is not a leap year")







































