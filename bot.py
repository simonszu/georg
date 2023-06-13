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
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  # don't respond to ourselves
  if message.author == client.user:
    return

  if message.content == 'ping':
    await message.channel.send('pong')

  if message.content == "!react":
    c_channel = discord.utils.get(message.guild.text_channels, name='counting channel')
    messages = await c_channel.history(limit=2).flatten()
    if message.channel == c_channel and int(messages[1].content) + 1 != int(message.content):
        await message.delete()

client.run(TOKEN)