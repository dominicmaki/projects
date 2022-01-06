import string
import random
import sys
import json


def get_password_specs():
    print("Which option would you like the generated password to match??\n"
          "1: Numbers\n"
          "2: Symbols\n"
          "3: Letters\n"
          "4: Uppercase/Lowercase letters\n"
          "5: Numbers and Symbols\n"
          "6: Numbers and Upper/Lowercase letters\n"
          "7: Upper/Lowercase letters and Symbols\n"
          "8: Numbers, Upper/Lowercase letters, and Symbols\n")
    option = input()
    length = random.randrange(6, 15)
    return option, length


def generate_password(option, length):

    if option == "1":
        letters = string.digits
    elif option == "2":
        letters = string.punctuation
    elif option == "3":
        letters = string.ascii_lowercase
    elif option == "4":
        letters = string.ascii_lowercase + string.ascii_uppercase
    elif option == "5":
        letters = string.digits + string.punctuation
    elif option == "6":
        letters = string.digits + string.ascii_uppercase + string.ascii_lowercase
    elif option == "7":
        letters = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    elif option == "8":
        letters = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation

    password = ''.join(random.choice(letters) for _ in range(length))
    return password


def store_password(password):

    d = {}
    print("What name would you like the password to be stored under?\n"
          "Enter:")
    key = input()
    value = password
    d[key] = value
    print(key)
    with open("passwords.txt", "a") as f:
        f.write(json.dumps(d))
        f.write("\n")


def read_file():

    d = {}
    with open("passwords.txt") as f:
        for line in f:
            (key, value) = line.split(':', 1)
            key = str(key).strip('{')
            key = str(key).strip('"')
            d[key] = value
            print(key)
    return d


def enter_database(d):
    print("Password keys:")
    for key in d:
        print(key)

    print("Enter the key to the database you'd like to enter:")
    key = input()
    print(d[key])


def create_own_password():

    d = {}
    print("What would you like the password to be stored under?")
    key = input()
    print("Enter the password you would like stored with" + " " + key)
    value = input()
    d[key] = value
    store_created_password(d)


def store_created_password(d):
    with open("passwords.txt", "a") as f:
        f.write(json.dumps(d))
        f.write("\n")


def main():

    print("Welcome to the Password Generator")
    while True:
        print("Which would you like to do?\n"
              "1: Generate a password\n"
              "2: Access the password database\n"
              "3: Create and store password\n"
              "4: Exit System")
        answer = input()

        if answer == "1":
            option, length = get_password_specs()
            password = generate_password(option, length)
            print(password)

            print("Would you like to store this generated password?\n"
                  "Yes or No")
            answer = input()
            if answer == "Yes":
                store_password(password)
                with open("passwords.txt") as f:
                    print(f.readline())

        elif answer == "2":
            d = read_file()
            enter_database(d)

        elif answer == "3":
            create_own_password()

        elif answer == "4":
            sys.exit()


if __name__ == "__main__":
    main()