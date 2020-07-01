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
			await mainMessage.author.edit(nick="{}".format(mainMessage.author.display_name[6:]))
			await mainMessage.channel.send(f"Welcome back, **{mainMessage.author.display_name}**!")
	elif mainMessage.content == "pls snipe":
		await mainMessage.channel.send(f"**{mainMessage.author.display_name}** the command is now ``*snipe``.")
	elif mainMessage.content == "pls editsnipe":
		await mainMessage.channel.send(f"**{mainMessage.author.display_name}** the command is now ``*editsnipe``.")
			
	await bot.process_commands(message)
			
@bot.event
async def on_member_join(member):
	if member.guild.id == 631921445987156019:
		memberCount = bot.get_channel(665508950996680705)
		await memberCount.edit(name="babies: {}".format(member.guild.member_count))
		
@bot.event
async def on_member_remove(member):
	if member.guild.id == 631921445987156019:
		memberCount = bot.get_channel(665508950996680705)
		await memberCount.edit(name="babies: {}".format(member.guild.member_count))
		
@bot.event
async def on_message_delete(message):
	snipe_msgs[str(message.channel.id)] = "{}|{}".format(message.content, message.author.id)
	snipe_msgs_time[str(message.channel.id)] = datetime.utcnow()

@bot.event
async def on_message_edit(before, after):
	editsnipe_msgs[str(before.channel.id)] = "{}|{}".format(before.content, before.author.id)
	editsnipe_msgs_time[str(after.channel.id)] = datetime.utcnow()
