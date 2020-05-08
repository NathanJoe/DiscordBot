#Discord bot
#Credits : 
#Python community
#DankCoder#9983
#SoulRika#0002
import asyncio
import discord, random
from discord.ext import commands
#Prefix
client=commands.Bot(command_prefix='/')
#joe mama ligma balls yuritarded
@client.command()
async def joe(ctx):
    await ctx.send('mama')
@client.command()
async def ligma(ctx):
    await ctx.send('balls') 
@client.command()
async def yuri(ctx):
    await ctx.send('tarded')     
#this is for dm'ing a person you. Usage/ex : /dm @VorTex below_is#5517 [insert message here]
@client.command()
@commands.is_owner()
async def dm(ctx, user: discord.Member, *, content):
    await user.send(content)
    await asyncio.sleep(1)
    await ctx.message.delete()
#only me that can use it. Usage/ex : /ban @Aether#1123
#yes, idk how to add reason, embed message maybe?
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member=None):
    if not member:
        await ctx.send('Please mention a fucking member dumbass')
        return
    await member.ban()
    await ctx.send(f'{member.display_name}\'s free trial of being in this server has ended')
#unban, it's what u think it is Usage/ex : /unban Aether#1123
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, userid):
  user=await client.fetch_user(userid)
  await ctx.guild.unban(user)
  await ctx.send(f"Unbanned {user.name}")
#kick command, Usage/ex : /kick Aether#1123
#yes, idk how to add reason, embed message maybe?
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member=None):
    if not member:
        await ctx.send('Please mention a fucking member dumbass')
        return
    await member.kick()
    await ctx.send(f'{member.display_name}\'s ass was kicked from the server')
#this is a roast command, credits to Unishe Dextern Wilstone#2222
#just do /roast and you will be greeted with a roast
@client.command()
async def roast(ctx):
    replies=['You\'re like a swirl of dark clouds, it\'s better when you go away','You\'re so ugly Hello Kitty said goodbye to you','If your face was a Counter Strike map, it would be de_formed','Your birth certificate is an apology from the abortion clinic','John Lennon is better at dodging bullets than you','You must have been born on a highway because that\'s where most accidents happen','I\'d ask you to shoot yourself, but you\'d probably still miss','Your birth certification is a rumour','I saw gay people straighter than your mind',]
    await ctx.send(random.choice(replies))
#this is supposed to be an error log post, but it doesnt work
@client.event
async def on_error(ctx, error):
    await ctx.send(error)
#mute command, this is hard to code, wouldnt be possible without the guys i mentioned before <3
#yes, im still dont know how to add timer
#usage/ex : /mute @Aether#1123
#no reason as always :(
@client.command()
@commands.is_owner()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, user : discord.Member):
    for channel in ctx.guild.channels:
        await channel.set_permissions(user, read_messages=True, send_messages=False)
    
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await user.add_roles(role)
    return await ctx.send("1'ed.")
#unmute, usage/ex : /unmute @Aether#1123
@client.command()
@commands.is_owner()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, user : discord.Member):
    for channel in ctx.guild.channels:
        await channel.set_permissions(user, read_messages=True, send_messages=True)

        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await user.remove_roles(role)
        return await ctx.send("Unmuted.")
#ping, pong! usage/ex : /ping
@client.command()
async def ping(ctx):
  await ctx.send(f"Pong! {client.latency}ms")
#remove the inbuilt help command
client.remove_command('help')
@client.command()
async def help(ctx):
     embed=discord.Embed(title="Help commands", description="")
     embed.add_field(name="joe", value="mama")
     embed.add_field(name="ligma", value="balls")
     embed.add_field(name="yuri", value="tarded")
     embed.add_field(name="dm", value="dm'ing a person you pinged")
     embed.add_field(name="ban", value="for banning an abusive person, annoying person")
     embed.add_field(name="unban", value="for unbanning the person you have banned before")
     embed.add_field(name="kick", value="for kicking an abusive person, annoying person")
     embed.add_field(name="roast", value="it does what you think it is")
     embed.add_field(name="mute", value="muting a person that is spamming, or annoying")
     embed.add_field(name="unmute", value="unmute the person you have muted")
     embed.add_field(name="ping", value="check your latency (i think)")
     embed.add_field(name="help", value="thats, why you are here....")
     await ctx.send(embed=embed)
client.run('NzA2Njk2Njc2MDkzNTkxNjIz.Xq-ArA.x0Fqt9Je5aOUDoDAlDcxn3mONJM')
