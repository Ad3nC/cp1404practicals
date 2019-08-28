import random

NUMBERS = 6
LOWEST = 1
HIGHEST = 45


def main():
    quick_picks = int(input(" how many quick picks would you like to generate "))
    for i in range(quick_picks):
        quick_set = []
        for n in range(NUMBERS):
            number = random.randint(LOWEST, HIGHEST)
            quick_set.append(number)
        quick_set.sort()
        print(quick_set)


main()
