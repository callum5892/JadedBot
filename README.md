### Installation.

The easiest time you'll have installing this bot is in a UNIX like environment such a Linux/BSD.

You made need sudo access for pip3 access aswell as ffmpeg installed on your system if you want to play music over voice channels.

```
$ git clone https://github.com/Virtual-/JadedBot
$ cd JadedBot
$ pip3 install -r requirements.txt
$ touch configfile
```

Notice at the end we created a configfile. This is the file that will hold the settings we need in order for the bot to work properly so edit the file and input the following:

```
[JadedBot]
TOKEN = DISCORDTOKENHERE
REDDIT_ID = REDDITTOKENHERE
REDDIT_SECRET = REDDITSECRETHERE
```

These entries in the file need to be filled, the top `TOKEN` is your discord API key. The following two are only necessary if you want reddit functionality. If you want that follow this [guide](https://praw.readthedocs.io/en/latest/getting_started/authentication.html).

Start up the program with `$ python3 jaded.py`. It's best to run this in the background somehow, there are various ways to do this on Linux/BSD systems with GNU Screen, Tmux or simply running `$ python3 jaded.py &`.


### Usage

Commands:
- !youtube, !yt <search> - Searches YouTube and returns the first video found.
- !ck2 <search> - Searches the Crusader Kings II Wiki and returns the first page.
- !everquest, !eq <search> - Searches the Project 1999 Wiki and returns the first page. 
- !vaporwave - Returns a random vaporwave themed video from youtube.
- !join - Joins the voice channel of the user who typed the command.
- !leave - Leaves the current channel the bot is in.
- !nobodyhere, !nobody - Starts playing nobodyhere.
- !shitpost - Professionally starts shitposting (Posts a random post from /r/copypasta).
- !redpill - Drops an Alex Jones quote.
- !audiophile - Inserts a meme about audiophiles.
- !greentext - Pulls a random greentext image (from /r/greentext).
- !ding - Plays EQ ding sound effect.
- !play - Resumes stopped audio.
- !stop - Stops current audio.
- !pause - Pauses current audio.
- !popping - Plays whats popping audio.
