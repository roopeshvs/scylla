import discord
from discord.ext import commands

class Admin(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def clear(self, ctx, amount=3):
		await ctx.channel.purge(limit=amount)

	@clear.error
	async def clear_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send("Specify the amount in positive integers please.")

def setup(bot):
	bot.add_cog(Admin(bot))

