import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Estou pronta para soltar rajadões de scat!, {bot.user.name} está online!")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1438061573712248833)
    await channel.send(f"{member.name} se juntou para a Festa Peidorreira!")

@bot.command(name="FrasesScat")
async def frasescat(ctx):
    frases = [
        "E o nosso shake? 🥤😋",
        "Cadê o Hambúrguer desse lanxhyr ;-; 🍔😭",
        "Cadê o patê pra passar na torrada amor? 🥖💔",
        "Cadê minha comida?! 🍽️😡",
        "O BASTÃO É MEU! 🏒🔥",  # Overwatch vibes
        "Cadê a pia? como eu faço para escovar meus dentes? 🪥🚰",
        "Gentyr chocotonyyyr 🍫🎄",
        "Like seriously wtf was that? 🤨💀",
        "Dessa vez vai ter que funcionar... 🚽💩🧻",
        "Você tá colando sua filha da putar!? 😤📄",
        "Você gosta do balão? 🎈🤡",
        "Meu essa brincadeira é sensacionais! 🤪🎉",
        "Saori DEIXA ESSA PASSAR? 😳👀",
        "ahhn! Fazer um STRIPER! 💃🔥",
        "Oi Diego tudo bem? como vai as baladas? 🕺🎶",
        "HAAHAAHAAN! GANHEI... uhul! 🏆🥳",
        "Eu vou te PUNIR! e depois não vai ter volta... 😈🔪",
        "O que que ta escrito aquir? hmm... Scale? 📖🤔",
        "puhhrh!... tá tirando né, eu coloco as flores aqui- 🌸💨",
        "O meu peido, é bem melhor que o seu... 💨😤",
        "É anos de peido? 😭🍑",
        "Bom já que todo mundo caga muito eu quero ver QUEM CAGA MAIS! 💩👑",
        "SABE OQ Q É... SCAAAAAAAAAAAAT! 💀💥",
        "pera amiga mas... o que que é um elfo? 🧝‍♀️❓",
        "O elfo é um ser de luz que realiza pedidos 🤖✨",
        "agora você vai comer essa porra desse lanchyr! 🍔🔥",
        "Eu sou uma rata senhora 🐀👒",
        "o chocolate... eu deixei assim pra fazer na hora né 🍫😩",
        "É MUSSSYR? de acordo com o que vocês comeram ó o que torna 🧀🍽️",
        "O bolo é ruim... a festa é ruim... Ninguééém vai vir mesmo... ninguém gosta de bolo de coco 🎂😭",
        "OIir eu sou a Vitória você tá atrasado você não achar... ⏰😅",
        "É os ovos de codorna ;-; 🥚😢",
        "A língua! a língua! a língua! 👅😱",
        "filadapulta... nossa to com tanto ódio dessa desgraçada 😤💢",
        "preparar... apontar... ó! FOGOOOO! 🎯🔥",
        "ihhhh JÁ! 🏁💥",
        "OLhá as roupas que você visti- véste 👗😳",
        "Respeito por favor, a sua superiora 👑🙄",
        "INÚTIL! traga champagne 🍾😤",
        "Pedi pra você por se não quis por... pois agora eu vou te mostrar a farinha ;-; 🥖😠",
        "Comer... a merda... QUE MERDÃ? 💩💀",
        "O dia que eu saí de casa minha mãe... 🎸😭",
        "quer? dou não, ESSE SCAT É MEU! 💀🔥",
        "Meus cocos vindos do HAWAII? 🥥🌺",
        "eu trouxe uma sopinha como prato principal ;-; 🍲😭"
    ]

    # 2. Essas linhas precisam estar DENTRO da função (com indentação)
    resposta = random.choice(frases)
    await ctx.send(resposta)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)