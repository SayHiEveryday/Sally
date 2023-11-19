from utils import arg
import os


initial_extension = []

for filename in os.listdir(os.path.dirname(__file__) + "/../cogs"):
    if filename.endswith('.py'):
        try:
            initial_extension.append("cogs." + filename[:-3])
        except Exception as e:
            print(e)
for filename in os.listdir(os.path.dirname(__file__) + "/../cogs/fun"):
    if filename.endswith('.py'):
        try:
            initial_extension.append("cogs."+ "fun." + filename[:-3])
        except Exception as e:
            print(e)

for filename in os.listdir(os.path.dirname(__file__) + "/../cogs/moderation"):
    if filename.endswith('.py'):
        try:
            initial_extension.append("cogs." + "moderation."+ filename[:-3])
        except Exception as e:
            print(e)

for filename in os.listdir(os.path.dirname(__file__) + "/../cogs/misc"):
    if filename.endswith('.py'):
        try:
            initial_extension.append("cogs." + "misc."+ filename[:-3])
        except Exception as e:
                print(e)

for filename in os.listdir(os.path.dirname(__file__) + "/../cogs/salonly"):
    if filename.endswith('.py'):
        try:
            initial_extension.append("cogs."+ "salonly." + filename[:-3])
        except Exception as e:
            print(e)

for filename in os.listdir(os.path.dirname(__file__) + "/../cogs/bot"):
    if filename.endswith('.py'):
        try:
            initial_extension.append("cogs."+ "bot." + filename[:-3])
        except Exception as e:
            print(e)

for filename in os.listdir(os.path.dirname(__file__) + "/../event"):
    if filename.endswith('.py'):
        try:
            initial_extension.append("event."+ filename[:-3])
        except Exception as e:
            print(e)
