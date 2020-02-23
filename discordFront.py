import discord
from dotenv import load_dotenv
import os
import re
from gameInfoMain import getSummonerInfo, getMatchInfo, getHelpText

iboisChannelID=594973116019638515
botTestingID=649304929613250560
if os.name == "nt":
    channelID=botTestingID
else:
    channelID=iboisChannelID

# GetToken
token = os.environ['discordToken']
print("Token: {}".format(token))

load_dotenv()
client = discord.Client()

@client.event
async def on_message(message):
    if message.channel.id == channelID:
        if message.author == client.user:
            return
        if "lol" == message.content.lower():
            await message.channel.send('rito sux')
        if "su:" in message.content.lower():
            returnText = getSummonerInfo(message)
            if isinstance(returnText, str):
                await message.channel.send(returnText)
                return
            await message.channel.send(embed=returnText)

        if "ig:" in message.content.lower():
            returnText = getMatchInfo(message)
            if re.search("temp*", returnText):
                await message.channel.send(file=discord.File(returnText))
            else:
                await message.channel.send(returnText)

        if "help:" in message.content.lower():
            await message.channel.send(embed=getHelpText())

        if "test:" in message.content.lower():
            await message.channel.send(embed="")

client.run(token)

