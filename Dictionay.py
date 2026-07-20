

#simpole dictioary
dog = {
    'name':'bug',
    'color':'balck',
    'breed':'german'

}
print(dog['name']  ) #access dictioanery item using its defined key

#dictioanary methods
student = {
    'first_name':'ahmed',
    'last_name':'mohamed',
    'gender':'male',
    'age':29,
    'skills':['coder','baker','killer'],
    'martial status':'Married',
    'country':'Pakistan',
    'city':'Karachi',
    'address':'14th street'
}
print(len(student))
print(student['skills'])
print(type(student['skills']))      #type of value stored in the key
student['skills'].extend(['fighting','jogging'])  #applying the methods of the data type via key
print(student['skills'])
dk = student.keys() #gives list of all the keys
dv = student.values() #list of all values
print(dk)
print(dv)
print(student.items())
del student['address']
print(student)
student.clear()         #empties dictionary
print(student)