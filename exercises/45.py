import random
def pokemon():
	output_list = []
	pokemon_names = """audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"""
	pokemon_names_list = pokemon_names.rstrip().split(' ')
	start = random.choice(pokemon_names_list)
	output_list.append(start)
	for element in pokemon_names_list:
		if element.startswith(start[-1]) and element not in output_list:
			output_list.append(element)
			start = element
	print output_list
pokemon() 