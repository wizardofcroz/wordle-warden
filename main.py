from datetime import datetime
from datetime import time
import discord
import random
from discord.ext import tasks

import helper as helper
import sys
import os
import glob
api_key = os.getenv('DISCORD_KEY')


if api_key == '':
    sys.exit("Error: api_key not found")

# no-ribbits = 445995937819656198
# only-5-letters-type-like-ur-having-a-stroke =  939204794051100712
# test-halariousBot-channel = 920354525305528400

client = discord.Client()

sixth_try = 'Wordle 231 6/6 ⬛🟩🟨⬛⬛ 🟩🟩⬛🟨⬛ 🟩🟩🟩⬛⬛ 🟩🟩🟩⬛⬛ 🟩🟩🟩⬛⬛ 🟩🟩🟩🟩🟩'


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if str(message.channel.id) == '939204794051100712':
        if message.content.startswith('Wordle'):
            score = helper.record_score(message)
            if score == 6:
                await message.channel.send(f"6th try loser {str(message.author.nick)}")
        elif message.content.lower().startswith('scores'):
            await message.channel.send(helper.get_winners())
        elif message.content.lower().startswith('leaderboard'):
            await message.channel.send(helper.get_leaderboard())
        elif message.author != client.user and not helper.is_five_letters(message.content):
                await message.channel.send(
                    "What {0} meant to say was\n`{1}`\nbut they used the wrong format").format(
                        str(message.author.nick),
                        helper.to_five_char_line(str(message.content)))
                await message.delete()

    if str(message.channel) == 'g_fuel' and "quack" in message.content.lower():
        with open(random.choice(glob.glob("./quacks/*.webp")), "rb") as fh:
            f = discord.File(fh, filename=fh.name)
        await message.channel.send(file=f)


client.run(api_key)
