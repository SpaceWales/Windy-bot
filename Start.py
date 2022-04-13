import requests
import json
import time
import discord
import os
from dotenv import load_dotenv
import Location
import Weather
import CustomizeWeather

#temporary 
import sys

#setup
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = discord.Client()

bot_commands = [
    "-location",
    "-current",
    "-hourly",
    "-daily",
    "-windonly"
]

def is_command(message):
    if len(message.content) == 0:
        return False
    if message.content.split()[0] =='!windy':
        return True
    else:
        return False

def help_commands():
    msg = ""
    for command in bot_commands:
        msg += ("{}\n".format(command))
    return msg


@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print("{} : {}".format(guild.id,guild.name))
        guild_count += 1
    print("Bot appears in {} servers".format(str(guild_count)))

@bot.event
async def on_message(message):
    #don't run commands against the bot
    if message.author != bot.user:
        #check if command
        if is_command(message):
            #split message, [0] is !windy and can be ignored
            msg = ""
            msgContent = message.content.split()
            if "help" == msgContent[1]:
                msg += help_commands()
                await message.channel.send("Sure {}. Commands are: \n{}".format(message.author, msg))
            if "-location" == msgContent[1]:
                #send msgContent[2] to location API to get coordinates
                location_data = Location.start(msgContent[2])
                #send location_data to weather API
                weather_data = Weather.start(location_data,"minutely")
                #check current tag
                if msgContent[3] is not None or "-current" in msgContent[3] or len(msgContent[3] == 0):
                    msg += CustomizeWeather.start(weather_data, msgContent[3])
                await message.channel.send(msg)
            


#offline functions for testing

#pass in arguments that get handed to functions to simulate bot tests

def offline_mode():
    msg = ""
    location_data = Location.start("farmington")
    weather_data = Weather.start(location_data,"minutely")
    msg  += CustomizeWeather.start(weather_data,"-current")
    print(msg)


#commented out for local runs
bot.run(DISCORD_TOKEN)

#offline_mode()





