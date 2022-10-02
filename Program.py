from numpy import random
BURN_HEIGHT = 250
with open('Settings.txt', 'r') as s:
    settings_file = s.readlines()
operator_chances = settings_file[settings_file.index("  Operators:\n")+1:settings_file.index("  Accepted numbers:\n")-1]
accepted_numbers = settings_file[settings_file.index("  Accepted numbers:\n")+1:settings_file.index("Guide:\n")-1]
OPERATIONS = random.choice([value[4:5] for value in operator_chances], p=[value[7:13] for value in operator_chances], size=(20))
operators = [value[4:5] for value in operator_chances]
accepted_numbers = {number[4:5] for number in accepted_numbers}
while True:
    print("Input your number! [0-9]")
    number = input("->: ")
    if number in accepted_numbers:
        number = int(number)
        break
    print(f"Sorry. {number} is not an allowed number!\n")
while len(operator_chances) > 0:
    print(f"\nYour number: {number}")
    print(f"Burn height: {BURN_HEIGHT}")
    print(f"{number} ? {number}")
    print("Pick an operator: ", end="")
    print(*operators)
    chosen_operator = input("->: ")
    if chosen_operator in operators:
        match chosen_operator:
            case "^": number = int(number**number)
            case "*": number = int(number*number)
            case "/": number = int(number/number)
            case "+": number = int(number+number)
            case "-": number = int(number-number)
        if number == 0: number = 1
