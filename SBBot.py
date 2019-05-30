import discord
from discord.ext import commands
import random
import asyncio
from discord.utils import get
import json
 

bot = commands.Bot(command_prefix='.',help_command = None)



@bot.command()
async def help(ctx):
    id1 = "<@&572074683457863680>"
    id2 = "<@&572075090557272074>"
    await ctx.send(f"{ctx.author.mention} {id1} {id2} צריך את עזרתכם")



    
@bot.event
async def on_message(message):
     if 'חרא' in message.content:
        await message.delete()
     if 'זונה' in message.content:
        await message.delete()
     if 'זין' in message.content:
        await message.delete()
     if 'מזוין' in message.content:
        await message.delete()
     if 'שרמוטה' in message.content:
        await message.delete()
     if 'זיין' in message.content:
        await message.delete()
     await bot.process_commands(message)
       
     
     
     
 
    



@bot.event
async def on_ready():
 print('bot is ready')


bot.run("NTgzNjMyMDgyODcwNDY4NjI4.XO_LyA.r26W4rsd1exfAHkvLfy_9dXszvk")
