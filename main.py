import discord
from discord.ext import commands, tasks
import os
from random import randint
from keep_alive import keep_alive
from useless import Date, getDifference
import datetime
from bs4 import BeautifulSoup
import requests
from hentai import Hentai
import time
from discord.ui import button, View, Button
from discord.interactions import Interaction
from glyrics import lyric

bot = commands.Bot(
    command_prefix=["oi ", "Oi ", "oi", "Oi", "OI ", "OI", "oI", "oI "])
buSitaDate = Date(24, 4, 2021)
weekday = {"sun": "0", "mon": "1", "tue": "2",
           "wed": "3", "thu": "4", "fri": "5", "sat": "6"}


@bot.event
async def on_ready():
    print(f"Connected as {bot.user}!")
    homieCounter.start()


@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)


@bot.command()
async def qnbank(ctx):
    Mathematics = Button(
        label="Mathematics", url="https://aakritsubedi9.com.np/uploads/que-bank/Engineering-Mathematics-II.pdf")
    Chemistry = Button(
        label="Chemistry", url="https://aakritsubedi9.com.np/uploads/que-bank/Engineering-Chemistry.pdf")
    Drawing = Button(
        label="Drawing", url="https://aakritsubedi9.com.np/uploads/que-bank/Engineering-Drawing-II.pdf")
    Electronics = Button(
        label="Electronics", url="https://aakritsubedi9.com.np/uploads/que-bank/Basic-Electronics-Engineering.pdf")
    Thermodynamics = Button(
        label="Thermodynamics", url="https://aakritsubedi9.com.np/uploads/que-bank/Thermodynamics.pdf")
    view = View()
    view.add_item(Mathematics)
    view.add_item(Chemistry)
    view.add_item(Drawing)
    view.add_item(Electronics)
    view.add_item(Thermodynamics)
    await ctx.reply("**Old Questions**\nPro tip: Once you click __trust this domain__, the button will directly open the url without the confirmation box", view=view)


@bot.command()
async def resources(ctx):
    MathSolution = Button(
        label="Math Solution", url="https://aakritsubedi9.com.np/uploads/2/SH451_2020-12-07T02:52:49.778Z_Maths%20Solution%20II%20Sem.pdf")
    view = View()
    view.add_item(MathSolution)
    await ctx.reply("**OK NERD!!**", view=view)

@bot.command()
async def lyrics(ctx, *, song):
    if song is None:
        await ctx.reply("Give me some words to search for you dickhead!!")
    else:
        ly = lyric(song)
        embed=discord.Embed(title=f"{ly.title} - {ly.artist}", description=f"{ly.song_lyrics}")
        await ctx.send(embed=embed)


# updates homie counter vc by calculating day difference of today and busita date

@tasks.loop(seconds=600)
async def homieCounter():
    today = datetime.date.today()
    d = int(today.strftime("%d"))
    m = int(today.strftime("%m"))
    y = int(today.strftime("%Y"))
    todayDate = Date(d, m, y)
    s = f"Homies: {getDifference(buSitaDate, todayDate)} days"
    await bot.get_channel(856965820788637706).edit(name=s)


# send random advice
@bot.command()
async def advice(ctx):
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    advice = response.json()["slip"]["advice"]
    embed = discord.Embed(
        description=advice,
        color=discord.Color.green())
    await ctx.send(embed=embed)

# send random joke


@bot.command()
async def joke(ctx):
    url = "https://icanhazdadjoke.com/"
    response = requests.get(url, headers={"Accept": "application/json"})
    url = response.json()["joke"]
    embed = discord.Embed(
        description=url,
        color=discord.Color.green())
    await ctx.send(embed=embed)

# sends random waifu pics


@bot.command()
async def waifu(ctx):
    url = "https://api.waifu.pics/sfw/waifu"
    response = requests.get(url)
    imageUrl = response.json()["url"]
    e = discord.Embed(title="Waifu", url=imageUrl, color=0xff66d6)
    e.set_image(url=url)
    await ctx.reply(embed=e)

# sends random catgirl pics


@bot.command()
async def catgirl(ctx):
    url = "https://api.waifu.pics/sfw/neko"
    response = requests.get(url)
    url = response.json()["url"]
    e = discord.Embed(title="Catgirl", url=url, color=0xff66d6)
    e.set_image(url=url)
    await ctx.reply(embed=e)


@bot.command()
async def ping(ctx):
    embed = discord.Embed(title=f'{round(bot.latency * 1000)}ms',
                          color=discord.Color.red())
    await ctx.send(embed=embed)


@bot.command()
async def routine(ctx):
    view = View()
    Sunday = Button(label="Sunday", style=discord.ButtonStyle.green)

    async def Sunday_callback(interaction):
        embed = discord.Embed(title="   ", color=0xe100ff)
        embed.set_author(name="-SUNDAY-")
        embed.add_field(name="**Test**", value="11:00 - 11:45", inline=False)
        embed.add_field(name="**Maths - ChD**",
                        value="11:45 - 1:15", inline=False)
        embed.add_field(name="**Drawing**", value="2:00 - 5:00", inline=False)
        embed.set_footer(text="Hope you fail!")
        await interaction.response.send_message(embed=embed)
    Sunday.callback = Sunday_callback
    view.add_item(Sunday)

    Monday = Button(label="Monday", style=discord.ButtonStyle.green)

    async def Monday_callback(interaction):
        embed = discord.Embed(title="   ", color=0xe100ff)
        embed.set_author(name="-MONDAY-")
        embed.add_field(name="**Thermodynamics**",
                        value="11:00 - 12:30", inline=False)
        embed.add_field(name="**Electronics - BRM**",
                        value="12:30 - 1:15", inline=False)
        embed.add_field(name="**Drawing**", value="2:00 - 5:00", inline=False)
        embed.set_footer(text="Hope you fail!")
        await interaction.response.send_message(embed=embed)
    Monday.callback = Monday_callback
    view.add_item(Monday)

    Tuesday = Button(label="Tuesday", style=discord.ButtonStyle.green)

    async def Tuesday_callback(interaction):
        embed = discord.Embed(title="   ", color=0xe100ff)
        embed.set_author(name="-TUESDAY-")
        embed.add_field(name="**Math - BK**",
                        value="11:00 - 12:30", inline=False)
        embed.add_field(name="**Electronics - DG**",
                        value="12:30 - 2:00", inline=False)
        embed.add_field(name="**Math - ChD**",
                        value="2:45 - 3:30", inline=False)
        embed.add_field(name="**Chemistry - RPD**",
                        value="3:30 - 5:00", inline=False)
        await interaction.response.send_message(embed=embed)
    Tuesday.callback = Tuesday_callback
    view.add_item(Tuesday)

    Wednesday = Button(label="Wednesday", style=discord.ButtonStyle.green)

    async def Wednesday_callback(interaction):
        embed = discord.Embed(title="   ", color=0xe100ff)
        embed.set_author(name="-WEDNESDAY-")
        embed.add_field(name="**Thermodynamics/Elctronics Lab**",
                        value="11:00 - 1:45", inline=False)
        embed.add_field(name="**Chemistry - RPD**",
                        value="11:45 - 1:15", inline=False)
        embed.add_field(name="**Thermodynamics -MLP**",
                        value="2:00 - 5:00", inline=False)
        embed.set_footer(text="Hope you fail!")
        await interaction.response.send_message(embed=embed)
    Wednesday.callback = Wednesday_callback
    view.add_item(Wednesday)

    Thurdsday = Button(label="Thurdsday", style=discord.ButtonStyle.green)

    async def Thurdsday_callback(interaction):
        embed = discord.Embed(title="   ", color=0xe100ff)
        embed.set_author(name="-THURSDAY-")
        embed.add_field(name="**Thermodynamics**",
                        value="11:00 - 12:30", inline=False)
        embed.add_field(name="**Electronics - BRM**",
                        value="12:30 - 1:15", inline=False)
        embed.add_field(name="**Chemistry**",
                        value="2:00 - 2:45", inline=False)
        embed.add_field(name="**Tutorial - BK**",
                        value="2:45 - 3:30", inline=False)
        embed.add_field(name="**Tutorial - MLP**",
                        value="3:30 - 4:15", inline=False)
        embed.add_field(name="**Tutorial - DG**",
                        value="4:15 - 5:00", inline=False)
        embed.set_footer(text="Hope you fail!")
        await interaction.response.send_message(embed=embed)
    Thurdsday.callback = Thurdsday_callback
    view.add_item(Thurdsday)

    Friday = Button(label="Friday", style=discord.ButtonStyle.green)

    async def Friday_callback(interaction):
        embed = discord.Embed(title="   ", color=0x45a1f7)
        embed.set_author(name="-FRIDAY-")
        embed.add_field(name="**Electronics - BRM**",
                        value="11 - 12:30", inline=False)
        embed.add_field(name="**Maths - ChD**",
                        value="12:30 - 1:15", inline=False)
        embed.add_field(name="**Chemistry - NRB**",
                        value="2:00 - 2:45", inline=False)
        embed.add_field(name="**Chemistry Lab**",
                        value="2:45 - 5:00", inline=False)
        embed.set_footer(text="Hope you fail!")
        await interaction.response.send_message(embed=embed)
    Friday.callback = Friday_callback
    view.add_item(Friday)

    await ctx.reply("**Routine**", view=view)


@bot.command()
async def nsfw(ctx):
    if ctx.channel.is_nsfw():
        url = "https://api.waifu.pics/nsfw/waifu"
        response = requests.get(url)
        url = response.json()["url"]
        e = discord.Embed(title="Waifu", url=url, color=0xff66d6)
        e.set_image(url=url)
        await ctx.reply(embed=e)
    else:
        embed = discord.Embed(
            title="You cannot use this command in this channel",
            color=discord.Color.red())

        await ctx.send(embed=embed)


@bot.command()
async def hentai(ctx, n: int):
    doujin = Hentai(n)

    if ctx.channel.is_nsfw():
        for link in doujin.image_urls:
            time.sleep(1)
            await ctx.send(link)
        await ctx.reply('Here you go!')
    else:
        embed = discord.Embed(
            title="You cannot use this command in this channel",
            color=discord.Color.red())

        await ctx.send(embed=embed)

# nsfw


@bot.command(name='random', aliases=['rd'])
async def random(ctx, a: int):
    if a == 6:
        title = "404 – Not Found"
        while title == "404 – Not Found":
            range_start = 10**(a - 1)
            range_end = (10**a) - 1
            num = randint(range_start, range_end)
            url = f"https://nhentai.net/g/{num}"
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")
            title = soup.select('h1')[0].text.strip()
            if title != "404 – Not Found":
                n = num

        embed = discord.Embed(title=n,
                              url=f"https://nhentai.net/g/{n}",
                              color=discord.Color.dark_red())

        await ctx.send(embed=embed)
    else:
        range_start = 10**(a - 1)
        range_end = (10**a) - 1
        num = randint(range_start, range_end)
        embed = discord.Embed(title=num, color=discord.Color.dark_red())

        await ctx.send(embed=embed)


@random.error
async def random_error(ctx, error):
    embed = discord.Embed(description=":x: Inavlid Agruement",
                          color=discord.Color.red())

    await ctx.send(embed=embed)


@bot.command()
async def tuturu(ctx):
    await ctx.send("hajur")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    msg = message.content.lower()
    if msg.find("kekw") >= 0:
        await message.channel.send("https://cdn.discordapp.com/attachments/835792107296784395/911300358645645312/kek.png")
    if msg.find("homie") >= 0 and msg != "oi homiecount":
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/835550498840903724/840228503399694336/ezgif.com-gif-maker.gif"
        )
    else:
        await bot.process_commands(message)

keep_alive()
bot.run(os.getenv('token'))