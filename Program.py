import random
#Normal difficulty
#  Operators:
OPERATORS = ['* or /', '+ or -']
OPERATORS_CHANCES = [0.5, 0.5]
amount_of_operations = [15, 18, 21, 24, 27]
AMOUNT_OF_OPERATIONS_CHANCES = [0.15, 0.2, 0.3, 0.2, 0.15]
amount_of_operations = random.choices(amount_of_operations, weights=AMOUNT_OF_OPERATIONS_CHANCES, k=1)
USER_OPERATIONS =  random.choices(OPERATORS, weights=OPERATORS_CHANCES, k=amount_of_operations[0])
#  Game settings:
BURN_HEIGHT = random.randint(800, 3300)
GAME_MODE = 'Normal'
ACCEPTED_NUMBERS = [str(i) for i in range(10) if i != 0]
# INIT:
high_score = "0"
amount_of_moves = 0
prefix = ""
while True:
    print(f"Input your number! [{ACCEPTED_NUMBERS[0]}-{ACCEPTED_NUMBERS[-1]}]")
    number = input("->: ")
    if number in ACCEPTED_NUMBERS:
        number = number
        break
    print(f"Sorry. {number} is not an allowed number!\n")
    
while len(USER_OPERATIONS) > 0:
    print(f"\nYour number: {number}")
    print(f"Burn height: {BURN_HEIGHT}")
    print(f"Your high score: {high_score}")
    print("Pick an operator: ")
    print(f"{OPERATORS[0]} [{USER_OPERATIONS.count(OPERATORS[0])}x]")
    print(f"{OPERATORS[1]} [{USER_OPERATIONS.count(OPERATORS[1])}x]")
    if number[0] == "-": prefix = "-"
    chosen_operator = input("->: ")
    if [v for _,v in enumerate(USER_OPERATIONS) if chosen_operator in v]:
        match chosen_operator:
            case "*":
                print(f"{number}*{int(str(number)[0])}")
                number = int(number * int(str(number)[0]))
                amount_of_moves = amount_of_moves+1
            case "/":
                print(f"{number}/{int(str(number)[0])}")
                number = int(number / int(str(number)[0]))
                amount_of_moves = amount_of_moves+1
            case "+":
                print(f"{number}+{sum([int(v) for v in list(str(number))])}")
                number = int(number + sum([int(v) for v in list(str(number))]))
                amount_of_moves = amount_of_moves+1
            case "-":
                print(f"{number}-{sum(i for i in number)}")
                number = int(number - sum([int(v) for v in list(str(number))]))
                amount_of_moves = amount_of_moves+1
        if (number == 0): number = -2
        elif (number > int(high_score)): high_score = str(number)
        if (number > BURN_HEIGHT): 
            print("We're sorry you lost!")
            print(f"Your number: {number}, is larger then burn number: {BURN_HEIGHT}")
            with open('HighScores.txt', "a") as f:
                f.write(f"High score: *\n")
                f.write(f" -Amount of moves: {amount_of_moves}\n")
            break
        operator_quantity_check = str([v for _,v in enumerate(USER_OPERATIONS) if chosen_operator in v][0])
        if(operator_quantity_check): #remove used operation
            USER_OPERATIONS.remove(operator_quantity_check)
        else:
            print(f"Nope, no more \"{chosen_operator}\" left over. sorry!")
        if number <= 0 and len(USER_OPERATIONS) <= 0: #win condition
            print(f"You win! Your high score was: {high_score}") 
            with open('HighScores.txt', "a") as f:
                f.write(f"High score: {high_score}\n")
                f.write(f" -Amount of moves: {amount_of_moves}\n")
        elif len(USER_OPERATIONS) <= 0:
            print(f"Your number: {number}")
            print("We're sorry you lost!")
            with open('HighScores.txt', "a") as f:
                f.write(f"High score: F\n")
                f.write(f" -Amount of moves: {amount_of_moves}\n")
    else:
        print("Invalid operator. Please choose another one.")
