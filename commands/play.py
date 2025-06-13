from termcolor import colored
import os
import random


def run():
    env_file = "settings.env"
    
    wordlength_value = 5
    with open(env_file, "r") as file:
        # Read all lines from the file
        lines = file.readlines()
    

    for line in lines:

        if line.strip().startswith("WORDLENGTH="):
            wordlength_value = line.split('=')[1].strip()
            break
    
    os.chdir("wordlists")
    print(os.getcwd()) 
    with open(f"{wordlength_value}.txt") as textfile:
        lines = len(textfile.readlines())
        
    """ TODO - Create a random number based on the number of lines and then afterwards pick a word from this list. 
    
    After that, create an array and then prompt the user.
    Think of creative ways to show ouput. 
    """
    
    
    os.chdir("..")