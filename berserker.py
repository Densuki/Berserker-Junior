# ===================================================
# IMPORT'S
# ===================================================

import discord
# import asyncio

import secreto
import random
# import chalk

# ----------------------------------------------------

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
bot = commands.Bot(command_prefix='%')
# cargos = cargos.cargos()
# coin = moedas.moeda()
# msg_id = None
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
    print('Dai Ikuyo! WariansForce!')
    print('===================================================')


# ===================================================
# TEST
# ===================================================

# ===================================================
# LOOP BREAK
# ===================================================

@client.event
async def on_message(text):
    # if text.author.id == '445388160969605131': return # Nayron
    # if text.author.id == '451072026023690241': return # Nayron Debug [A.I Ignis]
    # if text.author.id == '451510020614389761': return # Berserker Debug
    if text.author.id == '451519133838737409': return # Berserker Jr.



# ===================================================
# MODELO PARA COMANDOS
# ===================================================

@client.event
async def on_message(message):  # Condição
    if message.content.lower().startswith('fala'):  # PREFIX DO COMANDO (Deste, no caso)
        await client.send_message(message.channel,
                                  "**não irei falar! Você não manda em mim!**")  # Mensagem como resultado

    if message.content.lower().startswith('test'):
        await client.send_message(message.channel, "Qual foi Otário? Tá testando oq?")

    if message.content.lower().startswith('%%'):
        await client.send_message(message.channel, "~~viado~~ gente boa")

    if message.content.lower().startswith('dino'):
        await client.send_message(message.channel, "**Meu Mestre!**")

    if message.content.lower().startswith('berserker jr'):
        await client.send_message(message.channel,
                                  "Olá, me chamo **Berserker Jr.**. Prazer em conhecê-los. Serei o **BOT** desta GUILD"
                                  "com a função e finalidade de ser a ferramenta de informação e de eventos de vocês."
                                  "Espero que gostem de mim :smile:")

    ## if message.content.lower().startswith('ignis'):
    ##    await client.send_message(message.channel,
    ##                              "Olá, me chamo **Ignis**. Sou uma **A.I.** com função de Debug e ser a ferramenta "
    ##                              "de testes do @Nayron#0766. Espero que gostem de mim :smile:")


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

    if message.content.lower().startswith('%disgrace'):  # PREFIX DO COMANDO (Deste, no caso)
        disgrace = discord.Embed(
            title="**PORRA**",
            color=COR, )

        botmsg = await client.send_message(message.channel, embed=disgrace)

        await client.send_message(message.channel, "https://i.imgur.com/b2Aj1l2.png")

    if message.content.lower().startswith('thinking'):
        thinking = discord.Embed(
            title="Fascinante!",
            color=COR, )

        botmsg = await client.send_message(message.channel, embed=thinking)

        await client.send_message(message.channel, "http://prntscr.com/jnu8g3")
        await client.send_message(message.channel, "http://prntscr.com/jnu2t2")
        await client.send_message(message.channel, "http://prntscr.com/jnu31b")
        await client.send_message(message.channel, "http://prntscr.com/jnu3a2")

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
