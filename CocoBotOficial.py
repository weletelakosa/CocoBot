import discord
import os
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

cococadena = False
cococontador = 0

record_file = 'record.txt' # archivo donde se guarda el actual record
coco_emoji = "\U0001F965"  # El cococode (coco emoji)


# abrir y leer el archivo
def leer_record():
    try:
        with open(record_file, 'r') as file:
            return int(file.read()) # regresa el record actual del archivo
    except FileNotFoundError:
        return 0


# actualizar el archivo del record
def actualizar_record(contador):
    record_actual = leer_record()

    if contador > record_actual:
        with open(record_file, 'w') as file:
            file.write(str(contador))
            print('Actualizado')
        return True

    return False # si el if no se cumple, se retorna False, si se ejecuta el if retorn True y esta parte se salta        


# Pa saber que el bot esta corriendo como Forrest Gump
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


# Manda un coquito bien fachero al hacer /coco
@bot.command()
async def coco(ctx):
    await ctx.send(coco_emoji)


# Inicia el culto del coco al hacer /cocotime
@bot.command()
async def cocotime(ctx):
    global cococadena, cococontador

    if cococadena:
        await ctx.send('Re perdido el Einstein, unete ya!')
    else:
        await ctx.send('COCOTIMEEEEEEEE WOOOOOOO, manda un cocardo bien fachero para continuarla <3 (o ere puto)')
        await ctx.send(coco_emoji)

        cococadena = True
        cococontador = 1


@bot.command()
async def record(ctx):
    record_actual = leer_record()

    await ctx.send(f'El record actual de la CocoSecuencia es de {record_actual}.')


@bot.event
async def on_message(message):
    global cococadena, cococontador

    # pa evitor ataques esquizofrenicos por parte del bot 
    if message.author == bot.user:
        return
    
    if cococadena and message.content == coco_emoji:
        cococontador += 1
    elif cococadena:
        await message.channel.send(f'Cocotime is over :( llegamos a {cococontador} cocardos. Gracias a todos los que participaron y palazo al que rompio la cadena)')
        
        # chequeamos si es un nuevo record
        if actualizar_record(cococontador):
            await message.channel.send('Nuevo record!!')
            
        # reseteamos las variables a su valor original
        cococadena = False
        cococontador = 0

    await bot.process_commands(message)

# Tokenazo del mejor bot en el mundo
bot.run('MTE0ODA3NjM2MTk4Mjk1MTQyNA.GQhxas.UQeOAimZK_3UDWy377k_yxAcEGXAYPb4BuWRzs')