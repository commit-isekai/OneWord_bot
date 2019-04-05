import discord
from discord.ext import commands
import re
import asyncio
from discord.utils import get

Bot = commands.Bot(command_prefix='&')
TOKEN = 'Insert token here'

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
    signs_detected = re.search(r"[_!?@><#$%^{:'}&*+)(-]", msg)

    print(signs_detected)

    if message.channel.name == "one-word-story":
        if signs_detected or word_len > 1:
            await message.delete()
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
        value="`_!?@><#$%^{:'}&*+)(-`",
        inline=False
    )

    embed.add_field(
        name="Naming scheme:",
        value="""
set the name of the channel that
belongs to the bot to `one-word-story`
or else it won't work.""",
        inline=False
    )

    embed.add_field(
        name="Prefix:",
        value="`&`",
        inline=False
    )

    embed.set_footer(
        text="Word v1.0 | No website yet | kui#0629",
        icon_url="https://cdn1.iconfinder.com/data/icons/application-file-formats/128/microsoft-word-512.png"
    )

    personal = discord.Embed(
        title="Enter the command in any channel other than `one-word-story`",
        color=discord.Color.from_rgb(29, 105, 226)
    )

    personal.set_footer(
        text="Word v1.0 | no website yet | kui#0629",
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
