from numpy import random
#Normal difficulty
#  Operators:
OPERATORS = ['* or /', '+ or -']
OPERATORS_CHANCES = [0.5, 0.5]
AMOUNT_OF_OPERATIONS = [10, 13, 15, 18, 21]
AMOUNT_OF_OPERATIONS_CHANCES = [0.15, 0.2, 0.3, 0.2, 0.15]
AMOUNT_OF_OPERATIONS = random.choice(AMOUNT_OF_OPERATIONS, p=AMOUNT_OF_OPERATIONS_CHANCES, size=(1)).tolist()
USER_OPERATIONS = random.choice(OPERATORS, p=OPERATORS_CHANCES, size=(AMOUNT_OF_OPERATIONS)).tolist()
#  Game settings:
BURN_HEIGHT = 3000
GAME_MODE = 'Normal'
ACCEPTED_NUMBERS = [str(i) for i in range(10) if i != 0]
# INIT:
high_score = 0
while True:
    print(f"Input your number! [{ACCEPTED_NUMBERS[0]}-{ACCEPTED_NUMBERS[-1]}]")
    number = input("->: ")
    if number in ACCEPTED_NUMBERS:
        number = int(number)
        break
    print(f"Sorry. {number} is not an allowed number!\n")
    
while len(USER_OPERATIONS) > 0:
    print(f"\nYour number: {number}")
    print(f"Burn height: {BURN_HEIGHT}")
    print(f"Your high score: {high_score}")
    print("Pick an operator: ")
    print(f"{OPERATORS[0]} [{USER_OPERATIONS.count(OPERATORS[0])}x]")
    print(f"{OPERATORS[1]} [{USER_OPERATIONS.count(OPERATORS[1])}x]")
    chosen_operator = input("->: ")
    if [v for _,v in enumerate(USER_OPERATIONS) if chosen_operator in v]:
        match chosen_operator:
            case "*":
                print(f"{number}*{int(list(str(number))[0])}")
                number = int(number * int(list(str(number))[0]))
            case "/":
                print(f"{number}/{int(list(str(number))[0])}")
                number = int(number / int(list(str(number))[0]))
            case "+":
                print(f"{number}+{sum([int(v) for v in list(str(number))])}")
                number = int(number + sum([int(v) for v in list(str(number))]))
            case "-":
                print(f"{number}-{sum([int(v) for v in list(str(number))])}")
                number = int(number - sum([int(v) for v in list(str(number))]))
        if (number == 0): number = 5
        elif (number > high_score): high_score = number
        if (number > BURN_HEIGHT): 
            print("We're sorry you lost!")
            print(f"Your number: {number}, is larger then burn number: {BURN_HEIGHT}")
            break
        operator_quantity_check = str([v for _,v in enumerate(USER_OPERATIONS) if chosen_operator in v][0])
        if(operator_quantity_check): #remove used operation
            USER_OPERATIONS.remove(operator_quantity_check)
        else:
            print(f"Nope, no more \"{chosen_operator}\" left over. sorry!")
        if number <= 0 and len(USER_OPERATIONS) <= 0: #win condition
            print(f"You win! Your high score was: {high_score}") 
        elif len(USER_OPERATIONS) <= 0:
            print(f"Your number: {number}")
            print("We're sorry you lost!")
    else:
        print("Invalid operator. Please choose another one.")
