# TOOLSHED
import math
import random
line_divider = """------------------------------------------------------------"""
space_divider = """ """





print(line_divider)
# GAME PROJECT
stats = []
inventory = []
bank = 0

gender = input("Are you male (m) or female? (f): ").lower()
if gender == "male" or gender == "m":
    gender = "he"
elif gender == "female" or gender == "f":
    gender = "she"
else:
    print("Invalid entry")
    print(gender)

username = str(input("Create username: "))
password = str(input("Create password: "))

print(line_divider)
while True: 
    user_input = input("""Press (1) to start quest
Press (2) to level up
Press (3) to view stats
Press (4) to view inventory
Press (5) to change music
press (L) to log out
Enter option here: """)
    if user_input == "1":
        choose_quest = input(f"Ohhh...{username} fancy's a quest does {gender}? Pick a quest! ANY QUEST! ")
    # if user_input == "2":

    # if user_input == "3":

    # if user_input == "4":

    # if user_input == "5":

    if user_input.upper() == "L":
        # randomized log out quotes
        break

print(line_divider)
# END OF PAGE