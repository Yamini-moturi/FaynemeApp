import datetime
from discord.ext import commands
import discord
import time

TOKEN ='HIDDEN FOR SECURITY'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

clients = []
flag = 0
i = 0

@client.event
async def on_message(message):
    global flag
    global client
    global i

    msg = str(message.content)
    
    if message.author == client.user:
        return

    if msg == "-Feyn" and flag == 0:
        await message.channel.send("WELCOME to Feyn-Me! :books: ")
        await message.channel.send("To Join The session type: -join")
        await message.channel.send("To Start The session type: -start -t (Number of Minutes you want to study) (your topic)")
        await message.channel.send("Join the Feyn-Me Session!")
        flag = 1
    
    if(flag == 1 and msg == "-join" and not(message.author.name in clients)):
        await message.channel.send(message.author.name + " Joined the Session")
        i+=1
        clients.append(message.author.name)
        print(clients)

    start = msg.split()
    print(start)
    if(len(start) >= 4):
        if(flag == 1 and start[0] == "-start" and start[1] == "-t"):
            start.remove("-start")
            start.remove("-t")
            x = int(start[0])
            start.remove(start[0])

            await message.channel.send("Feyn-me Session has Started!")
            for i in range (0,len(clients)):
                await message.channel.send(clients[i])
            await message.channel.send("The Topic is: " + ' '.join(start))
            await message.channel.send("You have " + str(x) + " minutes :alarm_clock: to learn")
            
            total_seconds =  60*x
        while total_seconds > 0:
            timer = datetime.timedelta(seconds = total_seconds)
            ##print(timer, end="\r")
            time.sleep(1)
            if(total_seconds % 20 == 0):
                await message.channel.send("Current Time Left: " + str(timer))
            total_seconds -= 1

        await message.channel.send(":bangbang: TIME IS UP :bangbang: ")

        for i in range(0,len(clients)):
            await message.channel.send(clients[i] + " Its your Turn to Present")

            total_seconds =  30
            while total_seconds > 0:
                timer = datetime.timedelta(seconds = total_seconds)
            ##print(timer, end="\r")
                time.sleep(1)
                if(total_seconds % 20 == 0):
                    await message.channel.send("Current Time Left to type: " + str(timer))
                total_seconds -= 1
            await message.channel.send(":bangbang: TIME IS UP :bangbang: ")
            await message.channel.send("20 second voting time")
            await message.channel.send("Do you understand: " + ' '.join(start) + " through, " + clients[i])
            await message.channel.send("Vote ✅ for yes and ❌ for no")
            time.sleep(20)

        await message.channel.send("If ✅ less than: " + str(int(len(clients)/2)) + " then Restart session")
        await message.channel.send("Session is Done")


client.run(TOKEN)
    