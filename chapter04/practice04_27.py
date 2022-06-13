from copy import copy, deepcopy


def print_content_ids(list_obj: list):
    print(id(list_obj), list_obj)
    for element in list_obj:
        print(id(element), element)


if __name__ == '__main__':
    print("\n--- 1. copy list with immutable elements ---")
    list1 = ['Anna', 'Mary', 'John', 'Jack', 'Victor']
    print_content_ids(list1)

    list2 = copy(list1)
    print_content_ids(list2)

    print("\n--- 2. copy vs deepcopy when the list contains mutable object ---")
    print("--- 2.0. original list ---")
    list3 = [[1, 2, 3], True, (0, 0, 0)]
    print(id(list3), list3)
    print(id(list3[0]), list3[0])
    print(id(list3[1]), list3[1])
    print(id(list3[2]), list3[2])

    list4 = copy(list3)
    list5 = deepcopy(list3)

    print("--- 2.1. copy result---")
    print(id(list4), list4)
    print(id(list4[0]), list4[0])
    print(id(list4[1]), list4[1])
    print(id(list4[2]), list4[2])

    print("--- 2.2. deepcopy result ---")
    print(id(list5), list5)
    print(id(list5[0]), list5[0])
    print(id(list5[1]), list5[1])
    print(id(list5[2]), list5[2])
