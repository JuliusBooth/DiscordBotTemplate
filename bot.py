from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
from getpass import getpass

load_dotenv()
if os.getenv('DISCORD_TOKEN') is None:
    TOKEN = getpass("Discord Token: ")
else:
    TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print('Connected!')    

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return
    # If the message is "ping", respond with "pong"
    if message.content == 'ping':
        await message.channel.send('pong')
    # process all commands
    await bot.process_commands(message)
            
@bot.command(pass_context=True, name='repeat')
async def repeat(ctx, *args):
    await ctx.send('_'.join(args))

bot.run(TOKEN)
