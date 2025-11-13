import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random
import copy  # Importado para copiar a lista de frases

# --- Configuração de Ambiente e Token ---
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# --- Configuração de Logging ---
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# --- Configuração de Intents e Bot ---
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# O prefixo '!' não é mais necessário para slash commands,
# mas podemos manter para comandos antigos, se houver.
bot = commands.Bot(command_prefix='!', intents=intents)

# --- [INÍCIO] LÓGICA DO /FRASESSCAT ---

FRASES_ORIGINAIS = [
    "💅🥤✨ E o nosso shake?? 😋💃🍓",
    "🍔😭💔 Cadê o Hambúrguer desse lanxhyr 😭🍔😩",
    "🥖💔😩 Cadê o patê pra passar na torrada amor 😭😭😭💀",
    "🍽️😡💢 CADÊ MINHA COMIDA 😭🔥🍴",
    "🏒🔥💅 O BASTÃO É MEU 😤⚔️💥",  # Overwatch vibes
    "🪥capa😩 Cadê a pia?? como eu faço pra escovar meus dentes 😭🧼",
    "🍫🎄✨ Gentyr chocotonyyyr 😭🍩💀",
    "🤨💀 Like seriously wtf was that 💀🤡😳",
    "🚽💩🧻 Dessa vez vai ter que funcionar 😭🙏😩💦",
    "😤📄💀 Você tá colando sua filha da putar 🤨👊📚",
    "🎈🤡💅 Você gosta do balão 🎉😩🎈",
    "🤪🎉🔥 Meu essa brincadeira é sensacionais 😭😂💃",
    "😳👀💅 Saori DEIXA ESSA PASSAR 😭🫠✨",
    "💃🔥💋 ahhn! Fazer um STRIPER 😩💀🕺",
    "🕺🎶🎧 Oi Diego tudo bem?? como vai as baladas 😭🔥💃",
    "🏆🥳💅 HAAHAAHAAN!! GANHEI... UHUL 😭💀✨",
    "😈🔪 Eu vou te PUNIR!! e depois não vai ter volta 😭💅🔥",
    "📖🤔💀 O que tá escrito aquir?? hmm... Scale? 😩📜",
    "🌸💨 puhhrh! tá tirando né, eu coloco as flores aqui 😭🌷💀",
    "💨😤😭 O meu peido é bem melhor que o seu 😭🍑💀",
    "😭🍑💨 É ANOS DE PEIDO 😭💅💀",
    "💩👑🔥 Bom já que todo mundo caga muito quero ver QUEM CAGA MAIS 😭💀🧻",
    "💀💥😩 SABE OQ Q É... SCAAAAAAAAAAAAT 💅😭🔥",
    "🧝‍♀️❓😭 pera amiga mas... o que que é um elfo 😭🌟✨",
    "🧝✨💅 O elfo é um ser de luz que realiza pedidos 😭💀🌈",
    "🍔🔥😭 agora você vai comer essa porra desse lanchyr 💅💀🍔",
    "🐀👒💅 Eu sou uma rata senhora 😭✨🐁",
    "🍫😩😭 o chocolate... eu deixei assim pra fazer na hora né 💀🍫💋",
    "🧀🍽️😭 É MUSSSYR? de acordo com o que vocês comeram ó o que torna 😩💅",
    "🎂😭😭 O bolo é ruim... a festa é ruim... Ninguééém vai vir mesmo... 😭💅🎈",
    "⏰😅💀 OIir eu sou a Vitória você tá atrasado você não achar 😭💅",
    "🥚😢💔 É os ovos de codorna 😭🥚😭",
    "👅😱💀 A língua! a língua! a língua! 😭💅",
    "😤💢😭 filadapulta... to com tanto ódio dessa desgraçada 😭💀🔥",
    "🎯🔥💥 preparar... apontar... ó! FOGOOOO 😭💅💀",
    "🏁💥🔥 ihhhh JÁ 😭💅",
    "👗😳💅 OLhá as roupas que você visti- véste 😭👜💀",
    "👑🙄💅 Respeito por favor, a sua superiora 😭💀",
    "🍾😤💅 INÚTIL!! traga champagne 😭💀🥂",
    "🥖😠😭 Pedi pra você por se não quis por... pois agora vou te mostrar a farinha 😩💅",
    "💩💀😭 Comer... a merda... QUE MERDÃ 😭🧻🔥",
    "🎸😭💅 O dia que eu saí de casa minha mãe... 😭🎶😭",
    "💀🔥😭 quer? dou não, ESSE SCAT É MEU 😭💅💀",
    "🥥🌺💅 Meus cocos vindos do HAWAII 😭🌴🔥",
    "🍲😭💅 eu trouxe uma sopinha como prato principal 😭💀🥣"
]
frases_disponiveis = copy.copy(FRASES_ORIGINAIS)

# --- [FIM] LÓGICA DO /FRASESSCAT ---


# --- [INÍCIO] LÓGICA DO /FOTOSSCATEIRAS ---

# 1. Coloque os links das suas fotos aqui.
#    (Botão direito na imagem no Discord > "Copiar Link")
FOTOS_ORIGINAIS = [
    "https://cdn.discordapp.com/attachments/1438498654028828693/1438499915796975686/image.png?ex=69171af1&is=6915c971&hm=35af0dc0a594aa7d077daa5b9fa14f099f6733d2786e5cabfd6b7d34fa274463&",  # <-- Substitua este link
    "https://cdn.discordapp.com/attachments/1438498654028828693/1438500044960563260/image.png?ex=69171b10&is=6915c990&hm=53c74c12ffee122182bac251635d9756a3a248e8775d09cafbb859f4e218bdb2&",  # <-- Substitua este link
    "https://cdn.discordapp.com/attachments/1438498654028828693/1438500268298866759/artworks-51Gia3KjYxV3E1LE-NtKyAg-t1080x1080.png?ex=69171b46&is=6915c9c6&hm=97f848f785eae5fdd2c3a7043a8bd4f8dbb1d917dcf4b30d5f5f29baef688c7a&",
    "https://media.tenor.com/BhqhmwSeDRsAAAAe/newmfx-saori-kido.png",
    "https://pbs.twimg.com/ext_tw_video_thumb/1575171908747886592/pu/img/YXv7-4MJWzsHyN9Y.jpg",
    "https://i.ytimg.com/vi/0INq984CfZk/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCYr-pYLvLemPSpSo4S9Y2mUNaUhg",
    "https://pbs.twimg.com/ext_tw_video_thumb/1708268951006855168/pu/img/eWDGfH8uIjMnBczM.jpg",
    "https://media.tenor.com/ZZVSHVPHFbIAAAAM/saori-kido-newmfx.gif",
    "https://pbs.twimg.com/profile_images/1820791221469552640/CWDk2izV.jpg",
    "https://pt.quizur.com/_image?href=https://img.quizur.com/f/img62a8a9499a9493.07553446.png?lastEdited=1655220561&w=1024&h=1024&f=webp",
    "https://i.gruposwhats.app/grupo-de-whatsapp-flop-newmfx-6764a72a785d4.webp",
    "https://media.tenor.com/3hSJbQlW4bAAAAAM/vaninha-newmfx.gif",
    "https://media.tenor.com/TxDpXcNh65oAAAAM/newmfx-shake.gif",
    "https://i1.sndcdn.com/artworks-DB1SsAwSgyl361uF-fsglMg-t500x500.jpg",
    "https://pt.quizur.com/_image?href=https%3A%2F%2Fimg.quizur.com%2Ff%2Fimg632c971928f3f7.43833336.jpg%3FlastEdited%3D1663866661&w=400&h=400&f=webp",
    "https://i.pinimg.com/736x/89/0d/fd/890dfd6939fbe27d4eca9214666bfb75.jpg",
    "https://media.tenor.com/9Sasg04ziisAAAAM/newmfx-saori-kido.gif",
    "https://pt.quizur.com/_image?href=https://dev-beta.quizur.com/storage/v1/object/public//imagens//20227569/281546e5-7210-47c2-b731-19e41e571534.png&w=600&h=600&f=webp",
    "https://pbs.twimg.com/ext_tw_video_thumb/1714763373143826433/pu/img/W5MNZbfM2Q8xYgfk.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPyYh1E5i_wpgkCkyFy8zPkdRG6sKM4uSTYI6ItnkO0IYu6L8Ul7o5eovMrgDMnnr8UNQ&usqp=CAU",
    "https://pt.quizur.com/_image?href=https%3A%2F%2Fimg.quizur.com%2Ff%2Fimg632c9801d53d48.44929953.jpg%3FlastEdited%3D1663866886&w=400&h=400&f=webp",
    "https://pbs.twimg.com/ext_tw_video_thumb/1563991365549187072/pu/img/rHQKUkEY5r26iyXP.jpg",
    "https://i.pinimg.com/236x/7e/e7/4c/7ee74c38961105368233e559491425f3.jpg",
    "https://pbs.twimg.com/ext_tw_video_thumb/1772666092894216192/pu/img/Weh7INmKm6LTrWGk.jpg",
    "https://pbs.twimg.com/profile_images/1577539043931430913/h6iRSjcc_400x400.jpg",
    "https://pbs.twimg.com/ext_tw_video_thumb/1551398762047848448/pu/img/FM_xRQKSp-XSy9MG.jpg",
    "https://pbs.twimg.com/ext_tw_video_thumb/1531325850142101504/pu/img/75ZKX9dTtdvfRUGM.jpg",
    "https://pbs.twimg.com/media/GMI93DQXoAI4dSX.jpg",
    "https://pbs.twimg.com/media/GVM4lNcXkAAJMAA.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgeWMqJ3tFNfORVlZGPBenQ337T6IdzSqGZA&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_pyKO_-bmbKWBJDGt9-GbVHbj0_wilore4Q&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWnTthI7LyynsqW9i1Ex7VvbVMgTZZSZFDWA&s",
]
fotos_disponiveis = copy.copy(FOTOS_ORIGINAIS)


# --- [FIM] LÓGICA DO /FOTOSSCATEIRAS ---


# --- Eventos do Bot ---

@bot.event
async def on_ready():
    print(f"Estou pronta para soltar rajadões de scat!, {bot.user.name} está online!")
    # Sincroniza os slash commands com o Discord
    try:
        synced = await bot.tree.sync()
        print(f"Sincronizados {len(synced)} comandos de /")
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1438061573712248833)
    if channel:
        await channel.send(f"{member.name} se juntou para a Festa Peidorreira!")
    else:
        print(f"Erro: Canal com ID 1438061573712248833 não encontrado.")


# --- Comandos de Slash ---

@bot.tree.command(name="frasesscat", description="Envia uma frase aleatória do Scat!")
async def frasescat_slash(interaction: discord.Interaction):
    global frases_disponiveis

    if not frases_disponiveis:
        frases_disponiveis = copy.copy(FRASES_ORIGINAIS)
        print("Ciclo de frases Scat completado. Recarregando as frases.")

    resposta = random.choice(frases_disponiveis)
    frases_disponiveis.remove(resposta)

    await interaction.response.send_message(resposta)


# NOVO COMANDO: /fotosscateiras
@bot.tree.command(name="fotosscateiras", description="Envia uma foto scateira aleatória!")
async def fotosscateiras_slash(interaction: discord.Interaction):
    # Indica ao Python que estamos usando a variável global
    global fotos_disponiveis

    # 1. Checa se a lista de fotos disponíveis está vazia
    if not fotos_disponiveis:
        # Se estiver vazia, recarrega a lista para um novo ciclo.
        fotos_disponiveis = copy.copy(FOTOS_ORIGINAIS)
        print("Ciclo de FOTOS Scat completado. Recarregando as fotos.")

    # 2. Escolhe uma foto (link) aleatória das disponíveis
    link_da_foto = random.choice(fotos_disponiveis)

    # 3. Remove a foto escolhida da lista de disponíveis
    fotos_disponiveis.remove(link_da_foto)

    # 4. Envia a resposta (o link). O Discord vai "embedar" a imagem.
    await interaction.response.send_message(link_da_foto)


# --- Rodar o Bot ---
if token:
    bot.run(token, log_handler=handler, log_level=logging.DEBUG)
else:
    print("ERRO: DISCORD_TOKEN não encontrado no arquivo .env")
    print("Por favor, crie um arquivo .env e adicione DISCORD_TOKEN=SEU_TOKEN_AQUI")