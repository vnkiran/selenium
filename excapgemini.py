#Interviewer expected result
list = [1,33,55,77,1,44,99,100]
#print(max(list)) # max value
list.remove(max(list))
print(max(list))# max second value

list.pop(-1)
print(max(list))

list1 = [1,2,3,4,5,6,7,8,9,10]#print even and odd number using list compprehensive

even = [i for i in list1 if (i%2)==0]
print("Even Numbers :",even)
odd = [i for i in list1 if (i%2)!=0]
print("Odd Numbers :", odd)
