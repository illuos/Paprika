def help():
    async def command(client, message, args):
        # Check if args contain a particular command
        if args["remainder"] == "":
            return await generalHelp(client, message, args)

        # Check if the command exists
        if args["remainder"] not in client.commandsList.keys():
            return await message.channel.send(f"Sorry, I don't know the command `{args['remainder']}`.")

        # Otherwise, send the detailed help for the command
        command = client.commandsList[args["remainder"]]
        response = f"**{command['name']}**"
        if command["owner"]:
            response += " *(owner only)*\n"
        else:
            response += "\n"

        response += f"*Group:* {command['group']} {client.groups[command['group']]['emoji']}\n\n"

        response += f"{command['detailed']}\n"

        response += f"*Usage:* {', '.join(command['usage'])}"

        await message.channel.send(response)

    async def generalHelp(client, message, args):
        response = f"Need some help about a particular command? Try `@Paprika help <command>`.\nOtherwise, here's a list of the commands I know:\n\n"

        # Add the commands to the response
        for group in client.groups.keys():
            response += f"**{group}** {client.groups[group]['emoji']}\n"

            for command in client.groups[group]["commands"]:
                response += f"- `{command}`: {client.commandsList[command]['description']}\n"

            response += "\n"

        await message.channel.send(response)

    return {
        "name": "help",
        "owner": False,
        "group": "status",
        "description": "Displays information about commands, or a list of commands.",
        "usage": ["`@Paprika help`", "`@Paprika help <command>`"],
        "detailed": "Ask me about commands! You can ask me about a specific command, or you can ask me for a full list of commands. I'll tell you what each command does, and how to use it.",
        "command": command
    }
