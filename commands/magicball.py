import discord
from discord.ext import commands
import random
import sys
import traceback
import asyncio
import datetime
import json
from datetime import datetime
from cv import *

responses = [
    "No",
    "Yes",
    "Perhaps",
    "It could not be possible",
    "I think so",
    "I don't think so",
    "Never",
    "It is very likely",
    "Probably",
    "Probably not"
]

@bot.command(name="8ball", aliases=["ball", "q"])
async def magicball(ctx, *, question: str):
	embed1 = discord.Embed(description="❓ **{}**\n\n. . .".format(question), color=0xFFFFFF)
	msg = await ctx.send("The ball is thinking...", embed=embed1)
	await asyncio.sleep(randint(1, 3))
	embed2 = discord.Embed(description="❓ **{}**\n\n__{}__".format(question, random.choice(responses)), color=0xFFFFFF)
	await msg.edit(content="Your question has been answered.", embed=embed2)
	
@magicball.error
async def magicball_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f"**{ctx.message.author.name}** ask again, but give me a question to answer")
	else:
		print('Ignoring exception in command av:', file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
		embed = discord.Embed(description="{}".format(error), color=0x000000)
		await ctx.send("uh, oops, i guess?", embed=embed)
	
