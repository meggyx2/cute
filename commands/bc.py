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

@bot.command(aliases=["botclear", "botclean", "clean", "clear", "fuckoffbots"])
@commands.has_permissions(manage_messages=True)
async def bc(ctx):
	def check(m):
		return m.author.bot
	await ctx.message.delete()
	await ctx.message.channel.purge(limit=100, check=check)
	# under this is just for fun
	def check2(m):
		return m.channel == ctx.message.channel
	msg = await client.wait_for('message', check=check)
	await msg.add_reaction("<a:speedclean:653273382812647425>")
	
@bc.error
async def bc_error(error, ctx):
	if isinstance(error, commands.CheckFailure):
		await ctx.send("f**{ctx.message.author.name}** you don't have the **manage messages** perms, duh.")
	else:
		print('Ignoring exception in command bc:', file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
		embed = discord.Embed(description="{}".format(error), color=0x000000)
		await ctx.send("uh, oops, i guess?", embed=embed)
	
