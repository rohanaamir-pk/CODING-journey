#CLASSES & OBJECTS---//DAY-16//
#_______________________________________________________________________________________________________________________________________________________
#creating ann class
class Person:
    pass #pass is used to indicate that the class has no attributes or methods

#creating an object of the class
person1 = Person() #creating an object of the class Person
#_________________________________________________________________________________________________________________
#constructors
class Person:
    def __init__(self, name, age): #__init__ is a constructor that is called when an object of the class is created
        self.name = name #self is used to refer to the instance of the class
        self.age = age
        print("Person object created with name:", self.name, "and age:", self.age) #prints the name and age of the person when the object is created

person1 = Person('jane', 22) #creating an object of the class Person
person1.name = "Jane" #modifying the name of the person
person1.age = 25 #modifying the age of the person
print(person1.name, person1.age) #prints the name and age of the person
#_________________________________________________________________________________________________________________
#object methods
class student:
    def __init__(self):
        print(f'successfully created {self}' )
    pass
    def grade(self, marks=0, tm=100): #find percentage of marks and print the grade
        grd = (marks/tm) *100 
        print(f"Percentage: {grd:.2f}%")
        return grd
    def format(self, grds): #prints the grade based on the percentage of marks
        if grds >= 90:
            GRADE = "A"
        elif grds >= 80:
            GRADE = "B"
        elif grds >= 70:
            GRADE = "C"
        elif grds >= 60:
            GRADE = "D"
        else:
            GRADE = "F"
        print(f"Grade: {GRADE}")
        return GRADE
class Teacher(student):
    def __init__(self):
        print("Acess granted") 
    def Show_report(self, grds, format):
        print(f"Student has acquired a {grds} and a {format} Grade")

    
#main body
s1 = student()
marks = float(input("Enter the marks obtained: ")) #takes input from the user for marks obtained
tm = float(input("Enter the total marks: ")) #takes input from the user for total marks
percent = s1.grade(marks, tm) #calls the grade method of the student class and passes the marks and total marks as arguments
grading = s1.format(percent) #calls the format method and passes the grade as an argument

T1 = Teacher()
T1.Show_report(percent, grading)


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||X[PROGRAM]X|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||]
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Python has the module called statistics and we can use this module to do all the statistical calculations. 
However, to learn how to make function and reuse function let us try to develop a program, which calculates 
the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). 
In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample.
 You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. 
 Check the output below.'''


from collections import Counter
from math import *

class statistics:
    def __init__(self, data):
        self.data = data

    def mean(self): #the mean is the average of a set of values. It is calculated by adding up all the values in the data set and then dividing that sum by the total number of values. The mean is a measure of central tendency that represents the typical value in a distribution. In other words, it is the value that is most representative of the entire data set.
        return sum(self.data) / len(self.data)
    
    def median(self): #the median is the middle value of a data set when it is ordered from least to greatest. It is a measure of central tendency that represents the value that separates the higher half from the lower half of a distribution. In other words, it is the value that lies at the midpoint of a data set when it is arranged in ascending or descending order. If there is an even number of values in the data set, the median is calculated by taking the average of the two middle values.
        self.data
        if (len(self.data)%2==0):
            return (self.data[len(self.data)/2])
        else:
            return (self.data[int(len(self.data)/2)] + self.data[(int(len(self.data)/2))-1])/2
        
    def mode(self): #the mode is the value that appears most frequently in a data set. It is a measure of central tendency that represents the most common value in a distribution. In other words, it is the value that occurs with the highest frequency in a given set of data.
        self.data = sorted(list(map(int, self.data)))
        occurences = Counter(self.data)
        return occurences.most_common(1)[0][0]
    
    def range(self): #the range is a measure of variability that represents the difference between the maximum and minimum values in a data set. It provides an indication of how spread out the values are in the distribution. The range is calculated by subtracting the minimum value from the maximum value. A larger range indicates greater variability, while a smaller range suggests less variability in the data.
        return self.data[len(self.data)-1]- self.data[0]
    
    def variance(self): #the variance is a measure of variability that represents the average of the squared differences from the mean. It provides an indication of how spread out the values are in the distribution. The variance is calculated by taking the sum of the squared differences from the mean and dividing by the total number of values. A larger variance indicates greater variability, while a smaller variance suggests less variability in the data.
        mean = self.mean()
        return sum([(x - mean)**2 for x in self.data])/len(self.data)
    
    def standard_deviation(self): #the standard deviation is a measure of variability that represents the square root of the variance. It provides an indication of how spread out the values are in the distribution. The standard deviation is calculated by taking the square root of the variance. A larger standard deviation indicates greater variability, while a smaller standard deviation suggests less variability in the data.
        mean = self.mean()
        return sum([sqrt(y) for y in [(x - mean)**2 for x in self.data]])/len(self.data)
    
    def min(self): #the minimum value is the smallest value in a data set. It is a measure of central tendency that represents the lowest value in a distribution. In other words, it is the value that is less than or equal to all other values in the data set. The minimum value can be useful for identifying outliers or extreme values in a distribution, as well as for understanding the range of values in the data set.
        return min(self.data)
    
    def max(self): #the maximum value is the largest value in a data set. It is a measure of central tendency that represents the highest value in a distribution. In other words, it is the value that is greater than or equal to all other values in the data set. The maximum value can be useful for identifying outliers or extreme values in a distribution, as well as for understanding the range of values in the data set.
        return max(self.data)
    
    def count(self): #the count is the total number of values in a data set. It is a simple measure that indicates how many observations are available for analysis. The count is often used in conjunction with other measures to provide a comprehensive overview of the data.
        return len(self.data)
    
    def percentile(self, percentile): #the percentile is a measure that indicates the relative standing of a value within a data set. It represents the percentage of values that fall below a given value. For example, if a value is at the 75th percentile, it means that 75% of the values in the data set are lower than that value. Percentiles are often used to understand the distribution of data and to compare individual values to the overall data set.
        self.data = sorted(list(map(int, self.data)))
        index = (percentile/100) * len(self.data)
        if index.is_integer():
            return (self.data[int(index)-1] + self.data[int(index)])/2
        else:
            return self.data[ceil(index)-1]
        
    def frequency_distribution(self): #the frequency distribution is a summary of how often each value occurs in a data set. It provides an overview of the distribution of values and can help identify patterns or trends in the data. The frequency distribution is typically presented in a table or graph, showing the values and their corresponding frequencies. It can be useful for understanding the shape of the distribution, identifying outliers, and making comparisons between different data sets.
        occurences = Counter(self.data)
        return occurences.most_common()

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
ages = sorted(list(map(float, ages)))
print(ages)
stats = statistics(ages)

print(f'Mean: {stats.mean()}')
print(f'Median: {stats.median()}')
print(f'Mode: {stats.mode()}')
print(f'Range: {stats.range()}')
print(f'Variance: {stats.variance():.2f}')
print(f'Standard Deviation: {stats.standard_deviation():.3f}')
print(f'Min: {stats.min()}')
print(f'Max: {stats.max()}')
print(f'Count: {stats.count()}')    
print(f'Percentile: {stats.percentile(50)}')
print(f'Frequency Distribution: {stats.frequency_distribution()}')


