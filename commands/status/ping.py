def ping():
    async def command(client, message, args):
        await message.channel.send(f":ping_pong: Pong! Latency was {round(client.latency * 1000)}ms.")

    return {
        "name": "ping",
        "owner": False,
        "group": "status",
        "description": "Pings the bot.",
        "usage": ["`@Paprika ping`"],
        "detailed": "Use this command to ping me. Upon usage, I'll respond with a small message containing the latency between me and Discord's servers, in milliseconds.",
        "command": command
    }
