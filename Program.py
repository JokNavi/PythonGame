import random
#Normal difficulty
# Operators:
OPERATORS = ['* or /', '+ or -']
OPERATORS_CHANCES = [0.5, 0.5]
amount_of_operations = [21, 25, 28, 32, 35]
AMOUNT_OF_OPERATIONS_CHANCES = [0.15, 0.2, 0.3, 0.2, 0.15]
amount_of_operations = random.choices(amount_of_operations, weights=AMOUNT_OF_OPERATIONS_CHANCES, k=1)
USER_OPERATIONS =  random.choices(OPERATORS, weights=OPERATORS_CHANCES, k=amount_of_operations[0])
# Game settings:
BURN_HEIGHT = random.randint(3250, 5300)
GAME_MODE = 'Normal'
ACCEPTED_NUMBERS = [str(i) for i in range(10) if i != 0]
# Highscores.py:
high_score = 0
amount_of_moves = 0
# Init
def print_output_file(high_score):
    with open('HighScores.txt', "a") as f:
        f.write(f"\nHigh score: {high_score}\n")
        f.write(f" -Amount of moves: {amount_of_moves}\n")

while True:
    print(f"Input your number! [{ACCEPTED_NUMBERS[0]}-{ACCEPTED_NUMBERS[-1]}]")
    number = input("->: ")
    if number in ACCEPTED_NUMBERS:
        print("")
        break
    print(f"Sorry. {number} is not an allowed number!\n")
    
while len(USER_OPERATIONS) > 0:
    print(f"Your number: {number}")
    print(f"Burn height: {BURN_HEIGHT}")
    print(f"Your high score: {high_score}")
    print("Pick an operator: ")
    print(f"{OPERATORS[0]} [{USER_OPERATIONS.count(OPERATORS[0])}x]")
    print(f"{OPERATORS[1]} [{USER_OPERATIONS.count(OPERATORS[1])}x]")
    chosen_operator = input("->: ")
    if [v for _,v in enumerate(USER_OPERATIONS) if chosen_operator in v]:
        number_list = []
        if number[0] == "-": 
            number_list.append(number[0:2])
            number_list.extend([number[2:]])                    
        elif len(number) > 0: number_list = number
        match chosen_operator:
            case "*":
                print(f"{number} * {int(number_list[0])}")
                number = str(int(int(number) * int(number_list[0])))
            case "/":
                print(f"{number} / {int(number_list[0])}")
                number = str(int(int(number) / int(number_list[0])))
            case "+":
                print(f"{number} + {sum(int(d) for d in number_list)}")
                number = str(int(int(number) + sum(int(d) for d in number_list)))
            case "-":
                print(f"{number} - {sum(int(d) for d in number_list)}")
                number = str(int(int(number) - sum(int(d) for d in number_list)))
        if number == "0": number = "-5"
        if int(number) > high_score: high_score = int(number)
        operator_quantity_check = [v for _,v in enumerate(USER_OPERATIONS) if chosen_operator in v]
        if(operator_quantity_check): #remove used operation
            USER_OPERATIONS.remove(operator_quantity_check[0])
        else:
            print(f"Nope, no more \"{chosen_operator}\" left over. sorry!")
        if (int(number) > BURN_HEIGHT): 
            print("We're sorry you lost!")
            print(f"Your number: {number}, is larger then burn number: {BURN_HEIGHT}")
            print_output_file("*")
            break
        elif int(number) <= 0 and len(USER_OPERATIONS) <= 0: #win condition
            print(f"You win! Your high score was: {high_score}") 
            print_output_file(high_score)
            break
        elif len(USER_OPERATIONS) <= 0:
            print(f"Your number: {number}")
            print("We're sorry you lost!")
            print_output_file("F")
            break
    else:
        print("Invalid operator. Please choose another one.")
