#LISTs. & methods---//DAY-3//

#Acessing list items
list0 = ['apple', 'banana', 'kiwi', 'peach', 'pear', 'lemon']
print(len(list0))
print(list0[0])
print(list0[2:4])
print(list0[-1])

#List methods
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IPM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
ed = it_companies.pop(6)
print(it_companies)
ed = 'Youtube'
it_companies.append(ed) #adds value of ed into the list
print(it_companies)
it_companies.insert(4, 'Twitter') #inserts to index 4
print(it_companies)
it_companies[0].upper()
it_companies[3] = 'ITU'


joined_companies = '#;  '.join(it_companies)
print(joined_companies)


if 'Facebook' in it_companies: #checks for certain value in list
    print('Facebook is in the list')
else:
    print('Facebook is not in the list')

it_companies.sort( reverse=True) #sorts list alphabetically and if reverse is true then in reverse alphabetical
print(it_companies)

print(it_companies[3:])
print(it_companies[:3])
print(it_companies.remove('Google')) #removes item form the list
print(it_companies.clear())             #clears the list
print(it_companies)


#shows operations on list
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full = front_end + back_end #adds the items into one list
full_copy = full.copy()         #copies a l;ist and stores into a new list
print(full)
full_copy.extend(['Python', 'SQL'])     #extends the list 
print(full_copy)

#a program that acceses the list anfd then using conditions finds median
ages = [19, 22, 19, 24, 20, 25, 26, 24,31, 25, 24]
ages.sort()
print(ages)
min = ages[0]
max = ages[-1]
print(min)
print(max)
if len(ages) % 2 == 0:
  x = ages.pop(int(len(ages)/2 - 1))
  y = ages.pop(int(len(ages)/2))
  median = (x + y) / 2
  print(median)
else:
  y = ages.pop(int(len(ages)/2) + 1)
  print(y)
print(sum(ages)/len(ages))
range = max - min
print(range)