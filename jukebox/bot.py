import discord
import os

from discord.ext import tasks, commands
from dotenv import load_dotenv

load_dotenv()

description = '''A self-hosted discord bot for making a
YouTube playlist with songs provided by your server members.'''

INTENTS = discord.Intents.none()
INTENTS.messages = True
INTENTS.guilds = True

PREFIX='j?'
TOKEN=os.getenv('DISCORD_SECRET')

bot = commands.Bot(command_prefix=PREFIX, description=description, intents=INTENTS)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    slow_count.start()


@bot.command()
async def ping(ctx):
    """Adds two numbers together."""
    await ctx.message.reply('pong')


@tasks.loop(seconds=5.0, count=5)
async def slow_count():
    print(slow_count.current_loop)

@slow_count.after_loop
async def after_slow_count():
    print('done!')



bot.run(TOKEN)