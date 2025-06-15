from termcolor import colored
import os
import random

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run():
    
    wordlength_value = fetchsetting("WORDLENGTH=")
    
    os.chdir("wordlists")
    print(os.getcwd()) 
    with open(f"{wordlength_value}.txt", "r") as textfile:
        content = textfile.readlines()
        lines = len(content)
        wordnum = (random.randint(1, lines) - 1) # includes start and stop
        word = content[wordnum]
        
    os.chdir("..")    
    clearscreen()
    play(word, wordlength_value)
    
def fetchsetting(settingname):
    env_file = "settings.env"

    with open(env_file, "r") as file:
        lines = file.readlines()

    found = False
    for line in lines:
        if line.strip().startswith(settingname):
            returnvalue = line.split('=')[1].strip()
            return returnvalue
            found = True
            break

    if not found:
        raise Exception("ATTEMPTS setting not found in settings.env")

def play(target_word, wordlength_value):
    wordlist = list(target_word.lower())
    clean_wordlist = wordlist[:-1]
    
    attemptsnum = fetchsetting("ATTEMPTS=")
    guesses = []
    guessesnotxt = []
    print("Word length: ", wordlength_value)
    for i in range(int(attemptsnum)):
        print()
        userinput = str(input(colored("Enter your word here ->   ", 'red')))
        
        userword = list(userinput)
        userwordlength = len(userword)
        wordlength = len(wordlist) - 1
        #print(wordlist)
        #print("userwordlength: ", userwordlength, "and wordlength: ", wordlength)
        if userwordlength < wordlength:
            raise Exception(f"Your word is too short! Please keep it to a length of {wordlength_value}!")
        elif userwordlength > wordlength:
            raise Exception(f"Your word is too long! Please keep it to a length of {wordlength_value}!")
        else:
            pass
        guesses.append(userword)
        guessesnotxt.append(userinput)
        
        clearscreen()
        elapsedguesses = i + 1
        guessremain = int(attemptsnum) - elapsedguesses
        print("Elapsed guesses: ", elapsedguesses, "   Guesses remaining: ", guessremain)
        print()
        print(colored("Your current guesses: ", "blue", attrs=["bold"]))
        print()
        for guess_index, guess_word in enumerate(guessesnotxt):
                    # REMOVE COMMENT IF YOU WANT ANSWER: print("The word: ", target_word)
            lowercaselist = list(map(str.lower, guesses[guess_index]))

            if lowercaselist == clean_wordlist and guess_index+1==1:
                print()
                print(colored("Congratulations! You guessed the word in", 'green', attrs=['bold']), colored(f"{guess_index+1} try!", 'cyan', attrs=['bold']))
                print()
                return True
            if lowercaselist == clean_wordlist:
                print()
                print(colored("Congratulations! You guessed the word in", 'green', attrs=['bold']), colored(f"{guess_index+1} tries!", 'cyan', attrs=['bold']))
                print()
                return True 

            for char_index, char in enumerate(lowercaselist):
                colorstate = "grey"
                
                if char in wordlist:
                    colorstate = "yellow"
                    
                if char == wordlist[char_index]:
                    colorstate = "green"
                
                print(colored(char.upper(), colorstate), end=" ")
                
                    
        
            print()   
    print()
    print(colored(f"Game over! The word was: {target_word}", 'red', attrs=['bold']))
    return False 
    