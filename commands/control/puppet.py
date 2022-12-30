def puppet():
    async def command(client, message, args):
        # Delete the original message
        await message.delete()

        # Send the remainder of the message
        await message.channel.send(args["remainder"])

    return {
        "owner": True,
        "description": "Sends a message as Paprika",
        "usage": "`@Paprika puppet <message>`",
        "command": command
    }
