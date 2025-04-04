import os
import importlib

# Get all Python files in the `commands` folder (excluding __init__.py)
modules = [
    f[:-3] for f in os.listdir(os.path.dirname(__file__)) 
    if f.endswith(".py") and f != "__init__.py"
]

# Dynamically import all modules
__all__ = {}
for module in modules:
    imported_module = importlib.import_module(f"commands.{module}")
    __all__[module] = imported_module  # Store them in a dictionary
