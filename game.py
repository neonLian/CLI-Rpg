import socket
import time
import util as u
import cause
from threading import Thread
import save
from player import *
from battle import *
from weapon import *
# from shop import *

# connect a socket

HOST = ""
PORT = 6425

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("Socket Created")

s.bind((HOST, PORT))

print("Socket binded")

s.listen(42)

print("Server now listening")

player_list = {}
battle_list = []
battle = False
battle_start = None
time_left = 10
"""
def new_shop(player):	
	Shop1 = Shop(player.money,weapon_list,player.conn,player.currency,player.weapons,player)
	u.s2c(player.conn,'HELLO!Welcome to my SHOP!what can i DO for you!')
	Shop1.shop_state()
	print(player.weapons)
	Shop1.buy()
	player.add_weapon(Shop1.temp_wep)
	print(player.weapons)
"""

def ready_up(player):
	battle_list.append(player)
	u.s2c(player.conn, "You are ready for battle!")
"""
option_list = {"shop": new_shop, "battle": None}

def menu(player):
	while not player in battle_list:
		u.s2c(player.conn,"What would you like to do?")
		option = u.menu_option(option_list.keys(), player.conn)
		try:
			option = int(option)
			option = list(option_list.keys())[option]
		except ValueError:
			pass
		option_list[option](player)
"""
########################
# save the players in a seperate dictionary and start a battle
def start_battle():
	global battle_list
	bl = list(battle_list)
	battle_list = []
	Battle(bl)
		
def new_player(c):
	try:
		# gives player information
		u.s2c(c, "Welcome to Outlandland!")
		u.s2c(c, "What is your name?")
		# ask for player's name
		name = u.rfc(c)
		try:
			player = save.recv_player(name, c)
			u.s2c(c, "Player loaded!")
			print("Player loaded")
		except FileNotFoundError:
			# create new player
			player = Player(c, r.choice(cause.Clist), r.choice(cause.Money), name)
			# give player a few weapons and spells
			player.add_weapon(r.choice(weapon_list).name)
			player.add_weapon("Manapua")
			player.add_weapon("Edible Rainbow")
			save.save_player(player)
		u.s2c(c, "%s, your cause for fighting everyone is because %s" % (player.name, player.cause.lower()))
		u.s2c(c, "On your journeys, you will pay with %s." % (player.currency))
		u.s2c(c, "You will enter a battle when enough players are online!")
		u.s2c(c, "There are %d other players online." % len(player_list))
		# add player to the player list
		player_list[player.name] = player
		# begin notifying player when new people are online
		last_players = dict(player_list)
		Thread(target=menu, args=(player,)).start()
		while True:
			if player.xp > 100 * player.multiplier:
				player.xp -= player.multiplier * 100
				player.level_up()
			# check for new player
			if not player_list == last_players:
				new_player = dict(player_list)
				for known_player in last_players:
					new_player.pop(known_player)
				new_player = list(new_player)[0]
				u.s2c(c, new_player + " has joined the game")
				last_players = dict(player_list)

	except BrokenPipeError:
		# close socket and remove them from player list when they disconnect
		for player in player_list:
			if player.conn == c:
				del player_list[player.name]
		c.close()

def matchmaking():
	global battle_start
	global battle
	global player_list
	global time_left
	while True:
		# if a new battle is starting
		if battle_start is not None:
			# if it is time to start battle
			if time.time() >= battle_start:
				battle_start = None
				battle = True
				Thread(target=start_battle).start()
				for player in battle_list:
					players_in_battle.append(battle_list.pop(player))
			# countdown to battle start
			else:
				time.sleep(1)
				for player in player_list.values():
					u.s2c(player.conn, "Battle starting in %d seconds!" % time_left)
				time_left -= 1
		# start new battle if battle_start is not none
		elif len(battle_list) >= 2:
			battle_start = time.time() + 10
			time_left = 10

# start checking if a battle can start
Thread(target=matchmaking).start()
# accept new connections
while True:
	conn, address = s.accept()
	print("Connected to by %s:%s" % (address[0], address[1]))
	Thread(target=new_player, args=(conn,)).start()
