Lower = 33
Higher = 127


def main():
    character = input("enter a character")
    print(" The ASCII code for {} is {}".format(character, ord(character)))
    number = int(input("Enter a number between {} and {}".format(Lower, Higher)))
    while number < Lower or number > Higher:
        print("Invalid number must be between {} and {}".format(Lower, Higher))
        number = int(input("Enter a number between {} and {}".format(Lower, Higher)))

    print(" the ASCII cod for {} is {}".format(number, chr(number)))


main()
