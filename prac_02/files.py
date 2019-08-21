def main():
    file = open("name.txt", "w")
    name = input("enter your name")
    file.write(name)
    file.close()

    with open("name.txt", "r") as in_file:
        name = in_file.read().strip()
    print("Your name is", name)

    read = open("numbers.txt", "r")
    number1 = int(read.readline())
    number2 = int(read.readline())
    read.close()
    print(number1 + number2)

    read = open("numbers.txt", "r")
    total = 0
    for line in read:
        number = int(line)
        total += number
    read.close()
    print(total)


main()
