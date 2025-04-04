import os

def update_env_variable(variable_name, new_value, env_file="settings.env"):
    # Read the current content of the .env file
    with open(env_file, "r") as file:
        lines = file.readlines()

    # Update the variable if it exists
    updated = False
    for i, line in enumerate(lines):
        if line.startswith(variable_name + "="):
            lines[i] = f"{variable_name}={new_value}\n"
            updated = True
            break

    # If the variable is not found, add it at the end
    if not updated:
        lines.append(f"{variable_name}={new_value}\n")

    # Write the updated content back to the .env file
    with open(env_file, "w") as file:
        file.writelines(lines)

    print(f"Updated {variable_name} to {new_value} in {env_file}.")

def run():
    env_file = "settings.env"
    with open(env_file, "r") as file:
        content = file.readlines()

    print("\nCurrent environment variables in .env file:")
    for line in content:
        # Skip empty lines and comments
        if line.strip() and not line.startswith("#"):
            print(line.strip())

    variable = input("Enter the variable you want to update: ").strip().upper()
    new_value = input(f"Enter the new value for {variable}: ").strip().upper()

    update_env_variable(variable, new_value)