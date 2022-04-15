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





# FISHING LVL
def fishing(): 
    print(f"{Style.BRIGHT}A Nearby Channel{Style.NORMAL}")
    print(line_divider)
    if config.fishing_lvl <= 3:
        fish_types_low = ["shrimp 🦐","generic fish 🐟"]
        randomized_fish_types_low = random.choice(fish_types_low)
        for _ in range(5):  # Change to control no. of 'blinks'
            print("fishing...", end='\r')
            sleep(0.5)  # To create the blinking effect
            sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
            sleep(0.5)
    print(f"✨You caught {Style.BRIGHT}{randomized_fish_types_low}{Style.NORMAL}!✨") 
    config.fishing_lvl += 1
    input(f"✨You reached lvl {Style.BRIGHT}{config.fishing_lvl}{Style.NORMAL} fishing!✨")
    print(space_divider)
    input("(press enter to exit)")
    # if config.fishing_lvl <= 10 and config.fishing_lvl >= 4:
    #     fish_types_medium = ["puffer fish 🐡","squid 🦑"]
    #     randomized_fish_types_low = random.choice(fish_types_medium)
    #     for _ in range(10):  # Change to control no. of 'blinks'
    #         print("...", end='\r')
    #         sleep(0.5)  # To create the blinking effect
    #         sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
    #         sleep(0.5)
    # print(f"✨You caught {Style.BRIGHT}{randomized_fish_types_low}{Style.NORMAL}!✨") 
    # config.fishing_lvl += 1
    # input(f"✨You reached lvl {Style.BRIGHT}{config.fishing_lvl}{Style.NORMAL} fishing!✨")
    # print(space_divider)
    # input("(press enter to exit)")        






