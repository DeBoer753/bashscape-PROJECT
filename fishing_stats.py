# TOOLSHED
import random
import sys
import config
import math
import os
from time import sleep
from colorama import Fore, Back, Style
line_divider = """------------------------------------------------------------"""
space_divider = """ """




# Fishing Lvl 0 - 1
def fishing(): 
    print(f"{Style.BRIGHT}A Nearby Channel{Style.NORMAL}")
    print(line_divider)

    if config.fishing_lvl <= 1:
        fish_types = ["generic fish 🐟"]
        randomized_fish_types = random.choice(fish_types)
        for _ in range(5):  # Change to control no. of 'blinks'
            print("fishing...", end='\r')
            sleep(0.5)  # To create the blinking effect
            sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
            sleep(0.5)
        fish_chosen = randomized_fish_types
        config.inventory += fish_chosen[-1]
        config.fishing_lvl += 0.3
        print(f"✨You caught {Style.BRIGHT}{fish_chosen}{Style.NORMAL}!✨")
        if config.fishing_lvl >= 1 and config.fishing_lvl <= 1.2 :
            print(f"✨You reached lvl {Style.BRIGHT}{int(config.fishing_lvl)}{Style.NORMAL} fishing!✨")
            print(f"✨You can now catch {Style.BRIGHT}shrimp{Style.NORMAL} 🦐!✨")
        print(space_divider)
        input("(press enter to exit)")
        return


# Fishing Lvl 5 - 15
    if config.fishing_lvl > 1 and config.fishing_lvl <= 5:
        fish_types = ["shrimp 🦐", "generic fish 🐟", "generic fish 🐟"]
        randomized_fish_types = random.choice(fish_types)
        for _ in range(15):  # Change to control no. of 'blinks'
            print("You cast your net...", end='\r')
            sleep(0.5)  # To create the blinking effect
            sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
            sleep(0.5)
        fish_chosen = randomized_fish_types
        config.inventory += str(fish_chosen)
        config.fishing_lvl += 0.345
        print(f"✨You caught {Style.BRIGHT}{fish_chosen}{Style.NORMAL}!✨")
        if config.fishing_lvl >= 5 and config.fishing_lvl <= 5.2 :
            print(f"✨You reached lvl {Style.BRIGHT}{int(config.fishing_lvl)}{Style.NORMAL} fishing!✨")
            print(f"✨You can now catch {Style.BRIGHT}squid{Style.NORMAL} 🦑!✨")
        print(space_divider)
        input("(press enter to exit)")
        return
        


















