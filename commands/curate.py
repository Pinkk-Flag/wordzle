from wordfreq import top_n_list

wordlist = top_n_list("en", 20000)

def curate():

    lower = 3
    upper = 10
    i = lower
    
    
    import os
    os.makedirs("wordlists", exist_ok=True)
    
    while i <= upper:
        wordzlearray = filtercuratation(i)
        with open(f"wordlists/{i}.txt", "w") as f:
            for word in wordzlearray:
                f.write(word + "\n")
        
        i += 1
    

def filtercuratation(word_length):
    filtered_words = []
    for word in wordlist:
        if len(word) == word_length:
            filtered_words.append(word)
    return filtered_words


curate()