'''
Q1 :
Write a program to generate a dictionary that contains (i,i*i) such that is an integral no
between 1 & n (both included).Suppose the following input is supplied to the program
input - 8
then the output should be:
{1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64}
'''
n = int(input("enter a number:"))
d = {}
for i in range(1,n+1):
    d[i] = i*i
    #print(d)

'''
Q2 :
u have a record of N students. Each record contains the students name and their % in 
Maths,Physics and Chemistry. the marks can be floating values.THe user enter N ......

Sample Input :
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output:
56.00
'''
#Challenge-1 : Store marks with respect to name
#ch -2: Find the average
#CH -3 : RETURN THE OUTPUT ACCORDING TO USER INPUT AS FLOAT ROUND 2

# Solution:
n = int(input("enter no of stdnts"))
marksheet = {}

for i in range(n):
    name,*marks = input("enter name & score :").split()
    scores=list(map(float,marks))
    marksheet[name] = scores

student = input("enter student name")
scores = marksheet[student]
avg = sum(scores)/len(scores)

#print(avg)
'''
Take Two lists, say for example these two:
a= [1,1,2,3,5,8,13,21,34,55,89]
b= [1,2,3,4,5,6,7,8,9,10,11,12,13]
and write a program that return a list that contains only the elements 
that common between the list(without duplicate).
make sure your program works on two lists
'''
a= [1,1,2,3,5,8,13,21,34,55,89]
b= [1,2,3,4,5,6,7,8,9,10,11,12,13

l = []

for i in a:
    if i in b:
        if i not in l:
            l.append(i)

print(l)



