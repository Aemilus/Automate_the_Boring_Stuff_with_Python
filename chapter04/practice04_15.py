if __name__ == '__main__':
    print("\n--- original list ---")
    colors = ['red', 'black', 'blue', 'white', 'orange', 'yellow', 'green']
    print(colors)

    print("\n--- index of specific color ---")
    color_idx = colors.index('yellow')
    print(color_idx, colors[color_idx])

    print("\n--- index of non-existent color ---")
    try:
        color_idx = colors.index('pink')
    except ValueError as err:
        print(err)
