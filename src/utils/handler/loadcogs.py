import os

directory = os.path.dirname(__file__) + "\..\..\commands"
initial_extension = []

for root, dirs, files in os.walk(directory):
    for file in files:
        if "pycache" not in root and not file.startswith("__init__") and file.endswith(".py"):
            initial_extension.append(f"commands.{os.path.basename(root)}.{file[:-3]}")

for filename in os.listdir(os.path.dirname(__file__) + "\..\..\event"):
    if filename.endswith(".py"):
        initial_extension.append("event." + filename[:-3])