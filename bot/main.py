# ANCHOR MAIN DEPENDENCIES

import discord
from discord.ext import commands
import os

# ANCHOR OPTIONAL DEPENDENCIES

import datetime

# ANCHOR INITIALIZING VARIABLES

token = os.getenv('SCYLLA_TOKEN')
description = '''
A community driven Discord Bot made for programmers, developers and hackers.
'''

# ANCHOR MAIN FUNCTION

if __name__ == '__main__':

	bot = Bot(command_prefix='>', description=description)


	try:
		 bot.run(token)
	except KeyboradInterrupt:
		 bot.logout()

