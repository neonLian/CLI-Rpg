import util as u
from copy import deepcopy


class Battle:
	""" Usage: Battle([player1, player2]) """
	def __init__(self, players):
		self.players = players
		self.playernames = []
		for player in self.players:
			self.playernames.append(player.name)
		self.start()
		print("Game Over! %s has won!" % self.players[0].name)
	
	def inform(self):
		self.bc("Player information:")
		for player in self.players:
			self.bc(str(player))
	
	def bc(self, msg): # broadcast
		for player in self.players:
			u.s2c(player.conn, msg) 
	
	def attack(self, player):
		u.s2c(player.conn, "\nWhat weapon would you like to use? ")
		wpn_list = dict(player.weapons)
		for wep in player.weapons:
			new_name = wep + " (" + str(wpn_list[wep].mana_cost) + " mana)"
			wpn_list[new_name] = wpn_list.pop(wep) 
		weapon = u.menu_option(wpn_list, player.conn)
		try:
			weapon = int(weapon)
			weapon = list(wpn_list.values())[weapon]
		except (ValueError, IndexError):
			try:
				weapon = player.weapons[weapon]
			except KeyError:
				raise u.GameError("Invalid weapon.")
		if weapon.mana_cost > player.mana:
			raise u.GameError("You need %d mana to use this weapon." % weapon.mana_cost)
		if weapon.buff:
			target = player
		else:
			u.s2c(player.conn, player.name + ", who would you like to attack?")
			targets = list(self.players)
			for i, t in enumerate(targets):
				if player.name == t.name:
					targets.pop(i)
			target = u.menu_option(targets, player.conn)
			for p in self.players:
				if p.name == target:
					target = p
		try:
			target_player = target
			target = target_player.name
			if target_player in self.players and ((target == player.name) == weapon.buff):
				self.bc(player.name + " attacked " + target + " with " + weapon.name)
				weapon.attack(target_player)
		except AttributeError:
			raise u.GameError("Invalid player.")
	
	def turn(self, player):
		player_stats = {"hp": player.HP, "mana": player.mana}
		try:
			player.do_effects()
			if player.HP > 0:
				self.attack(player)
			for i, p in enumerate(self.players):
				if p.HP <= 0:
					self.bc(p.name + " has died.")
					self.players.pop(i)
		except u.GameError as e:
			u.s2c(player.conn, str(e))
			player.HP, player.mana = (player_stats["hp"], player_stats["mana"])
			self.turn(player)
	def start(self):
		player_index = 0
		while len(self.players) > 1:
			next_p = self.players[player_index]
			try:
				self.bc("\n-- %s's Turn --" % next_p.name)
				self.inform()
				self.turn(next_p)
			except (BrokenPipeError, OSError):
				name = next_p.name
				next_p.conn.close()
				del next_p
			player_index += 1
			if player_index > len(self.players) - 1:
				player_index = 0
		winner = self.players[0]
		u.s2c(winner.conn, "You have won the match!")
		


