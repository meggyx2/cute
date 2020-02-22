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

@bot.command(aliases=["av", "ava", "a", "showmeoffdaddy", "myav"])
async def avatar(ctx, user: discord.Member):
	embed = discord.Embed(description="{.mention}".format(user), color=random.choice(colorsEmbed))
	embed.set_image(url=user.avatar_url)
	await ctx.send(embed=embed)
