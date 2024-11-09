import os
import discord
import random
import requests
from discord.ext import commands
from bot_gencontraseña import gen_pass

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

print(os.listdir())
print(os.listdir('M2L1/image'))

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot llamado {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Adios amigo!')

@bot.command()
async def genera_contraseña(ctx, longitud = 0):
    if longitud == 0:
        await ctx.send(f'No podemos generar una contraseña de 0 digitos. ;)')
    else:
        await ctx.send(f'Muy bien! Tu contraseña generada es: ' + gen_pass(longitud))

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def adivina(ctx, numero_decidido = -1):
    numero_seleccionado = random.randint(0, 10)

    if numero_seleccionado == numero_decidido:
        await ctx.send("Muy bien! El número que adivinaste es el mismo que yo pense!")
    else:
        await ctx.send("Aw! El número que escribiste no es el mismo que yo pense! Yo pense en el número " + str(numero_seleccionado))

@bot.command()
async def mem(ctx):
    #img_name = random.choice(os.listdir('M2L1\image'))
    img_name = 'a'
    if random.randint(0, 100) < 10:
        img_name = 'mem4.png'
    elif random.randint(0, 100) in range(10, 29):
        img_name = 'mem3.jpeg'
    elif random.randint(0, 100) in range(30, 69):
        img_name = 'mem2.jpeg'
    elif random.randint(0, 100) >= 70:
        img_name = 'mem1.jpeg'
    print(img_name)
    with open(os.path.join('M2L1\image', img_name), 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

bot.run()