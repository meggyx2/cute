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

@bot.command(aliases=["av", "ava", "a", "showmeoffdaddy", "myav"])
async def avatar(ctx, user: discord.Member):
	embed = discord.Embed(description="{.mention}".format(user), color=0xFFFFFF)
	embed.set_image(url=user.avatar_url)
	await ctx.send(embed=embed)
	await ctx.message.delete()
	
@avatar.error
async def avatar_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="{.mention}".format(ctx.message.author), color=0xFFFFFF)
		embed.set_image(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
		await ctx.message.delete()
	elif isinstance(error, commands.BadArgument):
		await ctx.send(f"**{ctx.message.author.name}** either you're drunk or i'm retarded, cuz no member like that exists.")
	else:
		print('Ignoring exception in command av:', file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
		embed = discord.Embed(description="{}".format(error), color=0x000000)
		await ctx.send("uh, oops, i guess?", embed=embed)

	
