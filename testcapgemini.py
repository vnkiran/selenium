list =[41,42,1,2,3,4,5,66,7]
list.remove(max(list))
#print(list)
print(max(list))
#
#print(max(list)) #find max number of list
'''list.sort()
print(list[-2])'''
#print max second number in list|


#print even and odd number in list coprehensive
list = [1,2,3,4,5,6,7,8,9,10]

list_even = [i for i in list if (i % 2)==0]
print(list_even)

odd = [i for i in list if (i % 2) !=0]
print(odd)


for i in list:
    if i % 2 ==0:
        print(i,"Even Number")
    if i % 2 !=0:
        print(i,"------Odd number")


