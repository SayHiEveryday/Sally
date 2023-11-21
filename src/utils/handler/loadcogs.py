from utils import arg
import os


initial_extension = []

for filename in os.listdir(os.path.dirname(__file__) + "\..\..\commands"):
    if filename.endswith('.py'):
        try:
            initial_extension.append("commands." + filename[:-3])
        except Exception as e:
            print(e)
for filename in os.listdir(os.path.dirname(__file__) + "\..\..\commands\/\\fun"):
    if filename.endswith('.py'):
        try:
            initial_extension.append("commands."+ "fun." + filename[:-3])
        except Exception as e:
            print(e)

for filename in os.listdir(os.path.dirname(__file__) + "\..\..\commands\moderation"):
    if filename.endswith('.py'):
        try:
            initial_extension.append("commands." + "moderation."+ filename[:-3])
        except Exception as e:
            print(e)

for filename in os.listdir(os.path.dirname(__file__) + "\..\..\commands\misc"):
    if filename.endswith('.py'):
        try:
            initial_extension.append("commands." + "misc."+ filename[:-3])
        except Exception as e:
                print(e)

for filename in os.listdir(os.path.dirname(__file__) + "\..\..\commands\salonly"):
    if filename.endswith('.py'):
        try:
            initial_extension.append("commands."+ "salonly." + filename[:-3])
        except Exception as e:
            print(e)

for filename in os.listdir(os.path.dirname(__file__) + "\..\..\commands\/\\bot"):
    if filename.endswith('.py'):
        try:
            initial_extension.append("commands."+ "bot." + filename[:-3])
        except Exception as e:
            print(e)

for filename in os.listdir(os.path.dirname(__file__) + "\..\..\event"):
    if filename.endswith('.py'):
        try:
            initial_extension.append("event."+ filename[:-3])
        except Exception as e:
            print(e)
