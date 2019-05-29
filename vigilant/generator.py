"""Module to generate random strings"""
import string
import random


def random_string_digits(string_length=10):
    """Generate a random string of letters and digits """
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(string_length))


def random_password(string_length=10):
    """ Generate a ten-character alphanumeric password with at least one lowercase character,
    at least one uppercase character, at least one digits and at least one special character. """
    random_source = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    for i in range(string_length):
        password += random.choice(random_source)
    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password


def main():
    """Main function"""
    print(random_string_digits(32))
    print(random_password(10))


if __name__ == '__main__':
    main()
