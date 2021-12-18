import os
import discord
from keep_alive import keep_alive


intents = discord.Intents.default()
intents.members=True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author==client.user:
        return
    if message.content.startswith("=Hello"):
        await message.channel.send("Fuck Yourself "+str(message.author))
    if message.content.startswith("=How are you?"):
        await message.channel.send("I am fine. How are you?")
    if message.content.startswith("=Jubair"):
        await message.channel.send("Halay haramjada") 
@client.event
async def on_member_join(member):
    # await member.send("hello 123")
    server=member.guild
    if server.system_channel is not None:
          to_send ="yo"
          await server.system_channel.send(to_send)
my_secret = os.environ['tokken']
keep_alive()
client.run(my_secret)

