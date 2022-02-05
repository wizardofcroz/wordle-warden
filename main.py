from operator import truediv
import discord
import secrets
import logging
# Worlde channel = 939204794051100712

api_key = secrets.api_key
client = discord.Client()

logging.getLogger().setLevel(logging.INFO)

def fromWordleChannel(message):
    if (message.channel.id == 939204794051100712):
        return True
    else:
        return False
def fromSelf(message):
    if (message.author == client.user):
        return True
    else:
        return False 

def worldFormat(message):
    print(message)

@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client))
    for c in client.get_all_channels():
        logging.info('Name: %s\n' \
                      'ID: %s\n',c.name,c.id)

@client.event
async def on_message(message):
    if(fromWordleChannel(message) and not fromSelf(message)):
        logging.info(message.content)
        words = message.content.split()
        print (words)
    #    await message.channel.send("hello")
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')


client.run(api_key)