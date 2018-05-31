# ===================================================
# IMPORT'S
# ===================================================

import discord
import asyncio

import secreto
import random
# import chalk

# ----------------------------------------------------

from discord import member
from discord.ext import commands

# ----------------------------------------------------

# import cargos
# import moedas
# import reação
# import purge
# import music

# ===================================================
client = discord.Client()
# ===================================================
COR = 0x690FC3
Token = secreto.seu_token()
bot = commands.Bot(command_prefix='#')
# cargos = cargos.cargos()
# coin = moedas.moeda()
msg_id = None
msg_user = None


# user.name = None
# user.id = None
# user.status = None
# user.top_role = None
# user.joined_at = None
# ===================================================
# IDENTIDADE PELO CONSOLE
# ===================================================

@client.event
async def on_ready():
    print('===================================================')
    print('BOT ONLINE: - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('===================================================')
    print('Version - 1.2')
    print('===================================================')


# ===================================================
# TEST
# ===================================================

# ===================================================
# LOOP BREAK
# ===================================================

@client.event
async def on_message(text):

    if text.author.id == '451519133838737409': return # Berserker Jr.



# ===================================================
# MODELO PARA COMANDOS
# ===================================================

@client.event
async def on_message(message):  # Condição
    if message.content.lower().startswith('%%'):  # PREFIX DO COMANDO (Deste, no caso)
        await client.send_message(message.channel,
                                  "**não irei falar! Você não manda em mim!**")  # Mensagem como resultado

    if message.content.lower().startswith('test'):
        await client.send_message(message.channel, "Qual foi Otário? Tá testando oq?")

    if message.content.lower().startswith('tururu'):
        await client.send_message(message.channel, "https://youtu.be/wEWF2xh5E8s")

    if message.content.lower().startswith('%%'):
        await client.send_message(message.channel, "**Meu Mestre!**")

    if message.content.lower().startswith('berserker jr'):
        await client.send_message(message.channel,
                                  "Olá, me chamo **Berserker Jr.**. Prazer em conhecê-los. Serei o **BOT** desta GUILD"
                                  "com a função e finalidade de ser a ferramenta de informação e de eventos de vocês."
                                  "Espero que gostem de mim :smile:")


        # ===================================================
    # Mensagens Contínuas
    # ===================================================

    # ===================================================
    # Respostas por Embed | Imagens
    # ===================================================

    if message.content.lower().startswith('fazer oq'):  # PREFIX DO COMANDO (Deste, no caso) Não escrever em Maiúsculo.
        fazer = discord.Embed(
            title="**fazer o que né!**",
            color=COR, )

        botmsg = await client.send_message(message.channel, embed=fazer)

        await client.send_message(message.channel, "http://prntscr.com/jhraie")

    # ===================================================
    # FLIP COIN
    # ===================================================

    if message.content.lower().startswith('moeda'):  # Condição
        # if message.author.id == "336311215099740160": #permissão por ID
        # if message.author.id == "author.id":  # permissão por ID
        # if message.author.id == msg.server.roles(STAFF):
        # if message.author.role == ("STAFF"):
        # role = discord.utils.find(lambda r: r.name == "STAFF", msg.server.roles)
        choice = random.randint(1, 2)
        if choice == 1:
            await client.add_reaction(message, '😑')  # Reação por Emoji
        if choice == 2:
            await client.add_reaction(message, '👑')  # Reação por Emoji
    # else:
    # await client.send_message(message.channel, " Você não tem permissão para usar esse comando")
    # ===================================================
    # DICE
    # ===================================================

    # if message.content.lower().startswith('##dado'):  # Condição

    #    choice = random.randint(1, 6)
    #    if choice == 1:
    #        await client.add_reaction(message, '😑')  # Reação por Emoji
    #    if choice == 2:
    #        await client.add_reaction(message, '👑')  # Reação por Emoji
    #    if choice == 3:
    #        await client.add_reaction(message, '😑')  # Reação por Emoji
    #    if choice == 4:
    #        await client.add_reaction(message, '👑')  # Reação por Emoji
    #    if choice == 5:
    #        await client.add_reaction(message, '😑')  # Reação por Emoji
    #    if choice == 6:
    #        await client.add_reaction(message, '👑')  # Reação por Emoji

    #    await client.event(message.channel, )
    #    return
    # else:


# ===================================================
# PING
# ===================================================

# ===================================================
# INFO
# ===================================================

# ===================================================
# WELCOME | LEAVE
# ===================================================

@client.event
async def on_member_join(member):
    canal = client.get_channel("389927650816294925")
    regras = client.get_channel("390906027983372319")
    msg = "Seja Bem-Vindo {}!\n leia as {}\n".format(member.mention, regras.mention)
    await client.send_message(canal, msg)  # substitua canal por member para enviar a msg no DM do membro


@client.event
async def on_member_remove(member):
    canal = client.get_channel("389927650816294925")
    msg = "É uma pena que mais um de nossa tropa acabara de nos deixar {}".format(member.mention)
    await client.send_message(canal, msg)  # substitua canal por member para enviar a msg no DM do membro


# ===================================================
# MUTE
# ===================================================

# ===================================================
# CARGOS
# ===================================================

# ===================================================
# MÚSICA
# ===================================================

# ===================================================
# PARA FUNCIONAR
# ===================================================
client.run(Token)
# ===================================================
