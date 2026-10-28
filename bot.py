import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

MAX_PLAYERS = 12
joined_users = set()

@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} jest online!")

@bot.command()
async def join(ctx):
    if ctx.author.id in joined_users:
        await ctx.send(f"⚠️ {ctx.author.mention}, już jesteś na liście!")
        return
    if len(joined_users) >= MAX_PLAYERS:
        await ctx.send("❌ Serwer jest już pełny! (**12/12**)")
        return
    joined_users.add(ctx.author.id)
    await ctx.send(f"✅ **{ctx.author.display_name}** dołączył(a)! Stan: **{len(joined_users)}/{MAX_PLAYERS}**")

@bot.command()
async def leave(ctx):
    if ctx.author.id not in joined_users:
        await ctx.send(f"⚠️ {ctx.author.mention}, nie ma Cię na liście!")
        return
    joined_users.remove(ctx.author.id)
    await ctx.send(f"❌ **{ctx.author.display_name}** wyszedł/wyszła. Stan: **{len(joined_users)}/{MAX_PLAYERS}**")

@bot.command()
async def status(ctx):
    await ctx.send(f"📊 Aktualny stan: **{len(joined_users)}/{MAX_PLAYERS}**")

bot.run("MTU2NTAyMDY1ODIxNDM3OTU5MA.Gd75Lc.vmguBRI9Fwlo1V0C33Sor5pwUfHEEsO7KLFFFw")