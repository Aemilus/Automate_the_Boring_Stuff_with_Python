import pprint


if __name__ == '__main__':
    print("\n--- original dict ---")
    my_dict = {'cat': 'Thomas', 'eyes': 'blue', 'age': 8, 'color': 'orange'}
    print('my_dict:', my_dict)

    print("\n--- pprint dict ---")
    pprint.pprint(my_dict)
    print("\n--- pprint dict, force width ---")
    pprint.pprint(my_dict, width=1)

    print("\n--- get prettified dict as string ---")
    my_dict_str = pprint.pformat(my_dict, width=1)
    print(my_dict_str)
