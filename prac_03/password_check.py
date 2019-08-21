def main():
    password = input("Enter a password")

    print("*" * len(password_check(password)))


def password_check(password):
    while len(password) < 5:
        password = input("Enter a password")
    return password


main()
