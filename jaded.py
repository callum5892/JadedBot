"""
Copyright (c) 2020 Virtual-. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import os
import discord
import requests
import json
import praw
import configparser
from jones import quotes
from random import randint
from youtubesearchpython import SearchVideos
from discord.ext import commands
from bs4 import BeautifulSoup

bot = commands.Bot(command_prefix='!', description="Jaded Bot")

def wiki_search(search, wiki):
    if wiki == 'everquest':
        end_url = 'https://wiki.project1999.com'
        query_url = 'https://wiki.project1999.com/index.php?title=Special%3ASearch&search={0}&fulltext=Search'.format(search.replace(" ", "+"))
    if wiki == 'ck2':
        end_url = 'https://ck2.paradoxwikis.com'
        query_url = 'https://ck2.paradoxwikis.com/index.php?search={0}&title=Special:Search&profile=default&fulltext=1'.format(search.replace(" ", "+"))
    page = requests.get(query_url).text
    soup = BeautifulSoup(page, 'html.parser')
    result = soup.find(class_="mw-search-result-heading")
    end_string = str(result.select_one("a")['href'])
    
    return end_url + end_string


@bot.command()
async def everquest(ctx, *, search):
    eq_string = wiki_search(search, 'everquest')

    await ctx.send('' + eq_string)


@bot.command()
async def youtube(ctx, *, search):
    search = SearchVideos(search, offset = 1, mode = "json", max_results = 1)
    result = search.result()
    result = json.loads(result)
    await ctx.send(result['search_result'][0]['title'] + " " + str(result['search_result'][0]['views']) + " views")
    await ctx.send(result['search_result'][0]['link'])

@bot.command()
async def ck2(ctx, *, search):
    ck_string = wiki_search(search, 'ck2')

    await ctx.send('' + ck_string)
    
@bot.command()
async def vaporwave(ctx):
    search = SearchVideos('vaporwave', offset = 1, mode = "json", max_results = 25)
    result = search.result()
    result = json.loads(result)
    index = randint(0, 24)
    await ctx.send(result['search_result'][index]['title'] + " " + str(result['search_result'][index]['views']) + " views")
    await ctx.send(result['search_result'][index]['link'])

@bot.command()
async def shitpost(ctx):
    reddit = praw.Reddit(client_id=REDDIT_ID, client_secret=REDDIT_SECRET, user_agent="jadedbot")
    random_num = randint(0, 99)
    submission = reddit.subreddit("copypasta").hot(limit=100)
    for i, post in enumerate(submission):
        if i == random_num:
            if (len(post.selftext) > 2000):
                a,b = post.selftext[:len(post.selftext)/2], post.selftext[len(post.selftext)/2:]
                await ctx.send(post.title)
                await ctx.send(a)
                await ctx.send(b)
            else:
                await ctx.send(post.title)
                await ctx.send(post.selftext)


@bot.command()
async def redpill(ctx):
    random_num = randint(0, len(quotes))
    await ctx.send(quotes[random_num])


@bot.listen()
async def on_message(message):
    if "jaded bot" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('```Command List:\n!everquest <search> - Searches P99 Wiki and returns first result.\n!youtube <search> - Searches youtube and returns first video.\n!ck2 <search> - Searches CK2 Wiki and returns first result.\n!vaporwave - Returns random vaporwave track.\n!shitpost - Professionally shitposts in chat.\n!redpill - Drops some fresh redpills from Alex Jones.\n```')
        await bot.process_commands(message)


config = configparser.ConfigParser()
config.read('configfile')

TOKEN = config['JadedBot']['TOKEN']
REDDIT_ID = config['JadedBot']['REDDIT_ID']
REDDIT_SECRET = config['JadedBot']['REDDIT_SECRET']

bot.run(TOKEN)
