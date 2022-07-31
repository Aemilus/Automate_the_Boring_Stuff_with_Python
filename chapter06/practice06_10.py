if __name__ == '__main__':
    print("\n--- original strings ---")
    s1 = 'Michael'
    s2 = 'Alireza'
    print(s1, s2)

    width = 20
    print(f"\n--- rjust ---")
    print(s1.rjust(width), s2)

    print(f"\n--- ljust ---")
    print(s1.ljust(width), s2)

    print(f"\n--- center ---")
    print(s1.center(width), s2)

    fill = '#'
    print(f"\n--- rjust ---")
    print(s1.rjust(width, fill), s2)

    print(f"\n--- ljust ---")
    print(s1.ljust(width, fill), s2)

    print(f"\n--- center ---")
    print(s1.center(width, fill), s2)
