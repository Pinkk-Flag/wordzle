import requests

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

def curate():
    res = requests.get("https://raw.githubusercontent.com/first20hours/google-10000-english/refs/heads/master/google-10000-english-no-swears.txt")
    wordlist = res.text
    
    
    lower = int(fetchsetting("MINWORDS="))
    upper = int(fetchsetting("MAXWORDS="))
    i = lower
    
    import os
    os.makedirs("wordlists", exist_ok=True)
    # print(os.getcwd())
    os.chdir("wordlists")
    
    while i <= upper:
        wordzlearray = filtercuratation(i)
        with open(f"{i}.txt", "w") as f:
            for word in wordzlearray:
                f.write(word + "\n")
        
        i += 1
    
    os.chdir("..")

def filtercuratation(word_length):
    res = requests.get("https://raw.githubusercontent.com/first20hours/google-10000-english/refs/heads/master/google-10000-english-no-swears.txt")
    wordlist = res.text
    filtered_words = []
    for word in wordlist.split():
        if len(word) == word_length:
            filtered_words.append(word)
    return filtered_words

def run():
    curate()
    