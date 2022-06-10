if __name__ == '__main__':
    print("\n--- original list ---")
    colors = ['red', 'black', 'blue', 'white', 'orange', 'yellow', 'green']
    print(colors)

    print("\n--- using enumerate() ---")
    for color_idx, color in enumerate(colors):
        print(color_idx, color)
