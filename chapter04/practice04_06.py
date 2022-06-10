if __name__ == '__main__':
    print("\n--- original list ---")
    colors = ['red', 'black', 'blue', 'white', 'orange', 'yellow', 'green']
    print(colors)

    print("\n--- change one element value ---")
    print(colors[0])
    colors[0] = 'cyan'
    print(colors[0])

    print("\n--- swap two elements ---")
    print(colors[1:3])
    tmp_color = colors[1]
    colors[1] = colors[2]
    colors[2] = tmp_color
    print(colors[1:3])

    print("\n--- swap two elements (another way) ---")
    print(colors[1:3])
    colors[1], colors[2] = colors[2], colors[1]
    print(colors[1:3])
