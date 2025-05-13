import discord 
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Tu bot {bot.user} está en línea!')

@bot.command()
async def contaminacion(ctx, *, mensaje: str):
    mensaje = mensaje.lower().strip()

    saludos = {
        'contaminacion': 'El medio ambiente es el conjunto de elementos naturales y artificiales que rodean a los seres vivos e influyen en su desarrollo y supervivencia.',
        'en que afecta la contaminacion plastica en el caribe': 'La contaminación plástica en el Caribe afecta gravemente al medio ambiente, la salud y la economía.',
        'Cómo afecta a los adolescentes': 'La contaminación plástica en el Caribe afecta a los adolescentes dañando su salud, bienestar emocional y espacios de recreación.',
        'aidos': 'adiós, espero que te vaya bien',
        'nos vemos': 'nos vemos luego',
        'hablamos orita': 'está bien, adiós'
    }

    respuesta = saludos.get(mensaje, "No entendí tu saludo 😕")
    await ctx.send(respuesta)




token = ""
bot.run(token)
