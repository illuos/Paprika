import commands.index as index
import discord

# ===== Configuration and secret variables =====================================

from dotenv import dotenv_values
config = dotenv_values(".env")

# ===== Discord bot construction ===============================================

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
client.commandsList = {}


@client.event
async def on_ready():
    print(f"Logged in as {client.user} on {len(client.guilds)} guild(s)")

    # Load in all commands dynamically based on the files in the commands folder
    client.commandsList = index.indexAllCommands()

    # Verify all fields are present in the commands
    fieldsList = ["owner", "description", "usage", "command"]

    for command in client.commandsList.keys():
        for field in fieldsList:
            if field not in client.commandsList[command]:
                print(f"Error: {command} is missing the {field} field")
                exit(1)


# ===== Command handling =======================================================


@client.event
async def on_message(message):
    # Ignore messages from self
    if message.author == client.user:
        return

    # Ignore messages from other bots
    if message.author.bot:
        return

    # Ignore messages that don't mention Paprika
    if client.user not in message.mentions:
        return

    # Create some arguments for the message
    args = {
        # Strip the mention from the message
        "content": message.content.replace(
            "<@{}> ".format(client.user.id), ""),
        # Strip the command only from the message
        "command": message.content.replace(
            "<@{}> ".format(client.user.id), "").split(" ")[0],
        # Strip the remainder of the message, without command or mention
        "remainder": message.content.replace(
            "<@{}> ".format(client.user.id), "").replace(
            message.content.replace(
                "<@{}> ".format(client.user.id), "").split(" ")[0], ""),
    }

    # Check if the message is a command
    if args["command"] in client.commandsList.keys():
        # Check if the command is owner only
        if client.commandsList[args["command"]]["owner"] and not message.author.id == config["DISCORD_OWNER_ID"]:
            await message.channel.send("This command is owner only.")
            return

        # Run the command
        await client.commandsList[args["command"]]["command"](client, message, args)


# ===== Main ===================================================================

client.run(config["DISCORD_BOT_TOKEN"])
