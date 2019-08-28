"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)


choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        temperature = float(input("Celsius:"))
        print("Result: {:.2f} F".format(fahrenheit_calculation(temperature)))
    elif choice == "F":
        temperature = float(input("Fahrenheit: "))
        print("Result: {:.2f} C".format(celcius_calculation(temperature)))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")


def fahrenheit_calculation(temperature):
    fahrenheit = temperature * 9.0 / 5 + 32
    return fahrenheit


def celcius_calculation(temperature):
    celcius = 5 / 9 * (temperature - 32)
    return celcius


main()
