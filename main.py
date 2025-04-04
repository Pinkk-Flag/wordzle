import commands
import os
from dotenv import load_dotenv


commands.__all__["welcome"].run()  # Run welcome.py's function

while True:
    command = input("What do you wish to do: ").strip().lower()

    if command in commands.__all__:
        commands.__all__[command].run()  # Run the corresponding command
    elif command == "q":
        commands.__all__["end"].run()
        break
    else:
        print("Unknown command. Try again.")
