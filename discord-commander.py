#bot.py
import os
import discord
import random

#from dotenv import load_dotenv
#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')     Not working: need to figure out how to set system env variable

TOKEN = 'OTM1MzAyODQ2MjYwMzM4Nzc4.Ye8qpw.qeejQwrZ7KFS_c350p5zD53T87M'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    announce = ["UEF ", "a little trace of incredible, dinosaur, fantastic, Seraphim DNA", "Cheating AI is best AI", "Calling all Supreme Commanders: It is time to team up on Senior", "Daily reminder to spam Gunships", "Embrace Monkelord", "The Man challenges Senior to a 1v1 nukes enabled"]
    triggers = ["monke","supreme commander", "supreme", "sc", "supreme commander 2", "sc2", "uef", "illuminate", "cybran", "monkeylord"]

    if (message.content).lower() in triggers:
        response = random.choice(announce)
        await message.channel.send(response)

client.run(TOKEN)
