import art

def add(n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2


operation_dict = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    #choice = True
    print(art.logo)
    f_number = float(input("What's the first number? "))
    while True:
        operation = input("+\n-\n*\n/\nPick an operation: ")
        s_number = float(input("What's the next number? "))
        result = operation_dict[operation](f_number, s_number)
        print(f"{f_number} {operation} {s_number} = {result}")

        if input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ") == "n":
            calculator()
        else:
            f_number = result

calculator()