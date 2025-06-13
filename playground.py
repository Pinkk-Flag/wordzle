import os

print(os.getcwd())



def run():
    print(os.getcwd())
    os.chdir("wordlists")
    filelist = os.listdir()
    for file in filelist:
        
        # print("file value in loop: ", file)
        # print("Type of value of file var: ", type(file))
        
        if file[-3:] == "txt":
            os.remove(file)
            # print("Hit a text file with name: ", file)
        
run()