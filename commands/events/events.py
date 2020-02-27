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

@bot.event
async def on_message(message):
	mainMessage = message
	if len(mainMessage.mentions) > 0:
		mentionedMember = mainMessage.mentions[0]
		if mentionedMember.nick is not None:
			if mentionedMember.nick.startswith("[AFK]"):
				await mainMessage.channel.send(f"{mainMessage.author.mention}, **{mentionedMember.name}** is currently AFK.")
	elif mainMessage.author.nick is not None:
		if mainMessage.author.nick.startswith("[AFK]"):
			await mainMessage.author.edit(nick="{}".format(mainMessage.author.nick[6:]))
			await mainMessage.channel.send(f"Welcome back, **{mainMessage.author.display_name}**!")

	await bot.process_commands(message)
