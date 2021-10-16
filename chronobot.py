import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from urllib.error import HTTPError
from riotwatcher import LolWatcher, ApiError
from globalData import champ_dict
import time

load_dotenv()
TOKEN = os.getenv('TOKEN')
prefix = ">"
bot = commands.Bot(command_prefix=prefix)

api_key = ''
watcher = LolWatcher(api_key)
my_region = 'na1'

'''
commands = {}
commandFiles = os.listdir('commands')
for command in commandFiles:
    commands[command[:-3]] = command
print(commands)
'''

@bot.event
async def on_ready():
    print("Ready!")
'''
@bot.event
async def on_message(message):
    if not(message.content.startswith(prefix)) or message.author.bot:
        return
'''
@bot.command(name="rank")
async def _rank(ctx, arg):
    try:
        summonerName = arg
        account = watcher.summoner.by_name(my_region, summonerName)
        rank = watcher.league.by_summoner(my_region, account['id'])
        rankString = rank[1]['tier'] + ' ' + rank[0]['rank']
        LPString = str(rank[1]['leaguePoints']) + 'LP'
        rankEmbed = discord.Embed(title=summonerName + "'s Rank", color=0xA5F5D8)
        rankEmbed.add_field(name=rankString, value=LPString, inline=False)

        wins = rank[1]['wins']
        losses = rank[1]['losses']

        winratio = "{:.1f}".format(wins / (wins + losses) * 100) + "%"
        rankEmbed.add_field(name='Win Ratio: ' + winratio, value="```python\nWins: " + str(wins) + "\nLosses: " + str(losses) + "\n```", inline=False)

        file = discord.File("ranked-emblems/Emblem_" + rank[1]['tier'][0] + rank[1]['tier'][1:].lower() + ".png", filename="image.png")
        rankEmbed.set_image(url="attachment://image.png")

        await ctx.send(file=file, embed=rankEmbed)
    except ApiError as err:
        if err.response.status_code == 404:
            await ctx.send("Summoner name not found. You may have forgotten quotes or you may have misspelled the name. Name may not exist.")
        elif err.response.status_code == 429:
            await ctx.send("Server busy, please try again later.")
    except IndexError:
        await ctx.send("Summoner does not have a solo rank.")
    except Exception as err:
        print (err)
        await ctx.send("Something went wrong, please try again later!")

@bot.command(name="timePlayed")
async def _timePlayed(ctx, arg):
    try:
        summonerName = arg
        ts = time.time()
        curr_time = round(ts) * 1000

        account = watcher.summoner.by_name(my_region, summonerName)
        matches = watcher.match.matchlist_by_account(my_region, account['accountId'], begin_time=curr_time-604800000)

        secondsPlayed = 0
        for i in matches['matches']:
            match_detail = watcher.match.by_id(my_region, i['gameId'])
            secondsPlayed += match_detail['gameDuration']
        h = secondsPlayed // 3600; m = secondsPlayed % 3600 // 60
        
        timePlayedString = str(h) + " hours " + str(m) + " minutes"
        timePlayedEmbed = discord.Embed(title=summonerName + "'s Time Played This Week", description=timePlayedString, color=0xA5F5D8)
        await ctx.send(embed=timePlayedEmbed)
    except ApiError as err:
        if err.response.status_code == 404:
            await ctx.send("Summoner name not found. You may have forgotten quotes or you may have misspelled the name. Name may not exist.")
        elif err.response.status_code == 429:
            await ctx.send("Server busy, please try again later.")
    except Exception as err:
        print (err)
        await ctx.send("Something went wrong, please try again later!")

@bot.command(name="mastery")
async def _mastery(ctx, arg):
    try:
        summonerName = arg
        account = watcher.summoner.by_name(my_region, summonerName)
        mastery = watcher.champion_mastery.by_summoner(my_region, account['id'])
        masteryEmbed = discord.Embed(title=summonerName + "'s Top 5 Champs", color=0xA5F5D8)
        for i in range(5):
            masteryEmbed.add_field(name="(" + str(i+1) +") " + champ_dict[mastery[i]['championId']], value=mastery[i]['championPoints'], inline=False)
        masteryEmbed.set_image(url="http://ddragon.leagueoflegends.com/cdn/img/champion/splash/" + champ_dict[mastery[0]['championId']] + "_0.jpg")
        await ctx.send(embed=masteryEmbed)
    except ApiError as err:
        if err.response.status_code == 404:
            await ctx.send("Summoner name not found. You may have forgotten quotes or you may have misspelled the name. Name may not exist.")
        elif err.response.status_code == 429:
            await ctx.send("Server busy, please try again later.")
    except Exception as err:
        print("Error: " + err)
        await ctx.send("Something went wrong, please try again later!")

bot.run(TOKEN)
