if __name__ == '__main__':
    print("\n--- original dict ---")
    my_dict = {'cat': 'Thomas', 'eyes': 'blue', 'age': 8, 'color': 'orange'}
    print('my_dict:', my_dict)

    print("\n--- keys() method ---")
    print('keys():', my_dict.keys())

    print("\n--- values() method ---")
    print('values():', my_dict.values())

    print("\n--- items() method ---")
    print('items():', my_dict.items())

    print("\n--- iterate over dict ---")
    print(f"{'key':^15}|{'value':^15}")
    print(f"{'-' * 15}|{'-' * 15}")
    for k, v in my_dict.items():
        print(f"{k:<15}|{v:>15}")
