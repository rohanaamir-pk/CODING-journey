#MODULE(random & string)---//DAY-9//

import random
import string


#using random and string to generate ID with built-ni functions
def generate_random_user_id():
    """
    Generates a six-character random user ID consisting of uppercase letters and digits.
    """
    characters = string.ascii_uppercase + string.digits
    random_id = ''.join(random.choice(characters) for i in range(6))
    return random_id

# Example usage:
user_id = generate_random_user_id()
print(f"Generated Random User ID: {user_id}")


#similar to before but this time lenght is user defined
def user_id_gen_by_user():
  lenght = input('enter lenght of id')
  characters = string.ascii_letters+string.digits
  random_id = ''.join(random.choice(characters) for i in range(int(lenght)))
  return random_id

user_id_gen_by_user()

#generating rgb color code
x = random.randint(0,255)
y = random.randint(0,255)
z = random.randint(0,255)
print(f'rgb({x},{y},{z})')

#a function that will generate the required number of colors in choice of format rgb/hex
def generate_colors(num_colors, color_format='hex'):
    """
    Generates a list of random color codes in either hexadecimal or RGB format.

    Args:
        num_colors (int): The number of colors to generate.
        color_format (str, optional): The format of the colors.
                                      Must be 'hex' for hexadecimal or 'rgb' for RGB.
                                      Defaults to 'hex'.

    Returns:
        list: A list of color code strings.

    Raises:
        ValueError: If an invalid color_format is provided.
    """
    colors = []
    if num_colors <= 0:
        return colors

    if color_format == 'hex':
        for _ in range(num_colors):
            # Generate 6 random hexadecimal characters
            hex_code = ''.join(random.choice(string.hexdigits) for _ in range(6))
            colors.append(f'#{hex_code}')
    elif color_format == 'rgb':
        for _ in range(num_colors):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            colors.append(f'rgb({r},{g},{b})')
    else:
        raise ValueError("Invalid color_format. Must be 'hex' or 'rgb'.")
    return colors

# Example usage:
print("Generated 5 Hex Colors:")
hex_colors = generate_colors(5, 'hex')
for color in hex_colors:
    print(color)

print("\nGenerated 3 RGB Colors:")
rgb_colors = generate_colors(3, 'rgb')
for color in rgb_colors:
    print(color)


#making function to shuffle a list 
def shuffle_list(input_list):
    """
    Shuffles the elements of a list and returns a new shuffled list.

    Args:
        input_list (list): The list to be shuffled.

    Returns:
        list: A new list with elements shuffled.
    """
    # random.sample returns a new list with a given length from a population.
    # Using len(input_list) ensures all elements are included in the shuffled list.
    return random.sample(input_list, len(input_list))

# Example usage:
my_list = ['apple', 'banana', 'cherry', 'date']
shuffled_my_list = shuffle_list(my_list)

print(f"Original list: {my_list}")
print(f"Shuffled list: {shuffled_my_list}")

# Another example with numbers
numbers = [1, 2, 3, 4, 5]
shuffled_numbers = shuffle_list(numbers)
print(f"Original numbers: {numbers}")
print(f"Shuffled numbers: {shuffled_numbers}")