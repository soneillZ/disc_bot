'''

A Discord Bot that can be used to let users of your Rust Server know how long until your servers wipe.

If you do choose to use this bot on your server, please make sure to give credit to the creator: soneillZ ("https://github.com/soneillZ")
Thanks for using my code :D

'''

import discord
import asyncio
import time
from decimal import Decimal
from bs4 import BeautifulSoup
import requests
import lxml.html
import datetime
import string
from io import BytesIO
from lxml import html
import os
import json
from nested_lookup import nested_lookup

curr_day = datetime.date.today()
days_to_friday = datetime.timedelta(days=4)
days_to_monday = datetime.timedelta(days=3)

class Time:
    seconds_to_friday = days_to_friday.total_seconds()
    seconds_to_monday = days_to_monday.total_seconds()

client = discord.Client()

@client.event
async def on_ready():

    # CHANGE TO '1'

    if (curr_day.isoweekday() == 1):

        while True:

            sectofri = Time.seconds_to_friday + 3600



            em_1 = discord.Embed(title='**Paranoid.gg EU 3x Solo /Duo/Trio** \nHours to Wipe:', description= str(round(sectofri / 3600 , 1)), colour=0x388CBA)
            msg = await client.send_message(client.get_channel('552795486180868097'), embed=em_1)

            while True:


                print(sectofri)

                # FRENCH SERVER


                em_1 = discord.Embed(title='**Wipe Times** \n', description= 'Paranoid.gg EU 3x Solo /Duo/Trio: ' + '**' + str(round(sectofri / 3600 , 1)) + '**' + ' hours.\n\n' + 'Paranoid.gg EU 5x 6MAX: ' + '**' + str(round(sectofri / 3600 , 1)) + '**' + ' hours.\n\n' + 'Paranoid.gg EU Vanilla 2x: ' + '**' + str(round((sectofri - 3600) / 3600 , 1)) + '**' + ' hours.\n\n' + 'Paranoid.gg EU 3x Solo Only: ' + '**' + str(round((sectofri - 3600) / 3600 , 1)) + '**' + ' hours.\n\n' + 'Paranoid.gg US 3x Solo/Duo/Trio: ' + '**' + str(round((sectofri - 21600) / 3600 , 1)) + '**' + ' hours.\n\n' + 'Paranoid.gg US 3x Solo Only: ' + '**' + str(round((sectofri - 21600) / 3600 , 1)) + '**' + ' hours.\n\n', colour=0x388CBA)
                await client.edit_message(msg, embed=em_1)


                time.sleep(1)

                sectofri = sectofri - 85

    elif (curr_day.isoweekday() == 5):

        while True:

            sectomon = Time.seconds_to_monday
            em_1 = discord.Embed(title='**Paranoid.gg EU 3x Solo /Duo/Trio** \n', description= 'Hours until Wipe: ' + str(round(sectomon / 3600 , 1)), colour=0x388CBA)
            msg = await client.send_message(client.get_channel('552795486180868097'), embed=em_1)

            while True:

                print(sectomon)


                em_1 = discord.Embed(title='**Wipe Times** \n', description= 'Paranoid.gg EU 3x Solo /Duo/Trio: ' + '**' + str(round(sectomon / 3600 , 1)) + '**' + ' hours.\n\n' + 'Paranoid.gg EU 5x 6MAX: ' + '**' + str(round(sectomon / 3600 , 1)) + '**' + ' hours.\n\n' + 'Paranoid.gg EU Vanilla 2x: ' + '**' + str(round((sectomon - 3600) / 3600 , 1)) + '**' + ' hours.\n\n' + 'Paranoid.gg EU 3x Solo Only: ' + '**' + str(round((sectomon - 3600) / 3600 , 1)) + '**' + ' hours.\n\n' + 'Paranoid.gg US 3x Solo/Duo/Trio: ' + '**' + str(round((sectomon - 21600) / 3600 , 1)) + '**' + ' hours.\n\n' + 'Paranoid.gg US 3x Solo Only: ' + '**' + str(round((sectomon - 21600) / 3600 , 1)) + '**' + ' hours.\n\n', colour=0x388CBA)
                await client.edit_message(msg, embed=em_1)

                time.sleep(1)

                sectomon = sectomon - 1

    else:

        em_1 = discord.Embed(title='**Waiting for server(s) to wipe. **', description= '', colour=0x388CBA)

        msg = await client.send_message(client.get_channel('552795486180868097'), embed=em_1)

        print("Wipe countdown will only start once bot can determine that it is wipe day.")

client.run('NTUxNDQ0NTI1NTgzOTU4MDE3.D1xnvw.qNOiHXI6mSTf_4hlz6jY4WtEOss')