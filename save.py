import os
def save_player(player):
	# open file
	if not os.path.exists("./.OLLSaveFiles"):
		os.mkdir("./.OLLSaveFiles")
	savefile = open(player.name + ".ollsave", "w")
	# transfer attributes into list
	name = player.name
	pw = player.password
	lvl = player.level
	money = player.money
	cause = player.cause
	currency = player.currency
	xp = player.xp
	weapons = player.weapons.values()
	attr_list = [name, pw, lvl, money, cause, currency, xp] + weapons
	# write into file
	for attr in attr_list:
		savefile.write(str(attr) + "\n")
	# close file
	savefile.close()

def recv_player(name):
	savefile = open
