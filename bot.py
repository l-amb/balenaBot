import os
import discord
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(TOKEN)
