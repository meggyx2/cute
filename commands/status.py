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
@commands.has_permissions(administrator=True)
async def status(ctx, a, b, *, status: str = " "):
    if len(a) != 0:
        if (a == "o" or a == "online") and (b == "p" or b == "playing"):
            embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(status),
                                                                type=discord.ActivityType.playing))
        elif (a == "o" or a == "online") and (b == "w" or b == "watching"):
            embed = discord.Embed(description="Status changed. \n**Online**\n**Watching {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(status),
                                                                type=discord.ActivityType.watching))
        elif (a == "o" or a == "online") and (b == "l" or b == "listening"):
            embed = discord.Embed(description="Status changed. \n**Online**\n**Listening to {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(status),
                                                                type=discord.ActivityType.listening))
        elif (a == "i" or a == "idle") and (b == "p" or b == "playing"):
            embed = discord.Embed(description="Status changed. \n**Idle**\n**Playing {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.idle,
                                      activity=discord.Activity(name='{}'.format(status),
                                                                type=discord.ActivityType.playing))
        elif (a == "i" or a == "idle") and (b == "w" or b == "watching"):
            embed = discord.Embed(description="Status changed. \n**Idle**\n**Watching {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.idle,
                                      activity=discord.Activity(name='{}'.format(status),
                                                                type=discord.ActivityType.watching))
        elif (a == "i" or a == "idle") and (b == "l" or b == "listening"):
            embed = discord.Embed(description="Status changed. \n**Idle**\n**Listening to {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.idle,
                                      activity=discord.Activity(name='{}'.format(status),
                                                                type=discord.ActivityType.listening))
        elif (a == "d" or a == "dnd") and (b == "p" or b == "playing"):
            embed = discord.Embed(description="Status changed. \n**Do Not Disturb**\n**Playing {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name='{}'.format(status),
                                                                                           type=discord.ActivityType.playing))
        elif (a == "d" or a == "dnd") and (b == "w" or b == "watching"):
            embed = discord.Embed(
                description="Status changed. \n**Do Not Disturb**\n**Watching {}**".format(status), color=0x000000)
            await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name='{}'.format(status),
                                                                                           type=discord.ActivityType.watching))
        elif (a == "d" or a == "dnd") and (b == "l" or b == "listening"):
            embed = discord.Embed(
                description="Status changed. \n**Do Not Disturb**\n**Listening to {}**".format(status),
                color=0x000000)
            await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name='{}'.format(status),
                                                                                           type=discord.ActivityType.listening))
        elif a == "o" or a == "online":
            if len(a) == 1:
                statuss = ctx.message.content[9:]
            elif len(a) == 6:
                statuss = ctx.message.content[14:]
            embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(statuss),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(statuss),
                                                                type=discord.ActivityType.playing))
            embed2 = discord.Embed(description="Since you didn't provide a valid **status_msg**, I chose the default one: **Playing**.", color=0xf2f542)
            embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed2)
        elif a == "i" or a == "idle":
            if len(a) == 1:
                statuss = ctx.message.content[9:]
            elif len(a) == 4:
                statuss = ctx.message.content[12:]
            embed = discord.Embed(description="Status changed. \n**Idle**\n**Playing {}**".format(statuss),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.idle,
                                      activity=discord.Activity(name='{}'.format(statuss),
                                                                type=discord.ActivityType.playing))
            embed2 = discord.Embed(
                description="Since you didn't provide a valid **status_msg**, I chose the default one: **Playing**.",
                color=0xf2f542)
            embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed2)
        elif a == "d" or a == "dnd":
            if len(a) == 1:
                statuss = ctx.message.content[9:]
            elif len(a) == 3:
                statuss = ctx.message.content[11:]
            embed = discord.Embed(
                description="Status changed. \n**Do Not Disturb**\n**Playing {}**".format(statuss), color=0x000000)
            await bot.change_presence(status=discord.Status.dnd,
                                      activity=discord.Activity(name='{}'.format(statuss),
                                                                type=discord.ActivityType.playing))
            embed2 = discord.Embed(
                description="Since you didn't provide a valid **status_msg**, I chose the default one: **Playing**.",
                color=0xf2f542)
            embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed2)
        elif a == "playing" or a == "p":
            if len(a) == 1:
                statuss = ctx.message.content[9:]
            elif len(a) == 7:
                statuss = ctx.message.content[15:]
            embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(statuss),
                                 color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(statuss),
                                                                type=discord.ActivityType.playing))
            embed2 = discord.Embed(
                description="Since you didn't provide a valid **status_ttpe**, I chose the default one: **Online**.",
                color=0xf2f542)
            embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed2)
        elif a == "w" or a == "watching":
            if len(a) == 1:
                statuss = ctx.message.content[9:]
            elif len(a) == 8:
                statuss = ctx.message.content[16:]
            embed = discord.Embed(description="Status changed. \n**Online**\n**Watching {}**".format(statuss),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(statuss),
                                                                type=discord.ActivityType.watching))
            embed2 = discord.Embed(
                description="Since you didn't provide a valid **status_type**, I chose the default one: **Online**.",
                color=0xf2f542)
            embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed2)
        elif a == "l" or a == "listening":
            if len(a) == 1:
                statuss = ctx.message.content[9:]
            elif len(a) == 9:
                statuss = ctx.message.content[17:]
            embed = discord.Embed(description="Status changed. \n**Online**\n**Listening to {}**".format(statuss),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(statuss),
                                                                type=discord.ActivityType.listening))
            embed2 = discord.Embed(
                description="Since you didn't provide a valid **status_type**, I chose the default one: **Online**.",
                color=0xf2f542)
            embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed2)
        else:
            embed2 = discord.Embed(
                description="Since you didn't provide a valid **status_type** and/or **status_msg** combination, I chose the default ones: **Online** and **Playing**.",
                color=0xf2f542)
            embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed2)
            embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(status),
                                                                type=discord.ActivityType.playing))

        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="You didn't provide a status.", color=0xFF3639)
        embed.set_image(url=ctx.message.author.guild.icon_url)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
        return

@status.error
async def status_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        if len(ctx.message.content) > 8:
            embed2 = discord.Embed(
                description="Since you didn't provide a valid **status_type** and/or **status_msg**, I think that the status is empty. I'll get the status by your message. (COULD **NOT BE WORKING PROPERLY**!)",
                color=0xf2f542)
            embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed2)
            status = ctx.message.content[7:]
            embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(status),
                                                                type=discord.ActivityType.playing))
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description="You didn't provide a status.", color=0xFF3639)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed)
            return
    if isinstance(error, commands.MissingRequiredArgument):
        if len(ctx.message.content) > 8:
            embed2 = discord.Embed(
                description="Since you didn't provide a valid **status_type** and/or **status_msg**, I think that the status is empty. I'll get the status by your message. (COULD **NOT BE WORKING PROPERLY**!)",
                color=0xf2f542)
            embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed2)
            status = ctx.message.content[7:]
            embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(status),
                                                                type=discord.ActivityType.playing))
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description="You didn't provide a status.", color=0xFF3639)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed)
            return
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f"**{ctx.message.author.name}** you don't have the **administrator** perms, duh.")
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
