if __name__ == '__main__':
    print("\n--- string concatenation ---")
    s1 = "Johny"
    s2 = 10
    # str + int concatenation doesn't work; needs to be cast to string
    s3 = "Hello " + s1 + ". You've won " + str(s2) + " dollars at lottery."
    print(s3)

    print("\n--- string interpolation ---")
    s3 = "Hello %s. You've won %s dollars at lottery." % (s1, s2)
    print(s3)

    print("\n--- f-strings ---")
    s3 = f"Hello {s1}. You've won {s2} dollars at lottery."
    print(s3)
