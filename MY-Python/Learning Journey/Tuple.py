#TUPLEs & methods---//DAY-4//

#tuple editing and methods
brothers = ('him', 'his', 'he')
sisters = ('her', 'she')
siblings = brothers + sisters       #adds both tuples into one
print(siblings)
print(len(siblings))
list_siblings = list(siblings)          #tuple cant be editted so change it into a list
list_siblings.append('Mother')
list_siblings.append('Father')
family = tuple(list_siblings)       #back to tuple
print(family)
m = 1
for i in family:
  print(str(m)+')' , end='')
  print(i)
  m+=1

#tuple access
  fruits = ('apple', 'lemon', 'kiwi')
vegetables = ('cabbage', 'potato', 'lettuce')
seafood = ('fish', 'prawn', 'squid')
food_stuff_tp = fruits + vegetables + seafood
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt[int(len(food_stuff_lt)/2)])
print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])
del food_stuff_tp

#checking item s in tuples
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print( 'Iceland' in nordic_countries)