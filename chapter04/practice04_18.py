if __name__ == '__main__':
    print("\n--- original list ---")
    colors = ['red', 'black', 'Red', 'white', 'orange', 'Yellow', 'green']
    print(colors)

    print("\n--- sort list in ASCIIbetical order ---")
    colors.sort()
    print(colors)

    print("\n--- sort in reverse order ---")
    colors.sort(reverse=True)
    print(colors)

    print("\n--- sort list in regular alphabetical order ---")
    colors.sort(key=str.lower)
    print(colors)

    print("\n--- unable to sort if elements are not of same type ---")
    mix = [2, 'pizza', '30$', 0.19, True, None]
    print('list with elements of mixed types:', mix)
    try:
        mix.sort()
    except TypeError as err:
        print(err)
