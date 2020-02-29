import discord
from discord import Message, Guild, Member
from typing import Optional
from discord.ext import commands
import os
import sys
import traceback
import asyncio
from datetime import datetime
import datetime
import random
import json
import requests

from cv import *

# LOADING COMMANDS:
import commands.say
import commands.bc
import commands.av
import commands.ship
import commands.magicball
import commands.afk
import commands.status
import commands.snipe
import commands.editsnipe
#
import commands.reactions.blush
import commands.reactions.poke
import commands.reactions.pat
import commands.reactions.slap
import commands.reactions.hug
import commands.reactions.facepalm
import commands.reactions.kiss
#
import commands.rate.sexyrate
import commands.rate.cuterate
import commands.rate.thotrate
import commands.rate.gayrate
import commands.rate.lesbianrate
import commands.rate.hotrate
#
import commands.events.events

@bot.event
async def on_ready():
	print("rat is ready")

bot.run("Njc0MjczOTQyODM1NTYwNTIx.XkkOBg.C2cfWpSHnN7p1ZW3pI2xW3XFOvc")
