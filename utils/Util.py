import json
import aiohttp
import asyncio
import async_timeout
import datetime
import random
from discord.ext import commands
from discord import utils

def convertToSeconds(value: int, type: str):
    type = type.lower()
    if len(type) > 1 and type[-1:] == 's': # plural -> singular
        type = type[:-1]
    if type == 'w' or type == 'week':
        value = value * 7
        type = 'd'
    if type == 'd' or type == 'day':
        value = value * 24
        type = 'h'
    if type == 'h' or type == 'hour':
        value = value * 60
        type = 'm'
    if type == 'm' or type == 'minute':
        value = value * 60
        type = 's'
    if type != 's' and type != 'second':
        raise commands.BadArgument(f"Invalid duration: `{type}`\nValid identifiers: week(s), day(s), hour(s), minute(s), second(s)")
    else:
        return value

def chop_microseconds(delta):
    return delta - datetime.timedelta(microseconds=delta.microseconds)

def trim_message(message, limit):
    if len(message) < limit - 3:
        return message
    return f"{message[:limit-1]}..."
