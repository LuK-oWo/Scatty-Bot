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

# --- LISTA DE FRASES (DEFINIÇÃO CONSTANTE) ---
FRASES_ORIGINAIS = [
    "💅🥤✨ E o nosso shake?? 😋💃🍓",
    "🍔😭💔 Cadê o Hambúrguer desse lanxhyr 😭🍔😩",
    "🥖💔😩 Cadê o patê pra passar na torrada amor 😭😭😭💀",
    "🍽️😡💢 CADÊ MINHA COMIDA 😭🔥🍴",
    "🏒🔥💅 O BASTÃO É MEU 😤⚔️💥",  # Overwatch vibes
    "🪥🚰😩 Cadê a pia?? como eu faço pra escovar meus dentes 😭🧼",
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

# Variável GLOBAL de estado: rastreia as frases que ainda não foram usadas.
# Inicializada com todas as frases.
frases_disponiveis = copy.copy(FRASES_ORIGINAIS)


# --- Eventos do Bot ---

@bot.event
async def on_ready():
    print(f"Estou pronta para soltar rajadões de scat!, {bot.user.name} está online!")
    # Adicionado: Sincroniza os slash commands com o Discord
    try:
        synced = await bot.tree.sync()
        print(f"Sincronizados {len(synced)} comandos de /")
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")


@bot.event
async def on_member_join(member):
    # ATENÇÃO: Verifique se este ID de canal está correto!
    # É uma boa prática buscar o canal pelo ID de forma mais robusta
    # ou usar o sistema de "canal de boas-vindas" do Discord.
    channel = bot.get_channel(1438061573712248833)
    if channel:
        await channel.send(f"{member.name} se juntou para a Festa Peidorreira!")
    else:
        print(f"Erro: Canal com ID 1438061573712248833 não encontrado.")


# --- Comando de Slash (/frasesscat) ---

@bot.tree.command(name="frasesscat", description="Envia uma frase aleatória do Scat!")
async def frasescat_slash(
        interaction: discord.Interaction
):
    # Indica ao Python que estamos usando a variável global
    global frases_disponiveis

    # 1. Checa se a lista de disponíveis está vazia
    if not frases_disponiveis:
        # Se estiver vazia, significa que todas as frases foram usadas.
        # Recarrega a lista para um novo ciclo.
        frases_disponiveis = copy.copy(FRASES_ORIGINAIS)
        # Opcional: Avisar no console quando o ciclo recomeça
        print("Ciclo de frases Scat completado. Recarregando as frases.")

    # 2. Escolhe uma frase aleatória das disponíveis
    resposta = random.choice(frases_disponiveis)

    # 3. Remove a frase escolhida para garantir que ela não seja repetida
    frases_disponiveis.remove(resposta)

    # 4. Envia a resposta
    await interaction.response.send_message(resposta)


# --- Rodar o Bot ---
# O seu token é lido do arquivo .env
if token:
    bot.run(token, log_handler=handler, log_level=logging.DEBUG)
else:
    print("ERRO: DISCORD_TOKEN não encontrado no arquivo .env")
    print("Por favor, crie um arquivo .env e adicione DISCORD_TOKEN=SEU_TOKEN_AQUI")