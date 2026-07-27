#REGULAR EXPRESSIONS---//DAY-14//
import re
from collections import Counter
#re.match only checks string in the begining if the index 0 is different it will give []'None']
txt = 'It is a New WORLD'
match = re.match('it is a' ,txt ,re.I) #re.I is short for re.IGNORECASE, it makes small and capital letters same it = It
print(match)
print(match.group())
print('Index' + str(match.span()))

#re.search checks entire string and returns index of the first occurence found in it
txt = '''I need to learn everything, the more I learn the better I become and the end.'''
search = re.search('learn', txt, re.I) 
print(search)
print(search.group())
print('Index: ' + str(search.span()))

#re.findall checks entire string and returns index of the every occurence found in it
txt = '''I need to learn everything, the more I learn the better I become and the end.'''
findall = re.findall('the', txt, re.I) 
print(findall)


#re.sub replaces the occurence of the string with the new string
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
sub = re.sub('%','', txt)
print(sub)

#re.split text into different items of a list
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split(' ',  txt)) # splitting using space - end of line symbol
print(re.split('\n',  txt)) # splitting using \n - end of line symbol

#counting the frequency of each word in a give string.
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
all_words = re.findall(r'\w+', paragraph.lower())
print(list(all_words))
word_count = Counter(all_words)
most_common  = word_count.most_common()
print(most_common)

#extracts cordinates and then uses them to calculete max distance
text = """The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."""
numbers = re.findall(r'-?\d+', text)
numbers = list(map(int, numbers))
distance = max(numbers) - min(numbers)
print("Positions:", numbers)
print("Furthest distance:", distance)

#checks if variable name is allowed or not
pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
n = str(input('enter a variable name:'))
if re.match(pattern, n):
        print(n, "is valid")
else:
        print(n, "is invalid")