if __name__ == '__main__':
    print("\n--- original list ---")
    colors = ['red', 'black', 'blue', 'white', 'orange', 'yellow', 'green']
    print(colors)

    print("\n--- length of entire list ---")
    colors_len = len(colors)
    print('Length:', colors_len)

    print("\n--- length of a sliced list ---")
    my_colors = colors[4:]
    print(my_colors)
    print(len(my_colors))
