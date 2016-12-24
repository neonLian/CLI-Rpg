import socket
import time
import util as u
import cause
from threading import Thread
from player import *
from battle import *
from weapon import *
from shop import *

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
comandL = [Battle(player_list)]
#################################################################

def menu():
	global comandL
	





#################################################################
def new_player(c):
	try:
		u.s2c(c, "Welcome to Outlandland!")
		u.s2c(c, "What is your name?")
		name = u.rfc(c)
		player = Player(c, r.choice(cause.Clist), r.choice(cause.Money), name)
		u.s2c(c, "%s, your cause for fighting everyone is because %s" % (player.name, player.cause.lower()))
		u.s2c(c, "On your journeys, you will pay with %s." % (player.currency))
		u.s2c(c, "You will enter a battle when enough players are online!")
		u.s2c(c, "There are %d other players online." % len(player_list))
		player_list[player.name] = player
		player.add_weapon(r.choice(weapon_list)(player))
		player.add_weapon(Manapua(player))
		player.add_weapon(EdibleRainbow(player))
		last_players = dict(player_list)
		while True:
			if not player_list == last_players:
				new_player = dict(player_list)
				print(new_player, player_list, last_players)
				for known_player in last_players:
					if known_player in last_players:
						new_player.pop(known_player)
				new_player = list(new_player)[0]
				u.s2c(c, new_player + " has joined the game")
				last_players = dict(player_list)
	except BrokenPipeError:
		for player in player_list:
			if player.conn == c:
				del player_list[player.name]
		c.close()

def matchmaking():
	global battle_start
	global battle
	global player_list
	while True:
		if battle_start is not None:
			if time.time() >= battle_start:
				battle_start = None
				battle = True
				print("Debug: battle started")
				print(list(player_list.values()))
				Battle(list(player_list.values()))
				battle = False
			elif battle_start - time.time() == 5:
				for player in player_list.values():
					u.s2c(player.conn, "Battle starting in 5 seconds!")
		elif len(player_list) >= 3 and battle == False:
			battle_start = time.time() + 10
			for player in player_list.values():
				u.s2c(player.conn, "Battle starting in 10 seconds!")
Thread(target=matchmaking).start()
while True:
	conn, address = s.accept()
	print("Connected to by %s:%s" % (address[0], address[1]))
	Thread(target=new_player, args=(conn,)).start()
