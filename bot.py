from asyncio.events import BaseDefaultEventLoopPolicy
import discord

intents = discord.Intents.default()
intents.typing = True
intents.presences = True

token = "THE TOKEN GOES HERE"
client = discord.Client(intents=intents)

@client.event
async def on_message(message: discord.message):
    print(f"{message.author}: {message.content}")
    if message.content == "!hi":
        print("Hi")
        await message.channel.send("Hello")

@client.event
async def on_member_update(before, after):
    nickname = after.nick
    print("i", nickname)
    if str(nickname).casefold() == "test":
        before_nick = str(before.nick)
        print("2", before_nick)
        if before_nick:
            print("3")
            await after.edit(nick=before_nick)
        else:
            print("4")
            await after.edit(nick="It Works!")

@client.event
async def on_ready():
    print("Ready!!!")

client.run(token)