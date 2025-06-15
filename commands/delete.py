import os


def run():
    os.chdir("wordlists")
    filelist = os.listdir()

    for file in filelist:
        
        if file[-3:] == "txt":
            os.remove(file)
    os.chdir("..")