def calculate_total():
    total = 0

    for i in range(5):
        number = int(input("Enter a number: "))
        total += number

    print("The running total is:", total)


def main():
    calculate_total()


if __name__ == "__main__":
    main()