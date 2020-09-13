
#TODO: load emojis and keep them cached
# Dict that maps elements to their respective emojis, to use them in embeds
icons = {
	'basic': 'basic',
	'light': 'light',
	'dark': 'dark',
	'fire': 'fire',
	'earth': 'earth',
	'water': 'water',

	'injured': 'injured',
	'downed': 'downed',
	'airborne': 'airborne',
	'all_maluses': 'all'
}

#icons = {
#	'basic': str(get(ctx.message.guild.emojis, name='basic')),
#	'light': str(get(ctx.message.guild.emojis, name='light')),
#	'dark': str(get(ctx.message.guild.emojis, name='dark')),
#	'fire': str(get(ctx.message.guild.emojis, name='fire')),
#	'earth': str(get(ctx.message.guild.emojis, name='earth')),
#	'water': str(get(ctx.message.guild.emojis, name='water'))
#}