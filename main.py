import discord # Import the discord.py API wrapper
import os # Import os to interact with the operating system
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

client = discord.Client() # Initialize a client to connect to the Discord application

phrases_list = [] # List contains all phrases which ask about the Dragon Ball Franchise
phrases_without_newline = [] # Phrases with no newline character
about_phrases = open('dragon_ball_about_phrases.txt', 'r')
phrases_list = about_phrases.readlines()

for phrase in phrases_list:
    split_phrase = phrase.split("\n")
    phrases_without_newline.append(split_phrase[0])


# Register the "on_ready" event to start using the bot
@client.event
async def on_ready():
    print('Successfully logged in as {0}'.format(client.user))

# Register the "on_message" event to react to messages in the Discord server
# The "on_message" event will trigger for every message received
@client.event
async def on_message(message):
    # Return nothing if the user who sends the message is the same as the client
    if message.author == client.user:
        return

    # Return a Wikipedia page explaining what Dragon Ball is
    for phrase in phrases_without_newline:
        if message.content.lower().startswith(phrase):
            # await will stop the execution of the function until the bot successfully sends out the Wikipedia link
            await message.channel.send('You should check this out...https://en.wikipedia.org/wiki/Dragon_Ball')

# Run the bot by retrieving the token from the .env file
client.run(os.getenv('TOKEN'))
