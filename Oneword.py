import discord
from discord.ext import commands
import re
import asyncio
from discord.utils import get
from itertools import cycle

Bot = commands.Bot(command_prefix='&')
TOKEN = 'NTQ0NDYxMzA2MjA0MjU4MzA0.D1Wtww.CAVWc4wjCLp_hba-nJauh-jFgSE'

Bot.remove_command('help')


@Bot.event
async def on_ready():

    await Bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="Your language"
        )
    )
    print('Words are being processed')

    if len(Bot.guilds) == 1:
        print(f'serving a lonely guild named: {guild.name}')

    else:
        print('serving {} guilds :)'.format(len(Bot.guilds)))


@Bot.event
async def on_message(message):
    msg = message.content
    author = message.author.name
    channel = message.channel

    if message.channel.name == "one-word-story":
        words = len(message.content.split())
        signs_detected = re.search(r'[@$%^&(,)-_};{?/.><]+', message.content)

        if signs_detected or words > 1:
            try:
                await message.channel.purge(limit=1)

            except discord.errors.NotFound:
                print('a simple error happened')

        else:
            pass
    else:
        pass

    await Bot.process_commands(message)


@Bot.command(pass_context=True)
async def help(ctx):

    embed = discord.Embed(
        title='The rules are simple,',
        description="""
You're allowed to write one word without
these characters below.""",
        color=discord.Color.from_rgb(29, 105, 226)
    )

    embed.add_field(
        name="Forbidden characters",
        value="`@$%^&(,)-_};{?/.><`",
        inline=False
    )

    embed.add_field(
        name="Naming scheme",
        value="""
set the name of the channel that
belongs to the bot to `one-word-story`
or it won't work.""",
        inline=False
    )

    embed.add_field(
        name="Prefix:",
        value="`&`",
        inline=False
    )

    embed.set_footer(
        text="Word v1.0 | No website yet | kui#????",
        icon_url="https://cdn1.iconfinder.com/data/icons/application-file-formats/128/microsoft-word-512.png"
    )

    personal = discord.Embed(
        title="Enter the command in any channel other than `one-word-story`",
        color=discord.Color.from_rgb(29, 105, 226)
    )

    personal.set_footer(
        text="Word v1.0 | no website yet | kui#????",
        icon_url="https://cdn1.iconfinder.com/data/icons/application-file-formats/128/microsoft-word-512.png"
    )

    if ctx.channel.name == "one-word-story":
        try:
            await ctx.author.send(embed=personal)

        except AttributeError:
            print("message sent successfully")

    else:
        await ctx.send(embed=embed)


Bot.run(TOKEN)
