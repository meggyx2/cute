from discord.ext.commands import Bot
from discord.ext import commands
import discord
import http.client
import requests
import json

bot = commands.Bot(command_prefix="*", case_insensitive=True)
bot.owner_ids = {680519129219727380, 623181235338084362}

snipe_msgs = {}
snipe_msgs_time = {}
editsnipe_msgs = {}
editsnipe_msgs_time = {}

colorsEmbed = ["FF2121", "F4FF21", "9BFF21", "42FF21", "21FFCB", "21AEFF", "3F21FF", "BC21FF", "FF219B", "000000", "FFFFFF"]
