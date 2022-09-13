# TOOLSHED
import math
import random
import os
import sys
import config
from colorama import Fore, Back, Style
line_divider = """------------------------------------------------------------"""
space_divider = """ """



# LOG OUT:
def logging_out(username):
    phrases_list = [f"{username} falls into a deep sleep...💤", 
    f"{username}: \"These pile of leaves will make for a decent bed tonight.\"💤",
    f"{username} spots a travelers Inn in the distance and rents a room for the night.💤", 
    f"{username} sets up camp by the stream and snores throughout the night.💤"]
    phrase = input(random.choice(phrases_list))
    print(phrase)

