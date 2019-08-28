def main():
    numbers = []
    for number in range(5):
        number = int(input("enter a number"))
        numbers.append(number)
    print("the first nuuber is {}".format(numbers[0]))
    print("the last number is {}".format(numbers[4]))
    print(" the largest number is {}".format(max(numbers)))
    print(" the smallest number is {}".format(min(numbers)))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    good_username = "access granted"
    bad_username = "access denied"
    username = input("enter username")
    if username in usernames:
        print(good_username)
    else:
        print(bad_username)



main()
