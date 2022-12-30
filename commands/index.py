# Import all commands from all subfolders within /commands/
import os


def indexAllCommands():
    commandDict = {}

    # Create a list of all subfolders within /commands/
    subfolders = [f.name for f in os.scandir("commands") if f.is_dir()]
    # Remove __pycache__
    subfolders.remove("__pycache__")

    for subfolders in subfolders:
        # Create a list of all .py files within the subfolder
        commands = [f.name[:-3] for f in os.scandir("commands/" + subfolders)
                    if f.is_file() and f.name.endswith(".py")]

        for command in commands:
            # TODO: Make this solution less... hacky

            # Import the command as a command
            exec("import commands." + subfolders +
                 "." + command + " as " + command)

            # Set the dictionary value to the command
            commandDict[command] = eval(command + "." + command + "()")

    return commandDict
