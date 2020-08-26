import os
import discord
import requests
import json
import praw
import configparser
import youtube_dl
from jones import quotes
from random import randint
from youtubesearchpython import SearchVideos
from discord.ext import commands
from bs4 import BeautifulSoup

class JadedBot(commands.Bot):
    def __init__(self, bot):
        super().__init__(command_prefix='!')
        self.config = configparser.ConfigParser()
        self.config.read('configfile')

        self.TOKEN = self.config['JadedBot']['TOKEN']
        self.REDDIT_ID = self.config['JadedBot']['REDDIT_ID']
        self.REDDIT_SECRET = self.config['JadedBot']['REDDIT_SECRET']
        self.command(aliases=['yt'])(self.youtube) # Need to tidy this up and make it modular.
        self.command(aliases=['eq'])(self.everquest)
        self.command()(self.ck2)
        self.command()(self.vaporwave)
        self.command()(self.shitpost)
        self.command()(self.greentext)
        self.command()(self.redpill)
        self.command()(self.join)
        self.command()(self.leave)
        self.command(aliases=['nobody'])(self.nobodyhere)
        self.command()(self.audiophile)
        self.command()(self.ding)
        self.command()(self.jaded)
        self.command()(self.stop)
        self.command()(self.pause)
        self.command()(self.play)
        self.command(aliases=['wow'])(self.anime)
        self.command()(self.popping)
        self.command(aliases=['ram'])(self.ramranch)
        self.command()(self.nice)
     
     
    def wiki_search(self, search, wiki):
        if wiki == 'everquest':
            end_url = 'https://wiki.project1999.com'
            query_url = 'https://wiki.project1999.com/index.php?title=Special%3ASearch&search={0}&fulltext=Search'.format(search.replace(" ", "+"))
        if wiki == 'ck2':
            end_url = 'https://ck2.paradoxwikis.com'
            query_url = 'https://ck2.paradoxwikis.com/index.php?search={0}&title=Special:Search&profile=default&fulltext=1'.format(search.replace(" ", "+"))
        try:
            page = requests.get(query_url).text
            soup = BeautifulSoup(page, 'html.parser')
            result = soup.find(class_="mw-search-result-heading")
            end_string = str(result.select_one("a")['href'])
            return end_url + end_string
        except AttributeError:
            return "Failed to find that page, Sorry."
    
    
    async def everquest(self, ctx, *, search):
        eq_string = self.wiki_search(search, 'everquest')
        await ctx.send('' + eq_string)
    
           
    async def youtube(self, ctx, *, search):
        search = SearchVideos(search, offset = 1, mode = "json", max_results = 1)
        result = search.result()
        result = json.loads(result)
        await ctx.send(result['search_result'][0]['title'] + " " + str(result['search_result'][0]['views']) + " views")
        await ctx.send(result['search_result'][0]['link'])
     
     
    async def ck2(self, ctx, *, search):
        ck_string = self.wiki_search(search, 'ck2')
        await ctx.send('' + ck_string)
        
    
    async def vaporwave(self, ctx):
        search = SearchVideos('vaporwave', offset = 1, mode = "json", max_results = 25)
        result = search.result()
        result = json.loads(result)
        index = randint(1, 24)
        await ctx.send(result['search_result'][index]['title'] + " " + str(result['search_result'][index]['views']) + " views")
        await ctx.send(result['search_result'][index]['link'])
    
    
    async def shitpost(self, ctx):
        reddit = praw.Reddit(client_id=self.REDDIT_ID, client_secret=self.REDDIT_SECRET, user_agent="jadedbot")
        random_num = randint(0, 99)
        submission = reddit.subreddit("copypasta").hot(limit=100)
        for i, post in enumerate(submission):
            if i == random_num:
                try:
                    await ctx.send(post.title)
                    await ctx.send(post.selftext)
                except:
                    #await ctx.send('An error occured sending the post (too long) try again.')
                    full_str = str(post.selftext)
                    #print(type(len(full_str)))
                    firstpart, secondpart = full_str[:1999], full_str[1999:]
                    await ctx.send(firstpart)
                    await ctx.send(secondpart)
    
    
    async def greentext(self, ctx):
        reddit = praw.Reddit(client_id=self.REDDIT_ID, client_secret=self.REDDIT_SECRET, user_agent="jadedbot")
        random_num = randint(0, 99)
        submission = reddit.subreddit("greentext").hot(limit=100)
        for i, post in enumerate(submission):
            if i == random_num:
                try:
                    await ctx.send(post.url)
                except:
                    await ctx.send('An error occured sending the image try again.')
    
    
    async def redpill(self, ctx):
        random_num = randint(0, len(quotes))
        await ctx.send(quotes[random_num])
    
    
    async def join(self, ctx, channel: discord.VoiceChannel="Jaded Bot Audio Room"):
        try:
            channel = ctx.author.voice.channel
            await channel.connect()
        except AttributeError:
            await ctx.send("You're not in a channel.")
            
            
    async def leave(self, ctx):
        try:
            await ctx.voice_client.disconnect()
        except AttributeError:
            await ctx.send("I'm not currently in a channel.")
            
            
    async def nobodyhere(self, ctx):
        try:
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('nobody.webm'))
            ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
            ctx.voice_client.source.volume = 30
        except AttributeError:
            await ctx.send("Join me to a channel with !join first.")
    
    
    async def anime(self, ctx):
        try:
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('anime.webm'))
            ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
            ctx.voice_client.source.volume = 30
        except AttributeError:
            await ctx.send("Join me to a channel with !join first.")
            
            
    async def audiophile(self, ctx):
        await ctx.send(file=discord.File('audiophile.jpg'))
        
        
    async def ding(self, ctx):
        try:
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('ding.webm'))
            ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
            ctx.voice_client.source.volume = 30
        except AttributeError:
            await ctx.send("Join me to a channel with !join first.")
            
            
    async def jaded(self, ctx):
        await ctx.send('```Command List:\n!jaded - Prints this command list.\n!everquest, !eq <search> - Searches P99 Wiki and returns first result.\n!youtube, !yt <search> - Searches youtube and returns first video.\n!ck2 <search> - Searches CK2 Wiki and returns first result.\n!vaporwave - Returns random vaporwave track.\n!shitpost - Professionally shitposts in chat.\n!redpill - Drops some fresh redpills from Alex Jones.\n!join - Joins the bot to the voice channel you\'re currently in.\n!leave - Leaves the voice channel the bot is currently in.\n!nobodyhere, !nobody - There is nobody here.\n!audiophile - Inserts man listening to Edd Ed and Eddy Music.\n!greentext - Inserts a random greentext.\n!ding - Plays EQ sound effect.\n!stop - Stops current audio.\n!pause - Pauses current audio.\n!play - Resumes current audio.\n!anime, !wow - Plays the woooow anime sound.\n!popping - Whats pawppping.\n!ramranch, !ram - Plays Ram Ranch.\n!nice - Click. Nice.```')
        
        
    async def stop(self, ctx):
        ctx.voice_client.stop()
    
    
    async def pause(self, ctx):
        ctx.voice_client.pause()
        
        
    async def play(self, ctx):
        ctx.voice_client.resume()
        

    async def popping(self, ctx):
        try:
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('popping.mp3'))
            ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
            ctx.voice_client.source.volume = 30
        except AttributeError:
            await ctx.send("Join me to a channel with !join first.")
            
    
    async def ramranch(self, ctx):
        try:
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('ram.webm'))
            ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
            ctx.voice_client.source.volume = 30
        except AttributeError:
            await ctx.send("Join me to a channel with !join first.")


    async def nice(self, ctx):
        try:
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('nice.webm'))
            ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
            ctx.voice_client.source.volume = 30
        except AttributeError:
            await ctx.send("Join me to a channel with !join first.")

bot = commands.Bot(command_prefix='!', description="Jaded Bot")
jaded = JadedBot(bot)

jaded.run(jaded.TOKEN)
