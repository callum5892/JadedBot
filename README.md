# JadedBot.
JadedBot is a simple Discord bot written in Python3+

### Install dependencies and setup.
Install the dependencies with

`$ pip3 install -r requirements.txt`

The `configfile` file is how you configure the Discord API Key and Reddit keys if you want functionality.
Simply edit the configfile and it will be loaded in at runtime.

Search praw login for their guide on that.

### Running the bot.
`$ python3 jaded.py`

### Using the bot.

Once the bot is up and running and you've added it into Discord when the bot is mentioned in chat it will give you a list of commands.

Commands:
- !youtube <search> - Searches YouTube and returns the first video found.
- !ck2 <search> - Searches the Crusader Kings II Wiki and returns the first page.
- !everquest <search> - Searches the Project 1999 Wiki and returns the first page. 
- !vaporwave - Returns a random vaporwave themed video from youtube.
- !shitpost - Professionally starts shitposting (Posts a random post from /r/copypasta).
- !redpill - Drops an Alex Jones quote.
