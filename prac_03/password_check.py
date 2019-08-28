def main():
    password = get_password()

    print("*" * len(password))


def get_password():
    password = input("Enter a password")
    while len(password) < 5:
        password = input("Enter a password")
    return password


main()
