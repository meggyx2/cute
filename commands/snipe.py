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
async def snipe(ctx):
	try:
		to_slice = snipe_msgs[str(ctx.message.channel.id)
		sniping = to_slice.split("|")
	except:
		await ctx.send(f"**{ctx.message.author.display_name}** there's nothing to snipe??")
		return
	author = ctx.guild.get_member(int(sniping[1]))
	embed = discord.Embed(title="{}".format(author.name), description="{}".format(sniping[0]), color=0xFFFFFF, timestamp=sniping[2])
	await ctx.send(embed=embed)
	
