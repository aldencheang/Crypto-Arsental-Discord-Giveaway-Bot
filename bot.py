import discord
from discord.ext import commands

#Discord Token connects bot to API
TOKEN = 'TOKEN'

#prefix cmd to activate commands
client = commands.Bot(command_prefix = '-', intents = discord.Intents.all())

#tells you if your bot working or naw
@client.event
async def on_ready():
    print('Bot Is Ready!')

#sends msg to sender letting them know to check their DMs & And sends msg to DMs
@client.command()
async def meetca(ctx):
    embed1 = discord.Embed(
        description=(
            f'Check your DMs ;)'),
        colour=discord.Colour.purple()
    )
    embed = discord.Embed(
        description=(
            f"Use gift code 'meettaipei2022' for a month of free Starter subscrition to Crypto Arsenal ($29 USD Value) \nOn the website you will find exclusive access to use Alex's strategy!"),
        colour=discord.Colour.purple()
    )
    await ctx.author.send(embed=embed)
    await ctx.send(embed=embed1)

#allows the bot to read all variations of commands i.e meetCa meEtCA MeeTcA
@client.event
async def on_message(message):
    message.content = message.content.lower().replace(' ', '')
    await client.process_commands(message)


client.run(TOKEN)
