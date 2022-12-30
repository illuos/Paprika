def ping():
    async def command(client, message):
        await message.channel.send(f":ping_pong: Pong! Latency was {round(client.latency * 1000)}ms.")

        return

    return {
        "description": "Responds with a 'pong' message",
        "usage": "`@Paprika ping`",
        "command": command
    }
