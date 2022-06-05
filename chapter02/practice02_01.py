if __name__ == '__main__':
    my_age = 31
    print('Guess my age!')
    input_age = input('> ')
    input_age = int(input_age)

    if input_age == my_age:
        print("That's right. You must be a wizard for guessing that!")
    elif input_age < 1:
        print("How can I be dead if I'm talking with you?")
    elif input_age > 90:
        print("I wish to be a vampire but I'm not.")
    else:
        print('Keep guessing.')
