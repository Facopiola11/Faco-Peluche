import discord
from discord.ext import commands
import random
import asyncio
import os


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def generar_respuesta(mensaje):
    boludeces = [
    "ola",
    "callate",
    "si",
    "no",
    "xd",
    "bombardeen polonia",
    "aguante river",
    "demako es gei",
    "charlikirk",
    "jefrieinstein",
    "electroencefalografista",
    "revivan el server",
    "Shh",
    "el de arriba es un therian",
    "asdasdasdas",
    "shut up",
    "mesi",
    "asdañsldkapompo",
    "facundo peluche",
    "Esternocleidomastoideo",
    "el de arriba le echa mayonesa al guiso",
    "lmao (im from unitedsteist)",
    "free puff",
    "proyect zomboid god",
    "señorpato chad",
    "pablito",
    "iam from amerika",
    ]
    return random.choice(boludeces)


lista = [
    "Por no suscribirse al demako",
    "Murió por nuv",
    "Se morio al contraer la enfermedad de VHS",
    "Morio por furro",
    "Morio pq si",
    "Fue brutalmente atropellado por un camión Volvo FH 420 4X2 que andaba a 45km/h, y transportaba mangos a la ciudad de San Ramón de nueva Orán",
    "Se desuscribió de la vida",
    "fue a conocer a jefrieinistein,charlikirk y rikifor",
    "Le cayó un yunque",
    "Le cayó un meteorito mientras caminaba en la calle",
    "Tuvo un aksidente aerio",
    "tomo agua susia y le agarro colera",
    "comio kk y se morio :v",
    "estaba reparando un asensor i le caio un tornillo y se morio",
    "un sikario vino a su casa y lo dejó como colador",
    "buscó gugul en gugul y se morio",
    "le agarro pendejitis aguda, y morio xd",
    "No gana la libertadores desde 2007 y se morio",
    "lo hicieron cagar y se enojo por que se cago y se morio del enojo",
    "tocó pasto por primera vez y explotó",
    "Dijo sikx seben y un viejo de 50 años vino corriendo y lo macheteo hasta que se morio xdddddddddd bien bramdom",
    "de tanto fumar le agarro EPOC (Enfermedad Pulmonar Obstructiva Cronica) y morio ;v"
    ]

@bot.event

async def on_message(message):
    if message.author.bot:
        return
    
    if random.random() < 0.1:
        respuesta = await generar_respuesta(message.content)
        await message.reply(respuesta)

    await bot.process_commands(message)    

@bot.command()       

async def deathnote(ctx, miembro: discord.Member):
   await ctx.send(f"{ctx.author.name} escribió el nombre de {miembro.name} en la Death Note")

   await asyncio.sleep(5)

   muertesrandom = random.choice(lista)

   await ctx.send(f"{miembro.mention}" f"{muertesrandom}")

TOKEN = os.environ["TOKEN"]

bot.run(TOKEN)


