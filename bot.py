

# bot.py
import os
import nest_asyncio
nest_asyncio.apply()

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name==GUILD:
            break
        
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id:{guild.id}) \n'
        )
    members = '\n -' .join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
#formatted string is used above 
#@client  I looped through the guild data that discord has sent client, namely client.guilds
#          

client.run(TOKEN)
