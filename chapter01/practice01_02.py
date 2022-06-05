# Although the string value of a number
# is considered a completely different value
# from the integer or floating-point version,
# an integer can be equal to a floating point.

if __name__ == '__main__':
    # False
    print(12 == '12')
    # True
    print(12 == 12.0)
    # True
    print(12.0 == 0012.0000)
