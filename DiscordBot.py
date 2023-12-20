from discord.ext import commands, tasks
import discord
import os
from dotenv import load_dotenv
from getpass import getpass
from datetime import datetime
import asyncio

load_dotenv()

# Getting Discord token from environment variable or input
DISCORD_TOKEN = getpass("Discord Token: ") if os.getenv('DISCORD_TOKEN') is None else os.getenv('DISCORD_TOKEN')

# Setting up Discord intents (permissions for the bot)
intents = discord.Intents.default()
intents.message_content = True

# Initializing the bot with a command prefix and intents
# Can choose to use a different prefix to "/" like "!" 
bot = commands.Bot(command_prefix='/', intents=intents)

# Event handler for when the bot is ready on startup
@bot.event
async def on_ready():
    if not post_at_specific_time_each_day.is_running():
        post_at_specific_time_each_day.start()
    if not repeated_task.is_running():
        repeated_task.start()
    print(f'{bot.user.name} has connected to Discord!')

CHANNEL_ID = None # Placeholder for the Discord channel ID
TIMED_TASK_FREQUENCY = 30  # Frequency of the repeated task in seconds

# A task that runs repeatedly based on the specified frequency
@tasks.loop(seconds=TIMED_TASK_FREQUENCY)
async def repeated_task():
    channel = bot.get_channel(CHANNEL_ID) # Retrieve the channel object using its ID
    await channel.send(f'message every {TIMED_TASK_FREQUENCY} seconds')

# A task that posts a message at a specific time each day
# This is a bit of a hack that lets the bot respond to other messages and commands
@tasks.loop(seconds=30)
async def post_at_specific_time_each_day():
    now = datetime.now() # make sure you have the correct timezone, can use pytz
    # Posting at 3:30 PM every day
    if now.hour == 15 and now.minute == 30:
        channel = bot.get_channel(CHANNEL_ID)
        await channel.send(f'message at 3:30 PM')
        await asyncio.sleep(61) # Sleep for 61 seconds to prevent sending multiple messages

# Before loop tasks to ensure the bot is ready before running the tasks
@post_at_specific_time_each_day.before_loop
@repeated_task.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting") 

# Event handler for processing incoming messages
# Message events are handled before command events
@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return
    # Respond to a specific message
    if message.content == 'ping':
        await message.channel.send('pong')
    # Process all commands. Without this, commands will not be processed
    await bot.process_commands(message)

# Invoked with /repeat <args>
@bot.command(pass_context=True, name='repeat')
async def repeat(ctx, *, args=None):
    message = "".join(args)
    await ctx.send(message)

bot.run(DISCORD_TOKEN)
