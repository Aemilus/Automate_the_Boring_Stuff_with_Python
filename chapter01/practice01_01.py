# This program says hello and asks for my name.

if __name__ == '__main__':
    print('Hello!')
    print("What's your name?")
    myName = input()
    print(f'Nice to meet you, {myName}!')
    print(f'Length of your name: {len(myName)}')
    print('How old are you?')
    myAge = input()
    print(f"Noted. You're {myAge} years old.")
