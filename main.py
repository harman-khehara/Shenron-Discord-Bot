import discord # Import the discord.py API wrapper
import os # Import os to interact with the operating system
from discord.ext import commands # Import commands to create commands for the bot
from dotenv import load_dotenv
import random

#----------------------------------------------------------------------------------

load_dotenv() # Load environment variables from .env file

#client = discord.Client() # Initialize a client to connect to the Discord application
client = commands.Bot(command_prefix = '$') # Initialize a Discord Bot which is an extended version of the Discord Client

# Variable declarations 
about_phrases_file = open('dragon_ball_about_phrases.txt', 'r')
about_phrases_list = about_phrases_file.readlines()
about_phrases_without_newline = [] # About phrases with no newline character

db_facts_file = open("dragon_ball_facts.txt", "r")
db_facts = db_facts_file.readlines()
db_facts_without_newline = []

characters = {
    'goku': ['Goku is a Saiyan and the main protagonist of Dragon Ball. He is the husband of Chi-Chi and father of Gohan and Goten.', 'https://raw.githubusercontent.com/harman-khehara/Shenron-Discord-Bot/main/Images/goku.jpg'],
    'vegeta': ['Vegeta is the prince of the Saiyan race, the husband of Bulma, and father of Trunks and Bulla.', 'https://raw.githubusercontent.com/harman-khehara/Shenron-Discord-Bot/main/Images/vegeta.png'],
    'krillin': ['Krillin is a supporting protagonist in Dragon Ball, the husband of Android 18, and father of Marron.', 'https://raw.githubusercontent.com/harman-khehara/Shenron-Discord-Bot/main/Images/krillin.jpg'],
    'tien': ['Tien Shinhan is a martial artist and one of the strongest Earthlings in Dragon Ball. He is often seen training with his best friend Chiaotzu.', 'https://raw.githubusercontent.com/harman-khehara/Shenron-Discord-Bot/main/Images/tien.jpg'],
    'bulma': ['Bulma is a scientist and the daughter of the founder of Capsule Corporation. She is also the first friend of Goku, the wife of Vegeta, and mother of Trunks and Bulla.', 'https://raw.githubusercontent.com/harman-khehara/Shenron-Discord-Bot/main/Images/bulma.jpg'],
    'trunks': ['Trunks is a hybrid of an Earthling and Saiyan and is the son of Vegeta and Bulma and the older brother of Bulla. He also has a best friend named Goten.', 'https://raw.githubusercontent.com/harman-khehara/Shenron-Discord-Bot/main/Images/trunks.jpg'],
    'goten': ['Goten is a hybrid of an Earthling and Saiyan and is the son of Goku and Chi-Chi. He is the youngest Saiyan to turn Super Saiyan and the younger brother of Gohan.', 'https://raw.githubusercontent.com/harman-khehara/Shenron-Discord-Bot/main/Images/goten.jpg'],
    'gohan': ["Gohan is the son of Goku and Chi-Chi, the elder brother of Goten, the husband of Videl, and the father of Pan. He is named after Goku's grandfather, Gohan.", 'https://raw.githubusercontent.com/harman-khehara/Shenron-Discord-Bot/main/Images/gohan.jpg'],
    'chi-chi': ["Chi-Chi is the daughter of the Ox-King and the wife of Goku. She has two children named Goten and Gohan.", 'https://raw.githubusercontent.com/harman-khehara/Shenron-Discord-Bot/main/Images/chi-chi.png'],
    'beerus': ["Beerus is the God of Destruction of Universe 7 and is usually seen with his attendant Whis. He also has a twin brother named Champa.", 'https://raw.githubusercontent.com/harman-khehara/Shenron-Discord-Bot/main/Images/beerus.jpg'],
    'whis': ['Whis is an angel who is the martial arts teacher and attendant of Beerus.', 'https://raw.githubusercontent.com/harman-khehara/Shenron-Discord-Bot/main/Images/whis.jpg'],
    'piccolo': ["Piccolo is a Namekian who is the reincarnation of the Demon King Piccolo. He was once the enemy of Goku, but later became Earth's greatest hero.", 'https://raw.githubusercontent.com/harman-khehara/Shenron-Discord-Bot/main/Images/piccolo.jpg'],
    'yamcha': ["Yamcha was the main protagonist in both the Dragon Ball manga and anime, but later became a supporting protagonist in Dragon Ball Z and Dragon Ball Super. He is a martial artist and a very good baseball player. He also has a best friend named Puar.", 'https://raw.githubusercontent.com/harman-khehara/Shenron-Discord-Bot/main/Images/yamcha.jpg']
}

for fact in db_facts:
    split_fact = fact.split("\n")
    db_facts_without_newline.append(split_fact[0])

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
@client.command(aliases = ["set-role", "Set-role", "Set-Role", "set-Role", "SET-ROLE", "setrole"])
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
@client.command(aliases = ["rmv-role", "Rmv-role", "Rmv-Role", "rmv-Role", "RMV-ROLE", "rmvrole"])
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

# Register the "db_fact" command which will send a random fact about Dragon Ball
@client.command(aliases=["dbfact", "DB-Fact", "db-Fact", "DB-FACT", "Db-fact", "Db-Fact", "db-fact", "fact"])
async def db_fact(context):
    await context.channel.send(random.choice(db_facts_without_newline))

#----------------------------------------------------------------------------------

# Register the "on_command_error" event to detect when a user attempts to use a command that doesn't exist
@client.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandNotFound):
        await context.channel.send("The command '{0}' does not exist.".format(context.message.content[1 : len(context.message.content)]))
        return

#----------------------------------------------------------------------------------

# Register the "db_character" command to display a description and image of a specific Dragon Ball character
@client.command(aliases=["dbchar", "char", "db-char", "db-character", "character"])
async def db_character(context, *, character_name):

    # Check that the character_name is in the characters dictionary
    char_exists = False
    for character in characters.keys():
        if character == character_name.lower():
            char_exists = True
    
    if char_exists is False:
        await context.channel.send("The character '{0}' does not exist in Dragon Ball.".format(character_name))
        return
    
    # Search the dictionary to retrieve the character information
    char_description = characters[character_name.lower()][0]
    char_img = characters[character_name.lower()][1]

    # Send the character information by using an Embed
    embed1 = discord.Embed(title = character_name.upper(), description = "Character Description")

    embed1.add_field(name = "---", value = char_description)
    embed1.set_image(url = char_img)

    await context.channel.send(embed = embed1)
#----------------------------------------------------------------------------------

# Run the bot by retrieving the token from the .env file
client.run(os.getenv('TOKEN'))
