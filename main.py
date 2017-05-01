import discord
import asyncio
import random
import time
import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
from discord.ext import commands

# https://discordapp.com/oauth2/authorize?&client_id=307514139926855680&scope=bot&permissions=0
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def coin_toss(message):
    outcome = random.randint(0,1)
    if outcome == 0:
        outcome = "Heads"
    else:
        outcome = "Tails"
    await client.send_message(message.channel, "Just a moment, flipping the coin...")
    await asyncio.sleep(.5)
    await client.send_message(message.channel, "The coin Shows, %s" % outcome)

@client.event
async def random_trapstorm(message):
    base_url = "http://www.trapstorm.com/randomsong"
    response = urllib.request.urlopen(base_url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    res = soup.findAll('iframe')[0].get('src')
    res_corrected = res.replace('embed/', 'watch?v=').replace('?autoplay=1', '')
    print(res_corrected)
    await client.send_message(message.channel, res_corrected)

@client.event
async def user_page(message, nickname):
    try:
        response = urllib.request.urlopen("http://www.trapstorm.com/user/%s" % nickname)
        await client.send_message(message.channel, response.geturl())
    except urllib.error.HTTPError:
        print("Error")
        await client.send_message(message.channel, "L'utilisateur n'existe pas, pédale.")

@client.event
async def on_message(message):
    if message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!trapstorm'):
        await client.send_message(message.channel, 'Visit http://www.trapstorm.com')
    elif message.content.startswith('!coin'):
        await coin_toss(message)
    elif message.content.startswith('!random'):
        await random_trapstorm(message)
    elif message.content.startswith('!user'):
        await user_page(message, message.content.split()[1])

client.run('MzA3NTE0MTM5OTI2ODU1Njgw.C-TaYA.QdZM0H1se-qdQIREqI2Gy70HiH8')