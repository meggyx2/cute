import discord
from discord.ext import commands
import traceback
import datetime
import asyncio
import random
from datetime import datetime
from cv import *

@bot.command(aliases=["howwhore", "howthot", "whorerate", "hoerate", "howhoe", "ratethot"])
async def thotrate(ctx, user: discord.Member):
	await ctx.send(f"**{user.name}** is **__{int(random.randint(0, 100))}__**% a thot! 🥴")

@thotrate.error
async def thotrate_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f"**{ctx.message.author.name}** is **__{int(random.randint(0, 100))}__**% a thot! 🥴")
	elif isinstance(error, commands.BadArgument):
		embed = discord.Embed(color=0xFFFFFF)
		embed.set_footer(text="Member not found.")
		await ctx.send(f"**babi** is **__not__** a thot, duh. She's loyal to Meg. 😳", embed=embed)
	else:
		print('Ignoring exception in command av:', file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
		embed = discord.Embed(description="{}".format(error), color=0x000000)
		await ctx.send("uh, oops, i guess?", embed=embed)
