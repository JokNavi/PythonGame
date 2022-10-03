from numpy import random
BURN_HEIGHT = 250
high_score = 0
with open('Settings.txt', 'r') as s:
    settings_file = s.readlines()
operator_chances = settings_file[settings_file.index("    Operators:\n")+1:settings_file.index("    Accepted numbers:\n")-1]
accepted_numbers = settings_file[settings_file.index("    Accepted numbers:\n")+1:settings_file.index("    Amount of operations:\n")-1]
game_mode = settings_file[settings_file.index("  Game mode:\n")+1:settings_file.index("Guide:\n")-1]
game_mode = str(*game_mode).lstrip("    ").rstrip("\n")
amount_of_operations = settings_file[settings_file.index("    Amount of operations:\n")+1:settings_file.index("  Master level:\n")-1]
amount_of_operations = [str(operation).lstrip("      ").rstrip("\n")for operation in amount_of_operations]
AMOUNT_OF_OPERATIONS = random.choice([value[0:2] for value in amount_of_operations], p=[value[3:8] for value in amount_of_operations], size=(1)).tolist()
OPERATIONS = random.choice([value[6:12] for value in operator_chances], p=[value[13:18] for value in operator_chances], size=(int(AMOUNT_OF_OPERATIONS[0]))).tolist()
operators = []
for i in range(2):
    operators.append(operator_chances[i][11:12])
    operators.append(operator_chances[i][6:7])
accepted_numbers = [str(number).lstrip("    ").rstrip("\n")for number in accepted_numbers]
while True:
    print("Input your number! [0-9]")
    number = input("->: ")
    if number in accepted_numbers:
        number = int(number)
        break
    print(f"Sorry. {number} is not an allowed number!\n")
while len(OPERATIONS) > 0:
    print(f"\nYour number: {number}")
    print(f"Burn height: {BURN_HEIGHT}")
    print(f"Your high score: {high_score}")
    print("Pick an operator: ")
    print(f"{operators[0]} or {operators[1]}", end="")
    print(f"  [{ OPERATIONS.count(str(operator_chances[0][6:12]))}]")
    print(f"{operators[2]} or {operators[3]}", end="")
    print(f"  [{OPERATIONS.count(str(operator_chances[1][6:12]))}]", end="\n\n")
    chosen_operator = input("->: ")
    if chosen_operator in operators:
        match chosen_operator:
            case "^":
                if game_mode == "Numbered":
                    print(f"->:{[number][0]}^{[number][0]}")
                    number = int([number][0]**[number][0])
            case "*":
                print(f"->:{number}*{[number][0]}")
                number = int(number * [number][0])
            case "/":
                print(f"->:{number}/{[number][0]}")
                number = int(number / [number][0])
            case "+":
                print(f"->:{number}+{sum([number])}")
                number = int(number + sum([number]))
            case "-":
                print(f"->:{number}-{sum([number])}")
                number = int(number - sum([number]))
        if number == 0:
            number = -5
        elif number > BURN_HEIGHT:
            print("We're sorry you lost!")
            break
        if chosen_operator in list(str([item for item in OPERATIONS])):
            f = [value for value in OPERATIONS if chosen_operator in value]
            OPERATIONS.remove(f[0])
        else:
            print(f"Nope, no more \"{chosen_operator}\" left over. sorry!")
        if number > high_score:
            high_score = number
        if len(OPERATIONS) <= 0:
            if number <= 0:
                print(f"You win! Your high score was: {high_score}")
            else:
                print(f"Your number: {number}")
                print("We're sorry you lost!")
    else:
        print("Invalid operator. Please choose another one.")
