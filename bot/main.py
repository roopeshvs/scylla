# ANCHOR MAIN DEPENDENCIES

import discord
from discord.ext import commands
import os

# ANCHOR OPTIONAL DEPENDENCIES

import datetime

# ANCHOR TOKEN, DESCRIPTION, ACTIVITY AND PREFIX

token = os.getenv("SCYLLA_TOKEN")
description = """
A community driven Discord Bot made for programmers, developers and hackers.
"""
prefix = ">"
custom_status = prefix + "help"

# ANCHOR MAIN FUNCTION


bot = commands.Bot(command_prefix=prefix, description=description)

@bot.event
async def on_ready():
	print("--------------------")
	print("Bot is online!")
	print("Build successful 🚀")
	print(f"Logged in as {bot.user.name}")
	print("--------------------")
	print("Setting status and activity")
	await bot.change_presence(status=discord.Status.online, type=1, activity=discord.Game(custom_status))
	print("Status set to")

@bot.command()
async def load(ctx, extension):
	bot.load_extension(f'cogs/{extension}.extension')

@bot.command()
async def unload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}.{extension}')




try:
	 bot.run(token)
except KeyboradInterrupt:
	 bot.logout()

