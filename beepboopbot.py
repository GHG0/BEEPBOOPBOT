import discord
import random
import time
import os
import json
from commands import comm as com


chase = 302915543747395585
deven = 689939738911965198
ffa = 775355712271941647
tchannels = []

with open('config.json') as f:
    config = json.load(f)
prefix = config['prefix']
token = config['token']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print()
        print(self.user.id)
        print('------')
    async def on_message(self, message):
        
        
        async def voicechat(user):
            #if people in voicechannel
                #create text channel for only those in voice channel
            pass

        #adding messages to array
        
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        else:
            #terminal code(checks to see if terminal)
            await com.terminals(message, message.channel)
            #My exception
            if message.author.id == deven and message.content.startswith("$"):
                await message.channel.send("YES, GRAND MASTER HACKERMAN")
            
            #chase can't new channel he is not grandmaster else startx with new channel function(above)
            if message.author.id == chase and message.content.startswith("$"):
                await message.channel.send("Chase, I might grant you  GRANDMASTER, but not now!")
            elif message.content == "$startx":
                await message.channel.send("**BEEPBOOPBOT ACTIVATED** Welcome {0.author.name}".format(message))
                await com.newchannel(message)
            elif message.content.startswith("$"):
                #command()
                pass
                #for now    

            #someone @s beepboopbot
            if message.content == '<@!775358011899117618>':
                await message.channel.send("WHAT DO YOU WANT {0.author.mention}".format(message))

client = MyClient()
client.run(token)



#regex



