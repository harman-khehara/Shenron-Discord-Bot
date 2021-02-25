import discord
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('what is dragon ball') or \
            message.content.lower().startswith('never heard of dragon ball'):
        await message.channel.send('You should check this out...' +
                                   ' https://en.wikipedia.org/wiki/Dragon_Ball')

client.run(os.getenv('TOKEN'))
