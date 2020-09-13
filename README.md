# How to start the bot?
Run `python bot.py TOKEN` with TOKEN being your discord bot token.

You can also easily run it in an AWS EC2 istance (the free one is good too), and you can pass the token through Redis by uncommenting the lines in bot.py related to Redis.

# TODOs (Most important to least):
- Refactor wp_json_api.py to load the whole heroes/items list once daily and maintain a local cache, and use that for the actual searches. (Load it on redis perhaps?)
- Create item.py and the relevant schema
- Finish adding the other useful information about heroes in the hero embed
- Split the code more so that discord embed code doesn't reside in bot.py
