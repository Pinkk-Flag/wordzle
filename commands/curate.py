import requests


def curate():
    res = requests.get("https://raw.githubusercontent.com/first20hours/google-10000-english/refs/heads/master/google-10000-english-no-swears.txt")
    wordlist = res.text
    
    
    lower = 3
    upper = 10
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