"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Magdalena Rajtarova
email: magda.rajt@gmail.com
"""

from string import punctuation

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

user = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

cara = "-" * 35
username = input("username:")
password = input("password:")

if username in user and password == user[username]:
    print(cara)
    print("Welcome to the app, " + username)
    print("We have 3 texts to be analyzed.")
    print(cara)
else:
    print("unregistered user, terminating the program..")
    exit()

text_selection = input("Enter a number btw. 1 and 3 to select: ")

if text_selection.isdigit():
    selected_index = int(text_selection) - 1
    if 0 <= selected_index < len(TEXTS):
        selected_text = TEXTS[selected_index]
        words = [word.strip(punctuation) for word in selected_text.split()]
        word_count = len(words)
        capitalized_words_count = sum(1 for word in words if word[0].isupper() and word[1:].islower())
        uppercase_words_count = sum(1 for word in words if word.isupper())
        lowercase_words_count = sum(1 for word in words if word.islower())
        numeric_strings_count = sum(1 for word in words if word.isdigit())
        numeric_sum = sum(int(word) for word in words if word.isdigit())
        print(cara)
        print(f"There are {word_count} words in the selected text.")
        print(f"There are {capitalized_words_count} titlecase words.")
        print(f"There are {uppercase_words_count} uppercase words.")
        print(f"There are {lowercase_words_count} lowercase words.")
        print(f"There are {numeric_strings_count} numeric strings.")
        print(f"The sum of all the numbers {numeric_sum}")
        print(cara)
        print("LEN|  OCCURENCES  |NR.")
        print(cara)
        length_count = {}
        for word in words:
            word_length = len(word)
            if word_length in length_count:
                length_count[word_length] += 1
            else:
                length_count[word_length] = 1
        for length, count in sorted(length_count.items()):
            print(f"{length:2}| {'*' * count:<20} |{count}")
    else:
        print("Invalid selection. Please enter a number between 1 and 3.")
        exit()
else:
    print("Invalid input. Please enter a valid number.")
    exit()
