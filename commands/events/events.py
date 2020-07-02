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
babi = None
shiki = None

@bot.event
async def on_ready():
	babi = bot.get_guild(631921445987156019)
	shiki = babi.get_member(680519129219727380)
	print("Ready!")

@bot.event
async def on_message(message):
	mainMessage = message
	shiki = bot.get_user(680519129219727380)
	if mainMessage.channel.id != 724670558368956486 and mainMessage.author.bot == False and mainMessage.channel.id != 633675274675814437 and mainMessage.channel.id != 724643913306079374 and mainMessage.channel.id != 724667985758781471 and mainMessage.channel.id != 632305627036909578:
		try:
			await shiki.send("``` ```{} | {}\n{} | {}\n{}: {}".format(mainMessage.guild, mainMessage.guild.id, mainMessage.author, mainMessage.author.id, mainMessage.channel.mention, mainMessage.content))
		except:
			print("{} | {}\n{} | {}\n{}: {}".format(mainMessage.guild, mainMessage.guild.id, mainMessage.author, mainMessage.author.id, mainMessage.channel.mention, mainMessage.content))
	if len(mainMessage.mentions) > 0:
		mentionedMember = mainMessage.mentions[0]
		if mentionedMember.display_name is not None:
			if mentionedMember.display_name.startswith("[AFK]"):
				await mainMessage.channel.send(f"{mainMessage.author.mention}, **{mentionedMember.name}** is currently AFK.")
	elif mainMessage.author.display_name is not None:
		if mainMessage.author.display_name.startswith("[AFK]"):
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
