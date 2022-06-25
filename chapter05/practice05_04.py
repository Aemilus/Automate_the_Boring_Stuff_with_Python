if __name__ == '__main__':
    print("\n--- original dict ---")
    my_dict = {'cat': 'Thomas', 'eyes': 'blue', 'age': 8, 'color': 'orange'}
    print('my_dict:', my_dict)

    x = 'cat'
    print(f"\n--- is '{x}' in keys() ---")
    print(x in my_dict.keys())

    x = 'blue'
    print(f"\n--- is '{x}' in values() ---")
    print(x in my_dict.values())

    x = 'dog'
    print(f"\n--- is '{x}' in keys() ---")
    print(x in my_dict.keys())

    x = 'red'
    print(f"\n--- is '{x}' in values() ---")
    print(x in my_dict.values())
