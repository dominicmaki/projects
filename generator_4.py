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


def read_json_file():
    with open("my_dict.json", "r") as f:
        try:
            d = json.load(f)
        except ValueError:
            d = {}
    return d


def update_dict(password):

    d = read_json_file()
    print("What name would you like the password to be stored under?\n"
        "Enter:\n")
    key = input()
    value = password
    d.update({key: value})
    return d


def store_password(d):

    with open("my_dict.json", "w") as f:
        json.dump(d, f)


def enter_database():

    d = read_json_file()
    print("Password keys:")
    for key in d:
        print(key)

    print("Enter the key to the database you'd like to enter:\n")
    key = input()
    print(d[key])


def create_own_password():

    d = read_json_file()
    print("What would you like the password to be stored under?")
    key = input()
    print("Enter the password you would like stored with" + " " + key)
    value = input()
    d.update({key: value})
    store_password(d)


def main():

    print("Welcome to the Password Generator\n")
    while True:
        print("Which would you like to do?\n"
              "1: Generate a password\n"
              "2: Access the password database\n"
              "3: Create and store password\n"
              "4: Exit System")
        #What if same password is stored twice?
        answer = input()

        if answer == "1":
            option, length = get_password_specs()
            password = generate_password(option, length)
            print(password)

            print("Would you like to store this generated password?\n"
                  "Yes or No")
            answer = input()
            if answer == "Yes":
                d = update_dict(password)
                store_password(d)

        elif answer == "2":
            enter_database()

        elif answer == "3":
            create_own_password()

        elif answer == "4":
            sys.exit()


if __name__ == "__main__":
    main()