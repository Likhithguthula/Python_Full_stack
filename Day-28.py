'''
Matplotlib
-----------
---> This is a library in python for data visualization, allowing users
     to create a variety of plots...
Basic Structure of Matplotlib
------------------------------
1)Figure
2)Axes
3)Grid
4)Title
5)Legend
'''
import matplotlib.pyplot as plt
Sales = ['A','B','C']
Values = [25,30,45]
plt.bar(Sales,Values)
plt.show()

import matplotlib.pyplot as plt
Sales = ['A','B','C']
Values = [25,30,45]
plt.bar(Sales,Values)
plt.xlabel('Car Model')
plt.ylabel('Values')
plt.title('BMW sales')
plt.show()

import matplotlib.pyplot as plt
Sales = ['A','B','C']
Values = [25,30,45]
plt.bar(Sales,Values, color = 'red', edgecolor = 'black')
plt.xlabel('Car Model')
plt.ylabel('Values')
plt.title('BMW sales')
plt.show()

import matplotlib.pyplot as plt
overs = [1,2,3,4,5]
score = [4,9,17,20,8]
plt.plot(overs,score, color = 'yellow')
plt.xlabel('overs')
plt.ylabel('score')
plt.title('score card')
plt.show()

import matplotlib.pyplot as plt
subjects = ['Python','Java','C']
students = [35,7,15]
plt.pie(students,labels = subjects)
plt.title('Students in Courses')
plt.show()

import matplotlib.pyplot as plt
subjects = ['Python','Java','C']
students = [35,7,15]
plt.pie(students,labels = subjects)
plt.legend(subjects)
plt.title('Students in Courses')
plt.show()

import matplotlib.pyplot as plt
subjects = ['Python','Java','C']
students = [35,7,15]
plt.pie(students,labels = subjects, autopct = '%1.1f%%')
plt.legend(subjects)
plt.title('Students in Courses')
plt.show()

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,15,18,20,13]

plt.scatter(x,y)
plt.title('Scatter plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()

import matplotlib.pyplot as plt
y = [10,15,18,20,13]

plt.hist(y)
plt.title('Histogram plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()
