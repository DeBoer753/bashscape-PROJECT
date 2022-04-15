# TOOLSHED
import math
import random
import os
import sys
import config
from colorama import Fore, Back, Style
line_divider = """------------------------------------------------------------"""
space_divider = """ """





# QUESTS 
def farmer_peesh(username): # add arguments 
        os.system('clear')
        print(f"{Style.BRIGHT}A Farmers Dillemma{Style.NORMAL}")
        print(line_divider)
        yes_or_no = input(f"""Farmer Peehs: "You there! Traveler! Care to help me shear my sheep?"
Yes/No?: """)
        print(space_divider)
        if yes_or_no.lower() == "no" or yes_or_no.lower() != "yes":
            input("Farmer Peehs: \"Then what good are yuh then huh? Go on..Get!\"")   
            print(space_divider)
            input("(press enter to exit)")
            os.system('clear')
            return
        if yes_or_no.lower() == "yes":
                os.system('clear')
                print(f"{Style.BRIGHT}A Farmers Dillemma{Style.NORMAL}")
                print(line_divider)
                input("Farmer Peehs: \"Excellent! Find me a pair of shears would yuh? I can't seem to find mine.\"")
                print(space_divider)
                input("(press enter to continue)")
                print(space_divider)
        while True:
            os.system('clear')
            print(f"{Style.BRIGHT}A Farmers Dillemma{Style.NORMAL}")
            print(line_divider)
            find_sheers = input("""Press (1) to check the barn
Press (2) to check the toolshed
Press (3) to check Farmer Peehs' backside pocket
Enter option here: """)
            os.system('clear')
            if find_sheers == "1":
                print(f"{Style.BRIGHT}A Farmers Dillemma{Style.NORMAL}")
                print(line_divider)
                input(f"{username}: \"Hmmm...nope nothing...\"")
                print(space_divider)
                input("(press enter to try again)")
            os.system('clear')
            if find_sheers == "2":
                print(f"{Style.BRIGHT}A Farmers Dillemma{Style.NORMAL}")
                print(line_divider)
                input(f"{username}: \"Damn! I could have sworn they would have been here!\"")
                print(space_divider)
                input("(press enter to try again)")
                os.system('clear')
            if find_sheers == "3":
                print(f"{Style.BRIGHT}A Farmers Dillemma{Style.NORMAL}")
                print(line_divider)
                input(f"\"{username}: \"They're in your pocket!\"")
                print(space_divider)
                input("(press enter to continue)")
                os.system('clear')
                print(f"{Style.BRIGHT}A Farmers Dillemma{Style.NORMAL}")
                print(line_divider)
                input(f"""Farmer Peehs: "Oh dear, my age has really taken a toll on me. 
Or perhaps it was the bar fight I got into with Farmer Gip at the tavern last night...
Eh, whatever it is, I shouldn't dwell on it! There's more to life than dwelling!
Thank you {username}! Here take this..You earned it kid.\"""") 
                print(space_divider)
                input("(press enter to continue)")
                os.system('clear')
                print(f"{Style.BRIGHT}A Farmers Dillemma{Style.NORMAL}")
                print(line_divider)
                input("✨You earned" + Style.BRIGHT + " 5 " + Fore.BLUE + "QP 💠 " + Style.NORMAL + Fore.WHITE +  "and " + Style.BRIGHT + "300 " + Fore.YELLOW + "GP 💰" + Fore.WHITE + "!✨" + Style.NORMAL)
                print(space_divider)
                input("(press enter to exit quest)")
                os.system('clear')
                config.bank += 300
                config.quest_points += 5
                return
                
              
                



