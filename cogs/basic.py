import discord
import time 
import asyncio
import datetime
import traceback
import logging
from discord.ext import commands
from discord.ext.commands import BucketType
from discord import utils
from utils import Util
from datetime import datetime

class basic:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def cpr(self, ctx):
            """Shows that the bot is still alive"""
            await ctx.send("I am still alive!")

    @commands.command()
    @commands.guild_only()
    async def embed(self, ctx, title, *, embedding = ""):
        if(embedding != ""):
            try:
                embed = discord.Embed(title=title, colour=discord.Colour(0xf47b67), description=f"{embedding}")
                embed.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})")
                embed.set_footer(text="Do ``!embed <content>`` for embed testing.")
                message = await ctx.send(embed=embed)
            except discord.Forbidden:
                await ctx.send("Are you sure I have permission to do this?")
                return
        else: 
            await ctx.send("I can't just send an empty embed, bro.")
            return

    @commands.command()
    @commands.guild_only()
    async def windows(self, ctx):
        role = discord.utils.get(ctx.guild.roles, id=467929171016810507)
        if role not in ctx.author.roles:
            await ctx.message.author.add_roles(role)
            await ctx.send(f"Successfully joined {role.name}!")
        else:
            await ctx.message.author.remove_roles(role)
            await ctx.send(f"Successfully left {role.name}!")
    
    @commands.command()
    @commands.guild_only()
    async def mac(self, ctx):
        role = discord.utils.get(ctx.guild.roles, id=467930453605613578)
        if role not in ctx.author.roles:
            await ctx.message.author.add_roles(role)
            await ctx.send(f"Successfully joined {role.name}!")
        else:
            await ctx.message.author.remove_roles(role)
            await ctx.send(f"Successfully left {role.name}!")
    
    @commands.command()
    @commands.guild_only()
    async def ios(self, ctx):
        role = discord.utils.get(ctx.guild.roles, id=467939871672107018)
        if role not in ctx.author.roles:
            await ctx.message.author.add_roles(role)
            await ctx.send(f"Successfully joined {role.name}!")
        else:
            await ctx.message.author.remove_roles(role)
            await ctx.send(f"Successfully left {role.name}!")

    @commands.command()
    @commands.guild_only()
    async def android(self, ctx):
        role = discord.utils.get(ctx.guild.roles, id=467940055181164554)
        if role not in ctx.author.roles:
            await ctx.message.author.add_roles(role)
            await ctx.send(f"Successfully joined {role.name}!")
        else:
            await ctx.message.author.remove_roles(role)
            await ctx.send(f"Successfully left {role.name}!")

    @commands.command()
    @commands.guild_only()
    async def linux(self, ctx):
        role = discord.utils.get(ctx.guild.roles, id=467940096407109632)
        if role not in ctx.author.roles:
            await ctx.message.author.add_roles(role)
            await ctx.send(f"Successfully joined {role.name}!")
        else:
            await ctx.message.author.remove_roles(role)
            await ctx.send(f"Successfully left {role.name}!")

    @commands.command()
    @commands.guild_only()
    async def botupdate(self, ctx):
        role = discord.utils.get(ctx.guild.roles, id=472189143645028363)
        if role not in ctx.author.roles:
            await ctx.message.author.add_roles(role)
            await ctx.send(f"Successfully joined {role.name}!")
        else:
            await ctx.message.author.remove_roles(role)
            await ctx.send(f"Successfully left {role.name}!")

    @commands.command()
    @commands.guild_only()
    async def reactspam(self,ctx):
        react1 = utils.get(self.bot.emojis, id=420408755503759363)
        react2 = utils.get(self.bot.emojis, id=465214916962418688)
        react3 = utils.get(self.bot.emojis, id=397200742357794817)
        react4 = utils.get(self.bot.emojis, id=441686731268423691)
        react5 = utils.get(self.bot.emojis, id=451501861157994507)
        react6 = utils.get(self.bot.emojis, id=434406707704233984)
        react7 = utils.get(self.bot.emojis, id=420398455534649354)
        react8 = utils.get(self.bot.emojis, id=453579301766299658)
        react9 = utils.get(self.bot.emojis, id=443245661710974988)
        react10 = utils.get(self.bot.emojis, id=417535190051586058)


        await ctx.message.add_reaction(react1)
        await ctx.message.add_reaction(react2)
        await ctx.message.add_reaction(react3)
        await ctx.message.add_reaction(react4)
        await ctx.message.add_reaction(react5)
        await ctx.message.add_reaction(react6)
        await ctx.message.add_reaction(react7)
        await ctx.message.add_reaction(react8)
        await ctx.message.add_reaction(react9)
        await ctx.message.add_reaction(react10)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 30, BucketType.user)
    async def spam(self,ctx,amount:int=None):
        limit = 50
        if amount is not None:
            if amount > limit:
                await ctx.send(f"Hey! You trying to ratelimit me?! Please keep it under {limit}")
            else:
                while amount > 0:
                    await ctx.send("You have requested spam.")
                    await asyncio.sleep(5)
                    amount -= 1
        else:
            await ctx.send("You have requested spam.")
            await asyncio.sleep(5)
            await ctx.send("You have requested spam.")
            await asyncio.sleep(5)
            await ctx.send("You have requested spam.")
            await asyncio.sleep(5)
            await ctx.send("You have requested spam.")
            await asyncio.sleep(5)
            await ctx.send("You have requested spam.")
            await asyncio.sleep(5)
            await ctx.send("You have requested spam.")
            await asyncio.sleep(5)
            await ctx.send("You have requested spam.")
            await asyncio.sleep(5)
            await ctx.send("You have requested spam.")
            await asyncio.sleep(5)
            await ctx.send("You have requested spam.")
            await asyncio.sleep(5)
            await ctx.send("You have requested spam.")
            await asyncio.sleep(5)
            await ctx.send("You have requested spam.")

    @commands.command()
    @commands.guild_only()
    async def pong(self, ctx: commands.Context, durationNumber: int, durationIdentifier: str, *, comment = " "):
        if(comment != ""):
                try:    
                    duration = Util.convertToSeconds(durationNumber, durationIdentifier)
                    until = time.time() + duration
                    await asyncio.sleep(duration)
                    await ctx.send(f"<@{ctx.author.id}> {comment}")
                except discord.Forbidden:
                        await ctx.send("Are you sure I have permission to do this?")
                        return
        else: 
            await ctx.send(f"<@{ctx.author.id}>")
            return

    @commands.command()
    async def about(self, ctx: commands.Context):
        """Shows information about the bot"""
        embed = discord.Embed(color=0x98f5ff)
        embed.add_field(name='Name', value=f"{ctx.bot.user.name}", inline=True)
        embed.add_field(name='Uptime', value=Util.chop_microseconds(datetime.now()-ctx.bot.starttime),inline=True)
        embed.add_field(name='Description', value="A little, maybe not that little bot build to fullfil the needs of the Bug Hunters of the Bug-Bombing Area 600.\nThe bot is currently Work in progress!", inline=True)
        await ctx.send(embed=embed)

    @commands.group()
    async def invite(self, ctx):
        """searches for a valid invite and sends that."""
        if ctx.invoked_subcommand is None:
            invites = await ctx.guild.invites()
            if len(invites) > 0:
                inviteurl = None
                for invite in invites:
                    if invite.max_uses == 0 and invite.max_age == 0:
                        inviteurl = invite.url
                        break;

                if inviteurl is not None:
                    await ctx.send(inviteurl)
                else:
                    await ctx.send("there currently are no invites on this server.")
            else:
                await ctx.send("there currently are no invites on this server.")

    @invite.command(name='new')
    async def newInvite(self, ctx, uses :int = 1):
        """Generates a new invites based on your wished uses. By default the invite has one use."""
        invite = await ctx.guild.text_channels[0].create_invite(max_uses=(uses))
        invite_url = str(invite)
        await ctx.send(f"I've created an invite based of your input! Here is an invite with ``{uses}`` use(s).")
            

def setup(bot):
    bot.add_cog(basic(bot))
