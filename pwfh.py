'''input_string = "hello how are you"
print(input_string)

# reverse each word of the sentence
# example output: olleh woh era uoy

a = input_string[0:5]
b = input_string[6:9]
c= input_string[10:13]
d= input_string[13:]
print(a[::-1],b[::-1],c[::-1],d[::-1])
#e=a,b,c,d
#print(e[::-1])
#input string sentence
#------------------------------------------------------------------------------------------------

x = input("Enter Sentence :")
#print(x)
word = x.split()
#print(word)
revers = []
for i in word:
    revers.append(i[::-1])
#print(revers)
result = ' '.join(revers)
print(result)
#split the string sentence
#reverse each word of the sentence
#join the words
#---------------------------------------------------------------------------------------------------


revers_each_word = input("Enter any Sentence i can show the each word reversed...:")
word = revers_each_word.split()
#print(word)
empty_list = []
count = 0
for i in word:
    empty_list.append(i[::-1])
result = ' '.join(empty_list)
print(result)


for i in word:
    words = i.split()
    count += len(words)
print(count)
# print dictionary containing word, length of the word as key/value pair
# example output: {'hello': 5, 'how': 3, 'are': 3, 'you': 3}
dictionary = {'hello': 5, 'how': 3, 'are': 3, 'you': 3}
print(dictionary)
for key,value in dictionary.items():
    print(len(key))

'''
#print(len(dictionary)

# modify the code below to print second highest of all 'number' values
#qfor i in range(0,5):
#number = int(input("Enter a number: "))

#print(number)

b = "kiran kumar geddi...! hello how are you"
word = b.split()
empty = []
for i in word:
    empty.append(i[::-1])
    out = ' '.join(empty)
print(out)
#    print(word)
1


