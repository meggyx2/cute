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
		to_slice = snipe_msgs[str(ctx.message.channel.id)]
		sniping = to_slice.split("|")
	except:
		await ctx.send(f"**{ctx.message.author.display_name}** there's nothing to snipe??")
		return
	try:
		author = ctx.guild.get_member(int(sniping[1]))
	except:
		await ctx.send(f"**{ctx.message.author.display_name}** uh, it looks like the author of the message you're trying to snipe left the server. L")
		return
	embed = discord.Embed(description="{}".format(sniping[0]), color=0xFFFFFF, timestamp=snipe_msgs_time[str(ctx.message.channel.id)])
	embed.set_author(name="{}".format(author.name), icon_url=author.avatar_url)
	await ctx.send(embed=embed)
	
