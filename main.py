import os
from random import choice

import discord
from discord.ext import commands

import constants
import ascii

client = commands.Bot(command_prefix=">")


@client.event
async def on_ready():
    message = choice([ascii.BOT_ON_1, ascii.BOT_ON_2, ascii.BOT_ON_3, ascii.BOT_ON_4, ascii.BOT_ON_5, ascii.BOT_ON_6,
                      ascii.BOT_ON_7])
    print(message)


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
async def play_ult(context, char, language=constants.LANG_PT, *side):
    ally = None
    if side is not None:
        for x in side:
            if x.lower() == "enemy":
                ally = False
            elif x.lower() == "ally".lower():
                ally = True

    if ally is None:
        ally = choice([True, False])
    # Som da ult aliada
    if ally:
        # PT_BR
        if language.upper() == constants.LANG_PT:
            # PHOENIX
            if char.lower() == constants.PHOENIX.lower():
                return await play_sound(constants.PHOENIX_ULT_1_PT_BR, context)
            # RAZE
            elif char.lower() == constants.RAZE.lower():
                await play_sound(constants.RAZE_ULT_ALLY_1_PT_BR, context)
            # BRIM
            elif char.lower() == constants.BRIMSTONE.lower():
                await play_sound(constants.BRIMSTONE_ULT_ALLY_1_PT_BR, context)
        # EN
        elif language.upper() == constants.LANG_EN:
            if char.lower() == constants.PHOENIX.lower():
                return await play_sound("sounds/namoral_vc_morreu.mp3", context)
            elif char.lower() == constants.RAZE.lower():
                await play_sound(constants.RAZE_ULT_ALLY_1_EN, context)

    # Som da ult inimiga
    else:
        # PT_BR
        if language.upper() == constants.LANG_PT:
            # PHOENIX
            if char.lower() == constants.PHOENIX.lower():
                return await play_sound(constants.PHOENIX_ULT_1_PT_BR, context)
            # RAZE
            elif char.lower() == constants.RAZE.lower():
                await play_sound(constants.RAZE_ULT_ENEMY_1_PT_BR, context)
            # BRIM
            elif char.lower() == constants.BRIMSTONE.lower():
                await play_sound(constants.BRIMSTONE_ULT_ENEMY_1_PT_BR, context)
        # # EN
        # elif language.upper() == constants.LANG_EN:
        #     if char.lower() == constants.PHOENIX.lower():
        #         return await play_sound("sounds/namoral_vc_morreu.mp3", context)
        #     elif char.lower() == constants.RAZE.lower():
        #         await play_sound(constants.RAZE_ULT_1_EN, context)


# Toca toda a voice line do agente
@client.command("voiceline")
async def play_ult(context, char, language=constants.LANG_PT):
    # PT_BR
    if language.upper() == constants.LANG_PT:
        if char.lower() == constants.PHOENIX.lower():
            return await play_sound(constants.PHOENIX_ULT_1_PT_BR, context)
        # RAZE
        elif char.lower() == constants.RAZE.lower():
            await play_sound(constants.RAZE_ALL_VOICE_LINES_PT_BR, context)
        # RAZE
        elif char.lower() == constants.BRIMSTONE.lower():
            await play_sound(constants.BRIMSTONE_ALL_VOICE_LINES_PT_BR, context)
    # EN
    # elif language.upper() == constants.LANG_EN:
    #     if char.lower() == constants.PHOENIX.lower():
    #         return await play_sound("sounds/namoral_vc_morreu.mp3", context)
    #     elif char.lower() == constants.RAZE.lower():
    #         # await play_sound(constants.RAZE_ULT_1_EN, context)


@client.command("random")
async def random_voice_line(context, char, language=constants.LANG_PT):
    voiceLine = None
    # PT_BR
    if language.upper() == constants.LANG_PT:
        if char.lower() == constants.PHOENIX.lower():
            return await play_sound(constants.PHOENIX_ULT_1_PT_BR, context)
        # RAZE
        elif char.lower() == constants.RAZE.lower():
            voiceLine = choice(
                [constants.RAZE_FUCKED_PT_BR, constants.RAZE_SE_PICA_1_PT_BR, constants.RAZE_SE_PICA_2_PT_BR,
                 constants.AI_TU_BROCOU_1, constants.RAZE_ULT_ALLY_1_PT_BR])
        # BRIM
        elif char.lower() == constants.BRIMSTONE.lower():
            voiceLine = choice(
                [constants.BRIMSTONE_CHURRASQUINHO_PT_BR, constants.BRIMSTONE_RANDOM_1_PT_BR,
                 constants.BRIMSTONE_FUCKED_1_PT_BR])

    # EN
    # elif language.upper() == constants.LANG_EN:
    #     if char.lower() == constants.PHOENIX.lower():
    #         return await play_sound("sounds/namoral_vc_morreu.mp3", context)
    #     elif char.lower() == constants.RAZE.lower():
    #         await play_sound(constants.RAZE_ULT_1_EN, context)
    await play_sound(voiceLine, context)


@client.command("cursed")
async def random_voice_line(context, char, language=constants.LANG_PT):
    voiceLine = None
    # PT_BR
    if language.upper() == constants.LANG_PT:
        # if char.lower() == constants.PHOENIX.lower():
        #     return await play_sound(constants.PHOENIX_ULT_1_PT_BR, context)
        # # RAZE
        # elif char.lower() == constants.RAZE.lower():
        #     voiceLine = choice(
        #         [constants.RAZE_FUCKED_PT_BR, constants.RAZE_SE_PICA_1_PT_BR, constants.RAZE_SE_PICA_2_PT_BR,
        #          constants.AI_TU_BROCOU_1, constants.RAZE_ULT_ALLY_1_PT_BR])
        # BRIM
        if char.lower() == constants.BRIMSTONE.lower():
            voiceLine = choice(
                [constants.BRIMSTONE_CURSED_1_PT_BR, constants.BRIMSTONE_CURSED_2_PT_BR])

    # EN
    # elif language.upper() == constants.LANG_EN:
    #     if char.lower() == constants.PHOENIX.lower():
    #         return await play_sound("sounds/namoral_vc_morreu.mp3", context)
    #     elif char.lower() == constants.RAZE.lower():
    #         await play_sound(constants.RAZE_ULT_1_EN, context)
    await play_sound(voiceLine, context)


@client.command("brocou")
async def ai_tu_brocou(context):
    await play_sound(choice([
        constants.AI_TU_BROCOU_1,
        constants.AI_TU_BROCOU_2,
        constants.AI_TU_BROCOU_3
    ]), context)


client.run(os.environ["BOT_TOKEN"])
