def main():
    """
    CP1404/CP5632 - Practical
    Random word generator - based on format of words
    Another way to get just consonants would be to use string.ascii_lowercase
    (all letters) and remove the vowels.
    """
    import random

    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    word_format = "ccvcvvc"
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(consonants)
        else:
            word += random.choice(vowels)

    print(word)
    choice = input("Uppercase or Lowercase")

    if choice.upper() == "UPPERCASE":
        print(word.upper())
    else:
        print((word.lower()))


main()
