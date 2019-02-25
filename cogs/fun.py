import discord
import time 
import asyncio
import datetime
from discord.ext import commands
from discord.ext.commands import BadArgument
from discord import utils
from utils import Util, Configuration

class fun(commands.Cog):
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
    
    @commands.command(name='hug', aliases=['huh','hugh'])
    @commands.guild_only()
    async def hug(self, ctx: commands.Context, friend: discord.Member):
        """Hugs a person."""
        if friend == ctx.author:
            await ctx.send("You must be really lonely if you need to hug yourself, have one from me instead!")
        elif friend == self.bot.user:
            await ctx.send("Thanks for the hug!")
        else:
            await ctx.send(f"{friend.mention}, you have recieved a big, big hug from {ctx.author.name}!")

    @commands.command(name='fight', aliases=['fite'])
    @commands.guild_only()
    async def fight(self, ctx: commands.Context, friend: discord.Member):
        """Hugs a person."""
        if friend == ctx.author:
            await ctx.send("Why are you trying to fight yourself?")
        elif friend == self.bot.user:
            await ctx.send("Whoa, whoa. Why are you fighting me? :(")
        else:
            await ctx.send(f"{ctx.author.mention} has fought {friend.mention}!")

def setup(bot):
    bot.add_cog(fun(bot))
