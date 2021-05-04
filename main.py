#Importing required libraries
import discord
from discord.ext import commands
import os
from mohp import stats, number
from glyrics import lyric, search
from random import randint
from Notes import Notes
from helpers import getPath
from Assign import Assign
from helping import getPat

#Assigning Command Prefix
bot = commands.Bot(command_prefix=["oi ","Oi ", "oi", "Oi"])

#On Ready Function
@bot.event
async def on_ready():
    print(f"Connected as {bot.user}!")

#Checks every message
@bot.event
async def on_message(message):
    msg = message.content.lower()
    content = Assign(getPat(message)).get(msg) 
    if content: #Checks if the message is one of valid commands
        same = content
        await message.channel.send({same})
    else:

        await bot.process_commands(message) #Sends message to activate commands of it is not one of the assigned Commands


bot.remove_command("help")
@bot.command()
async def help(ctx):
    embed=discord.Embed(
    title="Tuturu Command List",
        color=discord.Color.blurple())
  
    embed.add_field(name="oi help", value="`Shows this message`", inline=True)
    embed.add_field(name="oi covid", value="`Sends covid updates`", inline=True)
    embed.add_field(name="oi lyrics <keyword>", value="`Sends lyrics of provided keyword`", inline=True)
    embed.add_field(name="oi searchly <artist_name> <song_name>", value="`Searches lyrics for a specific song`", inline=True)
    embed.add_field(name="oi random <digit>", value="`Sends random number of provided digit value`", inline=True)
    embed.add_field(name="oi aliases",value="`Shows available aliases for the commands`", inline=True)
    embed.add_field(name="oi note <name>", value="`Sends saved note`", inline=True)
    embed.add_field(name="oi notes", value="`Sends saved note titles`", inline=True)
    embed.add_field(name="oi writenote <name> <note>", value="`Creates new note`", inline=True)
    embed.add_field(name="oi editnote <name> <note>", value="`Edits note if it already exits`", inline=True)
    embed.add_field(name="oi deletenote <name>", value="`Deletes existing note`", inline=True)
    embed.add_field(name="oi assign <command> <message>", value="`Assigns custom command to send custom message`", inline=True)
    await ctx.send(embed=embed)


@bot.command()
async def aliases(ctx):
    embed=discord.Embed(
        title="Tuturu Command Aliases",
        description="covid - corona, update\nlyrics - ly,lyric\nrandom - rd\nnotes - dekha, show, all-notes\nnewnote - write, create, new, add\neditnote - edit\ndeletenote - del, remove, delete",
        color=discord.Color.blurple())

    embed.set_footer(text="Use `oi help` to see available commands")
    await ctx.send(embed=embed)

@bot.command(name='random', aliases=['rd'])
async def random(ctx, a:int):
    range_start = 10**(a-1)
    range_end = (10**a)-1
    n = randint(range_start, range_end)

    if a == 6:
        embed=discord.Embed(
            title = n,
            url=f"https://nhentai.net/g/{n}",
            color=discord.Color.dark_red())

        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(
            title = n,
            color=discord.Color.dark_red())

        await ctx.send(embed=embed)


@random.error
async def random_error(ctx, error):
    embed=discord.Embed(
            description=":x: Inavlid Agruement",
            color=discord.Color.red())
    
    await ctx.send(embed=embed)


@bot.command(name='covid', aliases=['corona', 'update'])
async def covid(ctx):
    data = stats()
    embed=discord.Embed(
    title=f"__**Data of {data[5][0:4]}/{data[5][5:7]}/{data[5][8:10]}**__",
        color=discord.Color.orange())
    embed.set_author(name="NepalCovid19Bot",
    url="https://twitter.com/NepalCovid19Bot",icon_url="https://i.imgur.com/VYrtBfo.jpg")

    embed.add_field(name="\nNew Covid-19 Cases:", value=number(data[7]), inline=False)
    embed.add_field(name="Deaths:", value=number(data[6]), inline=False)
    embed.add_field(name="Recovered:", value=number(data[8]), inline=False)
    embed.add_field(name="Total active cases:", value=number(int(data[2]) - int(data[3]) - int(data[4])), inline=False)
    embed.add_field(name="PCR Tests taken:", value=number(data[10]), inline=False)
    embed.add_field(name="RDT Tests taken:", value=number(data[9]), inline=False)
 
    embed.set_footer(text="Stay Safe!! I hope you're okay.")
    await ctx.send(embed=embed)


@bot.command(name='lyrics', aliases=['ly', 'lyric'])
async def lyrics(ctx, *, args):
    sangeet = lyric(args)
    for num in range(0,len(sangeet),2000):
        embed=discord.Embed(
            description=sangeet[num:num+2000],
            color=discord.Color.blue())
        await ctx.send(embed=embed)
        num = num + 2000


@bot.command()
async def searchly(ctx, artist_name, song_name):
    try:
        embed=discord.Embed(
            description=search(artist_name,song_name),
            color=discord.Color.blue())
        
        await ctx.send(embed=embed)
    except:
        embed=discord.Embed(
            description=":red_circle: Couldn't find either artist or song",
            color=discord.Color.red())
    
        await ctx.send(embed=embed)


@bot.command(name='notes', aliases=['dekha', 'show', 'all-notes'])
async def notes(ctx):
    # TODO: Make this an embed so commands to read each note can be embedded in
    #       notes names (not sure that's possible)

    notes = Notes(getPath(ctx)).getAll()
    if notes:
        
        message = ""
        for name in notes.keys():
            message += f"* {name}\n"


        embed=discord.Embed(
        title="Here are the notes available to read:",
        description = message,
        color=discord.Color.blue())

        embed.set_footer(text="Use oi note <name> to read a note!")

    else:
        embed=discord.Embed(
            description="There are no notes! You can add one with oi writenote <name> <content>.",
            color=discord.Color.blue())
   

    await ctx.send(embed = embed)


@bot.command()
async def note(ctx, name):
    name = name.lower().replace(" ", "-")
    content = Notes(getPath(ctx)).get(name)
    if content:
        msg = content
    else:
        msg = f"Note “{name}” does not exist.\nUse oi notes to get a list of available notes."

    embed=discord.Embed(
        description=f"{msg}",
        color=discord.Color.gold())
    await ctx.send(embed = embed)


@note.error
async def note_error(ctx, error):
    msg =" Usage: oi note <name>\nUse `oi notes` to get a list of available notes."
    embed=discord.Embed(
        description=f":x: {msg}",
        color=discord.Color.red())
    await ctx.send(embed = embed)


@bot.command(name='writenote', aliases=['write', 'new', 'create', 'addnote', 'add', 'createnote', 'newnote'])
async def writenote(ctx, *, args):
    try:
        (name, content) = args.split(maxsplit=1)
    except ValueError:
        msg = "You must provide a content for the note.\nUsage: `oi writenote <name> <content>`"
        embed=discord.Embed(
        description=f":x: {msg}",
        color=discord.Color.red())
        await ctx.send(embed = embed)
        return

    if not name.replace("-", "").replace("_", "").isalpha():
        msg = "Note name can only contain letters, “-” and “_”."
        embed=discord.Embed(
        description=f":x: {msg}",
        color=discord.Color.red())
        await ctx.send(embed = embed)
        return

    name = name.lower().replace(" ", "-")
    content = content.strip()
    if len(name) > 30:
        msg = "Note name cannot exceed 30 characters."
        embed=discord.Embed(
        description=f":x: {msg}",
        color=discord.Color.red())
        await ctx.send(embed = embed)
        return

    # Write notes to file
    notes = Notes(getPath(ctx))
    notes.write(name, content)
    print(
        f"Wrote note “{name}” on server “{ctx.guild.name}” ({ctx.guild.id}): {content}")
    embed=discord.Embed(
            description=f":white_check_mark:Successfully wrote note “{name}”, use `oi note {name}` to read it!",
            color=discord.Color.green())

    await ctx.send(embed = embed)


@writenote.error
async def writenote_error(ctx, error):
    print(f"Error on oi writenote: {error}")
    msg = "Usage: `oi writenote <name> <content>`"
    embed=discord.Embed(
        description=f":x: {msg}",
        color=discord.Color.red())
    await ctx.send(embed = embed)


@bot.command(name='editnote', aliases=['edit'])
async def editnote(ctx, *, args):
    try:
        (name, content) = args.split(maxsplit=1)
    except ValueError:
        msg = "You must provide a content for the note.\nUsage: `oi writenote <name> <content>`"
        embed=discord.Embed(
        description=f":x: {msg}",
        color=discord.Color.red())
        await ctx.send(embed = embed)
        return

    if not name.replace("-", "").replace("_", "").isalpha():
        msg = "Note name can only contain letters, “-” and “_”."
        embed=discord.Embed(
        description=f":x: {msg}",
        color=discord.Color.red())
        await ctx.send(embed = embed)
        return

    name = name.lower().replace(" ", "-")
    content = content.strip()
    if len(name) > 30:
        msg = "Note name cannot exceed 30 characters."
        embed=discord.Embed(
        description=f":x: {msg}",
        color=discord.Color.red())
        await ctx.send(embed = embed)
        return

    # Write notes to file
    notes = Notes(getPath(ctx))
    notes.edit(name, content)
    print(
        f"Wrote note “{name}” on server “{ctx.guild.name}” ({ctx.guild.id}): {content}")
    msg = f"Successfully wrote note “{name}”, use `oi note {name}` to read it!"
    embed=discord.Embed(
    description=f":white_check_mark: {msg}",
    color=discord.Color.green())
    await ctx.send(embed = embed)


@editnote.error
async def editnote_error(ctx, error):
    print(f"Error on oi writenote: {error}")
    await ctx.send("Usage: `oi writenote <name> <content>`")


@bot.command(name='deletenote', aliases=['del', 'remove', 'delete'])
async def deletenote(ctx, name):
    name = name.lower().replace(" ", "-")
    notes = Notes(getPath(ctx))

    if not name.replace("-", "").replace("_", "").isalpha():
        await ctx.send("Note name can only contain letters, “-” and “_”.")
        return

    if notes.delete(name):
        msg = f"Note “{name}” successfully deleted!"
        print(
            f"Deleted note “{name}” on server “{ctx.guild.name}” ({ctx.guild.id})")
    else:
        msg = f"Note {name} does not exist.\nUse `oi notes to get a list of available notes."


    embed=discord.Embed(
        description=f":x: {msg}",
        color=discord.Color.red())
    
    await ctx.send(embed = embed)


@deletenote.error
async def deletenote_error(ctx, error):
    print(f"Error on !deletenote: {error}")
    msg = "Usage: `!deletenote <name>`\nUse `!notes` to get a list of available notes."
    embed=discord.Embed(
        description=f":x: {msg}",
        color=discord.Color.red())
    await ctx.send(embed = embed)


@bot.command()
async def assign(ctx, *, args):
    (name, content) = args.split(maxsplit=1)
    com = Assign(getPat(ctx))
    com.write(name, content)
    print(
        f"Wrote note “{name}” on server “{ctx.guild.name}” ({ctx.guild.id}): {content}")
    embed=discord.Embed(
            description=f":white_check_mark:Successfully assigned command {name}",
            color=discord.Color.green())

    await ctx.send(embed = embed)

@bot.event
async def on_message(message):
    msg = message.content.lower()
    content = Assign(getPat(message)).get(msg)
    if content:
        same = content
        await message.channel.send({same})
    else:

        await bot.process_commands(message)
        

bot.run()