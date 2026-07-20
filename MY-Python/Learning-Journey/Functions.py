#FUNCTIONs---//DAY-8//

#A function to generate groups from arbitary arguments *arg
def generate_groups (team, *args):
    print(team)
    for i in args:
        print(i)
generate_groups('yoi','Asabeneh','Brook','David','Eyob')



# Define a function that takes two arguments: 'name' and 'location'
def greet(name, location):
    # Print a greeting message using the provided arguments
    for i in range(2):

      print("Hi there", name[i], "how is the weather in", location[i])

# Call the function using keyword arguments

# Output: Hi there Alice how is the weather in New York

# Create a dictionary with keys matching the function's parameter names
my_dict = {"name": ["Alice",'minta'],
           "location": ["New York",'pakis']}

# Call the function using dictionary unpacking
greet(**my_dict)
# The ** operator unpacks the dictionary, passing its key-value pairs
# as keyword arguments to the function.
# Output: Hi there Alice how is the weather in New York


#function that I dont remember what it does
def arbitrary_named_args(**args):
    args = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB"]
    }
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(" * key:", k, "value:", v)

arbitrary_named_args()


#You can pass functions around as parameters
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 8)) 

#function that checks for seaason on a month as an argument
def check_season(month):
  if month == 'September' or month == 'October' or month == 'November':
    print('Autumn')
  elif (month == 'December' or month == 'January' or month == 'February'):
    print('Winter')
  elif month == 'March' or month == 'April' or month == 'May':
    print('Spring')
  elif month == 'June' or month == 'July' or month == 'August':
    print('Summer')
  else:
    print('invalid')
check_season('January')