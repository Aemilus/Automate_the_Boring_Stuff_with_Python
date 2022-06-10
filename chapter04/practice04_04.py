if __name__ == '__main__':
    print("\n--- original list ---")
    colors = ['red', 'black', 'blue', 'white', 'orange', 'yellow', 'green']
    print(colors)

    print("\n--- a list with colors placed at indexes: 1, 2 and 3 ---")
    print(colors[1:4])

    print(f"\n--- to understand below result just "
          f"replace the negative index [-4] with corresponding positive index [3] ---")
    print(colors[1:-4])

    print("\n--- return empty list if the slice is invalid ---")
    print(colors[4:1])

    print("\n--- leaving out the first index in a slice is the same as using 0 ---")
    print(colors[:4])

    print(f"\n--- leaving out the second index in a slice is the same as using length of the list\n"
          f"and it's equivalent to saying: slice until the end of list ---")
    print(colors[4:])
    