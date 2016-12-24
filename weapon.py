import random as r
import util as u
class Weapon():
	def __init__(self, player, name, dmg, mana=0, effects=[]):
		self.name = name
		self.damage = dmg
		self.mana_cost = mana
		self.effects = effects
		self.buff = dmg <= 0
		self.player = player
	
	def special(self, player):
		pass
	
	def attack(self, player):
		self.special(player)
		if self.player.mana >= self.mana_cost:
			player.HP -= self.damage * self.player.multiplier + r.randint(-5, 5)
			self.player.mana -= self.mana_cost
		else:
			u.s2c(self.player.conn, "Need %d mana to use %s" % (self.mana_cost, self.name))
		for effect in self.effects:
			if not effect in player.effects:
				player.effects.append(effect)
	def desc(self):
		return "%s deals %d damage to a player for %d mana." % (self.name, self.damage, self.mana_cost)

class AngryPiranha(Weapon):
	def __init__(self, player):
		Weapon.__init__(self, player, "Angry Piranha", dmg=60, effects=["bleeding"])
	def desc(self):
		return Weapon.desc()  

class AntiFireExtinguisher(Weapon):
	def __init__(self, player):
		Weapon.__init__(self, player, "Anti-Fire Extinguisher", dmg=100, mana=40, effects=["burning"])

class EdibleRainbow(Weapon):
	def __init__(self, player):
		Weapon.__init__(self, player, "Edible Rainbow", dmg=-60, mana=30)
	
	def special(self, player):
		self.player.effects = []

class Manapua(Weapon):
	def __init__(self, player):
		Weapon.__init__(self, player, "Manapua", dmg=0)
	
	def special(self, player):
		player.mana += 50

class Matchmaker(Weapon):
	def __init__(self, player):
		Weapon.__init__(self,player,"Matchmaker",dmg=75, mana=25, effects=["burning"])

class axe(Weapon):
	def __init__(self, player):
		Weapon.__init__(self,player,"Executioner's Axe",dmg=40)
	
	def attack(self, player):
		if self.damage * 4 >= player.HP:
			player.HP = -100
		else:
			player.HP -= self.damage
class club(Weapon):
	def __init__(self, player):
		Weapon.__init__(self,player,"Club",dmg=65)

class spear(Weapon):
	def __init__(self, player):
		Weapon.__init__(self,player,"Spear",dmg=70)

# i was thinking you could load the bow with arows that have efects thats why the dmg is so low
class Bow(Weapon):
	def __init__(self, player):
		Weapon.__init__(self,player,"Bow",dmg=50)

	def special(self, player):
		player.mana -= 10
		self.player.mana += 10

class Zap(Weapon):
	def __init__(self, player):
		Weapon.__init__(self, player, "Zap", dmg=25)
	
	def special(self, player):
		player.mana -= 30
weapon_list = [AngryPiranha, AntiFireExtinguisher, Matchmaker, axe, club, spear, Bow, Zap]
