import discord
from discord.ext import commands
from discord.abc import PrivateChannel
from discord import NotFound
from discord.ext.commands import Bot
from random import *
import asyncio
import os
import subprocess
import time
import schedule
import threading
# import requests

TOKEN = "NzM0MzM3MDA4NzQ2MzY0OTQ4.XxQP6g.pl59iTwZaG13MSSDWx4Z6zcFjLc"
BOT_PREFIX = ("!", "?", "§")

client = commands.Bot(command_prefix=BOT_PREFIX)


@client.command()
async def test(ctx):
    await ctx.channel.send('test  :eyes:')

@client.command()
async def ping(ctx):
    await ctx.send(f'pong {round(client.latency *1000)} ms')

@client.command()
async def mention(ctx):
    mention = ctx.author.mention
    response = f"Je te mentionne {mention}"
    await ctx.channel.send(response)

@client.command()
async def Présentation(ctx):
    await ctx.channel.send('Hey, Je suis Alpha_Titouan :blush:')

@client.command()
async def Coucou_secret(ctx):
    nom = ctx.author
    await nom.send("Coucou :heart:")

kiss_image=['https://i.pinimg.com/originals/be/66/eb/be66ebf461e8529944cda8829197c2ab.jpg',
            'https://cdn.pixabay.com/photo/2017/09/23/16/33/pixel-heart-2779422_960_720.png',
            'https://www.artandstick.be/getsupercustomizedimage.php5?objid=260&colorid1=13&colorid2=4&colorid3=4&colorid4=4&colorid5=4&way=NORMAL&transparent=Y',
            'https://c7.uihere.com/files/769/939/779/sticker-love-telegram-emotion-clip-art-kiss-sticker.jpg',
            ]
@client.command()
async def kiss(ctx):
    member= ctx.message.mentions
    image_url=kiss_image[randint(0,len(kiss_image)-1)]
    embed = discord.Embed(title="**Kiss**", description=f":kissing_heart: {member[0].mention}")
    embed.set_image(url= image_url)
    await ctx.channel.send(embed=embed)


vote_kick = {}
# dictionnaire des id des messages de kicks démocratiques et des votes nécéssaires pour qu'ils soit kick

@client.command()
@commands.has_permissions(kick_members=True)
async def kick_democratique(ctx, cible: discord.Member, *, raison=None):
    if cible.id == 457878731097243649:
        await ctx.channel.send("Je ne vois pas de raison de bannir cette personne :face_with_monocle:")
    else:
        nbr_membres = ctx.guild.member_count
        # def check_emoji(reaction,user):
        #     return message.id == reaction.message.id and (str(reaction.emoji)=='✅' or str(reaction.emoji)=='❎')
        embed = discord.Embed(title="**Expulsion**", description=f"Doit on kick {cible.mention}")
        msg = await ctx.channel.send(embed=embed)
        await msg.add_reaction("❎")
        await msg.add_reaction("✅")
        vote_kick[msg.id] = nbr_membres/2
        print(vote_kick)
        await asyncio.sleep(60)
        del vote_kick[msg.id]

@client.event
async def on_reaction_add(reaction,user):
    id_mes = reaction.message.id
    print(user)
    if id_mes in vote_kick and str(reaction) == '✅' and str(user) != 'Alpha_Titouan#3310' :
        vote_kick[id_mes]-= 1.2
    print(vote_kick,vote_kick[id_mes])
    if vote_kick[id_mes] < 0:
        mes = (await ((reaction.message).channel).fetch_message(id_mes))
        print(mes.mentions)
        cible=(mes.mentions)[0]
        await cible.kick(reason=None)


@client.event
async def on_reaction_remove(reaction,user):
    if reaction.message.id in vote_kick and reaction == '✅' :
        vote_kick[reaction.message.id]+=1

#✅❎ trouvés sur getemoji.com

@client.command()
async def mon_id(ctx):
    await ctx.send(ctx.author.id)
#Mon id est 457878731097243649

@client.event
async def on_message(message):
    if isinstance(message.channel, PrivateChannel) and message.author != client.user and message.author.id != 457878731097243649:
        tit = await client.fetch_user(457878731097243649)
        await tit.send(f"{message.author} m'a envoyé en privé : {message.content}")
    await client.process_commands(message)



def job():
    # tit = await client.fetch_user(457878731097243649)
    # tit.send(f"Test toutes les minutes")
    print("test toutes les minutes")


@client.event
async def on_ready():
    print('Alpha_Titou est prêt')
    




schedule.every(1).minutes.do(job)
client.run(TOKEN)

#while True:
#    schedule.run_pending()
#    time.sleep(1)
