import discord
import secrets
import logging
api_key = secrets.api_key

client = discord.Client()
logging.getLogger().setLevel(logging.INFO)
@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client))
    for c in client.get_all_channels():
        logging.info('Name: %s\n' \
                      'ID: %s\n',c.name,c.id)
    # async def on_message(self, message):
    #     print('Message from {0.author}: {0.content}'.format(message))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')


client.run(api_key)