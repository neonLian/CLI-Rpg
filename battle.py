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
		print("Player information:")
		for player in self.players:
			print(player)
	
	def menu_option(self, options):
		for i, option in enumerate(options):
			print("%d. %s" % (i, option))
		print("Type in a number or option: ")
		choice = input()
		try:
			choice = options[int(choice)]
		except:
			pass
		return choice
	
	def attack(self, player):
		print("\nWhat weapon would you like to use? ")
		weapon = self.menu_option(player.weapons)
		try:
			weapon = int(weapon)
			weapon = list(player.weapons.values())[weapon]
		except ValueError:
			weapon = player.weapons[weapon]
		print(player.name + ", who would you like to attack?")
		target = self.menu_option(self.players)
		for p in self.players:
			if p == target:
				target_player = p
				break
		target = target_player.name
		if target_player in self.players and ((target == player.name) == weapon.buff):
			print(player.name + " attacked " + target + " with " + weapon.name)
			weapon.attack(target_player)
		else:
			print("Invalid player.")
	
	def turn(self, player):
		print("\n-- %s's Turn --" % player.name)
		player.do_effects()
		self.inform()
		self.attack(player)
	
	def start(self):
		player_index = 0
		while len(self.players) > 1:
			next_p = self.players[player_index]
			self.turn(next_p)
			for i, p in enumerate(self.players):
				if p.HP <= 0:
					print(p.name + " has died.")
					del self.players[i]
			player_index += 1
			if player_index > len(self.players) - 1:
				player_index = 0

