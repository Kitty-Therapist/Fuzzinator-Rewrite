import discord
import time 
import asyncio
import datetime
from discord.ext import commands
from discord.ext.commands import BadArgument
from discord import utils
from utils import Util

class fun:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def summon(self, ctx, *, target: str):
        """Summons a person."""
        try:
            member = await commands.MemberConverter().convert(ctx, target)
        except BadArgument as ex:
            await ctx.send(f"**I have summoned the one known as {target}!**")
            await asyncio.sleep(5)
            await ctx.send("Be prepared as there is no stopping this summoning!")
            await asyncio.sleep(5)
            await ctx.send("The summoning will be complete soon!")
            await asyncio.sleep(5)
            await ctx.send("_Please note that 'soon' in bot time is not always considered the same as 'soon' in human time_")
            await asyncio.sleep(5)
            await ctx.send("Have a nice day!")
        else:
            if member == ctx.author:
                await ctx.send("Summoning yourself? That's cheating!")
                ctx.command.reset_cooldown(ctx)
            if member == ctx.bot: 
                await ctx.send(f"**I have summoned the one known as {target}!**") 
                await asyncio.sleep(5) 
                await ctx.send("***WAIT!***") 
                await asyncio.sleep(5) 
                await ctx.send("Why do you need me to summon myself? :confused:") 
            else:
                await ctx.send(f"{member.name} is already a member of this server, do the ping youself, lazy humans.")

def setup(bot):
    bot.add_cog(fun(bot))
