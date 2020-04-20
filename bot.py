import discord
import asyncio
import config
from werewolves import Game

client = discord.Client()
games = {}

async def start_game(host, channel):
    games[channel.id] = Game(host, channel)
    msg = f'{host.mention} is starting a new game of Werewolves!'
    await channel.send(msg)

    return

@client.event
async def on_message(message):

    # Get channel game
    channel_id = message.channel.id
    try:
        game = games[channel_id]
    except KeyError:
        game = None

    print(games)

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # debug
    if message.content.startswith('!hello'):
        await message.channel.send(f'Hello {message.author.mention}!')
        return

    # Ignore any messages that don't start with the prefix
    if not message.content.startswith('!ww'):
        return 
    
    # We can strip out the prefix from now
    content = message.content[3:].lstrip()

    if content == 'help':
        await message.channel.send("In Discord, no one can hear you scream")
        return

    if game is None:
        if content == 'start':
            await start_game(message.author, message.channel)
        else:
            msg = "No game has yet started, use '!ww start'"
            await message.channel.send(msg)
        return

    if message.author.id in game.players:
        await game.command(message.author, content)
        return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(config.TOKEN)


