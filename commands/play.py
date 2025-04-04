from termcolor import colored
env_file = "settings.env"
def run():
    wordlength_value = 5
    with open(env_file, "r") as file:
        # Read all lines from the file
        lines = file.readlines()
    

    for line in lines:

        if line.strip().startswith("WORDLENGTH="):
            wordlength_value = line.split('=')[1].strip()
            break
    
    with open("")