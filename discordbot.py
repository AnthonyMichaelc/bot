# My Discord bot user talking
# import statements required
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

# Specifying the hashtag attribute
bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
  # prints to the console the bots name and id
    print("Ready when you are")
    print("I am runnning on" + bot.user.name)
    print("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
  # sends a pingpong emoji once somone sends a hashtag ping
  await bot.say(":ping_pong: ping!! o_0")

# Lets take care of pulling the user's info: name, id, status, role, joined
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="This is what was found", color=0x00ff00) # the establishing top message followed by requested data
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest Role", value=user.top_role, inline=True)
    embed.add_field(name="Joined", value=user.joined_at, inline=True)
    # Fires off
    await bot.say(embed=embed)

# Lets take care of pulling the servers's info: name, id, status, role, members
@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what was found", color=0x00ff00)# the establishing top message followed by requested data
    embed.set_author(name="Ant")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members), inline=True)
    # fires off
    await bot.say(embed=embed)

# setting kicking with specified role
@bot.command(pass_context=True)
@commands.has_role("test")
async def kick(ctx, user:discord.Member):
    await bot.say(":boot: Get Out of Here, {}. Weirdo!".format(user.name))
    await bot.kick(user)

# Embed features: title, footer, author, fields
@bot.command(pass_context=True)
async def embed(ctx):
  embed = discord.Embed(title="test", description="Simple bot", color=0x00ff00)
  embed.set_footer(text="foot-er-er-er-er-er-er")
  embed.set_author(name="Ant")
  embed.add_field(name="Fields", value="not really", inline=True)
  await bot.say(embed=embed)

# Must add your token here
bot.run("ADD_YOUR_OWN_TOKEN")
