from numpy import random
MAX_SCORES = 250
with open('Settings.txt', 'r') as s:
    settings_file = s.readlines()
operator_chances = settings_file[settings_file.index("Settings:\n")+1:settings_file.index("Guide:\n")-1]
OPERATIONS = random.choice([value[4:5] for value in operator_chances], p=[value[7:13] for value in operator_chances], size=(20))
print(OPERATIONS)

print("Choose your number")
chosen_number = input("->: ")

#'    ^  0.1\n'