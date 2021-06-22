import requests
import json
import scrapers
import os
from discord.ext import commands
import discord
import random
from dotenv import load_dotenv
'''
resp = requests.get('https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v001/',params= {'key':'D7D55CC00D5B38980B0E33BC370AC3C7','match_id':'6053528538'})
k = resp.json()
for i in range(0,9):
    print(k['result']['players'][i]['account_id'])
f = json.dumps(k,indent=1)
print(f)
'''
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()
bot = commands.Bot(command_prefix='-')

'''
@client.event

'''
'''
@client.event
async def on_message(message):
    member = discord.Member
    embed = discord.Embed(title = member.name ,description = member.mention, color=discord.Colour.red())
    embed.add_field(name = '',value = 'Sunny best kundi')
    responses = [
        'Sunny best kundi in kerala',
        'Surya cherumani'

    ]

    if message.content == '-sexytime':
        response = random.choice(responses)
        await message.channel.send(response)
'''
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)



@bot.command()
async def sexytime(ctx):
    responses = [
        'Sunny best kundi in kerala',
        'Surya cherumani'

    ]
    embed = discord.Embed(title='Quote of the day', description=random.choice(responses), color=discord.Colour.red())
    await ctx.send(embed=embed)

@bot.command()
async def winrate(ctx,arg):
    win = scrapers.hero_call(arg)
    embed = discord.Embed(title=arg, color = discord.Colour.red())
    embed.add_field(name = 'Win Rate', value=win)
    if arg=='anti-mage':
        arg = 'antimage'

    thumb ="https://cdn.dota2.com/apps/dota2/images/heroes/"+arg+"_vert.jpg"
    embed.set_thumbnail(url = thumb)
    await ctx.send(embed = embed)


bot.run(TOKEN)