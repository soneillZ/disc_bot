import discord
import asyncio
import time
from decimal import Decimal
from bs4 import BeautifulSoup
import requests
import lxml.html

def getTimeDay_UK():

    monday_timer_page = requests.get("https://www.timeanddate.com/countdown/generic?iso=20190304T00&p0=919&font=cursive")
    src = monday_timer_page.content
    soup = BeautifulSoup(src, 'html.parser')

    global clock_digits
    clock_digits = []

    for number in soup.find_all('div', class_ = 'csvg-digit-number'):
        clock_digits.append(number.text)


    clock_digits.pop()

    
    return clock_digits[0]

def getTimeHour_UK():

    monday_timer_page = requests.get("https://www.timeanddate.com/countdown/generic?iso=20190304T00&p0=919&font=cursive")
    src = monday_timer_page.content
    soup = BeautifulSoup(src, 'html.parser')

    global clock_digits
    clock_digits = []

    for number in soup.find_all('div', class_ = 'csvg-digit-number'):
        clock_digits.append(number.text)


    clock_digits.pop()

    
    return clock_digits[1]

def getTimeMinutes_UK():

    monday_timer_page = requests.get("https://www.timeanddate.com/countdown/generic?iso=20190304T00&p0=919&font=cursive")
    src = monday_timer_page.content
    soup = BeautifulSoup(src, 'html.parser')

    global clock_digits
    clock_digits = []

    for number in soup.find_all('div', class_ = 'csvg-digit-number'):
        clock_digits.append(number.text)


    clock_digits.pop()

    
    return clock_digits[2]



def getTimeDay_NA():

    monday_timer_page = requests.get("https://www.timeanddate.com/countdown/generic?iso=20190304T00&p0=179&font=cursive")
    src = monday_timer_page.content
    soup = BeautifulSoup(src, 'html.parser')

    global clock_digits
    clock_digits = []

    for number in soup.find_all('div', class_ = 'csvg-digit-number'):
        clock_digits.append(number.text)


    clock_digits.pop()

    
    return clock_digits[0]

def getTimeHour_NA():

    monday_timer_page = requests.get("https://www.timeanddate.com/countdown/generic?iso=20190304T00&p0=179&font=cursive")
    src = monday_timer_page.content
    soup = BeautifulSoup(src, 'html.parser')

    global clock_digits
    clock_digits = []

    for number in soup.find_all('div', class_ = 'csvg-digit-number'):
        clock_digits.append(number.text)


    clock_digits.pop()

    
    return clock_digits[1]

def getTimeMinutes_NA():

    monday_timer_page = requests.get("https://www.timeanddate.com/countdown/generic?iso=20190304T00&p0=179&font=cursive")
    src = monday_timer_page.content
    soup = BeautifulSoup(src, 'html.parser')

    global clock_digits
    clock_digits = []

    for number in soup.find_all('div', class_ = 'csvg-digit-number'):
        clock_digits.append(number.text)


    clock_digits.pop()

    
    return clock_digits[2]



def getTimeDay_FR():

    monday_timer_page = requests.get("https://www.timeanddate.com/countdown/generic?iso=20190304T00&p0=195&font=cursive")
    src = monday_timer_page.content
    soup = BeautifulSoup(src, 'html.parser')

    global clock_digits
    clock_digits = []

    for number in soup.find_all('div', class_ = 'csvg-digit-number'):
        clock_digits.append(number.text)


    clock_digits.pop()

    
    return clock_digits[0]

def getTimeHour_FR():

    monday_timer_page = requests.get("https://www.timeanddate.com/countdown/generic?iso=20190304T00&p0=195&font=cursive")
    src = monday_timer_page.content
    soup = BeautifulSoup(src, 'html.parser')

    global clock_digits
    clock_digits = []

    for number in soup.find_all('div', class_ = 'csvg-digit-number'):
        clock_digits.append(number.text)


    clock_digits.pop()

    
    return clock_digits[1]

def getTimeMinutes_FR():

    monday_timer_page = requests.get("https://www.timeanddate.com/countdown/generic?iso=20190304T00&p0=195&font=cursive")
    src = monday_timer_page.content
    soup = BeautifulSoup(src, 'html.parser')

    global clock_digits
    clock_digits = []

    for number in soup.find_all('div', class_ = 'csvg-digit-number'):
        clock_digits.append(number.text)


    clock_digits.pop()

    
    return clock_digits[2]


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as: {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.wipe'):

        msg_header = await client.send_message(message.channel, '**Wipe Times for Paranoid Servers** \n')
        msg = await client.send_message(message.channel, '[Paranoid.gg EU 3x Solo Only **[UK]**] : ')
        msg2 = await client.send_message(message.channel, '[Paranoid.gg US 3x Solo/Duo/Trio **[NA]**] : ')
        msg3 = await client.send_message(message.channel, '[Paranoid.gg US 3x Solo Only **[NA]**] : ')
        msg4 = await client.send_message(message.channel, '[Paranoid.gg EU 5x 6MAX **[France]**] : ')
        msg5 = await client.send_message(message.channel, '[Paranoid.gg EU 3x Solo/Duo/Trio **[France]**] : ')

        while True:

            await client.edit_message(msg, '[Paranoid.gg EU 3x Solo Only **[UK]**] : ' + getTimeDay_UK() + ' Day(s), ' + getTimeHour_UK() + ' hrs' + ' and ' + getTimeMinutes_UK() + ' minutes.')
            await client.edit_message(msg2, '[Paranoid.gg US 3x Solo/Duo/Trio **[NA]**] : ' + getTimeDay_NA() + ' Day(s), ' + getTimeHour_NA() + ' hrs' + ' and ' + getTimeMinutes_NA() + ' minutes.')
            await client.edit_message(msg3, '[Paranoid.gg US 3x Solo Only **[NA]**] : ' + getTimeDay_NA() + ' Day(s), ' + getTimeHour_NA() + ' hrs' + ' and ' + getTimeMinutes_NA() + ' minutes.')
            await client.edit_message(msg4, '[Paranoid.gg EU 5x 6MAX **[France]**] : ' + getTimeDay_FR() + ' Day(s), ' + getTimeHour_FR() + ' hrs' + ' and ' + getTimeMinutes_FR() + ' minutes.')
            await client.edit_message(msg5, '[Paranoid.gg EU 3x Solo/Duo/Trio **[France]**] : ' + getTimeDay_FR() + ' Day(s), ' + getTimeHour_FR() + ' hrs' + ' and ' + getTimeMinutes_FR() + ' minutes.')

        

client.run('NTUxNDQ0NTI1NTgzOTU4MDE3.D1xnvw.qNOiHXI6mSTf_4hlz6jY4WtEOss')