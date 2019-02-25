import asyncio
from subprocess import Popen
import subprocess
import configparser
import inspect
import textwrap
from contextlib import redirect_stdout
import io
import traceback
import discord
from discord.ext import commands 
import os
from discord import utils
from utils import Util, Configuration

class announcement(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_result = None 
    
    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    @commands.bot_has_permissions(manage_roles=True)       
    @commands.command()
    async def announce(self, ctx: commands.Context, role_name, *, message):
        Mods = discord.utils.get(ctx.guild.roles, id=391357618683379724)
        role = Configuration.get_role(ctx, role_name)
        channel = Configuration.get_channel(ctx, role_name)
        log = ctx.guild.get_channel(414716924057092106)

        if 391357618683379724 not in [role.id for role in ctx.author.roles]:
            return await ctx.send("Sorry, I'm afraid that you don't have the permission to use this secret command.")

        if role is None:
            return await ctx.send("This role might have been deleted, oops!")
        
        if message != None:
            await role.edit(mentionable=True)
            try:
                await channel.send(f"{role.mention}\n{message}")
                await log.send(f":mega: **{ctx.author.name}#{ctx.author.discriminator}** (``{ctx.author.id}``) made the following announcement: ```{message}``` with the {role.name} ping!")
            except discord.Forbidden:
                await ctx.send("I was not able to send a message. Can you check to make sure I have permission?")
            await role.edit(mentionable=False)
        else: 
            await ctx.send("I am unsure of what you are attempting to do.")

    @commands.command()
    async def update(self, ctx: commands.Context, role_name, message_id:int, *, new_message):
        channel = Configuration.get_channel(ctx, role_name)
        log = ctx.guild.get_channel(414716924057092106)
        Mods = discord.utils.get(ctx.guild.roles, id=391357618683379724)

        if 391357618683379724 not in [role.id for role in ctx.author.roles]:
            return await ctx.send("Sorry, I'm afraid that you don't have the permission to use this secret command.")
        try:
            message = await channel.get_message(message_id)
        except (discord.Forbidden) as e:
            await ctx.send("Hmmm.. Seems like I no longer have READ_MESSAGES permission for that channel for some reason.")
            return
        except (discord.Forbidden, discord.NotFound) as e:
            await ctx.send("It is possible that you gave me the wrong ID or I cannot find the message in the channel due to either the message or channel being deleted.")
            return

        if channel is None:
            return await ctx.send("Are you sure this is in a correct channel?")
        if message != None:
            try:
                await message.edit(content=f"{new_message}")
                await log.send(f":pencil: **{ctx.author.name}#{ctx.author.discriminator}** (``{ctx.author.id}``) has edited the following announcement ({message_id}) with: ```{new_message}```")
            except discord.Forbidden:
                await ctx.send("it appears that my SEND_MESSAGES perms have been revoked and I cannot edit the message.")
        else:
            await ctx.send("I'm not really sure what you are trying to do.")

    @commands.bot_has_permissions(manage_roles=True)  
    @commands.command()
    async def mention(self, ctx: commands.Context, role_name):
        role = Configuration.get_role(ctx, role_name)
        log = ctx.guild.get_channel(414716924057092106)
        Mods = discord.utils.get(ctx.guild.roles, id=391357618683379724)

        if 391357618683379724 not in [role.id for role in ctx.author.roles]:
            return await ctx.send("Sorry, I'm afraid that you don't have the permission to use this secret command.")
            
        if role.mentionable:
            await role.edit(mentionable=False)
            await ctx.send(f"{role.name} is now unmentionable!")
            return await log.send(f":warning: {role.name} has been made unmentionable by {ctx.author.name}#{ctx.author.discriminator} (``{ctx.author.id}``).")
        else:
            await role.edit(mentionable=True)
            await ctx.send(f"{role.name} is now mentionable!")
            return await log.send(f":warning: {role.name} has been made mentionable by {ctx.author.name}#{ctx.author.discriminator} (``{ctx.author.id}``).")
    
    @commands.bot_has_permissions(manage_roles=True)
    @commands.command()
    async def account(self, ctx:commands.Context, user: discord.Member):
        BugHunters = discord.utils.get(ctx.guild.roles, id=391357713428512780)
        role = discord.utils.get(ctx.guild.roles, id=468118767009005618)
        log = ctx.guild.get_channel(414716924057092106)

        if 391357713428512780 not in [role.id for role in ctx.author.roles]:
            return await ctx.send("Sorry, I'm afraid that you don't have the permission to use this secret command.")
        if role is None:
            return await ctx.send("This role may be either deleted or not configured properly.")
        try:
            await user.add_roles(role)
            await log.send(f"{ctx.author.mention} (``{ctx.author.id}``) has claimed {user.mention} (``{user.id}``) as their testing account!")
            await ctx.send(f":ok_hand: Made {user.mention} a Test Dummy!")
        except discord.Forbidden:
            await ctx.send(f"I was not able to add the Test Dummy role to the {user.name}#{user.discriminator} (`{user.id}`)")
    
    @commands.command(pass_context=True, hidden=True, name='eval')
    async def _eval(self, ctx, *, body: str):
        """Evaluates a code"""
        Mods = discord.utils.get(ctx.guild.roles, id=467952182713516032)

        if 467952182713516032 not in [role.id for role in ctx.author.roles]:
            return await ctx.send("Sorry, I'm afraid that you don't have the permission to use this secret command.")


        if "token" in body:
            await ctx.send("No token stealing allowed.")
            return

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                self._last_result = ret
                await ctx.send(f'```py\n{value}{ret}\n```')

def setup(bot):
    bot.add_cog(announcement(bot))
