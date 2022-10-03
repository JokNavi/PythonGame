from numpy import random
BURN_HEIGHT = 250
with open('Settings.txt', 'r') as s:
    settings_file = s.readlines()
operator_chances = settings_file[settings_file.index("  Operators:\n")+1:settings_file.index("  Accepted numbers:\n")-1]
accepted_numbers = settings_file[settings_file.index("  Accepted numbers:\n")+1:settings_file.index("  Master level:\n")-1]
game_mode = settings_file[settings_file.index("  Game mode:\n")+1:settings_file.index("Guide:\n")-1]
game_mode = str(*game_mode).lstrip("    ").rstrip("\n")
OPERATIONS = random.choice([value[4:10] for value in operator_chances], p=[value[12:16] for value in operator_chances], size=(20)).tolist()
operators = []
operators.append([line[9:10] for line in operator_chances])
operators.append([line[4:5] for line in operator_chances])
accepted_numbers = [int(str(number).lstrip("    ").rstrip("\n")) for number in accepted_numbers]
while True:
    print("Input your number! [0-9]")
    number = input("->: ")
    if int(number) in accepted_numbers:
        number = int(number)
        break
    print(f"Sorry. {number} is not an allowed number!\n")
while len(operator_chances) > 0:
    print(f"\nYour number: {number}")
    print(f"Burn height: {BURN_HEIGHT}")
    print(f"{number} ? {number}")
    print("Pick an operator: ")
    print(*[op for op in operators[0]], sep=" or ", end ="")
    print(f"  [{ OPERATIONS.count(str(operator_chances[1][4:10]))}]")
    print(*[op for op in operators[1]], sep=" or ", end="")
    print(f"  [{OPERATIONS.count(str(operator_chances[0][4:10]))}]", end="\n\n")
    chosen_operator = input("->: ")
    if chosen_operator in operators[0] or chosen_operator in operators[1]:
        match chosen_operator:
            case "^":
                if game_mode == "Numbered": number = int([number][0]^[number][0])
            case "*":number = int(number * [number][0])
            case "/":number = int(number / [number][0])
            case "+":number = int(number + sum([number]))
            case "-":number = int(number - sum([number]))
        if number == 0: number = 1
        elif number > BURN_HEIGHT: 
            print("We're sorry you lost!")
            break
        OPERATIONS.remove([group for group in OPERATIONS if chosen_operator in group][0])   
    else:print("Invalid operator. Please choose another one.")
