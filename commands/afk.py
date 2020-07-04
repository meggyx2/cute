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
async def afk(ctx):
	if ctx.message.author.display_name.startswith("[AFK]"):
		return
	else:
		await ctx.send(f"**{ctx.message.author.display_name}** is now AFK. We'll be waiting for your return! I'll notify anyone who mentions you.")
		try:
			await ctx.message.author.edit(nick="[AFK] {}".format(ctx.message.author.display_name))
		except:
			print(f"Couldn't change {ctx.message.author.display_name}'s name because it's too long (32 max char).")
