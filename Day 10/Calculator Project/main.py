import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](4, 8))


def calculator():
    from art import logo
    print(logo)
    num1 = float(input("Enter first number: "))
    more_operation = True
    while more_operation:
        for symbol in operations:
            print(symbol)

        operation = input("Enter operation: ")
        num2 = float(input("Enter second number: "))

        answer = operations[operation](num1, num2)
        print(answer)

        more_operation = input("Do you want to continue? (y/n): ")
        if more_operation == "y":
            num1 = answer
        else:
            more_operations = False
            print("\n" * 20)
            calculator()






calculator()




calculator()
