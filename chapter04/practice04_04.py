if __name__ == '__main__':
    colors = ['red', 'black', 'blue', 'white', 'orange', 'yellow', 'green']

    # a list with colors placed at indexes: 1, 2 and 3
    print(colors[1:4])

    # to understand below result just replace the negative index [-4] with corresponding positive index [3]
    print(colors[1:-4])

    # return empty list if the slice is invalid
    print(colors[4:1])

    # leaving out the first index in a slice is the same as using 0
    print(colors[:4])

    # leaving out the second index in a slice is the same as using length of the list;
    # this is equivalent to saying: slice until the end of list
    print(colors[4:])
    