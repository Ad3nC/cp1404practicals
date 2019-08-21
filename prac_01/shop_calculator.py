def main():

    items = int(input("enter amount of items"))
    while items <0:
        print("number of items is invalid ")
        items = int(input("enter amount of items"))
    total = 0
    for i in range(items):
        price = float(input("enter price of items"))
        total += price

    if total >= 100:
        total = total - total * 0.1
    print(total)


main()
