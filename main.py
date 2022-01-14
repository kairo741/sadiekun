from random import randint
import os
import discord
import constants
from discord.ext import commands

client = commands.Bot(command_prefix=">")


@client.event
async def on_ready():
    print("Bot on")


async def play_sound(file_name, context):
    connect = True
    connectedChannel = discord.utils.get(client.voice_clients,
                                         guild=context.guild)

    if connectedChannel is None:
        connect = await join_channel(context)

    if connect:
        channel = discord.utils.get(client.voice_clients, guild=context.guild)
        channel.play(
            discord.FFmpegPCMAudio(executable="C:/path/ffmpeg.exe",
                                   source=file_name))
        return True


async def join_channel(context):
    authorVoice = context.message.author.voice
    if authorVoice is not None:
        await authorVoice.channel.connect()
        return True
    else:
        return False


@client.command("leave")
async def disconnect(context):
    channel = discord.utils.get(client.voice_clients, guild=context.guild)
    if channel is not None:
        await channel.disconnect(force=True)


@client.command("stop")
async def stop_playing(context):
    channel = discord.utils.get(client.voice_clients, guild=context.guild)
    if channel is not None:
        channel.stop()


@client.command("ult")
async def play_ult(context, char, language="PT"):
    # PT_BR
    if language.upper() == constants.LANG_PT:
        if char.lower() == constants.PHOENIX.lower():
            return await play_sound(constants.PHOENIX_ULT_1_PT_BR, context)
        elif char.lower() == constants.RAZE.lower():
            await play_sound(constants.RAZE_ULT_1_PT_BR, context)
    # EN
    elif language.upper() == constants.LANG_EN:
        if char.lower() == constants.PHOENIX.lower():
            return await play_sound("sounds/namoral_vc_morreu.mp3", context)
        elif char.lower() == constants.RAZE.lower():
            await play_sound(constants.RAZE_ULT_1_EN, context)


# Toca toda a voice line do agente
@client.command("voiceline")
async def play_ult(context, char, language="PT"):
    # PT_BR
    if language.upper() == constants.LANG_PT:
        if char.lower() == constants.PHOENIX.lower():
            return await play_sound(constants.PHOENIX_ULT_1_PT_BR, context)
        elif char.lower() == constants.RAZE.lower():
            await play_sound(constants.RAZE_ALL_VOICE_LINES_PT_BR, context)
    # EN
    # elif language.upper() == constants.LANG_EN:
    #     if char.lower() == constants.PHOENIX.lower():
    #         return await play_sound("sounds/namoral_vc_morreu.mp3", context)
    #     elif char.lower() == constants.RAZE.lower():
    #         # await play_sound(constants.RAZE_ULT_1_EN, context)


@client.command("random")
async def play_ult(context, char, language="PT"):
    # PT_BR
    if language.upper() == constants.LANG_PT:
        if char.lower() == constants.PHOENIX.lower():
            return await play_sound(constants.PHOENIX_ULT_1_PT_BR, context)
        elif char.lower() == constants.RAZE.lower():
            await play_sound(constants.RAZE_FUCKED_PT_BR, context)
    # EN
    # elif language.upper() == constants.LANG_EN:
    #     if char.lower() == constants.PHOENIX.lower():
    #         return await play_sound("sounds/namoral_vc_morreu.mp3", context)
    #     elif char.lower() == constants.RAZE.lower():
    #         await play_sound(constants.RAZE_ULT_1_EN, context)


@client.command("brocou")
async def play_ult(context):
    await play_sound(get_random_brocou(), context)


def get_random_brocou():
    brocous = [
        constants.AI_TU_BROCOU_1,
        constants.AI_TU_BROCOU_2,
        constants.AI_TU_BROCOU_3
    ]
    return brocous[randint(0, len(brocous) - 1)]


client.run(os.environ["BOT_TOKEN"])