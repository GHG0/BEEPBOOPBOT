import discord
import random
import time
import os



chase = 302915543747395585
deven = 689939738911965198
ffa = 775355712271941647
tchannels = []
messages = []
Greet = ["Hello","Hey","Hi","Howdy","Yo","WHAZZUP","G'DAY"]
greet = ["hello","hey","hi","howdy","yo","whazzup","g'day"]

        
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print()
        print(self.user.id)
        print('------')
    async def on_message(self, message):
        
        async def newchannel(message):
            guild = message.guild
            nchannel = await guild.create_text_channel("{0.author.name}".format(message)+"'s terminal channel") 
            tchannels.append((nchannel.id, message.author.id))
            await nchannel.send("[{0.author.name}@".format(message)+channel.name+" **~**]$ ")
        async def terminals(message, channel):
            #create channel for only the message.author.id
            if (message.channel.id, message.author.id) in tchannels:
                if (message.content == "exit" or message.content == "stop"):
                    await channel.delete()
            if(message.content.lower() == "f"):
                await message.add_reaction("🇫")
            if(message.content.lower() == "beep"):
                await message.channel.send("boop")
            #out of range beepboopbot
            if len(messages) > 2:
                if(messages[len(messages)-3].content.lower() == "beep"):
                    if(messages[len(messages)-1].content.lower() =="bot"):
                        await message.channel.send("YAY")
                        for i in messages:
                            await i.add_reaction("🎉")
        async def voicechat(user):
            #if people in voicechannel
                #create text channel for only those in voice channel
            pass

        async def command():
            #file(commands.py)






        #adding messages to array
        messages.append(message)
        if len(messages)>10:
            messages.pop(0)
        print(len(messages))

        print(messages[len(messages)-1].content.lower())
        '''
        for i in messages:
            print(messages[i].content)
        '''
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        else:
            #terminal code(checks to see if terminal)
            await terminals(message, message.channel)
            #My exception
            if message.author.id == deven and message.content.startswith("$"):
                await message.channel.send("YES, GRAND MASTER HACKERMAN")
            
            #chase can't new channel he is not grandmaster else startx with new channel function(above)
            if message.author.id == chase and message.content.startswith("$"):
                await message.channel.send("Chase, I might grant you  GRANDMASTER, but not now!")
            elif message.content == "$startx":
                await message.channel.send("**BEEPBOOPBOT ACTIVATED** Welcome {0.author.name}".format(message))
                await newchannel(message)
            elif message.content.startswith("$"):
                command()

            #GREETINGS (HI hello sup)
            for i in greet:
                if message.content.lower().startswith(i) or message.content.lower().endswith(i) or (" "+i+" ") in message.content.lower():
                    a = await message.channel.send(Greet[random.randint(1,len(greet))])
                    await a.add_reaction("👋")
            
            if message.content == "clear -a":
                async for i in message.channel.history(limit=200):
                    if i.author == message.author:
                        await message.delete()
                        print("deleted")

            #someone @s beepboopbot
            if message.content == '<@!775358011899117618>':
                await message.channel.send("WHAT DO YOU WANT {0.author.mention}".format(message))

client = MyClient()
client.run('Nzc1MzU4MDExODk5MTE3NjE4.X6lKaw.tokXBro1hr_lXADKh2DFabdP9bs')



#regex