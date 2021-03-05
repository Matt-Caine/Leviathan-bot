# bot.py

import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("with Human Souls"))
    print("[Levi Bot Online]")


@client.command()
@commands.has_permissions(administrator=True)
async def result(ctx, team, desc, result):
    if result == "w":
        result = 0x6dd438
    elif result == "l":
        result = 0xde3939
    else:
        result = 0xc3c3c3

    embed = discord.Embed(title="**" + team + "**", description=desc, color=result)
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def resulthelp(ctx):
    await ctx.send('```!result "TeamName" "Score Breakdown" "w/l/[Leave blank for tie]"```')
    await ctx.send("```The Speech marks and spaces are needed, even when leaving the score result blank for a tie!```")


client.run("Secret Token")
