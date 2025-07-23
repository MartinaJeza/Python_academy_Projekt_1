"""
Projekt_1.py: První projekt do Engeto Online Python Akademie

author: Martina Jezkova
email: jezkova.m94@gmail.com
"""
import sys

SEPARATOR = "-" * 40

REGISTERED_USERS = {
    "bob": "123", 
    "mike": "password123", 
    "liz": "pass123"
}

TEXTS = [
    """Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.""",
    """At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.""",
]


def get_user_credentials() -> tuple[str, str]:
    """Prompt user for username and password.
    Returns:
        tuple: A tuple containing the username and password.
    """
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    return username, password


def verify_credentials(
    username: str, password: str, users: dict[str, str]
) -> None:
    """Check credentials agains registered users."""

    if not (username in users and password == users[username]):
        print(f"Unregistered user, terminating the program..")
        sys.exit()
    print(SEPARATOR)
    print(f"Welcome to the app, {username}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print(SEPARATOR)


def get_text_choice() -> int:
    """
    Prompt the user to select a text for analysis.

    The function asks the user to input a number between 1 and the total
    number of available texts.
    It validates whether the input is a digit. If not, the program
    prints an error message and exits.

    Returns:
        int: The user's selected text index as an integer.
    """
    text_choice = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
    print(SEPARATOR)
    if not text_choice.isdigit():
        print(f"You have not entered a number, terminating the app..")
        sys.exit()

    text_choice = int(text_choice)

    if not (1 <= text_choice <= len(TEXTS)):
        print(
            f"You have not entered a number btw. 1 and {len(TEXTS)}, "
            "terminating the app.."
        )
        sys.exit()

    return text_choice


def analyse_text(text_choice: int):
    """
    Perform a statistical analysis of the selected text.

    The function processes the text based on the user's choice and calculates:
        - total number of words,
        - number of titlecase words,
        - number of uppercase words,
        - number of lowercase words,
        - number of numeric strings,
        - sum of all numeric values,
        - frequency distribution of word lengths.

    It prints a formatted summary of the statistics.

    Args: text_choice (int): Index (1-based) of the selected text 
    from the TEXTS list.
    """
    text = TEXTS[text_choice - 1]
    raw_word = text.split()

    # Clean words
    cleaned_words = [
        word.strip('.,!?"“”:-') for word in raw_word if word.strip('.,!?"“”:-')
    ]

    # Basic counts
    word_count = len(cleaned_words)
    word_count_titlecase = sum(1 for word in cleaned_words if word.istitle())
    word_count_uppercase = sum(1 for word in cleaned_words if word.isupper())
    word_count_lowercase = sum(1 for word in cleaned_words if word.islower())

    # Numeric string
    numbers = [int(word) for word in cleaned_words if word.isnumeric()]
    word_count_numbers = len(numbers)

    # Frequency dictionary of word lenghts
    frequency = {}
    for word in cleaned_words:
        length = len(word)
        frequency[length] = frequency.get(length, 0) + 1

    max_count = max(frequency.values(), default=0)
    column_width = max(max_count, len("OCCURRENCES"))

    # Print result
    print(f"There are {word_count} words in the selected text.")
    print(f"There are {word_count_titlecase} titlecase words.")
    print(f"There are {word_count_uppercase} uppercase words.")
    print(f"There are {word_count_lowercase} lowercase words.")
    print(f"There are {word_count_numbers} numeric strings.")
    print(f"The sum of all the numbers is: {sum(numbers)}")
    print(SEPARATOR)
    print(f"LEN| {'OCCURRENCES':<{column_width}} |  NR.")
    print(SEPARATOR)
    for length in sorted(frequency.keys()):
        count = frequency[length]
        print(f"{length:>3}|  {'*' * count:<{column_width}} |  {count}")


def main():
    username, password = get_user_credentials()
    verify_credentials(username, password, REGISTERED_USERS)
    text_index = get_text_choice()
    analyse_text(text_index)


if __name__ == "__main__":
    main()


