#FILE HANDLING---//DAY-15//

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
f = open(r"C:\Users\rohan\Documents\github-projects\MY-Python\Learning-Journey\File-Handling\Files\reading_file_example.txt",'a')
"print(f.read())" #display all the stuff from the file
"print(f.read(15))" #specifies how much to display of the string from the file
"print(f.readlines())" #reads all lines from the file and outputs them in a list
"f.write('\nThis is a new line added through write.') "#writes a new line to the file
f.close()
with open(r"C:\Users\rohan\Documents\github-projects\MY-Python\Learning-Journey\File-Handling\Files\writing_file_example.txt",'w') as f: #file is created if it does not exist and opened in write mode
    f.write('This text will be written in a newly created file') #writes text to the file 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from fileinput import filename
import json
import re

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
with open(r"C:\Users\rohan\Documents\github-projects\MY-Python\Learning-Journey\File-Handling\Files\json_example.json",'r') as f:
    data = json.load(f) #loads the json file into a python dictionary
'''for key, value in data.items(): #data.items() returns a list of tuples containing key-value pairs from the dictionary
    print(key, ":", value)
    print(type(value)) #prints the type of the value in the dictionary'''
data['hobbies']= ['reading', 'writing', 'coding'] #adds a new key-value pair to the dictionary

with open(r"C:\Users\rohan\Documents\github-projects\MY-Python\Learning-Journey\File-Handling\Files\json_example.json",'w') as f:
    json.dump(data, f, indent=4) #writes the updated dictionary back to the json file

additional = {
    "degree": "AI",
    "university": "MIT",
    "year": 2024
}
for key, value in additional.items():
    data[key] = value #adds the key-value pairs from the additional dictionary to the data dictionary
with open(r"C:\Users\rohan\Documents\github-projects\MY-Python\Learning-Journey\File-Handling\Files\json_example.json",'w') as f:
    json.dump(data, f, indent=4) #writes the updated dictionary back to the json file
f.close()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from collections import Counter
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#returns the most spoken languages in the world
def most_spoken_language(filename = r"C:\Users\rohan\Documents\github-projects\MY-Python\Learning-Journey\File-Handling\Files\countries_data.json", num=5):
    language_count = Counter()
    with open(filename, 'r', encoding = 'utf-8') as f:
        data = json.load(f)
        for country in data:
            languages = country.get('languages', [])
            language_count.update(languages)
    return language_count.most_common(num)
print(json.dumps(most_spoken_language(filename = r"C:\Users\rohan\Documents\github-projects\MY-Python\Learning-Journey\File-Handling\Files\countries_data.json", num = 5), indent = 4))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#return the most populated countries in the world
def most_populated(filename = r"C:\Users\rohan\Documents\github-projects\MY-Python\Learning-Journey\File-Handling\Files\countries_data.json", num=5):
    with open(filename, 'r', encoding = 'utf-8') as f:
        data = json.load(f)
        countrie = []
        for country in data:
            countrie.append((country['name'], country['population']))
    countrie.sort(key=lambda x: x[1], reverse=True)

    return countrie[:num]
print(json.dumps(most_populated(filename = r"C:\Users\rohan\Documents\github-projects\MY-Python\Learning-Journey\File-Handling\Files\countries_data.json", num = 5), indent = 4))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#finds all the email addresses in a text file using regex
with open(r"C:\Users\rohan\Documents\github-projects\MY-Python\Learning-Journey\File-Handling\Files\email_exchanges.txt",'r', encoding = 'utf-8') as f:
    text = f.read()
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text) #regex pattern to find email addresses in the text
    print(emails)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#finds all the commonly used words in a text file using regex
with open(r"C:\Users\rohan\Documents\github-projects\MY-Python\Learning-Journey\File-Handling\Files\michelle_obama_speech.txt",'r', encoding = 'utf-8') as f:
    text = f.read()
    words = re.findall(r'\w+', text.lower()) #regex pattern to find all words in the text and convert them to lowercase
    word_count = Counter(words) #counts the frequency of each word in the text
    most_common_words = word_count.most_common(10) #returns the 10 most common words in the text
    print(most_common_words)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||X[PROGRAM]X|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||]
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#a flow to check the similarity between two texts using regex
def clean_text(text):
    #removes all the special characters from the text using regex
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return cleaned_text

def remove_supporting_words(cleaned_text, stop_words):
    #removes all the supporting words from the cleaned text using regex)
    filtered_words = []
    for word in cleaned_text:
        if word not in stop_words:
            filtered_words.append(word)
    return filtered_words

def check_text_similarity(text1, text2):
    #checks the similarity between two texts using regex
    cleaned_text1 = clean_text(text1)
    cleaned_text2 = clean_text(text2)
    stop_words = ['the', 'is', 'in', 'and', 'to', 'of', 'a', 'that', 'it', 'on', 'for', 'with', 'as', 'this', 'by', 'an']
    filtered_text1 = remove_supporting_words(cleaned_text1.split(), stop_words)
    filtered_text2 = remove_supporting_words(cleaned_text2.split(), stop_words)
    common_words = set(filtered_text1).intersection(set(filtered_text2))
    similarity_percentage = (len(common_words) / len(set(filtered_text1).union(set(filtered_text2)))) * 100
    return similarity_percentage

with open(r"C:\Users\rohan\Documents\github-projects\MY-Python\Learning-Journey\File-Handling\Files\melina_trump_speech.txt",'r', encoding = 'utf-8') as f:
    text1 = f.read()
with open(r"C:\Users\rohan\Documents\github-projects\MY-Python\Learning-Journey\File-Handling\Files\michelle_obama_speech.txt",'r', encoding = 'utf-8') as f:
    text2 = f.read()
    similarity = check_text_similarity(text1, text2)
    print(f"Similarity between the two texts: {similarity:.2f}%")