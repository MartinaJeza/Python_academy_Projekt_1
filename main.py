"""
Projekt_1.py: První projekt do Engeto Online Python Akademie

author: Martina Jezkova
email: jezkova.m94@gmail.com
"""
import sys

# list of texts:
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# database of registered users:
registered_users = {
    'bob': '123',                                                                                
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# user inputs for username and password: 
username = input('username:')
password = input('password:')

# check if entered username and password match the registered users:
# unregistered users:
if not (username in registered_users and password == registered_users[username]):                 
    print(f'unregistered user, terminating the program..')
    sys.exit()
# registered users:
else:
    print(f'----------------------------------------')
    print(f'Welcome to the app, {username}')
    print(f'We have {len(TEXTS)} texts to be analyzed.')
    print(f'----------------------------------------')

# choice of text to analyze:
choice_of_text = input(f'Enter a number btw. 1 and {len(TEXTS)} to select: ')
print(f'----------------------------------------')
# check if the input is a digit:
if not choice_of_text.isdigit():
        print(f'You have not entered a number, terminating the app..')
        sys.exit()

chosen_text = int(choice_of_text)
# input is not within the range of available texts:
if not (1 <= chosen_text <= len(TEXTS)):
    print(f'You have not entered a number btw. 1 and {len(TEXTS)}, terminating the app..')
    sys.exit()

else:
    # Text analysator:
    text = TEXTS[chosen_text - 1]
    word_list = text.split()

    word_count = 0
    word_count_titlecase = 0
    word_count_uppercase = 0
    word_count_lowercase = 0
    word_count_numbers = 0
    # list to store the numbers found in the text
    numbers = []
    # dictionary to store the frequency of word lengths
    frequency = {}
    
    for word in word_list:
        word = word.strip(".,!?\"“”:-")
        word_count += 1
        length_of_word = len(word)

        if word.istitle():
            word_count_titlecase += 1
            
        if word.isupper():
            word_count_uppercase += 1
            
        if word.islower():
            word_count_lowercase += 1
            
        if word.isnumeric():
            word_count_numbers += 1
            numbers.append(int(word))
            
        if length_of_word in frequency:
            frequency[length_of_word] += 1
        else:
            frequency[length_of_word] = 1
                
    max_count = max(frequency.values())
    column_width = max(max_count, len('OCCURRENCES'))
            
    # Print the results:
    print(f'There are {word_count} words in the selected text.')
    print(f'There are {word_count_titlecase} titlecase words.')
    print(f'There are {word_count_uppercase} uppercase words.')
    print(f'There are {word_count_lowercase} lowercase words.')
    print(f'There are {word_count_numbers} numeric strings.')
    print(f'The sum of all the numbers is: {sum(numbers)}')
    print(f'----------------------------------------')
    print(f'LEN| {'OCCURRENCES':<{column_width}} |  NR.')
    print(f'----------------------------------------')
    for length in sorted(frequency.keys()):
        count = frequency[length]
        # Print the frequency table:
        print(f'{length:>3}|  {'*' * count:<{column_width}} |  {count}')