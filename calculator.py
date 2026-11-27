"""Simple command-line calculator used to practise Git workflows."""

VERSION = "1.2"


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    return a ** b


def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot take modulo by zero")
    return a % b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
    "%": modulo,
}


def calculate(a, op, b):
    if op not in OPERATIONS:
        raise ValueError(f"Unsupported operator: {op}")
    return OPERATIONS[op](a, b)


def main():
    print(f"Simple Calculator v{VERSION}")
    print("Supported operators: " + " ".join(OPERATIONS))
    try:
        a = float(input("First number: "))
        op = input("Operator: ").strip()
        b = float(input("Second number: "))
        print("Result:", calculate(a, op, b))
    except ValueError as err:
        print("Error:", err)


if __name__ == "__main__":
    main()
