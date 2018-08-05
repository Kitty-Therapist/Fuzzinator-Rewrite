import asyncio
import datetime
import traceback
from concurrent.futures import CancelledError

import discord
import time
import math
from discord.ext import commands

class ModerationCog:
    def __init__(self, bot):
        self.bot = bot
        self.running = True
    
    def __unload(self):
        self.running = False

    @commands.command()
    async def ping(self, ctx: commands.Context):
            """Shows the Gateway Ping"""
            t1 = time.perf_counter()
            await ctx.trigger_typing()
            t2 = time.perf_counter()
            await ctx.send(f":hourglass: Gateway Ping is {round((t2 - t1) * 1000)}ms :hourglass:")
            
    @commands.command(hidden=True)
    async def restart(self, ctx):
        """Restarts the bot"""
        await ctx.send("Restarting...")
        await self.bot.logout()
        await self.bot.close()
    ##This will eventually have a better restart.

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason="No reason given."):
        if (ctx.author != user and user != ctx.bot.user and ctx.author.top_role > user.top_role) or ctx.guild.owner == ctx.author:
            await ctx.guild.kick(user, reason=f"Moderator: {ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id}) Reason: {reason}")
            await ctx.send(f":boot: {user.name}#{user.discriminator} (`{user.id}`) was kicked. Reason: `{reason}`")
        elif user == None:
            await ctx.send("Please specific an user that you are wanting to kick.")
        else:
            await ctx.send(f":no_entry: You are not allowed to kick {user.name}#{user.discriminator}!")
    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason="No reason given."):
        if (ctx.author != user and user != ctx.bot.user and ctx.author.top_role > user.top_role) or ctx.guild.owner == ctx.author:
            await ctx.guild.ban(user, reason=f"Moderator: {ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id}) Reason: {reason}")
            await ctx.send(f":rotating_light: {user.name}#{user.discriminator} (`{user.id}`) was banned. Reason: `{reason}`")
        elif user == None:
            await ctx.send("Please specific an user that you are wanting to ban.")
        else:
            await ctx.send(f":no_entry: You are not allowed to ban {user.name}#{user.discriminator}!")

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(ban_members=True)
    async def forceban(self, ctx, user_id: int, *, reason = "No reason given"):
        """Bans a user even if they are not in the server"""
        user = await ctx.bot.get_user_info(user_id)
        if user == ctx.bot.user:
            await ctx.send("Why would you like to forceban me? :disappointed_relieved:")
        elif user == ctx.author:
            await ctx.send("You have played yourself. But you cannot forceban yourself!")
        else:
            await ctx.guild.ban(user, reason=f"Moderator: {ctx.author.name} ({ctx.author.id}) Reason: {reason}")
            await ctx.send(f":ok_hand: {user.name} ({user.id}) was banned. Reason: `{reason}`.")

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(ban_members=True)
    async def tempban(self,ctx: commands.Context, user: discord.Member, durationNumber: int, durationIdentifier: str, *, reason="No reason provided."):
        """Temporarily bans someone."""
        if (ctx.author != user and user != ctx.bot.user and ctx.author.top_role > user.top_role) or ctx.guild.owner == ctx.author:
            duration = Util.convertToSeconds(durationNumber, durationIdentifier)
            until = time.time() + duration
            await ctx.guild.ban(user, reason=f"Moderator: {ctx.author.name} ({ctx.author.id}), Duration: {durationNumber}{durationIdentifier} Reason: {reason}")
            await ctx.send(f":ok_hand: {user.name} ({user.id}) has been banned for {durationNumber}{durationIdentifier}(``{reason}``)")
            await asyncio.sleep(duration)
            await ctx.guild.unban(user, reason=f"Moderator: {ctx.author.name} ({ctx.author.id}). Their temporary ban has expired.")
        elif user == None:
            await ctx.send("Please specific an user that you are wanting to ban.")
        else:
            await ctx.send(f":no_entry: You are not allowed to ban {user.name}#{user.discriminator}!")

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(ban_members=True)
    async def softban(self, ctx, user: discord.Member, *, reason="No reason given."):
        """Bans an user then unbans them afterwards, removing their messages."""
        if (ctx.author != user and user != ctx.bot.user and ctx.author.top_role > user.top_role) or ctx.guild.owner == ctx.author:
            await ctx.guild.ban(user, reason=f"Moderator: {ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id}) Reason: {reason}")
            await ctx.guild.unban(user)
            await ctx.send(f":rotating_light: {user.name}#{user.discriminator} (`{user.id}`) was softbanned. Reason: `{reason}`")
        elif user == None:
            await ctx.send("Please specific an user that you are wanting to ban.")
        else:
            await ctx.send(f":no_entry: You are not allowed to ban {user.name}#{user.discriminator}!")



    

def setup(bot):
    bot.add_cog(ModerationCog(bot))