from termcolor import colored
def run():
    print(colored("Welcome to Wordzle, a clone of Wordle that allows for unlimited tries in the game, including extra configuration that allows for longer/shorter words, tries, etc.", "light_blue"))
    print()
    print("Tying 'play' will begin playing the game. ")
    print()
    print("To find the rules of the game, go to this site: https://www.nytimes.com/2023/08/01/crosswords/how-to-talk-about-wordle.html")
    print()
    print(colored("Each command: ", "red", attrs=["underline"]))
    print()
    print(colored("`play` Command: ", "green", attrs=["bold"]))
    print("Begins playing the game with consideration of the settings you have within  `settings.env`. Functions similar to the real game. Have fun :)")

    
    print()
    print(colored("`curate` Command: ", "blue", attrs=["bold"]))
    print("Recollects and synchronises your system with the words that are found within the website.")
    print(colored("Please note that you will need an internet connection for this!", attrs=["bold"]))
    
    print()
    print(colored("`delete` Command: ", "blue", attrs=["bold"]))
    print("Removes all the words you have stored. Potentially harmful and may stop the functioning of the program")
    
    print()
    print(colored("`update` Command: ", "blue", attrs=["bold"]))
    print("Allows you to update any in game settings. It will display the current settings, and prompt you to type out the name of the setting you wish to change (note, must be identical spelling) and then afterwards a value you wish to assign.")
    print()
    print("All other commands are relatively irrelevant.")