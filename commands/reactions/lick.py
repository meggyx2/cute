import discord
from discord.ext import commands
import traceback
import datetime
import asyncio
import random
from datetime import datetime
from cv import *
    
lick_gifs = ["https://cdn.discordapp.com/attachments/729511530219176007/731303038135959563/tenor_4.gif", "https://cdn.discordapp.com/attachments/729511530219176007/731302428632416316/tenor_3.gif", "https://cdn.discordapp.com/attachments/729511530219176007/731301437300015204/rJ6hrQr6-.gif", "https://cdn.discordapp.com/attachments/730521739041439834/731303427623223317/image5.gif", "https://cdn.discordapp.com/attachments/730521739041439834/731303426696151060/image4.gif", "https://cdn.discordapp.com/attachments/730521739041439834/731303425819541604/image2.gif", "https://cdn.discordapp.com/attachments/730521739041439834/731303425500774420/image1.gif", "https://cdn.discordapp.com/attachments/728922679243046953/731303473659772939/anime-lick-gif-4.gif", "https://cdn.discordapp.com/attachments/728922679243046953/731303473445994607/PowerlessVictoriousBullfrog-small.gif", "https://cdn.discordapp.com/attachments/728922679243046953/731302956758204477/tenor-1.gif", "https://cdn.discordapp.com/attachments/728922679243046953/731302951351615548/BestBlueGalapagosalbatross-size_restricted.gif", "https://cdn.discordapp.com/attachments/728922679243046953/731302945957740565/YG4i71E.gif", "https://cdn.discordapp.com/attachments/728922679243046953/731302944963559491/tumblr_osuazevFcj1qcsnnso1_500.gif", "https://cdn.discordapp.com/attachments/728922679243046953/731302943533301900/tenor-3.gif", "https://cdn.discordapp.com/attachments/728922679243046953/731302939359969370/tenor-2.gif", "https://cdn.discordapp.com/attachments/728922679243046953/731302927196618802/unnamed.gif"]
    
@bot.command()
async def lick(ctx, user: discord.Member):
	embed = discord.Embed(description="**{.message.author.name}** licks **{.name}**. 😳".format(ctx, user), color=0xFFFFFF, timestamp=datetime.utcnow())
	embed.set_image(url=random.choice(lick_gifs))
	await ctx.send(embed=embed)
	
@lick.error
async def lick_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="**babi** licks **{.message.author.name}**. 😳".format(ctx), color=0xFFFFFF, timestamp=datetime.utcnow())
		embed.set_image(url=random.choice(lick_gifs))
		await ctx.send(embed=embed)
	elif isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="**babi** licks **{.message.author.name}**. 😳".format(ctx), color=0xFFFFFF, timestamp=datetime.utcnow())
		embed.set_image(url=random.choice(lick_gifs))
		await ctx.send(f"**{ctx.message.author.name}** member not found, I licked you instead", embed=embed)
	else:
		print('Ignoring exception in command av:', file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
		embed = discord.Embed(description="{}".format(error), color=0x000000)
		await ctx.send("uh, oops, i guess?", embed=embed)
