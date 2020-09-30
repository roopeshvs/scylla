

import discord
from discord.ext import commands

import time
import random

class General(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		self.initial_time = time.monotonic() # initialize time for calculating uptime
	 

	@commands.command()
	async def ping(self, ctx):
		current_ping = round(self.bot.latency, 2)
		current_uptime = round(time.monotonic() - self.initial_time, 2)
		embed = discord.Embed(title="Scylla", description="Ping Details", color=0xc41c1c)
		embed.set_thumbnail(url="https://github.com/p014ri5/scylla/raw/master/assets/profile.png")
		embed.add_field(name="🏓 Ping ", value=str(current_ping)+"s", inline=False)
		embed.add_field(name="👍 Uptime", value=str(current_uptime)+"s", inline=False)
		await ctx.send(embed=embed)

	@commands.command(aliases=['8ball'])
	async def ball(self, ctx, *, question):
		responses = [
			"It is certain.",
			"It is decidedly so.",
			"Without a doubt.",
			"Yes – definitely.",
			"You may rely on it.",
			"As I see it, yes.",
			"Most likely.",
			"Outlook good.",
			"Yes.",
			"Signs point to yes.",
			"Reply hazy, try again.",
			"Ask again later.",
			"Better not tell you now.",
			"Cannot predict now.",
			"Concentrate and ask again.",
			"Don't count on it.",
			"My reply is no.",
			"My sources say no.",
			"Outlook not so good.",
			"Very doubtful."
		]
		await ctx.send(f"{random.choice(responses)}")

	@commands.command(aliases=['bullsandcow'])
	async def BandC(self, ctx):
		number = [random.randint(0,9) for n in range(4)]
		count = 0
		while True:
			count += 1
			await ctx.send('Guess.')
			response = await self.bot.wait_for('message')
			print(str(response.content).lower())
			if str(response.content).lower() == 'end':
				await ctx.send(f'Game Over! The Number Was {"".join([str(x) for x in number])}')
				break
			try:
				check_int = int(response.content)
				if check_int < 1000 or check_int > 9999:
					await ctx.send('Enter A Number Between 1000 and 9999.')
					continue
			except:
				await ctx.send('Enter A Number To Guess. To End The Game, Send \'End\' ')
				continue
			guess = [int(i) for i in str(response.content)]
			if guess == number:
				await ctx.send('You Won!')
				await ctx.send(f'It took you {count} guesses.')
				break
			else:
				cows, bulls = 0, 0
				for i in range(4):
					if guess[i] == number[i]:
						cows += 1
					elif guess[i] in number:
						bulls += 1 
				await ctx.send(f'Cows: {cows} Bulls: {bulls}')

	@commands.command(aliases=['rockpaperscissors'])
	async def RPS(self, ctx):
		while True:
			player_win, computer_win = 0, 0
			options = ["Rock", "Paper", "Scissors"]
			computer = options[random.randint(0,2)]
			await ctx.send('Rock. Paper. Scissors?')
			response = await self.bot.wait_for('message')
			player = str(response.content).lower().capitalize()
			if player == "End":
				await ctx.send('Game Over!')
				break
			if player == computer:
				await ctx.send('Tie!')
			elif player == 'rock':
				if computer == 'paper':
					await ctx.send(f"You lose! {computer} covers {player}")
				else:
					await ctx.send(f"You win! {player} smashes {computer}")
			elif player == "Paper":
				if computer == "Scissors":
					await ctx.send(f"You lose! {computer} cuts {player}")
				else:
					await ctx.send(f"You win! {player} covers {computer}")
			elif player == "Scissors":
				if computer == "Rock":
					await ctx.send(f"You lose! {computer} smashes {player}")
				else:
					await ctx.send(f"You win! {player} cuts {computer}")
			else:
				await ctx.send("Invalid Move. Check your spelling! To End The Game, Send \'End\'")

def setup(bot):
	bot.add_cog(General(bot))