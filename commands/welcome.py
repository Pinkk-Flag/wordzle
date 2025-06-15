from termcolor import colored

def run():
    ascii_art = r"""
 __        __     _                                _         
 \ \      / /___ | |  ___  ___   _ __ ___    ___  | |_  ___  
  \ \ /\ / // _ \| | / __|/ _ \ | '_ ` _ \  / _ \ | __|/ _ \ 
   \ V  V /|  __/| || (__| (_) || | | | | ||  __/ | |_| (_) |
    \_/\_/  \___||_| \___|\___/ |_| |_| |_| \___|  \__|\___/ 
 __        __               _       _        _  _  _         
 \ \      / /___   _ __  __| | ____| |  ___ | || || |        
  \ \ /\ / // _ \ | '__|/ _` ||_  /| | / _ \| || || |        
   \ V  V /| (_) || |  | (_| | / / | ||  __/|_||_||_|        
    \_/\_/  \___/ |_|   \__,_|/___||_| \___|(_)(_)(_)        
                                                                       
    """

    print(colored(ascii_art, "light_green"))



    print("Type", colored('help', "light_magenta", attrs=["bold"]), "below to get help on how to get started, else, type", colored('play', "light_magenta", attrs=["bold"]) ,"to start playing!")

    print("\n")

