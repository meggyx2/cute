import discord
from discord.ext import commands
import random
import sys
import traceback
import asyncio
import datetime
import json
from cv.py import *
from datetime import datetime

@bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, chan: discord.TextChannel, *, msg: str):
	await ctx.message.delete()
	await chan.send(f"{msg}")
	
@say.error
async def say_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
		message = ctx.message[5:]
		await ctx.message.delete()
		if len(message) > 0:
			await ctx.send(f"{message}")
    elif isinstance(error, commands.BadArgument):
		await ctx.send(f"**{ctx.message.author.name}** that channel doesn't even exist, what are you doing?")
    elif isinstance(error, commands.CheckFailure):
		await ctx.send("f**{ctx.message.author.name}** you don't have the **administrator** perms, duh.")
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
		embed = discord.Embed(description="{}".format(error), color=0x000000)
		await ctx.send("uh, oops, i guess?", embed=embed)

		
