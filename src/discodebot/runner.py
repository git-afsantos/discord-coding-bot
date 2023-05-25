# SPDX-License-Identifier: MIT
# Copyright © 2023 André Santos

###############################################################################
# Imports
###############################################################################

import os

import discord
from dotenv import load_dotenv

from discodebot.editor import write_code

###############################################################################
# Entry Point
###############################################################################

CODE = """
def hello_world():
    print('Hello, world!')
"""

def run():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is connected to Discord!')
        for guild in client.guilds:
            print(f'Guild: {guild.name} (id: {guild.id})')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        print('> Received a message!')
        print(f'  * author:  {message.author} (id: {message.author.id})')
        print(f'  * guild:   {message.guild}')
        print(f'  * channel: {message.channel}')
        print(f'  * content: {message.content}')

        text = message.content
        if text.startswith('ping'):
            await message.channel.send('pong')

        if text.startswith('write '):
            text = text[6:]
            if text.startswith('function'):
                write_code(CODE)
            else:
                await message.channel.send("I don't know how to do that yet :confused:")


    client.run(TOKEN)
