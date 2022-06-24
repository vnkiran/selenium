#Q0
for i in range(1,11):
        if i % 2 == 0:
            print(i,".........even")
            #continue
        if i % 3 == 0  and i%2 !=0:
            print(i,"odd")
            #continue
        elif i % 2 !=0 and i % 3 !=0:
            print(i,"+++prime")
list1 = [1,2,3,4,5,6,7,8,9,10]
even = [x for x in list1 if (x%2) ==0]
print("Even Numbers :",even)
odd = [y for y in list1 if (y%3) ==0 and (y%2) !=0]
print("Odd Numbers :",odd)
prime = [z for z in list1 if (z%2) !=0 and (z%3) !=0]
print("Prime Numbers :",prime)
'''#Q1
n = "kiran"
p = "noon"
if(n==n[::-1]):
    print("Yes this is palindrome")
else:
    print("no")
if(p==p[::-1]):
    print("Yes this is palindrome")
else:
    print("no")
'''
'''#Q2
names = []
number = []
li = [1,2,3,"a","b",22,"nn"]
for i in li:
    if type(i)==str:

        names.append(i)
    if type(i)==int:
        number.append(i)
print(names, "----", number) '''
list3=[1,2,3,4,"aa","bb","ccc",5,6,"dd",10,"kiran"]
a =[]
b=[]
for i in list3:
    if type(i)==str:
        a.append(i)
    if type(i)==int:
        b.append(i)
print("Srtings :", a,"Numbers :", b)





