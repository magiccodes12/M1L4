import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f'Hola, soy un bot {client.user}!')
    elif message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
    elif message.content.startswith('bye'):
        await message.channel.send(f'Adios, hasta pronto')
        await message.channel.send("he" * count_heh)
    elif message.content.startswith('$smile'):
        await message.channel.send("(｡●́‿●̀｡)")
        
client.run("INSERT TOKEN")

"""#elif message.content.startswith('$smile'):
    #await message.channel.send("(｡●́‿●̀｡)")
elif message.content.startswith('$coin'):
    await message.channel.send(flip_coin())
elif message.content.startswith('$pass'):
    await message.channel.send(gen_pass(10))
else:
    await message.channel.send("No puedo procesar este comando, ¡lo siento!")"""
        
        
