#Condition Statements---//DAY-6//

#simple if-else conditon to check age
age = int(input('Enter age:'))
if age >= 18 :
  print('your old enough')
else:
  print(f'you must wait {18 - age} years to drive')

#nested if's
my_age = int(input('Enter age:'))
ur_age = int(input('Enter age:'))
if my_age != ur_age :
  if my_age > ur_age :
    if (my_age - ur_age) > 1:
      print(f'I am years older')
    else:
      print(f'I am a year older')

  if ur_age> my_age :
    if (ur_age - my_age) > 1:
      print(f'you are years older')
    else:
      print(f'you are a year older')
else:
  print('we are same age')

#if-else-if
n1 =int(input('enter 1st number:'))
n2 = int(input('enter 2nd number:'))
if n1 > n2 :
  print(f'{n1} is greater than {n2}')
elif n2 > n1 :
  print(f'  {n2} is greater than {n1}')
else:
  print(f'{n1} and {n2} are equal')

#A little bigger use
  person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
  print(person['skills'][int((len(person['skills']))/2)])

  skills = person['skills'] # Assign to a local variable for cleaner code

  # Changed elif to if to print all applicable roles
  if 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print('He is a fullstack developer')
  if 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print('He is a backend developer')
  if 'JavaScript' in skills and 'React' in skills:
    print('He is a front end developer')
  # No 'else' here, as we want to check all conditions. If none match, nothing specific is printed.
  # If you wanted to print 'unknown title' only if NO roles matched, additional logic would be needed.
else:
    print('unknown title')


if 'is_married' in person and person['is_married'] == True:
  if person['country'] == 'Finland':
    print(f'{person["first_name"]} {person["last_name"]} lives in Finland. He is married')