# TOOLSHED
import os
import math
import random
import getpass
import stdiomask 
import sys
import config
from tkinter import Menu
from time import sleep
from colorama import Fore, Back, Style
from log_out_function import logging_out
from fishing_stats import fishing
from quests import farmer_peesh
line_divider = """------------------------------------------------------------"""
space_divider = """ """






# import playsound 
# playsound('/Users/myles_deboer/Projects/project_game/6inMx8Ya9IxF.128.mp3')

# Intro:
os.system('clear') 
for _ in range(5):  # Change to control no. of 'blinks'
    print(f"{Style.BRIGHT}WELCOME TO BASHSCAPE ⌺{Style.NORMAL}", end='\r')
    sleep(0.5)  # To create the blinking effect
    sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
    sleep(0.5)
print(Style.BRIGHT + "WELCOME TO BASHSCAPE ⌺" + Style.NORMAL)
print(line_divider)
input("(press enter)")
os.system('clear') 
print(line_divider)
os.system('clear') 






# Choose Gender:
while True: 
    print(Style.BRIGHT + "Create An Account ⌺" + Style.NORMAL)
    print(line_divider)
    gender = input("Are you male (m) or female? (f): ").lower()
    if gender == "male" or gender == "m":
        gender = "he"
        break
    if gender == "female" or gender == "f":
        gender = "she"
        break
    if gender != "male" or gender != "m" or gender != "female" or gender != "f":
        os.system('clear') 


# Create Account:
while True:  
    os.system('clear') 
    print(Style.BRIGHT + "Create Username ⌺" + Style.NORMAL)
    print(line_divider)
    username = str(input("Username: "))
    os.system('clear') 
    break


# Create Account:
while True:
    os.system('clear')
    print(Style.BRIGHT + "Create Password ⌺" + Style.NORMAL)
    print(line_divider)
    password = str(stdiomask.getpass()) 
    os.system('clear')
    print(Style.BRIGHT + "Confirm Password ⌺" + Style.NORMAL)
    print(line_divider)
    confirm_password = str(stdiomask.getpass()) 
    os.system('clear')
    if password != confirm_password:
        print(Style.BRIGHT + "Create Password ⌺" + Style.NORMAL)
        print(line_divider)
        input("Password: (password did not match)")
    elif password == confirm_password:
        break


# Main Menu:
while True: 
    os.system('clear')
    print(Style.BRIGHT + "Main Menu ⏇" + Style.NORMAL)
    print(line_divider)
    user_input = input("""Press (1) to start quest
Press (2) to level up
Press (3) to view stats
Press (4) to view inventory
Press (L) to log out
Enter option here: """)





# Press 1:
    os.system('clear')   
    if user_input == "1":
        print(f"{Style.BRIGHT}Quest List ⍟{Style.NORMAL}")
        print(line_divider)
        quest_choice = input(f"""Quest Master: "Ohhh...{username} fancys a quest does {gender}? Pick a quest! ANY QUEST!" 

1. Help Farmer Peehs sheer his sheep - 5 Quest pts 
2. Assist Khomas Teller in helping him cook his famous scrambled eggs - 15 Quest pts (Members)
Enter (1-2) to choose a quest: """)
        print(space_divider)
        os.system('clear') 
        if quest_choice == "1":
            print(line_divider)
            farmer_peesh(username)
            os.system('clear')   
        if quest_choice == "2":
            print(f"{Style.BRIGHT}Holy Water Scrambled Eggs{Style.NORMAL}")
            print(line_divider)
            input("⭐️ You must be a member to access this quest ⭐️")
            print(space_divider)
            input("(press enter to exit)")
            os.system('clear') 
            print(line_divider)





# Press 2:        
    if user_input == "2":
        print(f"{Style.BRIGHT}BashScape ⌺{Style.NORMAL}")
        print(line_divider)
        level_up_choice = input("""Press (1) to start fishing
Press (2) to start cooking
Enter option here: """)
        if level_up_choice == "1":
            os.system('clear') 
            fishing()
        if level_up_choice == "2":
            os.system('clear') 
            print(f"{Style.BRIGHT}Fire Pit{Style.NORMAL}")
            print(line_divider)
            input("⭐️ You must be a member to access this lvl ⭐️")
            print(space_divider)
            input("(press enter to exit)")
            os.system('clear') 





# Press 3:
    if user_input == "3":
        print(f"{Style.BRIGHT}Stats ⏃{Style.NORMAL}")
        print(line_divider)
        viewing_key = input("""Press (1) to view levels
Press (2) to view quest points
Enter option here: """)
        os.system('clear') 
        if viewing_key != "1" or viewing_key != "2":
            os.system('clear') 
        if viewing_key == "1":
            print(line_divider)
            os.system('clear') 
            while True:
                print(f"{Style.BRIGHT}Level Field ⍜{Style.NORMAL}")
                print(line_divider)
                fishing_or_cooking = input("""(1) to view fishing lvl
(2) to view cooking lvl
Enter option here: """)
                try: 
                    fishing_or_cooking == "1" or fishing_or_cooking == "2"
                except:
                    os.system('clear') 
                if fishing_or_cooking != "1" or fishing_or_cooking != "2":
                    os.system('clear') 
                if fishing_or_cooking == "1":
                    print(f"{Style.BRIGHT}Fishing Lvl ♒︎{Style.NORMAL}")
                    print(line_divider)
                    input(f"🎣: You currently have a lvl {Style.BRIGHT}{int(config.fishing_lvl)}{Style.NORMAL} in fishing")
                    print(space_divider)
                    input("(press enter to exit)")
                    os.system('clear') 
                    break
                if fishing_or_cooking == "2":
                    print(f"{Style.BRIGHT}Cooking Lvl ♨︎{Style.NORMAL}")
                    print(line_divider)
                    input("⭐️ You must be a member to access this lvl ⭐️")
                    print(space_divider)
                    input("(press enter to exit)")
                    break
        if viewing_key == "2":
            print(f"{Style.BRIGHT}Quest Points ⏣{Style.NORMAL}")
            print(line_divider)
            input(f"💠: You currently have {Style.BRIGHT}{config.quest_points} {Fore.BLUE}QP{Style.NORMAL}{Fore.WHITE}")
            print(space_divider)
            input("(press enter to exit)")
            os.system('clear') 






# Press 4:
    if user_input == "4":
        print(f"{Style.BRIGHT}Inventory ⏍{Style.NORMAL}")
        print(line_divider)
        while True: 
            access_key = input("""Press (1) to access items
Press (2) to access bank account
Enter option here: """)
            try:
                access_key == "1" or access_key == "2"
            except:
                os.system('clear') 
            if access_key != "1" or access_key != "2":
                os.system('clear') 
            if access_key == "1":
                print(f"{Style.BRIGHT}Items ❐{Style.NORMAL}")
                print(line_divider)
                input(str(config.inventory))
                print(space_divider)
                input("""(press enter to exit)""")
                break 
            break
            
        if access_key == "2":
            print(f"{Style.BRIGHT}BashScape Bank ⍧{Style.NORMAL}")
            print(line_divider)
            input(f"💰: You currently have {Style.BRIGHT}{config.bank} {Fore.YELLOW}GP{Style.NORMAL}{Fore.WHITE}")
            print(space_divider)
            input("(press enter to exit)")
            os.system('clear') 





# Press L:
    if user_input.upper() == "L":
        for _ in range(5):  # Change to control no. of 'blinks'
            print(f"{Style.BRIGHT}Logging out....{Style.NORMAL}", end='\r')
            sleep(0.5)  # To create the blinking effect
            sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
            sleep(0.5)
        print(f"{Style.BRIGHT}Goodbye...{Style.NORMAL}")
        print(line_divider)
        logging_out(username)
        break
        


# END OF PAGE