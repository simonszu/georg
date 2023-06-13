import os
import discord
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online,activity=discord.Game("?help"))
  print('Logged on as', self.user)

@client.event
async def on_message(message):
  # don't respond to ourselves
  if message.author == client.user:
    return

  if message.content == 'ping':
    await message.channel.send('pong')

client.run(TOKEN)