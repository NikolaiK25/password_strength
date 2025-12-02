def is_very_long(password):
    return len(password) >= 13


def has_digit(password):
    return any(letter.isdigit() for letter in password)


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_symbols(password):
    return any(not letter.isdigit() and not letter.isalpha() for letter in password)


password_functions = [
    is_very_long,
    has_digit,
    has_lower_letters,
    has_upper_letters,
    has_symbols
]


if __name__ == '__main__':

    password = input("Введите пароль: ")

    score = 0

    for func in password_functions:
        if func(password):
            score += 2


    print(f"\nРейтинг пароля:  {score}")