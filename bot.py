#!/usr/bin/env python3
import asyncio
import datetime
import discord
import configparser
import time
import math
import traceback
import logging
from discord.ext import commands
from discord import utils
from discord import abc
from utils import Util, BotLogs

from discord.abc import PrivateChannel

TOKEN = "Bugs are cool"

bot = commands.Bot(command_prefix="+",
                   description='A bot meant for the Bug Hunters!')

bot.starttime = datetime.datetime.now()
bot.startup_done = False

initial_extensions = ['basic', 'Reload', 'announce', 'fun']

@bot.event
async def on_command_error(ctx: commands.Context, error):
    BOT_LOG_CHANNEL = bot.get_channel(414716924057092106)
    if isinstance(error, commands.NoPrivateMessage):
        await ctx.send("This command cannot be used in private messages.")
    elif isinstance(error, commands.BotMissingPermissions):
        BotLogs.error(f"Encountered a permissions error while executing {ctx.command}")
        await ctx.send(error)

    elif isinstance(error, commands.DisabledCommand):
        await ctx.send("Sorry. This command is disabled and cannot be used.")
    elif isinstance(error, commands.CheckFailure):
        if ctx.command.qualified_name is not "latest":
            await ctx.send(":lock: You do not have the required permissions to run this command")
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(error)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"You are missing a required argument!(See {ctx.prefix}help {ctx.command.qualified_name} for info on how to use this command)")
    elif isinstance(error, commands.BadArgument):
        await ctx.send(f"Invalid argument given! (See {ctx.prefix}help {ctx.command.qualified_name} for info on how to use this commmand)")
    elif isinstance(error, commands.CommandNotFound):
        return
    else:
        # log to logger first just in case botlog logging fails as well
        BotLogs.exception(f"Command execution failed:\n"
                                 f"    Command: {ctx.command}\n"
                                 f"    Message: {ctx.message.content}\n"
                                 f"    Channel: {'Private Message' if isinstance(ctx.channel, abc.PrivateChannel) else ctx.channel.name}\n"
                                 f"    Sender: {ctx.author.name}#{ctx.author.discriminator}\n"
                                 f"    Exception: {error}", error.original)
        # notify caller
        await ctx.send(":rotating_light: Something went wrong while executing that command :rotating_light:")

        embed = discord.Embed(colour=discord.Colour(0xff0000),
                              timestamp=datetime.datetime.utcfromtimestamp(time.time()))

        embed.set_author(name="Command execution failed:")
        embed.add_field(name="Command", value=ctx.command)
        embed.add_field(name="Original message", value=Util.trim_message(ctx.message.content, 1024))
        embed.add_field(name="Channel",
                        value='Private Message' if isinstance(ctx.channel, abc.PrivateChannel) else f"{ctx.channel.name} ({ctx.channel.id})")
        embed.add_field(name="Sender", value=f"{ctx.author.name}#{ctx.author.discriminator}")
        embed.add_field(name="Exception", value=error.original)
        v = ""
        for line in traceback.format_tb(error.original.__traceback__):
            if len(v) + len(line) > 1024:
                embed.add_field(name="Stacktrace", value=v)
                v = ""
            v = f"{v}\n{line}"
        if len(v) > 0:
            embed.add_field(name="Stacktrace", value=v)
            await BOT_LOG_CHANNEL.send(embed=embed)


@bot.event
async def on_error(event, *args, **kwargs):
    # something went wrong and it might have been in on_command_error, make sure we log to the log file first
    BOT_LOG_CHANNEL = bot.get_channel(414716924057092106)
    BotLogs.error(f"error in {event}\n{args}\n{kwargs}")
    embed = discord.Embed(colour=discord.Colour(0xff0000),
                          timestamp=datetime.datetime.utcfromtimestamp(time.time()))

    embed.set_author(name=f"Caught an error in {event}:")

    embed.add_field(name="args", value=str(args))
    embed.add_field(name="kwargs", value=str(kwargs))
    embed.add_field(name="cause message", value=traceback._cause_message)
    v = ""
    for line in traceback.format_exc():
        if len(v) + len(line) > 1024:
            embed.add_field(name="Stacktrace", value=v)
            v = ""
        v = f"{v}{line}"
    if len(v) > 0:
        embed.add_field(name="Stacktrace", value=v)

    await BOT_LOG_CHANNEL(embed=embed)
    # try logging to botlog, wrapped in an try catch as there is no higher lvl catching to prevent taking donwn the bot (and if we ended here it might have even been due to trying to log to botlog
    try:
        pass
    except Exception as ex:
        BotLogs.error(
            f"Failed to log to botlog, either discord broke or something is seriously wrong!\n{ex}")
        BotLogs.error(traceback.format_exc())


if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(f"cogs.{extension}")

@bot.event
async def on_ready():
    print("I'm ready for assistance!")
    await bot.change_presence(activity=discord.Activity(name='the Bug Hunters!', type=discord.ActivityType.watching))

bot.run(TOKEN)
