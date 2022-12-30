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

    # Strip the mention from the message
    message.content = message.content.replace(
        "<@{}> ".format(client.user.id), "")

    # Check if the message is a command
    if message.content in client.commandsList.keys():
        # Run the command
        await client.commandsList[message.content]["command"](client, message)


# ===== Main ===================================================================

client.run(config["DISCORD_BOT_TOKEN"])
