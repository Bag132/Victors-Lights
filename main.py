from discord import guild

import lights
import discord
import datetime
import time
import jibo
import asyncio
import threading
import nest_asyncio
from dotenv import load_dotenv
import tkinter as tk

# entrance music for voice chats
# for steven whenever he joins the vc say "What's up papi blanco"

load_dotenv()
TOKEN = "NzU5MTg0NTgxNzg1NTUwODU4.X25zvQ.hoLbYK4Mrvm0tvx_VPy-88scRYA"

client = discord.Client()


# receiver = jibo.Receiver()


def get_now():
    return datetime.datetime.now()


@client.event
async def on_ready():
    window = tk.Tk()

    print(f'{client.user} has connected to Discord!')


async def fake_on_message(message):
    try:
        if not str(message.author).__contains__("Victor's Lights") and str(message.content)[0] == '!':
            print(str(get_now()) + " | Recieved " + str(message.content) + " from " + str(message.author))
    except IndexError:
        return
    if message.content == '!on':
        await message.channel.send('Congrats! Victor\'s lights are now on!')
    elif message.content == '!off':
        await message.channel.send('Thanks! Victor is scared of the dark.')
    elif message.content == '!toggle':
        if lights.victor_switcher.get_status():
            await message.channel.send('Thanks! Victor is scared of the dark.')
        else:
            await message.channel.send('Congrats! Victor\'s lights are now on!')
    elif message.content == '!status':
        await message.channel.send(
            'Victor\'s lights are on.' if lights.victor_switcher.get_status() == 1 else 'Victor\'s lights are off.')


async def real_on_message(message):
    nest_asyncio.apply()
    try:
        if not str(message.author).__contains__("Victor's Lights") and str(message.content)[0] == '!':
            print(str(get_now()) + " | Received " + str(message.content) + " from " + str(message.author))
    except IndexError:
        return
    if message.content == '!on':
        lights.victor_switcher.lights_on()
        await message.channel.send('Congrats! Victor\'s lights are now on!')
    elif message.content == '!off':
        lights.victor_switcher.lights_off()
        await message.channel.send('Thanks! Victor is scared of the dark.')
    elif message.content == '!toggle':
        if lights.victor_switcher.get_status():
            lights.victor_switcher.lights_off()
            await message.channel.send('Thanks! Victor is scared of the dark.')
        else:
            lights.victor_switcher.lights_on()
            await message.channel.send('Congrats! Victor\'s lights are now on!')
    elif message.content == '!status':
        await message.channel.send(
            'Victor\'s lights are on.' if lights.victor_switcher.get_status() == 1 else 'Victor\'s lights are off.')
    elif message.content == '!bruh':
        await message.channel.send(file=discord.File('bruh.jpg'))
        await message.channel.send(
            'now ᴘʟᴀʏɪɴɢ: Who asked (Feat: Nobody) \n───────────⚪────── \n\t\t◄◄⠀▐▐⠀►► \n\t𝟸:𝟷𝟾 / 𝟹:𝟻𝟼⠀───○ 🔊')
    elif message.content == '!jibo':
        load_message = await message.channel.send('Loading photo...')
        await jibo.recieve()
        await message.channel.send(file=discord.File('jibo_image.jpg'))
        await load_message.delete()


@client.event
async def on_message(message):
    await real_on_message(message)


def acceptInput():
    while 1:
        command = input()
        if command == '!on':
            lights.victor_switcher.lights_on()
        elif command == '!off':
            lights.victor_switcher.lights_off()
        elif command == '!toggle':
            if lights.victor_switcher.get_status():
                lights.victor_switcher.lights_off()
            else:
                lights.victor_switcher.lights_on()
        elif command == '!status':
            print(
                'Victor\'s lights are on.' if lights.victor_switcher.get_status() == 1 else 'Victor\'s lights are off.')


def main():
    client.run(TOKEN)


if __name__ == "__main__":
    main()
