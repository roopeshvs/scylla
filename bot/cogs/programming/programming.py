import discord
from discord.ext import commands

class Programming(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

def setup(bot):
	bot.add_cog(Programming(bot))

