#FUNCTION-II(lambda, decorators, map, filter)---//DAY-11//

from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#Use map to create a new list by changing each country to uppercase in the countries list
def country_upper(abc):
    return abc.upper()
listofcountry = map(country_upper, countries)
print(list(listofcountry))


#Use map to create a new list by changing each number to its square in the numbers list
num = map(lambda x: x*x , numbers)
print(list(num))


#Use filter to filter out countries containing 'land'.
country = filter(lambda x: 'land' in x, countries)
print(list(country))


#Use filter to filter out countries having exactly six characters.
country = filter(lambda x: len(x)==6, countries)
print(list(country))


#Use filter to filter out countries starting with an 'E'
country = filter(lambda x: x[0]=='E', countries)
print(list(country))

#Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
marks = [123 , 213 , 172, 197]
def add_two_nums(x, y):
    return int(x) + int(y)
pass_std = reduce(add_two_nums, list(filter(lambda z: z%2==0 , list(map(lambda x: x*10, marks)))))
print(pass_std)

#Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
mix_list = ['ear', 12, 'toe', 9.8, False, 'eyes', 'foot']
srt_list = filter(lambda x: isinstance(x, str), mix_list )
print(list(srt_list))

#Use reduce to concatenate all the countries and to produce 
# this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def sentence(func):
    def wrapper(*args, **kargs):
        result = func(*args, **kargs)
        return result + ' are north European countries.'
    return wrapper

def concatenate(x, y):
    return x + ', ' + y

@sentence
def show(xyz):
    comb = reduce(concatenate , xyz)
    return comb
    
print(show(countries))