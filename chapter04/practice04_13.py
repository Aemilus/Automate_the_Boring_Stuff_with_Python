import random


if __name__ == '__main__':
    print("\n--- original list ---")
    colors = ['red', 'black', 'blue', 'white', 'orange', 'yellow', 'green']
    print(colors)

    print("\n--- random.choice() ---")
    my_choice = random.choice(colors)
    print(my_choice)

    print("\n--- random.shuffle() ---")
    random.shuffle(colors)
    print(colors)
