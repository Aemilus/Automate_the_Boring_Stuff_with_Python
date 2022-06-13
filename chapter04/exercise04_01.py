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


def comma_code(_elements: list):
    print('original list:', _elements)
    print('length:', len(_elements))

    stringified = ""
    if len(_elements) == 0:
        return stringified

    stringified = str(_elements[0])
    if len(_elements) == 1:
        return stringified
    else:
        for _element in _elements[1:-1]:
            stringified += ", " + str(_element)
        stringified += " and " + str(_elements[-1])
        return stringified


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

    print("\n--- mixed elements type ---")
    spam = ['apples', 1, None, False]
    print(comma_code(spam))
