import socket
import misc as m
import cause
from threading import Thread
from player import *
from battle import *
from weapon import *

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

def new_player(c):
	try:
		m.s2c(c, "Welcome to Outlandland!")
		m.s2c(c, "What is your name?")
		name = m.rfc(c)
		player = Player(c, r.choice(cause.Clist), r.choice(cause.Money), name)
		m.s2c(c, "%s, your cause for fighting everyone is because %s" % (player.name, player.cause.lower()))
		m.s2c(c, "On your journeys, you will pay with %s." % (player.currency))
		m.s2c(c, "You will enter a battle when enough players are online!")
		m.s2c(c, "There are %d other players online." % len(player_list))
		player_list[player.name] = player
		last_players = dict(player_list)
		while True:
			if not player_list == last_players:
				new_player = dict(player_list)
				print(new_player, player_list, last_players)
				for known_player in last_players:
					if known_player in last_players:
						new_player.pop(known_player)
				new_player = list(new_player)[0]
				m.s2c(c, new_player + " has joined the game")
				last_players = dict(player_list)
	except BrokenPipeError:
		for player in player_list:
			if player.conn == c:
				del player_list[player.name]
		c.close()

while True:
	conn, address = s.accept()
	print("Connected to by %s:%s" % (address[0], address[1]))
	Thread(target=new_player, args=(conn,)).start()
	print(player_list)
