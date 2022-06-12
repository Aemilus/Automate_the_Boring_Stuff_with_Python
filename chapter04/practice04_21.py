if __name__ == '__main__':
    # The Python sequence data types include lists, strings, range objects returned by range(), and tuples
    sequence_range = range(0, 4)
    sequence_str = 'word'
    sequence_list = ['this', 'is', 'a', 'list']
    sequence_tuple = ('this', 'is', 'a', 'tuple')

    for index in range(4):
        print(sequence_range[index], sequence_str[index], sequence_list[index], sequence_tuple[index])
