import discord
from discord.ext import commands
import random
import sys
import traceback
import asyncio
import datetime
import json
from datetime import datetime
from cv.py import *

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
