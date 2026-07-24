#PACKING & UN-PACKING---//DAY-13//

#unpacking list into a function as an argument
def mult_lsts(a, b, c, d, e):
    lst = a * b * c * d * e
    return lst
lst_1 = [2, 4, 1, 11, 3]
print(mult_lsts(*lst_1))

numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) 
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(list(numbers))      

#Packing items into function parameters
def mult_lsts(*args):
    P = 1
    for num in args:
        P *= num
    return P
print(mult_lsts(3, 4, 9, 11, 3))     



def unpacking_person_info(name, country, city, age, grade):
    return f'{name} lives in {country}, {city}. \n He is {age} year old. and his grade is {grade}.'
dct = {
        'name' : 'Rohan',
        'country' : 'Pakistan', 
        'city' : 'Lahore', 
        'age' : 25,
        'grade' : 'A'
        }
print(unpacking_person_info(**dct)) 


#unpacks dictionary as Argument and parameter then asks if modification is needed
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
        Choice = str(input('Do you want to change this (Y/N):'))
        if Choice.upper() == 'Y':
            kwargs[key]=input("Enter new value: ")
            print(f'New data is: \n\t {key} --> {kwargs[key]}\n\n')
        else:
            print(f'data is: \n\t {key} --> {kwargs[key]}\n\n')
    
dict = { 'name':"Asabeneh", 'country' :"Finland", 'city' :"Helsinki", 'age':250}
print(packing_person_info(**dict))


#multiplying two lists using indexing 
lst = []
lst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range(0, 10):
    lst.append(lst_1[i]*lst_2[i])
print(lst)
#multiplying two lists using zip 
lst = []
lst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i, j in zip(lst_1, lst_2):
    lst.append(i*j)
print(lst)

#somewhat similar to linear search using enumerate
status = True
numbers = [1, 2, 3, 12, 23, 12, 11, 87, 45, 32, 111, 98, 43]
target = int(input('enter number to find: '))
for index, i in enumerate(numbers):
    if i == target:
        print(f'The number {i} has been found at index {index}')
        status = True
        break
    status = False

if status == False:
    print("number not found")