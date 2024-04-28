import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def bye(ctx):
    await ctx.send(f'Adios, hasta pronto!')

@bot.command()
async def gen_pass(ctx, pass_length: int):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    await ctx.send(password)

@bot.command()
async def gen_emodji(ctx):
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    await ctx.send(random.choice(emodji))

@bot.command()
async def flip_coin(ctx):
    flip = random.randint(0, 2)
    if flip == 0:
        await ctx.send ("HEADS")
    else:
        await ctx.send ("TAILS")

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command(name='bot')
async def _bot(ctx):
    await ctx.send('Yes, the bot is cool.')

bot.run("INSERT TOKEN")