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
			await ctx.send("Specify Integer in decimal format. Not String You dumb.")
		if isinstance(error, commands.CommandInvokeError):
			await ctx.send("Umm.. You know what decimal numbers are right?")


	@convert.command()
	async def hex(self, ctx, number : str):
		number = int(number, 16)
		d = int(number)
		b = bin(number)
		o = oct(number)
		if number in range(1114112): 
			a = chr(number)
		else:
			a = "No Unicode representation found."
		
		embed = discord.Embed(title="Conversions", description=f"Numerical Conversions of {str(number)}", color=0xc41c1c)
		embed.add_field(name="Binary", value=b, inline=False)
		embed.add_field(name="Decimal", value=d, inline=False)
		embed.add_field(name="Octal", value=o, inline=False)
		embed.add_field(name="UTF-8", value=a, inline=False)

		await ctx.send(embed=embed)	

	@hex.error
	async def hex_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send("Specify valid hexadecimal numbers, not string.")
		if isinstance(error, commands.CommandInvokeError):
			await ctx.send("Hey, I said hexadecimal numbers..")

	@convert.command()
	async def oct(self, ctx, number : str):
		number = int(number, 8)
		d = int(number)
		b = bin(number)
		h = hex(number)
		if number in range(1114112): 
			a = chr(number)
		else:
			a = "No Unicode representation found."
		
		embed = discord.Embed(title="Conversions", description=f"Numerical Conversions of {str(number)}", color=0xc41c1c)
		embed.add_field(name="Binary", value=b, inline=False)
		embed.add_field(name="Decimal", value=d, inline=False)
		embed.add_field(name="Hexadecimal", value=h, inline=False)
		embed.add_field(name="UTF-8", value=a, inline=False)

		await ctx.send(embed=embed)	

	@oct.error
	async def oct_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send("Specify Valid Octal Number")
		if isinstance(error, commands.CommandInvokeError):
			await ctx.send("You know Octal Numbers right?")


def setup(bot):
	bot.add_cog(Programming(bot))

