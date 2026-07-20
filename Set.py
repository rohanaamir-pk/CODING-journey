#SETs & methods---//DAY-5//

#set methods
from ast import Delete

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['TCS','Infosys'])
print(it_companies)
it_companies.remove('TCS')
print(it_companies)
it_companies.discard('TCS')
print(it_companies)
#set functions from math
print(A.union(B))       #combines both
print(A.intersection(B))    #only chooses common ones
A.issubset(B)                       #checks if B element belong to A
A.isdisjoint(B)
'''
A.update(B)
print(A)
B.update(A)
print(B)
'''
A.symmetric_difference(B)
del A       #deletes set
del B

age_set = set(age)
print(len(age))
print(len(age_set))
if len(age_set) > len(age):
  print(age_set)
else:
  print(age)

sentence = 'I am a teacher and I love to inspire and teach people.'
sentence_set = set(sentence.split())    #splits stirng into set elements
print(sentence_set)