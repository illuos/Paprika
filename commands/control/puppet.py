def puppet():
    async def command(client, message, args):
        # Delete the original message
        await message.delete()

        # Send the remainder of the message
        await message.channel.send(args["remainder"])

    return {
        "name": "puppet",
        "owner": True,
        "group": "control",
        "description": "Sends a message as Paprika.",
        "usage": ["`@Paprika puppet <message>`"],
        "detailed": "Send a message as me. This can only be used by my owner. Upon usage, I'll delete your message, and send the remainder of what you said as a message from me.",
        "command": command
    }
