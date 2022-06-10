if __name__ == '__main__':
    print("\n--- original list ---")
    colors = ['red', 'black', 'blue', 'white', 'orange', 'yellow', 'green']
    print(colors)

    print("\n--- iterate over elements in a list with a for loop ---")
    for color_idx in range(len(colors)):
        print(color_idx, colors[color_idx])

    print("\n--- iterate over elements in a list with a for loop ---")
    for color in colors:
        print(color)
