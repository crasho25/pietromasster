import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

TOKEN = open("ID.txt","r").readline()
AUTORIZZATO = open("ID.txt","r").readline()
ctx = " "
role_id = "488118629246959625"

Client = discord.Client()
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
  print("Il Bot è pronto!")
  print('-' * 50)

@client.command()
async def ciao(ctx):
   
  if  ('{0.author.id}'.format(ctx)) == (AUTORIZZATO):
            await ctx.send('Ciao {0.author.mention} mio inventore!'.format(ctx))
  else:
         await ctx.send('NON SEI IL CREATORE DEL BOT {0.author.name}#{0.author.discriminator}'.format(ctx))
         

@client.event
async def on_message(message):
    message.content = message.content.lower().replace(' ', '')
    await client.process_commands(message)
    #print () scrivi il nome di chi usa il bot	 
	  
client.run(TOKEN)
