import discord
from discord.ext import commands

class Programming(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		
	@commands.group()
	async def convert(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send("Invalid Subcommand!")
	
	@convert.command()
	async def dec(self, ctx, number : int):
		
		h = hex(number)
		b = bin(number)
		o = oct(number)
		if number in range(1114112): 
			a = chr(number)
		else:
			a = "No Unicode representation found."
		
		embed = discord.Embed(title="Conversions", description=f"Numerical Conversions of {str(number)}", color=0xc41c1c)
		embed.add_field(name="Binary", value=b, inline=False)
		embed.add_field(name="Hexadecimal", value=h, inline=False)
		embed.add_field(name="Octal", value=o, inline=False)
		embed.add_field(name="UTF-8", value=a, inline=False)

		await ctx.send(embed=embed)

	@dec.error
	async def dec_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send("Specify Integer in decimal format.")

	@convert.command()
	async def hex(self, ctx, number : int):
		
		h = hex(number)
		b = bin(number)
		o = oct(number)
		if number in range(1114112): 
			a = chr(number)
		else:
			a = "No Unicode representation found."
		
		embed = discord.Embed(title="Conversions", description=f"Numerical Conversions of {str(number)}", color=0xc41c1c)
		embed.add_field(name="Binary", value=b, inline=False)
		embed.add_field(name="Hexadecimal", value=h, inline=False)
		embed.add_field(name="Octal", value=o, inline=False)
		embed.add_field(name="UTF-8", value=a, inline=False)

		await ctx.send(embed=embed)

	@dec.error
	async def dec_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send("Specify Integer in decimal format.")
	

def setup(bot):
	bot.add_cog(Programming(bot))

