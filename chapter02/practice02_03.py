if __name__ == '__main__':
    # count from 1 to user input desired value
    limit = int(input('Count from 1 to '))
    counter = 0
    while True:
        counter = counter + 1
        print(counter, end=' ')
        if counter == limit:
            # for zero or negative numbers the loop is infinite!
            break
