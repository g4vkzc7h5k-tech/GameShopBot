import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

@bot.command()
async def test(ctx):
    await ctx.send("GameShop is online!")

bot.run(MTUyNDg0MTA0MjY0NDQzNTAzNQ.GTNR_U.T18Et2e8PK1lbGDWWDoLDhZ22_-TZDICVqXJMA)
