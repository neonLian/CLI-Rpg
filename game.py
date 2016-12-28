import socket
import time
import util as u
import cause
from threading import Thread
from player import *
from battle import *
from weapon import *

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
battle = False
battle_start = None
time_left = 10

# save the players in a seperate dictionary and start a battle
def start_battle():
	global player_list
	pd = dict(player_list)
	pl = list(player_list.values())
	player_list = {}
	Battle(pl)
	player_list.update(pd)
		
def new_player(c):
	try:
		# gives player information
		u.s2c(c, "Welcome to Outlandland!")
		u.s2c(c, "What is your name?")
		# ask for player's name
		name = u.rfc(c)
		# create new player
		player = Player(c, r.choice(cause.Clist), r.choice(cause.Money), name)
		u.s2c(c, "%s, your cause for fighting everyone is because %s" % (player.name, player.cause.lower()))
		u.s2c(c, "On your journeys, you will pay with %s." % (player.currency))
		u.s2c(c, "You will enter a battle when enough players are online!")
		u.s2c(c, "There are %d other players online." % len(player_list))
		# add player to the player list
		player_list[player.name] = player
		# give player a few weapons and spells
		player.add_weapon(r.choice(weapon_list)(player))
		player.add_weapon(Manapua(player))
		player.add_weapon(EdibleRainbow(player))
		# begin notifying player when new people are online
		last_players = dict(player_list)
		while True:
			if not player_list == last_players:
				new_player = dict(player_list)
				for known_player in last_players:
					if known_player in last_players:
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
				for player in player_list:
					players_in_battle.append(player_list.pop(player))
			# countdown to battle start
			else:
				time.sleep(1)
				for player in player_list.values():
					u.s2c(player.conn, "Battle starting in %d seconds!" % time_left)
				time_left -= 1
		# start new battle if battle_start is not none
		elif len(player_list) >= 2:
			battle_start = time.time() + 10
			time_left = 10

# start checking if a battle can start
Thread(target=matchmaking).start()
# accept new connections
while True:
	conn, address = s.accept()
	print("Connected to by %s:%s" % (address[0], address[1]))
	Thread(target=new_player, args=(conn,)).start()
