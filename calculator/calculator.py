from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def new_calculator():
    print(logo)
    first_num = float(input("What's the first number?: "))

    should_continue = True
    while should_continue:
        for operation in dictionary:
            print(operation)
        user_choice = input("Choose an operation: ")
        second_num = float(input("What's the second number?: "))
        result = dictionary[user_choice](n1= first_num, n2=second_num)
        print(f"{first_num} {user_choice} {second_num} = {result}")
        want_to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculating: ").lower()
        if want_to_continue == "n":
            should_continue = False
            print("\n"*20)
            new_calculator()
        else:
            first_num = result

new_calculator()
