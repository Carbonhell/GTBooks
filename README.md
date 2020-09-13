# How to start the bot?
Run `python bot.py TOKEN` with TOKEN being your discord bot token.

You can also easily run it in an AWS EC2 istance (the free one is good too), and you can pass the token through Redis by uncommenting the lines in bot.py related to Redis.

# TODOs (Most important to least):
- Refactor local cache to support Redis
- Refactor the code to use Cogs
- Create item.py and the relevant schema
- Finish adding the other useful information about heroes in the hero embed
- Split the code more so that discord embed code doesn't reside in bot.py
- Add more customization in config.py, and perhaps make it a text config file instead of a python one for ease of use