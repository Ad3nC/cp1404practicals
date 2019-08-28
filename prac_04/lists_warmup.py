def main():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    numbers.remove(3)
    numbers[0] = "ten"
    numbers[-1] = 1
    print(numbers[2:])
    if 9 in numbers:
        print("ok")


main()
