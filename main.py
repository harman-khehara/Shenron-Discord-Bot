import discord # Import the discord.py API wrapper
import os # Import os to interact with the operating system
from discord.ext import commands # Import commands to create commands for the bot
from dotenv import load_dotenv

#----------------------------------------------------------------------------------

load_dotenv() # Load environment variables from .env file

#client = discord.Client() # Initialize a client to connect to the Discord application
client = commands.Bot(command_prefix = '$') # Initialize a Discord Bot which is an extended version of the Discord Client

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

# Register the "roles" command to return a list of all roles in the server, excludes the "@everyone" role
@client.command(aliases=["give-roles", "show-roles", "which-roles", "Roles"])
async def roles(context):
    roles = context.guild.roles
    roles_str = ''
    for i in range(1, len(roles)):
        if roles[i].is_bot_managed() is False:
            roles_str = roles_str + " " + roles[i].name + ","
    roles_str = roles_str[0 : len(roles_str) - 1] # Excludes the "@everyone" role which will always be the first element in the list of roles

    await context.channel.send(roles_str)

#----------------------------------------------------------------------------------

#Register the "set_role" command which allows a user to set their role
@client.command(aliases = ["set-role", "Set-role", "Set-Role", "set-Role", "SET-ROLE"])
async def set_role(context, *, role_name):

    # Server member already has role
    for role in context.author.roles:
        if role_name == role.name:
            await context.channel.send("{0} already has this role.".format(context.author))
            return
    
    # Role provided does not exist in server
    role_exists = False
    for role1 in context.guild.roles:
        if role_name == role1.name:
            role_exists = True
            role_to_give = role1

    if role_exists is False:
        await context.channel.send("The role '{0}' does not exist.".format(role_name))
        return
    
    # Role is a bot managed role
    if role_to_give.is_bot_managed():
        await context.channel.send("The role {0} can only be assigned to Discord Bots".format(role_to_give.name))
        return 

    # Role can be given to server member
    await context.author.add_roles(role_to_give)
    await context.channel.send("{0} has been assigned the role {1}.".format(context.author, role_name))

#----------------------------------------------------------------------------------

# Register the "rmv_role" command which allows a user to remove their role
@client.command(aliases = ["rmv-role", "Rmv-role", "Rmv-Role", "rmv-Role", "RMV-ROLE"])
async def rmv_role(context, *, role_name):

    # Role provided does not exist in server
    role_exists = False
    for role1 in context.guild.roles:
        if role_name == role1.name:
            role_exists = True

    if role_exists is False:
        await context.channel.send("The role '{0}' does not exist.".format(role_name))
        return

    # Make sure server member is already assigned the role
    member_has_role = False
    for role in context.author.roles:
        if role_name == role.name:
            member_has_role = True
            role_to_remove = role
    
    # Member does not already have the role
    if member_has_role is False:
        await context.channel.send("{0} is not assigned the role {1}.".format(context.author, role_name))
        return

    # Member is trying to remove the "@everyone" role 
    if role_to_remove.name == "@everyone":
        await context.channel.send("The role {0} cannot be removed".format(role_to_remove.name))
        return

    # Member role can be removed
    if member_has_role is True:
        await context.author.remove_roles(role_to_remove)
        await context.channel.send("{0} no longer has the role {1}.".format(context.author, role_name))

#----------------------------------------------------------------------------------

# Run the bot by retrieving the token from the .env file
client.run(os.getenv('TOKEN'))
