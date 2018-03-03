# My Discord bot user talking
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print("Ready when you are")
    print("I am runnning on" + bot.user.name)
    print("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
  await bot.say(":ping_pong: ping!! xSSSS")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="This is what was found", color=0x00ff00)
    # await bot.say("The users name is: {}").format(user.name)
    embed.add_field(name="Name", value=user.name, inline=True)
    # await bot.say("The users id is: {}").format(user.id)
    embed.add_field(name="ID", value=user.id, inline=True)
    # await bot.say("The users status is: {}").format(user.status)
    embed.add_field(name="Status", value=user.status, inline=True)
    # await bot.say("The users highest role is: {}").format(user.top_role)
    embed.add_field(name="Highest Role", value=user.top_role, inline=True)
    # await bot.say("The user joined at: {}").format(user.joined_at)
    embed.add_field(name="Joined", value=user.joined_at, inline=True)
    # embed.set_thumbnail(user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what was found", color=0x00ff00)
    embed.set_author(name="Ant")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members), inline=True)
    # embed.add_field(name="Joined", value=user.message.joined_at, inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("test")
async def kick(ctx, user:discord.Member):
    await bot.say(":boot: Cya, {}. Ya Loser!".format(user.name))
    await bot.kick(user)


@bot.command(pass_context=True)
async def embed(ctx):
  embed = discord.Embed(title="test", description="Simple bot", color=0x00ff00)
  embed.set_footer(text="foot-er-er-er-er-er-er")
  embed.set_author(name="Ant")
  embed.add_field(name="FIelds", value="not really", inline=True)
  await bot.say(embed=embed)


bot.run("ADD_YOUR_OWN_TOKEN")
