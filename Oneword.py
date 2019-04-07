import discord
from discord.ext import commands
import re
import asyncio
from discord.utils import get
from itertools import cycle

Bot = commands.Bot(command_prefix='&')
TOKEN = "NTQ0NDYxMzA2MjA0MjU4MzA0.XKmonw.bZe0XSxRJaqtqr35JD5G9qwkrD4"

Bot.remove_command('help')

# status = ["Your language", "prefix: &", "You by the window"]


@Bot.event
async def on_ready():

    await Bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="Your language"
        )
    )
    print('words are being processed')

    if len(Bot.guilds) == 1:
        print(f'serving a lonely guild named: {guild.name}')

    else:
        print('serving {} guilds :)'.format(len(Bot.guilds)))


@Bot.event
async def on_message(message):

    msg = message.content.lower()
    author = message.author.name
    channel = message.channel
    word_len = len(message.content.split())
    signs_detected = re.search(r"[_@>,<#$%^{:'}&*+)(-]", msg)

    if message.channel.name == "one-word-story":
        if signs_detected or word_len > 1:
                await message.delete()
        else:
            pass
    else:
        pass

    await Bot.process_commands(message)


@Bot.command(pass_context=True)
async def help(ctx):

    embed = discord.Embed(
        title='The rules are simple:',
        description="""
You're allowed to write one word without
these characters below.""",
        color=discord.Color.from_rgb(29, 105, 226)
    )

    embed.add_field(
        name="Forbidden characters:",
        value="`_@>,<#$%^{:'}&*+)(-`",
        inline=False
    )

    embed.add_field(
        name="Naming scheme:",
        value="""
Set the name of the channel that
belongs to the bot to `one-word-story`
or else it won't work.""",
        inline=False
    )

    embed.add_field(
        name="Prefix:",
        value="`&`",
        inline=False
    )

    embed.add_field(
        name="Commands:",
        value="""
`&help` Is to bring this message
`&ping` Is to know your current ping"""
    )

    embed.set_footer(
        text="Word v1.0 | No website yet | kui#0629",
        icon_url="https://cdn1.iconfinder.com/data/icons/application-file-formats/128/microsoft-word-512.png"
    )

    if ctx.channel.name == "one-word-story":
        try:
            await ctx.author.send(embed=embed)

        except Exception as e:
            print(e)
            print("message sent successfully")

    else:
        await ctx.send(embed=embed)


@Bot.command()
async def ping(ctx):

    embed = discord.Embed(
        title="Your ping is: `{0}ms`".format(round(Bot.latency, 2)),
        color=discord.Color.from_rgb(29, 105, 226)
    )

    if ctx.channel.name == "one-word-story":
        await ctx.author.send(embed=embed)

    else:
        await ctx.channel.send(embed=embed)


Bot.run(TOKEN)
