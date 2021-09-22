import os
import random
import discord
import json
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix="!")

with open("jokes.json", encoding="utf8") as jsonFile:
    jokes = json.load(jsonFile)
    jsonFile.close()

def get_joke():
        return random.choice(jokes)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='type !witz'))

    print(f'{client.user} has connected to Discord!')

@client.command()
async def witz(ctx):
    response = get_joke()
    await ctx.message.channel.send(response)


@client.command()
async def mudda(ctx):
    # grab the user who sent the command
    user=ctx.message.author
    voice_channel=user.voice.channel
    channel=None
    # only play music if user is in a voice channel
    if voice_channel!= None:
        # grab user's voice channel
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable='ffmpeg.exe', source='1.mp3'))
    else:
        await client.say('User is not in a channel.')

client.run(TOKEN)