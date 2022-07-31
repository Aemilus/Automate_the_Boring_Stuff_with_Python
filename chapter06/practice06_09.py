if __name__ == '__main__':
    print("\n--- original string ---")
    s1 = 'Your weight: 94 kg; Your height: 181 cm.'
    print(s1)

    sep = ';'
    print(f"\n--- partition({sep}) ---")
    print(s1.partition(sep))

    sep = ' '
    print(f"\n--- partition({sep}) ---")
    print(s1.partition(sep))

    sep = '?'
    print(f"\n--- partition({sep}) ---")
    print(s1.partition(sep))
