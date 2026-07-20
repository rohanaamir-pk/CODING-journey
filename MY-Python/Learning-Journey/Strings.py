#STRINGS & Methods---//DAY-2//

#Concatenation of strings using variables
a = 'Thirty'
b = 'Days'
c = 'Of'
d = 'Python'
e = a + b + c + d
print(e)

#String methods
company = 'Coding For All'
print(company)
print(len(company))         #lenght of string
print(company.lower())    #turns sting to lower case
print(company.upper())      #turns to uppercase
print(company.capitalize()+'\n'+company.title() ) #used to format it in a heading like way 
print(company[7:])      #string slicing
print(company.replace('Coding','Python'))  #replaces  the word Coding with Python
print(company.split(" "))   #detects s[paces in string then on its basis creates a list of the string]
print(company.index('C'))   #returns inde of character 
print(company.index(company[-1])) #returns last index number
print(company.find('Coding')) #finds first occurence of the word
print(company.rfind('Coding'))   #finds last occurence in string
print(company[0])
print(company.rfind('l'))

name = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(name.split(', '))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))
print(sentence.replace(' because because', ""))

#joins the list with # in btw
library = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
library='#'.join(library)
print(library)

#format specifier
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle of radiius {radius} is {area}')