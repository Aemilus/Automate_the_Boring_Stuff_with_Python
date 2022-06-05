def get_month(value):
    if value == 1:
        return 'January'
    elif value == 2:
        return 'February'
    elif value == 3:
        return 'March'
    elif value == 4:
        return 'April'
    elif value == 5:
        return 'May'
    elif value == 6:
        return 'June'
    elif value == 7:
        return 'July'
    elif value == 8:
        return 'August'
    elif value == 9:
        return 'September'
    elif value == 10:
        return 'October'
    elif value == 11:
        return 'November'
    elif value == 12:
        return 'December'
    else:
        return 'Error'


if __name__ == '__main__':
    # convert number to month value
    print(get_month(1))
    print(get_month(7))
    print(get_month("one"))
