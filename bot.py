import discord
from discord.ext import commands, tasks
from discord.utils import get
#import redis
import sys
from hero import Hero
from wp_json_api import load_heroes, APICache

#redis_server = redis.Redis()
AUTH_TOKEN = sys.argv[1]#str(redis_server.get('AUTH_TOKEN').decode('utf-8'))

client = discord.Client()

bot = commands.Bot(command_prefix='!')

#TODO: get hero with a converter
@bot.command()
async def hero(ctx, arg):
	hero = arg.lower().capitalize()
	hero = APICache.get_hero(hero)
	if not hero:
		await ctx.send('Hero not found!')
		return
	element_emoji = str(get(ctx.message.guild.emojis, name=hero.element.lower()))
	title = hero.full_name + ' ' + element_emoji
	embed = discord.Embed(title=title , color=Hero.EL_COLORS[hero.element])
	embed.url = hero.link
	embed.set_author(name='Guardian Tales Wiki', url='https://guardiantales.wiki/')
	embed.set_footer(text='© 2020 All Rights Reserved by Guardian Tales Wiki https://guardiantales.wiki/')
	embed.set_thumbnail(url=hero.scaled_picture)
	embed.add_field(name='Atk', value=hero.atk)
	embed.add_field(name='HP', value=hero.hp)
	embed.add_field(name='Def', value=hero.defense)
	embed.add_field(name='Heal', value=hero.heal)
	embed.add_field(name='Crit', value=hero.crit)
	embed.add_field(name='Damage Reduction', value=hero.dmgred)
	rendered_resistances = []
	for resistance_name, resistance in hero.resistances.items():
		emoji = str(get(ctx.message.guild.emojis, name=resistance['icon']))
		rendered_resistances.append(emoji + ' ' + resistance_name + ': ' + resistance['value'] + '%')
	embed.add_field(name='Resistances', value='\n'.join(rendered_resistances))
	embed.add_field(name='Compatible equipments', value=', '.join(hero.compatible_equipment))

	chain_state_trigger_emoji = str(get(ctx.message.guild.emojis, name=hero.chain_state_trigger.value['icon'])) if hero.chain_state_trigger.value else 'N/A'
	chain_state_result_emoji = str(get(ctx.message.guild.emojis, name=hero.chain_state_result.value['icon'])) if hero.chain_state_result.value else 'N/A'
	embed.add_field(name='Chain skill', value=chain_state_trigger_emoji + ' => ' + chain_state_result_emoji)
	await ctx.send(embed=embed)

@tasks.loop(hours=24.0)
async def refresh_heroes():
	print("RUNNING!")
	load_heroes()

@bot.event
async def on_ready():
	print('Bot ready!')
	refresh_heroes.start()

bot.run(AUTH_TOKEN) # TODO: solve error about task exception not being retrieved when stopping the bot with an interrupt
