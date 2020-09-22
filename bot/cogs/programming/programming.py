import discord
from discord.ext import commands

class Programming(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def convert(self, ctx, number):
		i = int(number)
		h = hex(number)
		b = bin(number)
		o = oct(number)
		embed = discord.Embed(title="Conversions", description=f"Numerical Conversions of {str(number)}")
		embed.add_field(name="Decimal", value=i, inline=False)
		embed.add_field(name="Binary", value=b, inline=False)
		embed.add_field(name="H", value=h, inline=False)
		embed.add_field(name="Octal", value=o, inline=False)

def setup(bot):
	bot.add_cog(Programming(bot))

