import discord
from discord.ext import commands 
from discord import utils
from utils import Util

class announce:
    def __init__(self,bot):
        self.bot = bot

    @commands.group()
    @commands.guild_only()
    async def ping(self, ctx:commands.Context):
        """Allows variety of roles to be pinged."""
        if ctx.subcommand_passed is None:
            await ctx.send(f"Use `{ctx.prefix}help pingCommand` for info on how to use this command.")

    @ping.command()
    async def BugHunter(self, ctx: commands.Context, *, BH):
        Mods = discord.utils.get(ctx.guild.roles, id=391357618683379724)
        BugHunters = discord.utils.get(ctx.guild.roles, id=391357713428512780)
        channel = ctx.guild.get_channel(392400500676362240)

        if 391357618683379724 not in [role.id for role in ctx.author.roles]:
            return await ctx.send("Sorry, I'm afraid that you don't have the permission to ping people.")

        if BugHunters is None:
            return await ctx.send("I think <@298618155281154058> accidentally deleted this role.")
        
        if BH != None:
            try:
                await BugHunters.edit(mentionable=True)
                await channel.send(f"{BugHunters.mention}\n{BH}")
                await BugHunters.edit(mentionable=False)      
            except discord.Forbidden:
                await ctx.send("I wasn't able to send a message in the announcement channel. Please check that I am able to talk.")
        else: 
            await ctx.send("I am unsure of what you are attempting to do.")

    @ping.command()
    async def BotUpdate(self, ctx: commands.Context, *, botupdatez):
        Mods = discord.utils.get(ctx.guild.roles, id=391357618683379724)
        BotUpdate = discord.utils.get(ctx.guild.roles, id=472189143645028363)
        channel = ctx.guild.get_channel(467918069553954817)

        if 391357618683379724 not in [role.id for role in ctx.author.roles]:
            return await ctx.send("Sorry, I'm afraid that you don't have the permission to ping people.")

        if BotUpdate is None:
            return await ctx.send("I think <@298618155281154058> accidentally deleted this role.")
        
        if botupdatez != None:
            try:
                await BotUpdate.edit(mentionable=True)
                await channel.send(f"{BotUpdate.mention}\n{botupdatez}")
                await BotUpdate.edit(mentionable=False)      
            except discord.Forbidden:
                await ctx.send("I wasn't able to send a message in the announcement channel. Please check that I am able to talk.")
        else: 
            await ctx.send("I am unsure of what you are attempting to do.")

    @ping.command()
    async def Update(self, ctx: commands.Context, *, updatez):
        Mods = discord.utils.get(ctx.guild.roles, id=391357618683379724)
        Update = discord.utils.get(ctx.guild.roles, id=438073053189111811)
        channel = ctx.guild.get_channel(392400500676362240)

        if 391357618683379724 not in [role.id for role in ctx.author.roles]:
            return await ctx.send("Sorry, I'm afraid that you don't have the permission to ping people.")

        if Update is None:
            return await ctx.send("I think <@298618155281154058> accidentally deleted this role.")
        
        if updatez != None:
            try:
                await Update.edit(mentionable=True)
                await channel.send(f"{Update.mention}\n{updatez}")
                await Update.edit(mentionable=False)      
            except discord.Forbidden:
                await ctx.send("I wasn't able to send a message in the announcement channel. Please check that I am able to talk.")
        else: 
            await ctx.send("I am unsure of what you are attempting to do.")

def setup(bot):
    bot.add_cog(announce(bot))
