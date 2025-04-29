import discord
import random 
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def en_linea():
    print(f'Tu bot {bot.user} esta en linea!')
    
@bot.command()
async def saludar(ctx,*, mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if mensaje == 'hola':
        
        await ctx.send('Hola, ¿cómo estás?')
        
    elif mensaje == 'que onda':
        
        await ctx.send('Todo bien')
    
    elif mensaje == 'klk':
        
        await ctx.send('Todo bien')
        
token = ''
bot.run(token)

@bot.command()
async def saludar(ctx,*, mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if mensaje == 'aidos':
        
        await ctx.send('adios, espero que te valla bien')
        
    elif mensaje == 'nos vemos':
        
        await ctx.send('nos vemos luego')
    
    elif mensaje == 'hablamos orita':
        
        await ctx.send('esta bien adios')

from discord.ext import commands
from typing import List
import discord

class BanFlags(commands.FlagConverter):
    members: List[discord.Member] = commands.flag(name='member')
    reason: str
    days: int = 1

@commands.command()
async def ban(ctx, *, flags: BanFlags):
    for member in flags.members:
        await member.ban(reason=flags.reason, delete_message_days=flags.days)

    members = ', '.join(str(member) for member in flags.members)
    plural = f'{flags.days} days' if flags.days != 1 else f'{flags.days} day'
    await ctx.send(f'Banned {members} for {flags.reason!r} (deleted {plural} worth of messages)')