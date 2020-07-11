import discord
from discord.ext import commands
import random
import sys
import http.client
import requests
import json
import traceback
import asyncio
import datetime
import json
from datetime import datetime
from cv import *
babi = None
shiki = None
countmessages = False
alltimemsg = {}
updatemsg = []
msgidinstorage = {}
storage = None
trigger_chan = None
log = None

def get_key(val): 
	for key, value in alltimemsg.items(): 
		if val == value: 
			return key 

def fetch_top_members():
	msgcount = alltimemsg.copy()
	msgdata_values = list(alltimemsg.values())
	msgdata_values.sort(reverse=True)
	print(msgcount)
	d = 1
	top_members = " " 
	while d < 11:
		idd = None
		try:
			for key, value in msgcount.items(): 
				if msgdata_values[0] == value: 
					idd = int(key)
			user = bot.get_user(idd)
			top_members = top_members + "\n**{}.** {} | **{}** messages".format(d, user.mention, msgdata_values[0])
		except:
			top_members = top_members + "\n**{}.** \"N/A (LEFT_GUILD)\" | **{}** messages".format(d, msgdata_values[0])
		del msgdata_values[0]
		del msgcount[idd]
		d += 1
	return top_members


@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='BOOST BABI!!', type=discord.ActivityType.listening))
	global countmessages
	global storage
	global trigger_chan
	global log
	storage = bot.get_channel(668462634634575905)
	trigger_chan = bot.get_channel(728009012028768257)
	log = bot.get_channel(729058195330433094)
	async for message in trigger_chan.history(limit=1):
		if message.content == "reset":
			print("Resuming resetting...")
			async for message in storage.history(limit=None):
				x = message.content.split("|")
				alltimemsg[int(x[0])] = int(x[1])
				msgidinstorage[int(x[0])] = message.id
			a = fetch_top_members()
			embed = discord.Embed(description="{}".format(a), color=0x000000)
			embed.set_footer(text="WEEKLY RESET | Seeing this means that the message leaderboard has been reset for its weekly reset.")
			await log.send(embed=embed)
			async for message in storage.history(limit=None):
				await message.delete()
			async for message in trigger_chan.history(limit=10):
				await message.delete()
			alltimemsg.clear()
			updatemsg.clear()
			msgidinstorage.clear()
			countmessages = True
			print("Ready!")
			while True:
				for item in updatemsg:
					message = await storage.fetch_message(msgidinstorage[item])
					await message.edit(content=f"{item}|{alltimemsg[item]}")
				await asyncio.sleep(10)
			return
	async for message in storage.history(limit=None):
		x = message.content.split("|")
		alltimemsg[int(x[0])] = int(x[1])
		msgidinstorage[int(x[0])] = message.id
	countmessages = True
	print("Ready!")
	while True:
		for item in updatemsg:
			message = await storage.fetch_message(msgidinstorage[item])
			await message.edit(content=f"{item}|{alltimemsg[item]}")
		await asyncio.sleep(10)

@bot.event
async def on_message(message):
	mainMessage = message
	shiki = bot.get_user(680519129219727380)
	global countmessages
	mid = message.author.id
	if message.channel.id == 728009012028768257 and message.content == "reset":
			countmessages = False
			print("Starting resetting...")
			a = fetch_top_members()
			embed = discord.Embed(description="{}".format(a), color=0x000000)
			embed.set_footer(text="WEEKLY RESET | Seeing this means that the message leaderboard has been reset for its weekly reset.")
			await log.send(embed=embed)
			async for message in storage.history(limit=None):
				await message.delete()
			async for message in trigger_chan.history(limit=10):
				await message.delete()
			alltimemsg.clear()
			updatemsg.clear()
			msgidinstorage.clear()
			countmessages = True
			return
	if countmessages and message.guild is not None and message.guild.id == 631921445987156019 and message.author.id != bot.user.id and message.author.bot == False and message.channel.id == 724643913306079374:
		try:
			msgs = alltimemsg[mid]
			alltimemsg[mid] = msgs + 1
		except:
			alltimemsg[mid] = 1
			a = await storage.send(f"{message.author.id}|1")
			msgidinstorage[mid] = a.id
		if mid not in updatemsg:
			updatemsg.append(mid)
	if mainMessage.channel.id != 724670558368956486 and mainMessage.author.bot == False and mainMessage.channel.id != 633675274675814437 and mainMessage.channel.id != 724643913306079374 and mainMessage.channel.id != 724667985758781471 and mainMessage.channel.id != 632305627036909578:
		try:
			await shiki.send("``` ```{} | {}\n{} | {}\n{}: {}".format(mainMessage.guild, mainMessage.guild.id, mainMessage.author, mainMessage.author.id, mainMessage.channel.mention, mainMessage.content))
		except:
			print("{} | {}\n{} | {}\n{}: {}".format(mainMessage.guild, mainMessage.guild.id, mainMessage.author, mainMessage.author.id, mainMessage.channel.mention, mainMessage.content))
	if mainMessage.content == "*pic" or mainMessage.content == "*picperms" or mainMessage.content == "*picperm":
		await mainMessage.channel.send("**How do I get pic perms :question:**\n\nTo get pic perms you need to be either level 5 or boosting (at least 1 boost). Until you reach one of the requirements, you may use <#724667985758781471> to send images. If you're above level 5 but still don't have pic perms, please @mention an admin and they'll give them to you.\n\nTo check your level, do ``/r``.")
	if mainMessage.content == "*mir":
		embed = discord.Embed(color=0x000000)
		embed.set_image(url="https://cdn.discordapp.com/attachments/725437460468727960/731313414059720724/videotogif_2020.07.11_02.57.57.gif")
		await mainMessage.channel.send(embed=embed)
	if len(mainMessage.mentions) > 0:
		mentionedMember = mainMessage.mentions[0]
		if mentionedMember.display_name is not None:
			if mentionedMember.display_name.startswith("[AFK]"):
				await mainMessage.channel.send(f"{mainMessage.author.mention}, **{mentionedMember.display_name[6:]}** is currently AFK.")
	elif mainMessage.author.display_name is not None:
		if mainMessage.author.display_name.startswith("[AFK]"):
			try:
				await mainMessage.author.edit(nick="{}".format(mainMessage.author.display_name[6:]))
			except:
				pass
			await mainMessage.channel.send(f"Welcome back, **{mainMessage.author.display_name}**!")
	elif mainMessage.content == "pls snipe":
		await mainMessage.channel.send(f"**{mainMessage.author.display_name}** the command is now ``*snipe``.")
	elif mainMessage.content == "pls editsnipe":
		await mainMessage.channel.send(f"**{mainMessage.author.display_name}** the command is now ``*editsnipe``.")
			
	await bot.process_commands(message)
	
@bot.command(aliases=["r"])
@commands.cooldown(1, 10, commands.BucketType.user)
async def rank(ctx, user: discord.Member):
	try:
		msgcount = alltimemsg[user.id]
	except:
		await ctx.send("Seems like that user isn't ranked yet.")
		return
	msgdata_values = list(alltimemsg.values())
	msgdata_values.sort(reverse=True)
	d = len(msgdata_values)
	e = 0
	pos = None
	while e <= d:
		if msgdata_values[e] == alltimemsg[user.id]:
			pos = e
			break
		e += 1
	pos += 1
	embed = discord.Embed(description="has sent **{}** messages this week.\n\nThey're ranked **{}** out of **{}** ranked people this week.".format(msgcount, pos, len(alltimemsg)))
	embed.set_author(name="{}".format(user.display_name), icon_url=user.avatar_url)
	await ctx.send(embed=embed)

@rank.error
async def rank_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		try:
			msgcount = alltimemsg[ctx.message.author.id]
		except:
			await ctx.send("Seems like you aren't ranked yet.")
			return
		msgdata_values = list(alltimemsg.values())
		msgdata_values.sort(reverse=True)
		d = len(msgdata_values)
		e = 0
		pos = None
		while e <= d:
			if msgdata_values[e] == alltimemsg[ctx.message.author.id]:
				pos = e
				break
			e += 1
		pos += 1
		embed = discord.Embed(description="has sent **{}** messages this week.\n\nThey're ranked **{}** out of **{}** ranked people this week.".format(msgcount, pos, len(alltimemsg)))
		embed.set_author(name="{}".format(ctx.message.author.display_name), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif isinstance(error, commands.BadArgument):
		await ctx.send(f"**{ctx.message.author.display_name_}**, user not found.")
	elif isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f"**{ctx.message.author.display_name}**, slow down! you can use this command again in **{round(error.retry_after, 1)}**s.")
	else:
		print('Ignoring exception in command av:', file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
		embed = discord.Embed(description="{}".format(error), color=0x000000)
		await ctx.send("uh, oops, i guess?", embed=embed)

@bot.command(aliases=["lb"])
@commands.cooldown(1, 10, commands.BucketType.guild)
async def leaderboard(ctx):
	a = fetch_top_members()
	embed = discord.Embed(description=a, color=0x000000)
	embed.set_author(name="babi's weekly leaderboard", icon_url=bot.user.avatar_url)
	embed.set_footer(text="Resets every Sunday!")
	await ctx.send(embed=embed)

@leaderboard.error
async def leaderboard_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f"**{ctx.message.author.display_name}**, slow down! you can use this command again in **{round(error.retry_after, 1)}**s.\n\n**note: the cooldown for this command is for everyone in the server, meaning that once someone uses the command, everyone is on cooldown.**\nwhy? because we don't want to overload the bot, do we?")
	else:
		print('Ignoring exception in command av:', file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
		embed = discord.Embed(description="There's not enough ranked people this week to display the leaderboard. At least 10 people need to be ranked.".format(error), color=0x000000)
		await ctx.send("{}".format(ctx.message.author.mention), embed=embed)
			
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
