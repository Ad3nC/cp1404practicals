def main():
    for i in range(1, 21, 2):
        print(i, end='')
    print()

    for i in range(0, 101, 10):
        print(i, end='\n')
    print("\n")

    for i in range(20, 0, -1):
        print(i, end='\n')
    print("\n")

    numbers = int(input("enter"))
    for i in range(numbers):
        print("*", end='')
    print("\n")

    for i in range(1, numbers + 1):
        print("*" * i)


main()
