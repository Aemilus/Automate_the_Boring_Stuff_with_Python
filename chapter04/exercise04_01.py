"""
Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space,
with 'and' inserted before the last item.

For example, passing the previous spam list to the function
would return 'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to it.
Be sure to test the case where an empty list [] is passed to your function.
"""


def comma_code(list_with_strings: list):
    print('original list:', list_with_strings)
    print('length:', len(list_with_strings))

    stringified_list = ""
    if len(list_with_strings) == 0:
        return stringified_list

    stringified_list = list_with_strings[0]
    if len(list_with_strings) == 1:
        return stringified_list
    else:
        for my_string in list_with_strings[1:-1]:
            stringified_list += ", " + my_string
        stringified_list += " and " + list_with_strings[-1]
        return stringified_list


if __name__ == '__main__':
    print("\n--- empty list ---")
    spam = []
    print(comma_code(spam))

    print("\n--- one string ---")
    spam = ['apples']
    print(comma_code(spam))

    print("\n--- two strings ---")
    spam = ['apples', 'bananas']
    print(comma_code(spam))

    print("\n--- multiple strings ---")
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(comma_code(spam))
