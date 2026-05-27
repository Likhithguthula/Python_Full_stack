'''
Fibbonic Series
Eg:-
'''
num = 0
num_2 = 1
def finaaci(num,num_2):
    limit = int(input("Enter the limit: "))
    print(num,num_2,end = " ")
    for i in range(1,limit):
        num_3 = num + num_2
        num = num_2
        num_2 = num_3
        print(num_3,end = " ")
finaaci(num,num_2)
'''
Remove Duplicates values
Eg:-
'''
any = [2,5,7,9,2,7]
new = []
def Dup(any,new):
    for j in any:
        if j not in new:
            new.append(j)
    print(new)
Dup(any,new)

'''
counting the paragraph words
Eg:-
'''
so ="Python is one of the world's most popular, high-level computer programming languages.".split()
def word_str(so,count):
    for j in so:
        count += 1
    print(count)
word_str(so,count)
    

        
                
    
        









































