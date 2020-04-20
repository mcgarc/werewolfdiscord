import discord
import asyncio
import config
from werewolves import Game

client = discord.Client()
game = None

async def start_game(host, channel):

    global game

    game = Game(host, channel)
    msg = f'{host.mention} has started a new game of Werewolves!'

    await channel.send(msg)

    return

@client.event
async def on_message(message):

    # I'm not sorry.
    global game

    print(game)
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
        # Start a new game with the starter as host
        await start_game(message.author, message.channel)
        return

    if message.author in game.players:
        await game.command(message.author, content)
        return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(config.TOKEN)


