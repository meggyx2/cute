import discord
from discord.ext import commands
import random
import sys
import traceback
import asyncio
import datetime
import json
from cv import *
from datetime import datetime

@bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, chan: discord.TextChannel, *, msg: str):
	await ctx.message.delete()
	embed = discord.Embed(description="{}".format(msg))
	await chan.send(embed=embed)
	
@say.error
async def say_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		message = ctx.message.content[5:]
		await ctx.message.delete()
		if len(message) > 0:
			embed = discord.Embed(description="{}".format(message))
			await ctx.channel.send(embed=embed)
	elif isinstance(error, commands.BadArgument):
		message = ctx.message.content[5:]
		await ctx.message.delete()
		if len(message) > 0:
			embed = discord.Embed(description="{}".format(message))
			await ctx.channel.send(embed=embed)
	elif isinstance(error, commands.CheckFailure):
		await ctx.send(f"**{ctx.message.author.name}** you don't have the **administrator** perms, duh.")
	else:
		print('Ignoring exception in command say:', file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
		embed = discord.Embed(description="{}".format(error), color=0x000000)
		await ctx.send("uh, oops, i guess?", embed=embed)

		
