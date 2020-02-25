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

@bot.command()
async def ship(ctx, match1: discord.Member, match2: discord.Member):
	percent = randint(0, 100)
	await ctx.send(f"**{match1.name}** is a **__{str(percent)}%__** match with **{match2.name}**! ❤️")
	
@ship.error
async def ship_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		match1 = ctx.message.author
		match2 = await commands.MemberConverter().convert(ctx, ctx.message.content[6:])
		if match2 is None:
			await ctx.send(f"**{match1.name}** you didn't give me at least 1 correct member to match you with, tward")
			return
		percent = randint(0, 100)
		await ctx.send(f"**{match1.name}** is a **__{str(percent)}%__** match with **{match2.name}**! ❤️")
	elif isinstance(error, commands.BadArgument):
		match1 = ctx.message.author
		match2 = await commands.MemberConverter().convert(ctx, ctx.message.content[6:])
		if match2 is None:
			await ctx.send(f"**{match1.name}** you didn't give me at least 1 correct member to match you with, tward")
			return
		percent = randint(0, 100)
		await ctx.send(f"**{match1.name}** is a **__{str(percent)}%__** match with **{match2.name}**! ❤️")
	else:
		print('Ignoring exception in command ship:', file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
		embed = discord.Embed(description="{}".format(error), color=0x000000)
		await ctx.send("uh, oops, i guess?", embed=embed)
		
