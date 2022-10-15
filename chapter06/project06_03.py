"""
Pig Latin is a silly made-up language that alters English words.
If a word begins with a vowel, the word yay is added to the end of it.
If a word begins with a consonant or consonant cluster (like ch or gr),
that consonant or cluster is moved to the end of the word followed by ay.
"""

yay = "yay"
ay = "ay"


VOWELS = ["a", "e", "i", "o", "u"]

if __name__ == '__main__':
    text = input("Please enter text:\n")

    words = text.split()

    pig_latin = list()
    for word in words:
        # extract non alpha characters in front of word if any
        word_prefix = ""
        if len(word) and not word[0].isalpha():
            word_prefix += word[0]
            word = word[1:]

        # if no alpha characters remained then this was not a real word; skip to next word
        if not len(word):
            pig_latin.append(word_prefix)
            continue

        # extract non alpha characters at end of word if any
        word_suffix = ""
        while not word[-1].isalpha():
            word_suffix += word[-1]
            word = word[:-1]

        # extract consonants at beginning of word
        consonants_group = ""
        while len(word) and word[0].lower() not in VOWELS:
            consonants_group += word[0]
            word = word[1:]

        # add pig latin ending
        if consonants_group:
            word += consonants_group + ay
        else:
            word += yay

        # store pig latin word version
        pig_latin.append(word_prefix + word + word_suffix)

    pig_latin_text = " ".join(pig_latin)
    print(f"Pig Latin text:\n"
          f"{pig_latin_text}")
