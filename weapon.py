import random as r
import util as u
class Weapon():
	def __init__(self, player, dmg, mana=0, effects=[],price = 0):
		self.name = type(self).name
		self.damage = dmg
		self.mana_cost = mana
		self.effects = effects
		self.buff = dmg <= 0
		self.player = player
		self.price = price
	
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
	name = "Angry Piranha "
	price = 180
	def __init__(self, player):
		Weapon.__init__(self, player, dmg=60, effects=["bleeding"],price = 180)
	def desc(self):
		return Weapon.desc()  

class AntiFireExtinguisher(Weapon):
	name = 'Anti-Fire Extinguisher'
	price = 210
	def __init__(self, player):
		Weapon.__init__(self, player, dmg=100, mana=40, effects=["burning"],price = 210)

class EdibleRainbow(Weapon):
	price = 50
	name = ' EdibleRainbow'
	def __init__(self, player):
		Weapon.__init__(self, player, dmg=-60, mana=30,price = 50)
	
	def special(self, player):
		self.player.effects = []

class Manapua(Weapon):
	name = 'Manapua '
	price = 40
	def __init__(self, player):
		Weapon.__init__(self, player, dmg=0,price = 40)
	
	def special(self, player):
		player.mana += 50

class Matchmaker(Weapon):
	price = 190
	name = 'Matchmaker '
	def __init__(self, player):
		Weapon.__init__(self,player,dmg=75, mana=25, effects=["burning"],price = 190)

class axe(Weapon):
	price = 150
	name = 'axe'
	def __init__(self, player):
		Weapon.__init__(self,player,dmg=40,price = 150)
	
	def attack(self, player):
		if self.damage * 4 >= player.HP:
			player.HP = -100
		else:
			player.HP -= self.damage
class club(Weapon):
	price = 60
	name = 'club '
	def __init__(self, player):
		Weapon.__init__(self,player,dmg=65,price = 60)

class spear(Weapon):
	price = 80
	name = 'spear '
	def __init__(self, player):
		Weapon.__init__(self,player,dmg=70,price = 80)

# i was thinking you could load the bow with arows that have efects thats why the dmg is so low
class Bow(Weapon):
	price = 70
	name = 'bow '
	def __init__(self, player):
		Weapon.__init__(self,player,dmg=50,price = 70)

	def special(self, player):
		player.mana -= 10
		self.player.mana += 10

class Zap(Weapon):
	price = 75
	name = 'zap '
	def __init__(self, player):
		Weapon.__init__(self, player, dmg=25,price = 75)
	
	def special(self, player):
		player.mana -= 30
weapon_list = [AngryPiranha, AntiFireExtinguisher, Matchmaker, axe, club, spear, Bow, Zap]
