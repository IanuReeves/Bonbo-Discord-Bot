# Class Libraries
import discord
import os
import random
from ec2_metadata import ec2_metadata 

# Output to make sure the class libraries work.
print(ec2_metadata.region)
print(ec2_metadata.instance_id)

# Create the client object and load the secret token from an environment variable.
botIntents = discord.Intents.default() # sets intents for the bot to call upon to the default intents
botIntents.message_content = True # set message content intent to true (simplest way I could get it to work on latest discord py)
client = discord.Bot(intents=botIntents)

token = os.getenv("DISCORD_TOKEN")

if token is None:
    print("Error: DISCORD_TOKEN environment variable not found.")
    exit()

@client.event 
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))
     
@client.event
async def on_message(message): 
    
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    
    print(f'Message {user_message} by {username} on {channel}')

    if message.author == client.user: 
        return 
    
    if channel == "testing":

        if user_message.lower() == "boomer?":
            print("Boomer recieved!")
            await message.channel.send(f"Sooner! {username} Your EC2 Data: {ec2_metadata.region}")
            return 
        
        elif user_message.lower() == "bad bot":
            await message.channel.send(f'😭 why tho')
            
        elif user_message.lower() == "clank":
            await message.channel.send(f'No, drumming monkey 🥁🐒')

        elif user_message.lower() == "region":
            await message.channel.send("Your instance region is " + ec2_metadata.region)

        elif user_message.lower() == "instance id":
            await message.channel.send("Your instance ID is " + ec2_metadata.instance_id)

        elif user_message.lower() == ":/":
            await message.channel.send(":/")
        
        elif user_message.lower().__contains__("should i"):
            responses = [
                "No, I wouldn't recommend it.",
                "Maybe. You could pull it off...",
                "Totally, you got what it takes"
            ]
            await message.channel.send(random.choice(responses))

client.run(token)