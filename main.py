from datetime import datetime
import dartetime 
from datetime import time
import discord
import random
import secrets
import helper as helper 
api_key = secrets.api_key

# no-ribbits = 445995937819656198
# only-5-letters-type-like-ur-having-a-stroke =  939204794051100712
#test-halariousBot-channel = 920354525305528400

client = discord.Client()

sixth_try = 'Wordle 231 6/6 ⬛🟩🟨⬛⬛ 🟩🟩⬛🟨⬛ 🟩🟩🟩⬛⬛ 🟩🟩🟩⬛⬛ 🟩🟩🟩⬛⬛ 🟩🟩🟩🟩🟩'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client) )
    


@client.event
async def on_message(message):
    if ( message.content.startswith('Wordle') and str(message.channel.id) == '939204794051100712'):
        helper.recordScore(message)
        if( len(message.content) > len(sixth_try)-4 ):
            await message.channel.send("6th try loser "+ str(message.author.nick))
    elif ( message.content.startswith('#waffle') and str(message.channel.id) == '939204794051100712' ) :
        message.channel.send("🧇")
    else :
        if message.author != client.user and not helper.isFiveLetters(message.content) and str(message.channel.id) == '939204794051100712' :
            await message.channel.send("What "+ str(message.author.nick) + " meant to say was\n`" +helper.toFiveCharLine( str(message.content)) +"`\nbut they used the wrong format") 
            await message.delete()
    
    if (str(message.channel) == 'g_fuel' and "quack" in message.content.lower()):
        pic = random.randrange(1,11)
        with open('./quacks/'+str(pic)+'.webp', "rb") as fh:
            f = discord.File(fh, filename='./quacks/'+str(pic)+'.webp')
        await message.channel.send(file = f)

  # you can even use hours and minutes
now = datetime.time()

@tasks.loop(minute=1)
async def send_message():
    if(datetime.now().time().hour == 20 and datetime.now().time().minute == 30):
        await client.get_channel('939204794051100712').send(helper.getWinners())



client.run(api_key)