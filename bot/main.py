# MAIN LIBRARIES

import discord
from discord.ext import commands
import os

# 

from datetime import datetime


token = os.getenv("SCYLLA_TOKEN")

description = "A community driven Discord bot made for programmers, developers and hackers."
prefix = ">"
custom_status = prefix + "help"


def initialize_cogs():
	cogs = ["general", "admin", "pentesting", "programming"]
	for extension in cogs:
		bot.load_extension(f'cogs.{extension}.{extension}')


bot = commands.Bot(command_prefix=prefix, description=description)

@bot.event
async def on_ready():
	print(f"[{datetime.now().strftime('%d/%m %H:%M:%S')}] Bot is online!")
	print(f"[{datetime.now().strftime('%d/%m %H:%M:%S')}] Build successful 🚀")
	print(f"[{datetime.now().strftime('%d/%m %H:%M:%S')}] Logged in as {bot.user.name}")
	print(f"[{datetime.now().strftime('%d/%m %H:%M:%S')}] Setting status and activity")
	await bot.change_presence(status=discord.Status.online, activity=discord.Game(custom_status))
	print(f"[{datetime.now().strftime('%d/%m %H:%M:%S')}] Status set to {custom_status}")
	print(f"[{datetime.now().strftime('%d/%m %H:%M:%S')}] Initializing cogs")
	initialize_cogs()
	print(f"[{datetime.now().strftime('%d/%m %H:%M:%S')}] Cogs Initialized")
	print(f"[{datetime.now().strftime('%d/%m %H:%M:%S')}] Startup Complete")


@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send("Invalid Command 😐")


# TODO ERROR HANDLING NoEntryPointError 
# TODO UPTIME HANDLING


try:
	 bot.run(token)
except KeyboardInterrupt:
	 bot.logout()

