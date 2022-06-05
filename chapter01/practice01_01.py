# This program says hello and asks for my name.

if __name__ == '__main__':
    print('Hello!')
    print("What's your name?")
    my_name = input()
    print(f'Nice to meet you, {my_name}!')
    print(f'Length of your name: {len(my_name)}')
    print('How old are you?')
    my_age = input()
    print(f"Noted. You're {my_age} years old.")
