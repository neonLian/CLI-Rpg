import os
save_directory = "./.OLLSaveFiles/"
def save_player(player):
	# open file
	if not os.path.exists(save_directory):
		os.mkdir(save_directory)
	savefile = open(save_directory + player.name + ".ollsave", "w")
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

def recv_player(name, conn):
	# open file
	savefile = open(save_directory + name + ".ollsave")
	# transfer text into a list
	attrs = savefile.readlines()
	# transfer list into variables
	name = attrs[0]
	pw = attrs[1]
	lvl = int(attrs[2])
	money = int(attrs[3])
	cause = attrs[4]
	currency = attrs[5]
	xp = int(attrs[6])
	weapons = attrs[7:]
	# create new player
	outplayer = Player(conn, cause, money, name)
	# change player's variables
	outplayer.password = pw
	for l in range(lvl-1):
		outplayer.level_up()
	outplayer.money = money
	outplayer.cause = cause
	outplayer.currency = currency
	outplayer.xp = xp
	for w in weapons:
		outplayer.add_weapon(w)
	return outplayer

