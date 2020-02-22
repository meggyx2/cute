from discord.ext.commands import Bot
from discord.ext import commands
import discord
import http.client
import requests
import json

bot = commands.Bot(command_prefix="*", case_insensitive=True)

colorsEmbed = ["0xFF2121", "0xF4FF21", "0x9BFF21", "0x42FF21", "0x21FFCB", "0x21AEFF", "0x3F21FF", "0xBC21FF", "0xFF219B", "0x000000", "0xFFFFFF"]
