class Weapon():
	def __init__(self, dmg, mana=0, effects=[]):
		self.damage = dmg
		self.mana_cost = mana
		self.effects = effects
		self.buff = dmg <= 0
	
	def special(self, player):
		pass
	
	def attack(self, player):
		player.HP -= self.damage
		for effect in self.effects:
			if not effect in player.effects:
				player.effects += effect
		self.special(player)

class Sword(Weapon):
	def __init__(self):
		super().__init__(dmg=25)

class Fireball(Weapon):
	def __init__(self):
		super().__init__(dmg=40, mana=40, effects=["burning"])

class Heal(Weapon):
	def __init__(self):
		super().__init__(dmg=-30, mana=30)

class RegenMana(Weapon):
	def __init__(self):
		super().__init__(dmg=0)
	
	def special(self, player):
		player.mana += 50
