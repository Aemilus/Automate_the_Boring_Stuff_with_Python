if __name__ == '__main__':
    # count by 2 from 1 to 100
    counter = 0
    skip = True
    while counter < 100:
        counter = counter + 1
        skip = not skip
        if not skip:
            print(counter, end=' ')
        else:
            continue
