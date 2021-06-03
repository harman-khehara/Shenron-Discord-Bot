import discord # Import the discord.py API wrapper
import os # Import os to interact with the operating system
from discord.ext import commands # Import commands to create commands for the bot
from dotenv import load_dotenv

#----------------------------------------------------------------------------------

load_dotenv() # Load environment variables from .env file

#client = discord.Client() # Initialize a client to connect to the Discord application
client = commands.Bot(command_prefix = '$') # Initialize a Discord bot which is an extended version of the Discord client

# Variable declarations 
about_phrases_file = open('dragon_ball_about_phrases.txt', 'r')
about_phrases_list = about_phrases_file.readlines()
about_phrases_without_newline = [] # About phrases with no newline character

for phrase in about_phrases_list:
    split_phrase = phrase.split("\n")
    about_phrases_without_newline.append(split_phrase[0])

#----------------------------------------------------------------------------------

# Register the "on_ready" event to start using the bot
@client.event
async def on_ready():
    print('Successfully logged in as {0}'.format(client.user))

#----------------------------------------------------------------------------------

# Register the "on_message" event to react to messages in the Discord server
# The "on_message" event will trigger for every message received
@client.event
async def on_message(message):
    # Return nothing if the user who sends the message is the same as the client
    if message.author == client.user:
        return

    # Return a Wikipedia page explaining what Dragon Ball is
    for phrase in about_phrases_without_newline:
        if message.content.lower().startswith(phrase):
            # await will stop the execution of the function until the bot successfully sends out the Wikipedia link
            await message.channel.send('You should check this out...https://en.wikipedia.org/wiki/Dragon_Ball')

    await client.process_commands(message) # Need this line of code to run commands when overriding the on_message event
#----------------------------------------------------------------------------------

# Register the "roles" command to return a list of all roles in the server
@client.command()
async def roles(context):
    roles = context.guild.roles
    roles_str = ''
    for i in range(1, len(roles)):
        roles_str = roles_str + " " + roles[i].name + ","
    roles_str = roles_str[0 : len(roles_str) - 1]

    await context.channel.send(roles_str)

#----------------------------------------------------------------------------------

# Run the bot by retrieving the token from the .env file
client.run(os.getenv('TOKEN'))
