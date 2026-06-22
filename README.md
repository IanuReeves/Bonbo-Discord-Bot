https://github.com/IanuReeves/Bonbo-Discord-Bot/ 

# Explanation

## *1. What does the Discord bot do?*
  A: My discord bot communicates with EC2 and discord APIs through python to ultimately respond to users within a text channel based on specific keywords or commands

## *2. What is the purpose of the Discord bot token?*
  A: Discord bot tokens are used to authenticate with the discord api, acting as a key for the discord bot to be controlled.

## *3. Why should the token be stored in an environement variable instead of inside the Python file?*
   A: Without the environment variable, those with access to the bot's source code can easily gain complete control of the discord bot, compromising the bot's security

## *4. What information does the bot retruve from the EC2 instance?*
  A: The bot retrieves the instance region and instance ID using the ec2_metadata library, as well as technically the discord token since it's stored on the server.

## *5: How does the bot use the Discord API?*
  A: It uses the Discord API to listen for messages in a server, then sends responses back to the channel. It also authenticates with Discord using the bot token stored in the EC2 server.

## *6. How does this assignment connect to cloud computing?*
  A: This bot runs from the cloud, meaning it has the capibilities to be always active and largely scalable depending on how large and high-computing the project needs to be. 

## *7. How is this bot a basic example of an engentic system?*
  A: This bot automatically listens and executes actions with response to user input.

## *8. Why might developers use a local editor or cloud IDE first, but still need to understand Nano or VIM on a server?*
  A: A few reasons for this:
  - terminal usage is widely popular, especially since most servers are not graphical
  - can be faster than traditional IDEs when editing single files quickly

## *9. How could a more advanced version of this bot be used in an organization?*
  A: A few ways:
  - Within discord, a more advanced version could dynamically search for profanity and ill intent, and execute actions from that information
  - Within discord, a more advanced version could reply to the user in private DMs to notify the status of support tickets or announcements, and even terms of service changes.
  - Within the bounds of discord, a more advanced version could integrate between discord, your app, and other apps to connect experiences together.
  - Outside of discord, a more advanced version could help answer questions for a product or service, becoming a technology of convienience

# Step by Step Showcase

<img width="1384" height="792" alt="Discord server working" src="https://github.com/user-attachments/assets/cb1a9e48-e41c-4350-8876-fbf6a0d59745" />

First, I created a discord server, and added a #testing channel for the bot to later send and recieve messages to/from


<img width="1307" height="532" alt="couldn&#39;t reference discord" src="https://github.com/user-attachments/assets/cde0065d-2c7e-4526-b6a9-2e7327b7335b" />

Then, I went ahead and created my discord bot (discord couldn't be used in the name, so I had name it something else from "Testing Discord Bot")


<img width="1391" height="728" alt="bot on the server" src="https://github.com/user-attachments/assets/ac590220-becc-49ef-a677-41469e3f37bc" />

<img width="1462" height="803" alt="instance summary" src="https://github.com/user-attachments/assets/86ecb2db-d6b3-4395-b678-0fc7907c02e7" />

Once the bot was one the server, I went over and started up the EC2 Instance, where I connected to a console window, and used nano to place the discord bot key inside of a global, persistent variable

<img width="1454" height="605" alt="nano_code" src="https://github.com/user-attachments/assets/d60b4ec7-6660-48e8-a64c-408dfe93547e" />

Using Nano, I also inserted the developed code into a file called bot.py, and used CTRL+O, Enter, and CTRL+X to save changes and exit.

# Bot Practical Showcase

<img width="1470" height="660" alt="running in ec2" src="https://github.com/user-attachments/assets/7a79f745-491b-4474-9bf8-8afc3f7245f7" />

<img width="827" height="482" alt="boomer?" src="https://github.com/user-attachments/assets/ccc6f2cd-b805-404d-8035-197dc977692d" />

Simple commands such as "boomer?", "status", and "instance ID" were created to test the access and availability of information the bot had access to.


<img width="1462" height="803" alt="bad bot" src="https://github.com/user-attachments/assets/15192613-7c06-47c6-b9de-a895b287a88d" />

This example goes beyond simple data collection, adding silly yet intentive commands made to entertain the user.


<img width="828" height="797" alt="optional custom command showcase" src="https://github.com/user-attachments/assets/2014fc74-fb83-45d0-ab0f-d459512f4d84" />

And best of all, a magic 3 ball, with the possibility of reaching exactly 9 possible combinations when sending up to three messages. Make sure the question is different, however, or you may not like the inconsistency!

