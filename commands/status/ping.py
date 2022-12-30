def ping():
    async def command(client, message, args):
        await message.channel.send(f":ping_pong: Pong! Latency was {round(client.latency * 1000)}ms.")

    return {
        "owner": False,
        "description": "Responds with a 'pong' message",
        "usage": "`@Paprika ping`",
        "command": command
    }
