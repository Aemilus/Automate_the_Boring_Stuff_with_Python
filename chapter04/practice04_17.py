if __name__ == '__main__':
    print("\n--- original list ---")
    colors = ['red', 'black', 'red', 'white', 'orange', 'yellow', 'green']
    print(colors)

    print("\n--- remove orange color from list ---")
    colors.remove('orange')
    print(colors)

    print("\n--- remove red color from list (only first occurrence is removed) ---")
    colors.remove('red')
    print(colors)

    print("\n--- try to remove non-existent color ---")
    try:
        colors.remove('pink')
    except ValueError as err:
        print(err)
