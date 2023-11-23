import os

directory = os.path.dirname(__file__) + "\..\..\commands"
initial_extension = []

for root, dirs, files in os.walk(directory):
    for file in files:
        initial_extension.append(f"commands.{os.path.basename(root)}.{file[:-3]}")
    for subdir in dirs:
        for subroot, subdirs, subfiles in os.walk(os.path.join(root, subdir)):
            for subfile in subfiles:
                initial_extension.append(f"commands.{os.path.basename(subroot)}.{subfile[:-3]}")
