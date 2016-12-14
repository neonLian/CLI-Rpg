class Battle:
	def __init__(self, players):
		self.players = players
		self.playernames = []
		for player in self.players:
			self.playernames.append(player.name)
	
	def inform:
		for player in self.players:
			print("%s [Lvl %d] has %d hp and %d mana\n" % (player.name, player.level, player.HP, player.mana))
	
	def attack(player):
		print("\n" + player.name + ", who would you like to attack?")
		target = input()
		for p in self.players:
			if p.name == target:
				target_player = p
				break
		if target in self.players and not target == player.name:
			print(player.name + " attacked " + target + " with " + player.weapon + " and dealt " + player.damage + " damage.")
			target_player.HP -= player.
